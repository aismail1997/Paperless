#!/usr/bin/env python

from urllib2 import urlopen
import json
from sklearn import cross_validation
from sklearn.svm import SVC
from time import time
import numpy as np

def ml_code(mydatapoint):

	training_data = []
	training_labels = []

	a = 0
	mydatapoints = []
	alphabet = ['T']
	for value in alphabet:
		b = 0
		fname = alphabet[a] + '-data.txt'
		with open(fname, 'r') as f:
			print 'Working with ' + fname + '\n'
			for line in f:
				if (b >= 10):
					sample = int(line)
				        # sample = a_sample.split()
					# mydatapoints.append(sample)
				        training_data.append(sample)
				        training_labels.append(a)
				b+=1
			a+=1

	all_training_data = np.array(training_data).reshape(-1, 1)
	all_training_labels = np.array(training_labels)
	print all_training_data.ndim
	print all_training_labels.ndim
		

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
