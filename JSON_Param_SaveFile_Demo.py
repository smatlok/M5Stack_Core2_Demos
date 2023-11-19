from m5stack import *
from m5stack_ui import *
from uiflow import *
from libs.json_py import *

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

params = {'Factor': 1.41,
          'Timeout': 10,
          'Limit': 1e6}

btn_load = M5Btn(text='load', x=60, y=50, w=80, h=40, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
btn_save = M5Btn(text='save', x=190, y=50, w=80, h=40, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)


label0 = M5Label('label0', x=10, y=140, color=0x000, font=FONT_MONT_14, parent=None)
label1 = M5Label('label0', x=10, y=160, color=0x000, font=FONT_MONT_14, parent=None)
label2 = M5Label('label0', x=10, y=180, color=0x000, font=FONT_MONT_14, parent=None)

def SaveToFile():
    f = open('data.txt', 'w')
    f.write(py_2_json(params))
    f.close()
    
def LoadFromFile():
    f = open('data.txt', 'r')
    global params
    params = json.loads(f.read())
    f.close()
    ShowParams()

def ShowParams():
     label0.set_text('Factor: ' + str(params['Factor']))
     label1.set_text('Timeout: ' + str(params['Timeout']))
     label2.set_text('Limit: ' + str(params['Limit']))
    
#MAIN
ShowParams()
btn_load.pressed(LoadFromFile)
btn_save.pressed(SaveToFile)

