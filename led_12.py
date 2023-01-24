# Sandbox program to control LED at pin 12
#  https://www.makeuseof.com/tag/raspberry-pi-control-led/

import ASUS.GPIO as GPIO
import time

import morse_translator as morse


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ledPin = 12
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)

exitNow = False

def on():
    GPIO.output(ledPin, GPIO.HIGH)

def off():
    GPIO.output(ledPin, GPIO.LOW)


translator = morse.MorseTranslator(0.1, on, off)

try:
    while not exitNow:
        val = input ("Type your message.  Type 'Q' to quit\n")
        val = val.strip()
        if val == "Q":
            exitNow = True
        else:
            translator.encode_signal(val)
except ValueError as value_error:
    print(str(value_error))
finally:
    GPIO.cleanup()
