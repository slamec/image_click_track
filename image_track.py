#!/usr/bin/env python3

import cv2 
import os 
import csv

img_path = input('Imsert image(s) path: ')

# coordinates x and y two lists - list_x[0] <-> list_y[0]
coordinates_x = []
coordinates_y = []

# key file name, value 2 lists 
coordinates_dic = {}

def mouse_track(event, x, y, flags, param):
    """Save mouse left button action to a list. Returns coordinates. Accepts only 5 parameters."""

    if event == cv2.EVENT_LBUTTONDOWN:

        # to check if coordinates macth with the filename 
        print(x, y)

        # append list with x and y coordinates
        coordinates_x.append(x)
        coordinates_y.append(y)


def open_img():
    """Loops over files in a directory, read image(s), shows, tracks mouse call backs and creates dictionary key = file name, value = lists of x and y coordinates"""

    # loop over image(s) in given directory
    for images in os.listdir(img_path):

        # path + files
        input_path = os.path.join(img_path, images)

        # read and show images - waitKey to keep window open  
        image = cv2.imread(str(input_path))
        
        cv2.imshow(images, image) 
        cv2.setMouseCallback(images, mouse_track)

        coordinates_dic[images] = coordinates_x, coordinates_y

        cv2.waitKey()

# call the function
open_img()

print(coordinates_dic)

# save dictionary to a csv file, avoid newline \n
with open('Coordinates.csv', 'w', newline = '') as file:

    # creating a csv writer object
    writerfile = csv.writer(file)

    # writing dictionary keys as headings of csv (filename)
    writerfile.writerow(coordinates_dic.keys())

    # writing list of dictionary
    writerfile.writerows(zip(*coordinates_dic.values()))




