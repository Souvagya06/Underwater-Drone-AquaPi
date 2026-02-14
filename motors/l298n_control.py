import RPi.GPIO as GPIO
import time

ENA, IN1, IN2 = 12, 17, 18
ENB, IN3, IN4 = 13, 22, 23

GPIO.setmode(GPIO.BCM)

pins = [ENA, ENB, IN1, IN2, IN3, IN4]
for p in pins:
    GPIO.setup(p, GPIO.OUT)

GPIO.output(ENA, 1)
GPIO.output(ENB, 1)

try:
    print("Motors running forward")

    GPIO.output(IN1, 1)
    GPIO.output(IN2, 0)

    GPIO.output(IN3, 1)
    GPIO.output(IN4, 0)

    time.sleep(5)

finally:
    GPIO.cleanup()
