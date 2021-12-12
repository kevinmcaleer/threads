# das_blinken_thread
# Kevin McAleer
# 12 December 2021

# Import the libraries
import _thread
from time import sleep
from machine import Pin

# Pin 2 on ESP32, Pin 25 on Pico
led = Pin(25, Pin.OUT)
# led = Pin(2, Pin.OUT)

def blink_led():
    """ Blink the built in LED on and then off """
    led.value(0)
    sleep(1)
    led.value(1)
    sleep(1)

def blink_forever():
    """ Blink the LED forever """
    while True:
        blink_led()
        
# Start a new thread 
_thread.start_new_thread(blink_forever,())

# Do something else
while True:
    print("hello world")
    sleep(2)

