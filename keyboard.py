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

def main():
    init();
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def say(msg):
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        print(msg)
        tty.setraw(sys.stdin.fileno())
        
    try:
        tty.setraw(sys.stdin.fileno())
        while True:
            ch = sys.stdin.read(1)
            if ch == '\x1b':
                key = sys.stdin.read(2)
                if key == '[A':
                    say('up')
                    stop()
                    forward()
                elif key == '[B':
                    say('down')
                    stop()
                    backward()
                elif key == '[C':
                    say('right')
                    stop()
                    right()
                elif key == '[D':
                    say('left')
                    stop()
                    left()

            else:
                say("%s: %02x" % (ch, ord(ch)))
                if ch == ' ':
                    stop()
                elif ch == 'q':
                    stop()
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                    exit(0)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

if __name__=='__main__':
    main()
