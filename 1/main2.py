from machine import Pin
import time

led = Pin(13, Pin.OUT)

while True:
    led.toggle()
    time.sleep(1)
