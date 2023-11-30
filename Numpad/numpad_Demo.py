#Numpad Demo 
#Demo how to edit a numeric variable
#based on M5Stack UIFlow1 Firmware
#direct access to lv library functions at some points as UIFlow doesnt support much features

from m5stack import *
from m5stack_ui import *
from uiflow import *
from numpad import *

parameter = 100

#Init some GUI elements
screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

label0 = M5Label('Initial Parameter: '+ str(parameter), x=67, y=113, color=0x000, font=FONT_MONT_18, parent=None)
label0.set_align(lv.ALIGN.IN_TOP_MID, x=0, y=40, ref=lv.scr_act())

touch_button0 = M5Btn(text='EDIT', x=0, y=0, w=150, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_18, parent=None)
touch_button0.set_align(lv.ALIGN.CENTER, x=-10, y=0, ref=screen.obj) #screen.obj or lv.scr_act()

#numpad_h = None
returned_ID = None

def NumpadCallback(value, ID): #Callback Function after numpad closing
    global numpad_h, parameter
    global returned_ID
    
    del numpad_h
    returned_ID = ID
    parameter = value
    
    label0.set_text('New Parameter '+ str(parameter))
    label0.set_align(lv.ALIGN.IN_TOP_MID, x=0, y=40, ref=lv.scr_act())

def BtnFunction(): #Callback function for GUI button - wrapper for 2 addional parameters
    global numpad_h, parameter
    numpad_h = NUMPAD(parameter, NumpadCallback, 'EDITBtn1')
    
touch_button0.pressed(BtnFunction) #register button callback
#MAIN SECTION----------------------------------- 


