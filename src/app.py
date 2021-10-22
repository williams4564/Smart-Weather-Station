from flask import Flask, render_template, url_for
#import serial
import time
import datetime


#Get a thermistor reading to display on webpage 
#ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 1 )
#ser.flush()
#temp = ser.readline().decode('utf-8') #assigns the serial reading into the variable "temp"


app = Flask(__name__)
@app.route('/')  #navigates to main directory
def index():
        now = datetime.datetime.now()
        timeString = now.strftime("%m-%d-%Y  %H:%M")

        templateData = {
                'time' : timeString,
                #'sensor' : temp
        }
        return render_template('data2.html', **templateData)

if __name__ == '__main__':
        app.run(debug=True, port=5000, host='0.0.0.0')
