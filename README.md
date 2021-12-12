# Files in this repository
- `das_blinken_thread.py` - flashed the built in LED whilst doing something else
- `test_thread.py` - 

# Micropython thread tutorial

Micropython programs are usually just a single flow of code, and therefore don't make use of the second core available on the Raspberry Pi Pico or Espressif ESP32 boards.

To add threads to your code is quite simple.

First import the _thread library:

```python
import _thread
```

Create a function that you want to run on the second core:

```python
def do_something():
   print("print hello from core 2")
```

then start this on the second core using:

```python
_thread.start_new_thread(do_something, ())
```

This will then start the function on the second core. The next line of code after this can continue simultaneously.

You will need to be careful when using global variables with threads; they won't cause your program to crash if both cores try to access the same memory, but you might not get the results you expect.

