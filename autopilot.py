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
        time.sleep(3)
        while True:
            forward()
            time.sleep(0.5)
            stop()
            time.sleep(2)
            for i in range(0, 4):
                right()
                time.sleep(0.1)
                stop()
                time.sleep(0.5)
            time.sleep(2)


if __name__=='__main__':
        main()
