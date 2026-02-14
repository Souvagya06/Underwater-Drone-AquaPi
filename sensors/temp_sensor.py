import os
import glob
import time

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp():
    with open(device_file, 'r') as f:
        lines = f.readlines()

    if lines[0].strip()[-3:] == 'YES':
        temp_pos = lines[1].find('t=')
        if temp_pos != -1:
            temp_string = lines[1][temp_pos+2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c

print("Temperature sensor started")

while True:
    temp = read_temp()
    print(f"Temperature: {temp:.2f} °C")
    time.sleep(2)
