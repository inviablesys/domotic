#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import subprocess
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)         #Read output from PIR motion sensor
GPIO.setup(11, GPIO.OUT)         #LED output pin
while True:
       i=GPIO.input(22)
       if i==0:                 #When output from motion sensor is LOW
             print "No intruders",i
             GPIO.output(11, 0)  #Turn OFF LED
             time.sleep(1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             GPIO.output(11, 1)  #Turn ON LED
	     subprocess.call(["/usr/bin/php", "/var/www/html/pir.php"])
	     while GPIO.input(22) == 1:
	     	time.sleep(1)
