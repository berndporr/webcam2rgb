import cv2
import numpy as np

def calc_RGB():
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        h, w, c = img.shape
        rgb = img[int(h/2),int(w/2)]

calc_RGB()
