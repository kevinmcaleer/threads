import _thread
import time
from machine import Pin

# Pin 2 on ESP32, Pin 25 on Pico
led = Pin(2, Pin.OUT)

value = 0
mutex = _thread.allocate_lock()

def test_thread():
    
    global led, value
    while True:
        led.value(0)
        msg = "Hello from thread" + str(value)
        print(msg)
        time.sleep(1)
        led.value(1)
        time.sleep(1)
        mutex.aquire()
        value += 1
        mutex.release()
        
def second_thread(name):
    global value
    while True:
        msg = "Thread " + name + str(value)
        print(msg)
        time.sleep(1)
        mutex.aquire()
        value += 1
        mutex.release()

_thread.start_new_thread(test_thread, ())
while True:
    message = "Core Code " + str(value)
    print(message)
    time.sleep(3)
_thread.start_new_thread(second_thread,["second"])
_thread.start_new_thread(second_thread,["third"])