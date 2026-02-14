import time
import board
import busio
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)

depth_channel = AnalogIn(ads, ADS1115.P1)

print("Depth sensor running...")

while True:
    voltage = depth_channel.voltage

    # Example calibration (adjust after testing)
    depth = voltage * 10

    print(f"Voltage: {voltage:.2f} V | Depth: {depth:.2f} cm")
    time.sleep(2)
