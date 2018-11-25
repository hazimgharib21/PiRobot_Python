import RPi.GPIO as GPIO
import time

class Button:

    def __init__(self,pin,config):
        self.pin = pin

        if(config == "PULLUP"):
            self.highState = 0
            self.lowState = 1
        elif(config == "PULLDOWN"):
            self.highState = 1
            self.lowState = 0
        else:
            print("Please specify PULLUP or PULLDOWN")

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.pin, GPIO.IN)

        self.currentState = GPIO.input(self.pin)
        self.lastState = self.currentState

    def getState(self):
        return GPIO.input(self.pin)

    def isPressed(self):
        self.currentState = GPIO.input(self.pin)
        if(self.currentState == self.highState and self.lastState == self.lowState):
            self.lastState = self.currentState
            return True
        elif(self.currentState == self.lowState and self.lastState == self.highState):
            self.lastState = self.currentState
            return False
        else:
            pass
