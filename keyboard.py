import sys,tty,termios
import RPi.GPIO as GPIO
import time

PINS = [13, 15, 16, 18, 35, 36, 37, 38]

def init():
    GPIO.setmode(GPIO.BOARD)
    for pin in PINS:
        GPIO.setup(pin, GPIO.OUT)

def test(pin): 
    GPIO.output(pin, 1)
    time.sleep(1)
    GPIO.output(pin, 0)

def stop():
    for pin in PINS:
        GPIO.output(pin, 0)

def forward():
    GPIO.output(15, 1)
    GPIO.output(18, 1)
    GPIO.output(36, 1)
    GPIO.output(38, 1)

def backward():
    GPIO.output(13, 1)
    GPIO.output(16, 1)
    GPIO.output(35, 1)
    GPIO.output(37, 1)

def left():
    GPIO.output(15, 1)
    GPIO.output(18, 1)
    GPIO.output(35, 1)
    GPIO.output(37, 1)

def right():
    GPIO.output(13, 1)
    GPIO.output(16, 1)
    GPIO.output(36, 1)
    GPIO.output(38, 1)

class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                print "up"
                stop()
                forward()
                #time.sleep(1)
                #stop()
        elif k=='\x1b[B':
                print "down"
                stop()
        elif k=='\x1b[C':
                print "right"
                stop()
                right()
                #time.sleep(0.5)
                #stop()
        elif k=='\x1b[D':
                print "left"
                stop()
                left()
                #time.sleep(0.5)
                #stop()
        else:
                print "not an arrow key!"
                stop()
                exit(0)

def main():
        init();
        while True:
                get()

if __name__=='__main__':
        main()
