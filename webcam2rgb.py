import cv2
import numpy as np

import threading



class CallbackThread(threading.Thread):

    def __init__(self, fs, callback: classmethod, stopEvent: threading.Event):
        super(CallbackThread,self).__init__()
        self.stopped = stopEvent
        self.callback = callback
        self.stop = lambda: self.stopped.set()
        if fs is 0:
            self.t = 0
        else:
            self.t = 1/fs
        
    def run(self):
        while not self.stopped.is_set():
            if self.t is not 0:
                self.stopped.wait(self.t)
                
            self.callback()



class Webcam2rgb():

    def __init__(self, cameraNumber=0):
        self.cam = cv2.VideoCapture(cameraNumber)
        print("camera samplerate: ", self.cameraFs())
        #create Event so we can stop the callback thread!
        self.stopEvent = threading.Event()

    def start(self, callback):
        self.thread = CallbackThread(fs = self.cameraFs()*2, callback = self.calc_BRG, stopEvent = self.stopEvent)
        self.thread.start()
        self.callback = callback

    def stop(self):
        self.thread.stop()
        self.thread.join()

    def calc_BRG(self):
        ret_val, img = self.cam.read()
        h, w, c = img.shape
        brg = img[int(h/2),int(w/2)]
        self.callback(ret_val,brg)

    def cameraFs(self):
        return self.cam.get(cv2.CAP_PROP_FPS)

