#!/usr/bin/env python

import sys, time
import RPi.GPIO as GPIO

redPin = 11
greenPin =13
bluePin = 15

def blink(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.HIGH)

def turnOff(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)

def redOn():
        blink(redPin)

def redOff():
        turnOff(redPin)

def greenOn():
        blink(greenPin)

def greenOff():
        turnOff(greenPin)

def blueOn():
	blink(bluePin)

def blueOff():
	turnOff(bluePin)

def main():
	print("Inicio Programa")
	try:
		while (True):
			redOn()
                        time.sleep(1)
                        redOff()
                        time.sleep(1)
			blueOn()
			time.sleep(1)
			blueOff()
			time.sleep(1)
			greenOn()
                        time.sleep(1)
                        greenOff()
                        time.sleep(1)
                        redOn()
			greenOn()
                        time.sleep(1)
                        blueOn()
			time.sleep(1)

	except KeyboardInterrupt:
		GPIO.cleanup()	
		print("Fin Programa")
main()	
