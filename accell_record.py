#!/usr/bin/env python

# This code reads the data being printed out to the serial
# The data is the processed ***

# DETERMINE ABC COORDINATE USING SONAR

import serial #Import Serial Library

# set the baudrate and serial port
# The port will differ for Windows and Mac
# not sure what these ports should be
# arduinoSerialData = serial.Serial('/dev/cu.usbmodem1421', 115200)

# here is where we define the number of samples we'd like for each full letter
samples_per_letter = 10

arduinoSerialData = serial.Serial('/dev/ttyACM0', 38400)

while (True):
    letter = raw_input('Enter the letter you wish to train. Press enter just before you begin drawing: ') # prompt for a letter
    fname = letter + '-data.txt' # create a file for that letter

    if (arduinoSerialData.inWaiting() > 0):
        # if there is data ready to be retrieved

        with open(fname, 'w') as f:

            for line in range(0, 110):

                #f.write(str(line + 1) + ' ') # write the line number

                # print the numeric string following the 'A' character, followed by a space
                # do so for 30 values

                for value in range(0, 10):

            	    a_sample = arduinoSerialData.readline()
                    print (a_sample + ' ')
                    if a_sample:
                        sample = a_sample.split()
                        f.write(sample[0])

            		#if sample[0] in 'A': # just an extra check
                    #            f.write(str(sample[1]) + ' ')
                    #else:
                    #    f.write('issue')
                    #    break # abandon this sample

                f.write('\n') # finish recording the line of samples
                print 'next one'


# # reading from serial
# while (1==1):
#     if (arduinoSerialData.inWaiting()>0):
#         myData = arduinoSerialData.readline()
#         if myData:
#             data = myData.split(",")
#             del last_five_x[0]
#             del last_five_y[0]
#             last_five_x.append(float(data[0]))
#             last_five_y.append(float(data[1]))
#             avg_x = (sum(last_five_x) / 5) * X_FACTOR # add shift
#             avg_y = (sum(last_five_y) / 5) * Y_FACTOR # add shift
#             for item in response['responses'][0]['textAnnotations']:
#                 coordinates = item['boundingPoly']['vertices']
#                 x_left = (int(coordinates[0]['x']) + int(coordinates[3]['x']))/2
#                 x_right = (int(coordinates[1]['x']) + int(coordinates[2]['x']))/2
#                 y_top = (int(coordinates[0]['y']) + int(coordinates[1]['y']))/2
#                 y_bot = (int(coordinates[2]['y']) + int(coordinates[3]['y']))/2
#                 if avg_x > x_left and avg_x < x_right and avg_y > y_bot and avg_y < y_top:
#                     url = "https://www.google.com/&q=%s" % item['description']
#                     print url #sanity check
#                     webbrowser.open_new(url)
#                     time.sleep(5) #sleep for 5 seconds while the browser loads
#
