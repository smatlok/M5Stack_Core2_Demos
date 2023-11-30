from m5stack import *
from m5stack_ui import *
from uiflow import *

class NUMPAD:
    
    def _numpad_event_handler(self, source, evt):
        if evt == lv.EVENT.VALUE_CHANGED:
            txt = source.get_active_btn_text()
            asciiVal = ord(txt[0]);
            if txt == lv.SYMBOL.BACKSPACE:
                self.ta.del_char()
           
            elif asciiVal >= 48 and asciiVal < 57:
                self.ta.add_text(txt)
          
            else: #exit numpad options
                taValue = self.ta.get_text() #backup input field before delete
                self.numpadCont.delete()
                #screen.set_screen_bg_color(0xFFFFFF) #refresh screen - maybe there is a better solution as well?
                returnVal = 0 #default
                if txt == lv.SYMBOL.NEW_LINE: #ENTER Symbol 
                    if len(taValue) > 0:
                        returnVal = int(taValue)
                else:
                    returnVal= self._initVal
                
                self._callBackFcn(returnVal, self._customID)
                
                
    def __init__(self, initVal, CallbackFcn, customID):
                 
        self._callBackFcn = CallbackFcn
        self._initVal = initVal
        self._customID = customID
        
        #print('Constructor called')
                 
        #Create Container to overlay backgroud objects (and easy handling like delete)
        self.numpadCont = lv.cont(lv.scr_act(),None)
        self.numpadCont.set_auto_realign(True)                 # Auto realign when the size changes
        self.numpadCont.align_mid(None,lv.ALIGN.CENTER,0,0)  # This parameters will be sued when realigned
        self.numpadCont.set_fit(lv.FIT.TIGHT)
        self.numpadCont.set_layout(lv.LAYOUT.COLUMN_MID);
    
        #Create number field (textarea)
        self.ta = lv.textarea(self.numpadCont,None) #default screen lv.scr_act()
        self.ta.align(None,lv.ALIGN.IN_TOP_MID,0,10)
        self.ta.set_one_line(True) #Adapt height to text
        self.ta.set_text(str(initVal))

        buttonm_map = ["1", "2", "3", "\n",
                    "4", "5", "6", "\n",
                    "7", "8", "9", "\n",
                    lv.SYMBOL.BACKSPACE, "#ff0000 CANCEL#", lv.SYMBOL.NEW_LINE, ""]

        self.buttonm = lv.btnmatrix(self.numpadCont, None)
        self.buttonm.set_recolor(True)
        self.buttonm.set_map(buttonm_map)
        self.buttonm.set_size(320, 180)
        self.buttonm.align(None,lv.ALIGN.IN_BOTTOM_MID,0,0)
        self.buttonm.set_event_cb(self._numpad_event_handler)
        
        def __del__(self):
            #print('Destructor called')
            pass

