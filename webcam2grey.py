import cv2
import numpy as np

def calc_Y(mirror=False):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        gray = lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114])
        gray = gray(img)  
        print(np.average(gray))

calc_Y()
