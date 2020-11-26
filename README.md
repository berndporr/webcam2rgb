# webcam2rgb
Turning your webcam into a simple RGB light sensor
sampling at the framerate.

## Prerequisites

```
pip3 install opencv-contrib-python
pip3 install opencv-python
```

## How to use

### Import it

```
import webcam2rgb
```

### Get an instance

```
camera = webcam2rgb.Webcam2rgb()
```

### Set up a callback function

```
def hasData(retval, data):
```
where data is an BGR tupel and retval contains any error from openCV

### Start continous acquisition

```
camera.start(callback = hasData)
```
the callback is then called at the framerate of the camera

This method has the following optional arguments:

 - `cameraNumber=0` starts acquisition from camera number `cameraNumber`
 - `width = None` tries to set the width of the camera acquisition
 - `height = None` tries to set the height of the camera acquisition
 - `fps = None` tries to set the framerate
 - `directShow = False` switches on Direct Show under Windows

### Stop the acquisition

```
camera.stop()
```

### Getting the sampling rate

```
fs = camera.cameraFs()
```


## Demo

Just run `demo.py`. It plots the R,G,B channels in three plot windows.


## Troubleshooting

### Spyder

Start your program from the (Anaconda-) console / terminal and never within Spyder. Here is
an example for Windows

```
    (base) D:\>
    (base) D:\>cd webcam2rgb
    (base) D:\webcam2rgb>python demo.py
```

The problem with Spyder is that it won't let your Python program terminate properly
which leaves the video camera in an undefined state. If you then re-run your program
it won't be able to talk to your camera. In the worst case you need to reboot your
computer. Bottomline: use Spyder for editing, run the program from the console / terminal.
