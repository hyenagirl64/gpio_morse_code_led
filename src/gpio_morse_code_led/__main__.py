# Sandbox program to control LED at pin 12
#  https://www.makeuseof.com/tag/raspberry-pi-control-led/

import ASUS.GPIO as GPIO
import time

import morse_translator as morse

def main():
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        beeperPin = 11
        GPIO.setup(beeperPin, GPIO.OUT, initial = GPIO.LOW)

        def on():
            GPIO.output(beeperPin, GPIO.HIGH)

        def off():
            GPIO.output(beeperPin, GPIO.LOW)

        ident = input("Enter 4-5 Character Callsign\n")
        ident = ident.strip()
        translator = morse.MorseTranslator(ident, 0.065, on, off)
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
        
        #added a little time here to give to 100 micro Farad capacitor time to discharge
        #without this, the buzzer gets a little whistle at the end
        time.sleep(0.5)
    except Exception as e:
            print(str(e))
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
