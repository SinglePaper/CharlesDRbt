# Charles D. Robot
Charles D. Robot can detect objects and center them in the frame. This guide can be used to recreate the results as seen in this [YouTube video](https://youtu.be/6JhAzuDE4sk).

## Building the robot
### Electronics
The following electronics are required for the build:
- [Raspberry Pi Zero WH](https://www.kiwi-electronics.nl/nl/raspberry-pi-zero-wh-header-voorgesoldeerd-3328?search=raspberry%20pi%20zero&page=2)
- [Raspberry Pi Zero camera](https://nl.aliexpress.com/item/32788881215.html?spm=a2g0s.9042311.0.0.27424c4dMKKQ5k)
- Micro SD card (min. 16GB, 32GB recommended)
- [Dual H-Bridge DC stepper motor driver - L298N](https://www.kiwi-electronics.nl/nl/dual-h-bridge-dc-stepper-motor-driver-l298n-4117?search=h-bridge)
- 2x [DC Gearbox Motor](https://www.kiwi-electronics.nl/nl/dc-gearbox-motor-tt-motor-200rpm-3-6vdc-10318?search=motor)
- [Set of jumperwires F/F](https://www.kiwi-electronics.nl/nl/jumperwires-10-stuks-f-f-15cm-362)
- [Set of jumperwires F/M](https://www.kiwi-electronics.nl/nl/jumperwires-10-stuks-m-f-15cm-311?search=jumper%20cable)
- [Switch (10x15mm)](https://nl.aliexpress.com/item/1005001513148147.html?spm=a2g0s.9042311.0.0.27424c4dBuHDV5)
- 4x M2.5\*15mm screws
- 4x M3\*15mm screws
- 4x M3\*25mm screws
- 1x 693ZZ ball bearing
- 1-2x 608zz ball bearing(s) (second is optional)

If any are unavailable, try to find an identical alternative.
### 3D-printed parts
All 3D-printed parts can be found on [Thingiverse](https://www.thingiverse.com/thing:5167214). All of the files' names are prefixed with the material it should be printed with and, if applicable, the amount required.

## Schematic
![schematic](https://user-images.githubusercontent.com/27017516/146649582-84fa802a-a21b-4eb1-aa96-c11541feb33e.png)


## Requirements (Raspberry Pi)
- Raspbian Buster
- flask

## Setup (Raspberry Pi)
```bash
git clone --recurse-submodules https://github.com/SinglePaper/CharlesDRbt-RPi.git
sudo nano /etc/rc.local
```
- At the bottom of the file, before ```exit 0```, add ```sudo python3 /home/pi/CharlesDRbt-RPi/receivey.py```
```bash
sudo apt update
sudo apt install uv4l uv4l-raspicam uv4l-raspicam-extras
sudo apt install uv4l-webrtc
```
- Go to ```[raspberrypi-ip]:8080/panel``` and change the following settings:
  - width: 800
  - height: 600
  - format: MJPEG Video (streamable)
  - frame rate: 10
  - Optional: change mirror or rotate settings if necessary  
  - Click 'Apply'

## Usage (Raspberry Pi)
- If you go to ```[raspberrypi-ip]``` now, you should see the camera feed and the controls. The controls should be able to control the motors now.

## Requirements (Windows)
- Git for Windows
- Python 3.7.9 64bit
  - [opencv-python>=4.5.4-dev](https://pypi.org/project/opencv-python/)
  - [tensorflow==2.5.0](https://pypi.org/project/tensorflow/2.5.0/)
  - [labelImg](https://pypi.org/project/labelImg/)
  - [pandas](https://pypi.org/project/pandas/)
  - [object_detection](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html#install-the-object-detection-api)

## Setup (Windows)
```bash
# From within 'Tensorflow' directory 
mkdir workspace
cd workspace
git clone --recurse-submodules https://github.com/SinglePaper/CharlesDRbt.git
cd CharlesDRbt
mkdir data
cd data
mkdir models
cd ..
```
Turn on your Raspberry Pi and wait for it to start up, then run:
```bash
ping raspberrypi.local
```
If host could not be found, change ```raspberrypi.local``` to your Raspberry Pi's ip in ```/detect.py``` and ```/images/collected_images/collect.py```.
## Usage (Training)
- Edit ```/annotations/label_map.pbtxt``` to match your object(s).
- When training for more than one object, change ```num_classes``` in ```models/ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8/pipeline.config``` to your amount of objects.
- Run ```/images/collected_images/collect.py``` and press space to capture images (esc to exit). Start with at least 25, preferably more, and vary background of image.
- From ```/images/collected_images```run ```labelImg ./```.
- For each image, press 'w', draw a square around the object and name it according to its name in ```/annotations/label_map.pbtxt```.
- Divide the gathered images and .xml files over ```/images/train``` and ```/images/test``` in ratio 9:1 respectively. Both should always have images.
- From ```Tensorflow/workspace/CharlesDRbt``` run ```train.bat```.
  - Keep running until total_loss decreases slowly or flatlines. 
    - If this happens before ~0.2, the model will likely be very inaccurate. Consider increasing the size of your database and creating more variation in the environment the images are taken in.
  - Optional: To view training process in graph format, open a second command prompt and from the same directory run ```eval.bat```.
- From the same directory, run ```export.bat``` and give it a name.
- Move the directory with that in ```/exported-models``` to ```/data/models```.
- Copy ```/annotations/label_map.pbtxt``` to the model's directory in ```/data/models```.

## Usage (Detection)
- Turn on the Raspberry Pi.
- Edit lines 3, 4 and 5 in ```/detect.py``` to your liking.
- From ```Tensorflow/CharlesDRbt/``` run ```python detect.py```.
