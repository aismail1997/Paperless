#!/usr/bin/env python

from urllib2 import urlopen
import json
from sklearn import cross_validation
from sklearn.svm import SVC
from time import time
import numpy as np

def ml_code(mydatapoint):
	#Inserted the API Key into the base URL. This ugly hack will work for now
	#BASE_URL = "https://data.phila.gov/resource/sspu-uyfa.json?$$app_token=bF12rIkELtbJ8PXnuzuZTWmVF"

	#REPLACE THESE WITH ACTUAL VALUES
	#longitude = "-75.176386"
	#latitude = "39.916687"

	#radius = "500" #set radius to 500 meters

	#Find all points around a specified radius
	#location_url = BASE_URL + ("&$where=within_circle(shape,%s,%s,%s)" % (latitude, longitude, radius))

	#response = urlopen(location_url)
	#data = json.loads(response.read().decode('utf-8'))

	#num_data_points = len(data)
	#print "Number of total data points = " + str(num_data_points)

	training_data = []
	training_labels = []

	#num_100 = 0
	#num_200 = 0
	#num_300 = 0
	#num_400 = 0
	#num_500 = 0
	#num_600 = 0
	#num_other = 0
	a = 0
	mydatapoints = []
	alphabet = ['C', 'O', 'T']
	for value in alphabet:
		b = 0
		fname = alphabet[a] + '-data.txt'
		with open(fname, 'r') as f:
			print 'Working with ' + fname + '\n'
			for line in fname:
				if (b > 10):
					a_sample = fname.readline
				        sample = a_sample.split()
					mydatapoints.append(sample)
				training_data.append(mydatapoints)
				training_labels.append(alphabet)
		a+=1
		b+=1
#				        sample = a_sample.split()
#					mydatapoint.append(sample)
#		training_data.append(mydatapoint)
#		a = a + 1
#		b = b + 1

	#for d in data:
	#	ucr = d.get('ucr_general')
	#	if ucr != None:
	#		ucr = int(ucr)
	#		#Round down the UCR Number to the nearest 100
	#		ucr = ucr - (ucr % 100)
	#		if not (ucr == 700 or ucr == 1000 or ucr == 1100 or ucr == 1200 or ucr == 1300 or ucr == 1500 or (ucr > 1500 and ucr <= 2400) or ucr == 2600):
	#			if ucr == 100:
	#				num_100 += 1
	#			elif ucr == 200:
	#				num_200 += 1
	#			elif ucr == 300:
	#				num_300 += 1
	#			elif ucr == 400:
	#				num_400 += 1
	#			elif ucr == 500:
	#				num_500 += 1
	#			elif ucr == 600:
	#				num_600 += 1
	#			else:
	#				num_other += 1
	#print
	#print "***For the area around (%s,%s)" % (latitude, longitude) + "***"
	#print "Number of homicides = " + str(num_100)
	#print "Number of rapes = " + str(num_200)
	#print "Number of robberies = " + str(num_300)
	#print "Number of assaults = " + str(num_400)
	#print "Number of burglaries = " + str(num_500)
	#print "Number of thefts = " + str(num_600)
	#print "Number of other crimes = " + str(num_other)

	#Need to reshape the training data because the vector is in 1D
	all_training_data = np.array(training_data)
	all_training_labels = np.array(training_labels)

	#Split all the data points into training and testing data
	features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(all_training_data, all_training_labels, test_size=0.1, random_state=42)

	print "Number of training data points = " + str(len(features_train))
	print "Number of testing data points = " + str(len(features_test))

	#Instantiate the Classifier. We use a support vector machine with an rbf kernel
	classifier = SVC(kernel="rbf", C=10000.0)
	if classifier == None:
	    print "Something went wrong - check packages!"
	    print
	    exit(1)

	#Get first timestamp
	time0 = time()

	#Fit the data
	classifier.fit(features_train, labels_train)

	#Get second timestamp
	training_time = round(time() - time0, 4)

	print "The training time was = " + str(training_time) + " seconds"


	#Use the testing data to find the accuracy of the model
	accuracy = classifier.score(features_test, labels_test)
	print "The Accuracy Score is = " + str(round(accuracy * 100, 3)) + " %"



	#Test for a random time of the day
	prediction = classifier.predict(np.array(mydatapoint))
	print str(prediction) + ' '


	#weighted_number = (num_100*7 + num_200*6 + num_300*5 + num_400*4 + num_500*3 + num_600*2 + num_other*1)
	#print "The weighted average number of crimes reported = " + str(weighted_number)

	#return weighted_number
