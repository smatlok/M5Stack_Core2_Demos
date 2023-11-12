#Numpad Demo 
#Demo how to edit a numeric variable
#based on M5Stack UIFlow1 Firmware
#direct access to lv library functions at some points as UIFlow doesnt support much features

from m5stack import *
from m5stack_ui import *
from uiflow import *

#NUMPAD SECTION-----------------------------------
def numpad_event_handler(source, evt):
   
    if evt == lv.EVENT.VALUE_CHANGED:
        txt = source.get_active_btn_text()
        asciiVal = ord(txt[0]);
        if txt == lv.SYMBOL.BACKSPACE:
           ta.del_char()
           
        elif asciiVal >= 48 and asciiVal < 57:
          ta.add_text(txt)
          
        else: #quit numpad
            taValue = int(ta.get_text()) #backup before delete
            numpadCont.delete()
            screen.set_screen_bg_color(0xFFFFFF) #refresh screen - maybe there is a better solution as well?
            
            if txt == lv.SYMBOL.NEW_LINE: #Newline is ENTER Symbol 
                _callBackPrt(taValue)
            else:
                _callBackPrt(_initVal)

        
def CallNumPad(funcPtr, initVal):
    #keep objects after calling
    global numpadCont
    global ta
    global buttonm
    global _callBackPrt
    global _initVal
    
    _callBackPrt = funcPtr
    _initVal = initVal;
    
    #Create Container to overlay backgroud objects (and easy handling like delete)
    numpadCont = lv.cont(lv.scr_act(),None)
    numpadCont.set_auto_realign(True)                 # Auto realign when the size changes
    numpadCont.align_mid(None,lv.ALIGN.CENTER,0,0)  # This parameters will be sued when realigned
    numpadCont.set_fit(lv.FIT.TIGHT)
    numpadCont.set_layout(lv.LAYOUT.COLUMN_MID);
    
    #Create number field (textarea)
    ta = lv.textarea(numpadCont,None) #default screen lv.scr_act()
    ta.align(None,lv.ALIGN.IN_TOP_MID,0,10)
    ta.set_one_line(True) #Adapt height to text
    ta.set_text(str(initVal))

    buttonm_map = ["1", "2", "3", "\n",
            "4", "5", "6", "\n",
            "7", "8", "9", "\n",
            lv.SYMBOL.BACKSPACE, "#ff0000 CANCEL#", lv.SYMBOL.NEW_LINE, ""]

    buttonm = lv.btnmatrix(numpadCont, None)
    buttonm.set_recolor(True)
    buttonm.set_map(buttonm_map)
    buttonm.set_size(320, 180)
    buttonm.align(None,lv.ALIGN.IN_BOTTOM_MID,0,0)
    buttonm.set_event_cb(numpad_event_handler)
#NUMPAD SECTION-----------------------------------
    
    
    
#MAIN SECTION-----------------------------------

# This 'parameter' is what its all about
parameter = 100

#Init some GUI elements
screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

label0 = M5Label('Initial Parameter: '+ str(parameter), x=67, y=113, color=0x000, font=FONT_MONT_18, parent=None)
label0.set_align(lv.ALIGN.IN_TOP_MID, x=0, y=40, ref=lv.scr_act())

touch_button0 = M5Btn(text='EDIT', x=0, y=0, w=150, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_18, parent=None)
touch_button0.set_align(lv.ALIGN.CENTER, x=-10, y=0, ref=screen.obj) #screen.obj or lv.scr_act()

def SetParam(value): #Callback Function after numpad closing
    global parameter
    parameter = value
    label0.set_text('New Parameter '+ str(parameter))
    label0.set_align(lv.ALIGN.IN_TOP_MID, x=0, y=40, ref=lv.scr_act())

def BtnFunction(): #Callback function for GUI button - wrapper for 2 addional parameters
    #global label0
    CallNumPad(SetParam, parameter)
    
touch_button0.pressed(BtnFunction) #register button callback
#MAIN SECTION----------------------------------- 

