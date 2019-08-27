#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys


RelayPin = 8   
arg = len(sys.argv) - 1
aux = 0

def setup():
	GPIO.setmode(GPIO.BCM) 
	GPIO.setup(RelayPin, GPIO.OUT)

def on():
	print 'Relay on'
	GPIO.output(RelayPin, GPIO.HIGH)

def off():
        print 'Relay off'
        GPIO.output(RelayPin, GPIO.LOW)

def destroy():
	print 'Destroy'
	GPIO.output(RelayPin, GPIO.LOW)
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	try:
		if (arg !=1 ):
                	print 'Debes intreoducir 1 solo parametro'
	                sys.exit(1)
        	elif (sys.argv[1]=="on"):
                	setup()
			on()
		elif (sys.argv[1]=="off"):
        	        setup()
                	off()
		elif (sys.argv[1]=="estado"):
			setup()
        	        estado =  GPIO.input(RelayPin)
			print estado		
		else:
			print 'Argumentos validos on off estado'

	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the chil$
	      	destroy()
