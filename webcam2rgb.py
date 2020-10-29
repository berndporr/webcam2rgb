import cv2
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

import threading


class Webcam2rgb():

    def __init__(self, cameraNumber=0):
        self.cam = cv2.VideoCapture(cameraNumber)
        print("camera samplerate: ", self.cameraFs())

    def calc_BRG(self):
        ret_val, img = self.cam.read()
        h, w, c = img.shape
        brg = img[int(h/2),int(w/2)]
        print(brg)
        return ret_val,brg

    def cameraFs(self):
        return self.cam.get(cv2.CAP_PROP_FPS)


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


class RealtimePlotWindow:

    def __init__(self, channel: str):
        # create a plot window
        self.fig, self.ax = plt.subplots()
        plt.title(f"Channel: {channel}")
        # that's our plotbuffer
        self.plotbuffer = np.zeros(500)
        # create an empty line
        self.line, = self.ax.plot(self.plotbuffer)
        # axis
        self.ax.set_ylim(0, 1)
        # That's our ringbuffer which accumluates the samples
        # It's emptied every time when the plot window below
        # does a repaint
        self.ringbuffer = []
        # add any initialisation code here (filters etc)
        # start the animation
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=100)


    # updates the plot
    def update(self, data):
        # add new data to the buffer
        self.plotbuffer = np.append(self.plotbuffer, self.ringbuffer)
        # only keep the 500 newest ones and discard the old ones
        self.plotbuffer = self.plotbuffer[-500:]
        self.ringbuffer = []
        # set the new 500 points of channel 9
        self.line.set_ydata(self.plotbuffer)
        self.ax.set_ylim(0, max(self.plotbuffer)+1)
        return self.line,

    # appends data to the ringbuffer
    def addData(self, v):
        self.ringbuffer.append(v)




if __name__ == '__main__':

    #create instances of camera and plots
    camera = Webcam2rgb(1)
    realtimePlotWindow = [RealtimePlotWindow(channel) for channel in ['Blue','Green','Red']]

    #create callback method reading camera and plotting in windows
    def callback():
        ret_val, data = camera.calc_BRG()

        for plot, data in zip(realtimePlotWindow, data):
            plot.addData(data)

    #create Event so we can stop the callback thread!
    stopEvent = threading.Event()

    #create the sampling thread using the cameras sample rate,
    thread = CallbackThread(fs = camera.cameraFs(), callback= callback, stopEvent = stopEvent)
    
    #start the thread and stop it when we close the plot windows
    thread.start()
    plt.show()
    thread.stop()
    thread.join()
    print('finished')

