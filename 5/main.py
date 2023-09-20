from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import dht
import machine
import utime

dht_pin = machine.Pin(18)

d = dht.DHT11(dht_pin)

i2c=I2C(0,sda=Pin(16), scl=Pin(17), freq=400000)
print(i2c.scan())
oled = SSD1306_I2C(128, 64, i2c)

while True:
    try:        
        d.measure()
        utime.sleep_ms(1000)

        temperature_c = d.temperature()
        humidity = d.humidity()
        oled.text("Refreshing...", 0, 0)
        oled.show()
        oled.fill(0)
        utime.sleep_ms(500)
        
        oled.text(f"Temperature :{temperature_c}", 0, 0)
        oled.text(f"Humidity :{humidity}", 0, 16)

        
        utime.sleep(2)
        oled.show()
        oled.fill(0)
        
    except KeyboardInterrupt:
        oled.text("Measurement stopped.", 0, 0)
        oled.show()
    


