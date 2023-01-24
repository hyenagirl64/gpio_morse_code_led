# Sandbox program to control LED at pin 12
#  https://www.makeuseof.com/tag/raspberry-pi-control-led/

import ASUS.GPIO as GPIO
import time

import morse_translator as morse

def main():
    try:
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
        while not exitNow:
            val = input ("Type your message.  Type '/q' to quit\n")
            val = val.strip()
            if val == "/q":
                exitNow = True
            else:
                try:
                    print("\ntransmitting...")
                    translator.encode_signal(val)
                    print("sent!\n\n")
                except ValueError as value_error:
                    print(str(value_error))
    except Exception as e:
            print(str(e))
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
