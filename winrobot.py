import serial

port = serial.Serial()
port.baudrate = 9600
port.port = 5
port.open()

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
    else:
      # f1 to f12, shift keys, caps lock, Home, End, Delete ...
        print( 'Special Key %r' % event.keysym )
        if event.keysym == 'Up':
            port.write([15])
        elif event.keysym == 'Left':
            port.write([13])
        elif event.keysym == 'Right':
            port.write([11])
        else:
            port.write([9])

root = tk.Tk()
print( "Press a key (Escape key to exit):" )
root.bind_all('<Key>', key)
# don't show the tk window
root.withdraw()
root.mainloop()
