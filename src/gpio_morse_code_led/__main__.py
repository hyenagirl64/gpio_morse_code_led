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
        buzzerPin = 35
        GPIO.setup(ledPin, GPIO.OUT)
        GPIO.setup(buzzerPin, GPIO.OUT)
        
        GPIO.output(buzzerPin, GPIO.LOW)
        GPIO.output(ledPin, GPIO.LOW)

        

        def on():
            GPIO.output(ledPin, GPIO.HIGH)
            GPIO.output(buzzerPin, GPIO.HIGH)

        def off():
            GPIO.output(ledPin, GPIO.LOW)
            GPIO.output(buzzerPin, GPIO.LOW)

        ident = input("Enter 4-5 Character Callsign\n")
        ident = ident.strip()
        translator = morse.MorseTranslator(ident, 0.1, on, off)
        print("Calling All Stations From " + ident + "...")
        translator.sign_on()

        close_station = False
        while not close_station:
            val = input ("\nEnter Message.  Type 'cl' to sign off\n")
            val = val.strip().lower()
            if val == "cl":
                close_station = True
            else:
                try:
                    print("\nTransmitting...")
                    translator.encode_signal(val)
                    print("Over!")
                except ValueError as value_error:
                    print(str(value_error))
        print("Closing Station " + ident + "...")
        translator.sign_off()
        print("Over and Out!")
    except Exception as e:
            print(str(e))
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
