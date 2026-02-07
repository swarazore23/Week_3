from machine import Pin

import time

LED_1 = Pin(22, Pin.OUT)

LED_2 = Pin(23, Pin.OUT)

while True:

    
    LED_1.on()
    LED_2.off()

 
    time.sleep(0.5)

    LED_1.off()
    LED_2.on()

   
    time.sleep(0.5)