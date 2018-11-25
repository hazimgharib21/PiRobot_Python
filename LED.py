import RPi.GPIO as GPIO
import time

class LED:
    
    def __init__(self, pin):
        self.pin = pin;

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)

    def On(self):
        GPIO.output(self.pin,GPIO.HIGH)

    def Off(self):
        GPIO.output(self.pin,GPIO.LOW)

led1 = LED(20)
led1.On()
time.sleep(1)
led1.Off()

