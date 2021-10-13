#Download Test
import time
from machine import Pin
led1=Pin(2,Pin.OUT)  #create LED object from pin2,Set Pin2 to output
led2=Pin(16,Pin.OUT)

while True:
    led1.value(1)    #turn off
    led2.value(0)    #turn on
    time.sleep(0.5)
    led1.value(0)    #turn on
    led2.value(1)    #turn off
    time.sleep(0.5)
