import RPi.GPIO as GPIO
import datetime
from flask import Flask, render_template

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Assign sensor pin
sensor = 14

# Initialize GPIO status variables
sensorSts = GPIO.LOW

# Set PIR sensor pin as an input
GPIO.setup(sensor, GPIO.IN)


@app.route('/')
def index():
    now = datetime.datetime.now()
	timeString = now.strftime("%Y-%m-%d  %H:%M")
	# Read GPIO status
	sensorSts = GPIO.input(sensor)


	templateData = {
		'time' : timeString,
		'sensor' : sensorSts
	}
	return render_template("sensor.html", **templateData)


if __name__ == '__main__':
	app.run(debug = True, port = '5000', host = '0.0.0.0')