#/usr/bin/env python3
import cv2 
import os 
import matplotlib.pyplot as plt

img_path = input('Imsert image(s) path: ')

def open_img():

    for images in os.listdir(img_path):
        input_path = os.path.join(img_path, images)


        image = cv2.imread(str(input_path))
        image =cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

        plt.imshow(image)
        show = plt.show()
        
    # return show

open_img()