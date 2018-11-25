from LED import LED
import time

led1 = LED(20)
led2 = LED(21)
led1.On()
time.sleep(1)
led1.Off()
led2.On()
time.sleep(1)
led2.Off()
