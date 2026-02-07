from machine import Pin
import time

LED = Pin(22, Pin.OUT)
LED.on()

time.sleep(0.2)

LED.off()

time.sleep(0.2)
