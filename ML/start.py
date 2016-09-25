import json
from urllib2 import urlopen
from main import ml_code
import serial

samples_per_letter = 10

arduinoSerialData = serial.Serial('/dev/ttyACM0', 38400)


while(True):
	if (arduinoSerialData.inWaiting() > 0):
		print '~'
		for value in range(0, 10):

			a_sample = arduinoSerialData.readline()
			if a_sample:
			    	mydatapoint = a_sample.split()
				if len(mydatapoint) == 10:
	        	    		print ml_code(mydatapoint)
