#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

LEDS = [17, 27, 22, 23, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pwms = []

for led in LEDS:
    GPIO.setup(led, GPIO.OUT)
    pwm = GPIO.PWM(led, 1000)
    pwm.start(0)
    pwms.append(pwm)

def fade(pwm):
    for dc in range(0, 101, 5):
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.01)
    for dc in range(100, -1, -5):
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.01)

try:
    while True:

        for pwm in pwms:
            fade(pwm)

        for pwm in reversed(pwms):
            fade(pwm)

except KeyboardInterrupt:
    pass

finally:
    for pwm in pwms:
        pwm.stop()
    GPIO.cleanup()
