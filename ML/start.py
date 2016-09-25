import json
from urllib2 import urlopen
from main import ml_code
import serial

samples_per_letter = 10

# arduinoSerialData = serial.Serial('/dev/ttyACM0', 38400)

mydatapoint = 309472826744767244762767441254207843242046252299802649042563136462275649624255592639744921306262580935418248892322725133201541919839061282162566845535

# while (True): # 	if (arduinoSerialData.inWaiting() > 0): # 		print '~' # 		for value in range(0, 10): # 	
# 			a_sample = arduinoSerialData.readline()
# 			if a_sample:
# 			    	mydatapoint = a_sample.split()
# 				if len(mydatapoint) == 10:
print ml_code(mydatapoint)
