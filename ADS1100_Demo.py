from machine import I2C #(original i2c_bus send function from M5Stack returns I2C Error 19)
from machine import Timer
from m5stack_ui import *

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

#Config I2C - choose pins (or port)
i2c = I2C(0, scl=27, sda=19, freq=400000) #Port E 
#i2c = I2C(0, scl=27, sda=19, freq=400000) #Port A 

#ADS1100 Default Address
ADC_address = 72

#Send defaults as start-up config IS NOT AS STATED IN DATASHEET! 
#8SPS(16bit), Gain=1, Continous Conv (SingleCon = 0)
#see https://www.ti.com/lit/ds/symlink/ads1100.pdf
i2c.writeto(ADC_address, b'\x0C')

label0 = M5Label('ADC raw value: ', x=67, y=113, color=0x000, font=FONT_MONT_18, parent=None)
label0.set_align(lv.ALIGN.CENTER, x=-30, y=0, ref=lv.scr_act())
    
def readADC(val):
    byteArrayRes=i2c.readfrom(ADC_address, 2)
    rawVal = int.from_bytes(byteArrayRes, "big")
    label0.set_text('ADC raw value: '+ str(rawVal))
    
timer0 = Timer(0)
timer0.init(period=1000, mode=Timer.PERIODIC, callback=readADC) #period in ms

#while True:
 #   byteArrayRes=i2c.readfrom(ADC_address, 2)
  #  rawVal = int.from_bytes(byteArrayRes, "big")
   # label0.set_text('ADC raw value: '+ str(rawVal))
    #wait_ms(100)
