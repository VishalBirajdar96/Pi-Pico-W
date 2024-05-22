from machine import Pin
import time

ledPin = Pin("LED",Pin.OUT)

while True:
    ledPin.off()
    time.sleep(1)
    ledPin.on()
    time.sleep(1)
