from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c=I2C(0,sda=Pin(16), scl=Pin(17), freq=400000)
print(i2c.scan())
oled = SSD1306_I2C(128, 64, i2c)
oled.text("WELCOME POULSTAR!", 0, 0)
oled.show()
