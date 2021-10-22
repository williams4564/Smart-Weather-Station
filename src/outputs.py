import RPi.GPIO as GPIO
import time
from time import sleep
import serial

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# assign GPIO outputs
heater = 23
ac = 24
indicator = 25
dummy = "80"

GPIO.setup(heater, GPIO.OUT)
GPIO.setup(ac, GPIO.OUT)



if __name__ == "__main__":


        #while sensor is on:
        #GPIO.output(indicator, GPIO.HIGH)


        while dummy <= "30":
                GPIO.output(heater, GPIO.HIGH)
                GPIO.output(ac, GPIO.LOW)

        while dummy == "75":
                GPIO.output(heater, GPIO.LOW)
                GPIO.output(ac, GPIO.LOW)

        while dummy >= "85":
                GPIO.output(ac, GPIO.HIGH)
                GPIO.output(heater, GPIO.LOW)