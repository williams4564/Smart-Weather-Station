import RPi.GPIO as GPIO
import time
from time import sleep
import serial

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ser = serial.Serial ('/dev/ttyS0', 115200, timeout=1)
temp = ser.readline().decode('utf-8') #decodes the serial data to readable values and puts it into a variable named temp

# assign GPIO outputs
heater = 23
ac = 24
indicator = 25 # LED that detects data being read
dummy = "30" # The test variable to test different temp values. When testing is confirmed this variable will be removed and replaced with temp as defined above

GPIO.setup(heater, GPIO.OUT)
GPIO.setup(ac, GPIO.OUT)
GPIO.setup(indicator, GPIO.OUT)

# defines the function and determines with GPIOs to activate
def heater_on():
        GPIO.output(heater, GPIO.HIGH)
        GPIO.output(ac, GPIO.LOW)

def nothing():
        return "nothing"


# Defines the switch cases. Case 4 is atest case to determine if while loop is reading the "nothing" function defined above
def switch(ledStatus):
        switcher = {
                1: { GPIO.output(heater, GPIO.HIGH), GPIO.output(ac, GPIO.LOW)}, # heater on
                2: {GPIO.output(heater, GPIO.LOW), GPIO.output(ac, GPIO.LOW)}, # idle
                3: {GPIO.output(heater, GPIO.LOW), GPIO.output(ac, GPIO.HIGH)}, # ac on
                4: nothing #testing to see if it prints def nothing() function
        }
        #return switcher.get(ledStatus, "invalid")


if __name__=="__main__":

#while True:
#       GPIO.output(indicator, GPIO.HIGH)

        while dummy <= "20":
                ledStatus(1)
                print('heater on')

        while dummy == "25":
                ledStatus = 2
                print('idle')

        while dummy >= "30":
                ledStatus = 3
                print('ac on')

        else:
                ledStatus = 2