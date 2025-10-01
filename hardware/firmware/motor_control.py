# Raspberry Pi Motor Control Example
import RPi.GPIO as GPIO
import time

motor_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_pin, GPIO.OUT)

try:
    while True:
        # Turn motor on
        GPIO.output(motor_pin, GPIO.HIGH)
        time.sleep(2)
        # Turn motor off
        GPIO.output(motor_pin, GPIO.LOW)
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
