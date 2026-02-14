import time
import board
import busio
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)

# Channel A0 for pH sensor
ph_channel = AnalogIn(ads, ADS1115.P0)

print("Starting pH sensor readings...")

while True:
    voltage = ph_channel.voltage

    # Simple calibration formula (adjust later)
    ph_value = 7 + ((2.5 - voltage) / 0.18)

    print(f"Voltage: {voltage:.2f} V | pH: {ph_value:.2f}")
    time.sleep(2)
