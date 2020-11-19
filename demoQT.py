#!/usr/bin/python3

import sys

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

import numpy as np

import webcam2rgb

# create a global QT application object
app = QtGui.QApplication(sys.argv)

# signals to all threads in endless loops that we'd like to run these
running = True

class QtPanningPlot:

    def __init__(self,title):
        self.win = pg.GraphicsLayoutWidget()
        self.win.setWindowTitle(title)
        self.plt = self.win.addPlot()
        self.plt.setYRange(0,256)
        self.plt.setXRange(0,500)
        self.curve = self.plt.plot()
        self.data = []
        # any additional initalisation code goes here (filters etc)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)
        self.layout = QtGui.QGridLayout()
        self.win.setLayout(self.layout)
        self.win.show()
        
    def update(self):
        self.data=self.data[-500:]
        if self.data:
            self.curve.setData(np.hstack(self.data))

    def addData(self,d):
        self.data.append(d)

# Let's create three instances of plot windows
qtPanningPlotBlue = QtPanningPlot("Blue channel")
qtPanningPlotGreen = QtPanningPlot("Green channel")
qtPanningPlotRed = QtPanningPlot("Red channel")



# called for every new sample at channel 0 which has arrived from the camera
# "data" contains the new sample
def callBack(retval, data):
    b = data[0]
    g = data[1]
    r = data[2]
    qtPanningPlotBlue.addData(b)
    qtPanningPlotGreen.addData(g)
    qtPanningPlotRed.addData(r)


camera = webcam2rgb.Webcam2rgb()
#start the thread and stop it when we close the plot windows
camera.start(callback = callBack, cameraNumber=0)
print("camera samplerate: ", camera.cameraFs(), "Hz")


# showing all the windows
app.exec_()

camera.stop()

print("Finished")
