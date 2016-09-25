import json
from urllib2 import urlopen
from main import ml_code
import serial

samples_per_letter = 10

arduinoSerialData = serial.Serial('com8', 38400)

if (arduinoSerialData.inWaiting() > 0):
	for value in range(0, 10):

		a_sample = arduinoSerialData.readline()
		if a_sample:
		    mydatapoint = a_sample.split()
	            print ml_code(mydatapoint)
