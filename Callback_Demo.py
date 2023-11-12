#Callback Demo

from m5stack import *
from m5stack_ui import *
from uiflow import *

#GUI SECTION-----------------------------------
screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

touch_button0 = M5Btn(text='Edit', x=50, y=50, w=100, h=50, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)

#button0_cb_ptr = None

def Button0_SetText(textvar):
   touch_button0.set_btn_text(textvar)
   
def Button0_SetCallback(func):
    #global button0_cb_ptr;
    #button0_cb_ptr = func;
    touch_button0.pressed(func)
#GUI SECTION-----------------------------------
    
    
#CODE SECTION-----------------------------------
code_result_cb_prt = None
number = 2;

def CalcSquare():
    global number
    number = number*2
    code_result_cb_prt(str(number))

def CalcSquare_SetCallback(func):
    global code_result_cb_prt
    code_result_cb_prt = func
    
#CODE SECTION-----------------------------------
    
    
#MAIN SECTION-----------------------------------
Button0_SetCallback(CalcSquare)
CalcSquare_SetCallback(Button0_SetText)
#MAIN SECTION-----------------------------------    