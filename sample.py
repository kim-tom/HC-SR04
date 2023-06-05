#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
def reading(sensor):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    TRIG = 3
    ECHO = 4
    
    if sensor == 0:
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.3)
        
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO) == 0:
            signaloff = time.time()
        while GPIO.input(ECHO) == 1:
            signalon = time.time()
                
        timepassed = signalon - signaloff
        distance = timepassed * 17000
        return distance
        GPIO.cleanup()
    else:
        print("Incorrect usonic() function varible.")
while(True):
    print(reading(0))
