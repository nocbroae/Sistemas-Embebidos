#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

LEDS = [17, 27, 22, 23, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for led in LEDS:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)

try:
    while True:

        for led in LEDS:
            GPIO.output(led, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(led, GPIO.LOW)

        for led in reversed(LEDS):
            GPIO.output(led, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(led, GPIO.LOW)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
