#/usr/bin/env python3
import cv2 
import os 

img_path = input('Imsert image(s) path: ')

def open_img():

    for images in os.listdir(img_path):
        input_path = os.path.join(img_path, images)

