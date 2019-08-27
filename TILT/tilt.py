#!/usr/bin/env python
import RPi.GPIO as GPIO

TiltPin = 11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(TiltPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.add_event_detect(TiltPin, GPIO.BOTH, callback=detect, bouncetime=200)


def Print(x):
	if x == 0:
		print '    *************'
		print '    *   Tilt!   *'
		print '    *************'
        else:
		print ' NO'
def detect(chn):
	Print(GPIO.input(TiltPin))

def loop():
	while True:
		pass

def destroy():
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

