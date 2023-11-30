from m5stack import *
from m5stack_ui import *
from uiflow import *
import machine

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

label0 = M5Label('label0', x=59, y=39, color=0x000, font=FONT_MONT_34, parent=None)

_lastCallTime = time.ticks_ms();
_relCount = 1
freq = 0

def AnalyzeFrequency(arg): #argument is a string like "Pin(13)"
    global _relCount, _lastCallTime, freq

    t_now = time.ticks_ms();
    t_diff = time.ticks_diff(t_now, _lastCallTime)
  
    if t_diff < 500: #If Time is too short for a half-way precise measure in MyP
        _relCount += 1
    else:
        freq = (_relCount*1e3)/t_diff #time in ms!
        _lastCallTime = t_now
        _relCount = 1

@timerSch.event('timer1')
def ttimer1():
  global freq
  label0.set_text(str(freq))
timerSch.run('timer1', 1000, 0x00) #Update Display by 1 Hz - fast is possible, but influences accuracy (seems to block IRQ Exec)

#Pin1 of Port A = Pin33 (Core2). Pin13 is a pin on backside of the Core2 Module
pin0 = machine.Pin(13, mode=machine.Pin.IN, pull=machine.Pin.PULL_HOLD)
pin0.irq(trigger=machine.Pin.IRQ_FALLING, handler=AnalyzeFrequency)

