from machine import Pin
from utime import sleep_ms

button = Pin(0, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)
State = 0
if _name_ == "__main__":
    while True:
        print(button.value())
        if button.value() == 0:
            if State == 0:
                led.value(1)
                sleep_ms = 100
                while button.value() == 0:
                    State = 1
            else:
                led.value(0)
                sleep_ms = 100
                while button.value() == 0:
                    State = 0
