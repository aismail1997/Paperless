import json
from urllib2 import urlopen
from main import ml_code
import serial

samples_per_letter = 10

# arduinoSerialData = serial.Serial('/dev/ttyACM0', 38400)

mydatapoint = [309472826744767, 244762767441254, 207843242046252, 299802649042563, 136462275649624, 255592639744921, 306262580935418, 248892322725133, 201541919839061, 282162566845535]

# while (True): # 	if (arduinoSerialData.inWaiting() > 0): # 		print '~' # 		for value in range(0, 10): # 	
# 			a_sample = arduinoSerialData.readline()
# 			if a_sample:
# 			    	mydatapoint = a_sample.split()
# 				if len(mydatapoint) == 10:
print ml_code(mydatapoint)
