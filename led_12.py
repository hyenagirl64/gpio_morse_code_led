# Sandbox program to control LED at pin 12
#  https://www.makeuseof.com/tag/raspberry-pi-control-led/

import ASUS.GPIO as GPIO
import msvcrt
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ledPin = 12
GPIO.setup(ledPin, GPIO.OUT)

import morse_translator as morse

exitNow = False

try:
    while not exitNow:
        val = input ("Type your message.  Type 'quit' to quit\n")
        val = val.strip()
        if val == "quit":
            exitNow = True
        else:
            print (val + " is not a valid input")
finally:
    GPIO.cleanup()
