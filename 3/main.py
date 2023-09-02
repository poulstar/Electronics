import dht
import machine
import utime

# Define the GPIO pin you connected the DHT11 to
dht_pin = machine.Pin(16)  # Replace with your GPIO pin number

# Create a DHT11 object
d = dht.DHT11(dht_pin)

try:
    while True:
        # Trigger a measurement and wait for the result
        d.measure()
        utime.sleep_ms(1000)  # Delay to stabilize readings

        # Read the temperature and humidity values
        temperature_c = d.temperature()
        humidity = d.humidity()

        # Print the data
        print("Temperature: {}°C".format(temperature_c))
        print("Humidity: {}%".format(humidity))

        utime.sleep(2)  # Delay between readings

except KeyboardInterrupt:
    print("Measurement stopped.")

finally:
    d.deinit()  # Deinitialize the DHT11 sensor

