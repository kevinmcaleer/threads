import _thread

def hello():
    print("Hello world")
    
    
for i in range(1,20):
    _thread.start_new_thread(hello,())
