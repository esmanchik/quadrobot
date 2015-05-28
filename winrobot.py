import serial
import time

def init(portNumber):
    port = serial.Serial()
    port.baudrate = 9600
    port.port = portNumber
    port.open()
    return port

def xchg(port, cmd):
    port.write(cmd)
    m = port.read(4)
    d = 0
    for i in range(0, 4):
        d |= m[i] << (i * 4)
    return d

def lookaround(port):
    for i in range(0, 9):
        print(xchg(port, [11]))
        time.sleep(0.05)
        print(xchg(port, [9]))

port = init(4)

try:
   # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

def key(event): 
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
            lookaround(port)
    else:
      # f1 to f12, shift keys, caps lock, Home, End, Delete ...
        print( 'Special Key %r' % event.keysym )
        if event.keysym == 'Up':
            print(xchg(port, [15]))
        elif event.keysym == 'Left':
            print(xchg(port, [13]))
        elif event.keysym == 'Right':
            print(xchg(port, [11]))
        else:
            print(xchg(port, [9]))

root = tk.Tk()
print( "Press a key (Escape key to exit):" )
root.bind_all('<Key>', key)
# don't show the tk window
root.withdraw()
root.mainloop()
