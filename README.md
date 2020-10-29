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
camera = webcam2rgb.Webcam2rgb(0)
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

### Stop the acquisition

```
camera.stop()
```
