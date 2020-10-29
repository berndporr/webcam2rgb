import cv2
import numpy as np

import threading



class Webcam2rgb():

    def __init__(self, cameraNumber=0):
        self.cam = cv2.VideoCapture(cameraNumber)

    def start(self, callback):
        self.running = True
        self.thread = threading.Thread(target = self.calc_BRG)
        self.thread.start()
        self.callback = callback

    def stop(self):
        self.running = False
        self.thread.join()

    def calc_BRG(self):
        while self.running:
            ret_val, img = self.cam.read()
            h, w, c = img.shape
            brg = img[int(h/2),int(w/2)]
            self.callback(ret_val,brg)

    def cameraFs(self):
        return self.cam.get(cv2.CAP_PROP_FPS)

