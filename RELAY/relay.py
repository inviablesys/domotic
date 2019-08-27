#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.HIGH)
time.sleep(10)

if (GPIO.input(7) == GPIO.LOW):
	print "Apagado"
else:
	print "Encendido"

GPIO.output(7, GPIO.LOW)
time.sleep(10)
GPIO.output(7, GPIO.HIGH)
time.sleep(10)
GPIO.output(7, GPIO.LOW)
time.sleep(10)
GPIO.output(7, GPIO.HIGH)
time.sleep(10)
GPIO.output(7, GPIO.LOW)
GPIO.cleanup()

print "Done!"
