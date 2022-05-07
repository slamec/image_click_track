#/usr/bin/env python3
import cv2 
import os 
import matplotlib.pyplot as plt

img_path = input('Imsert image(s) path: ')

coordinates = []

def mouse_track(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:

        # to check if coordinates are correct for a file name
        print(x, y)
        
        coordinates.append(x)
        coordinates.append(y)

def open_img():

    # loop over images in given directory
    for images in os.listdir(img_path):
        # directory + files
        input_path = os.path.join(img_path, images)

        # read and show images - waitKey to keep window open  
        image = cv2.imread(str(input_path))
        
        cv2.imshow(images, image) 
        cv2.setMouseCallback(images, mouse_track) 
        coordinates.append(images + ": ")
        cv2.waitKey()

open_img()

print(coordinates)
