# esp32_lots_of_threads
# Kevin McAleer
# December 2021
# The ESP32 can suport lots of threads, more than the 2 on the Raspberry Pi Pico

# import libraries
import _thread

# set some variables
mu = _thread.allocate_lock()
n = 0

def hello():
    global n
    mu.acquire()
    n = n + 1
    print("Hello world -", n)
    mu.release()
    _thread.exit()
    
for i in range(1,20):
    _thread.start_new_thread(hello,())

print("Done")