# Raspberry Pi Servo Control Example
import RPi.GPIO as GPIO
import time

servo_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

try:
    while True:
        # Rotate servo to 90 degrees
        pwm.ChangeDutyCycle(7.5)
        time.sleep(1)
        # Rotate servo back to 0 degrees
        pwm.ChangeDutyCycle(2.5)
        time.sleep(1)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
