#!/usr/bin/env python3
import serial
import time
import csv

#detects the device and its baud rate
if __name__ =='__main__':
	ser = serial.Serial('/dev/ttyACM0', 115200,timeout=1)
	ser.flush()

	while True:     #infinite loop to append data to file as strings
		if ser.inWaiting() >0:   #while serial connection is detected
			line = ser.readline().decode('utf-8').rstrip()
			print(line)
			with open("database3.csv","a") as f:
				writer = csv.writer(f,delimiter=",")
				writer.writerow([line])


