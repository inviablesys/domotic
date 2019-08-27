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

def main():
	print("Inicio Programa")
	try:
		while (True):
			cmd = raw_input("Choose an option:")
			if cmd == "red on":
				redOn()
			elif cmd == "red off":
				redOff()
			else:
				print("Not a valid command.")
	except KeyboardInterrupt:
		GPIO.cleanup()	
		print("Fin Programa")
main()	
