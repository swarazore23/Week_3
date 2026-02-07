from machine import Pin


import time


my_led = Pin(22, Pin.OUT)

mc = 1


while (mc < 6):


    my_led.on()

   
    time.sleep(0.5)


    my_led.off()


    time.sleep(0.5)

   
    print("Blink Number:", mc)

    
    mc = mc + 1


print("Execution Complete")