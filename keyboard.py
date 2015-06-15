import serial
import time
import sys

def stop(port):
    for i in range(0, 8):
        port.write("\x0c" + chr(i) + "\x00")
    port.write("\x0e")

def forward(port):
    for i in [1, 3, 5, 7]:
        port.write("\x0c" + chr(i) + "\x01")
    port.write("\x0e")

def backward(port):
    for i in [0, 2, 4, 6]:
        port.write("\x0c" + chr(i) + "\x01")
    port.write("\x0e")

def right(port):
    for i in [1, 3, 4, 6]:
        port.write("\x0c" + chr(i) + "\x01")
    port.write("\x0e")

def left(port):
    for i in [0, 2, 5, 7]:
        port.write("\x0c" + chr(i) + "\x01")
    port.write("\x0e")

def init(portNumber):
    port = serial.Serial()
    port.baudrate = 9600
    port.port = portNumber
    port.open()
    return port

print( "Enter port number: " )
num = sys.stdin.read(1)
print( "Opening port " + num )
port = init(int(num))

try:
   # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

def key(event): 
    stop(port)
    """shows key or tk code for the key"""
    if event.keysym == 'Escape':
        port.close()
        root.destroy()
    if event.char == event.keysym:
     # normal number and letter characters
        print( 'Normal Key %r' % event.char )
    elif len(event.char) == 1:
      # charcters like []/.,><#$ also Return and ctrl/key
        print( 'Punctuation Key %r (%r)' % (event.keysym, event.char) )
        if event.char == ' ':
            stop(port)
    else:
      # f1 to f12, shift keys, caps lock, Home, End, Delete ...
        print( 'Special Key %r' % event.keysym )
        if event.keysym == 'Up':
            forward(port)
        elif event.keysym == 'Down':
            backward(port)
        elif event.keysym == 'Left':
            left(port)
        elif event.keysym == 'Right':
            right(port)

root = tk.Tk()
print( "Press a key (Escape key to exit):" )
root.bind_all('<Key>', key)
# don't show the tk window
root.withdraw()
root.mainloop()
