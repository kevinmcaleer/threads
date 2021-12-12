import _thread
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
toggle = False
#lock = _thread.allocate_lock()

def led_on():
    led.value(1)
    
def led_off():
    led.value(0)

def switch_off():
    global toggle
    while True:
       #lock.acquire()
       if toggle:
           led_off()
           toggle = False
       sleep(1)
       #lock.release()
    

_thread.start_new_thread(switch_off,())

while True:
    #lock.acquire()
    toggle = True
    led_on()
    sleep(1)
    #lock.release()
    
