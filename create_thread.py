import _thread

def hello():
    print("Hello world")
    
_thread.start_new_thread(hello,())