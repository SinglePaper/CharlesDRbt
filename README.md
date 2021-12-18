# Charles D. Robot
Charles D. Robot can detect objects and center them in the frame. This guide can be used to recreate the results as seen in this [YouTube video](https://youtu.be/6JhAzuDE4sk).

## Building the robot
### Electronics
The following electronics are required for the build:
- [Raspberry Pi Zero WH](https://www.kiwi-electronics.nl/nl/raspberry-pi-zero-wh-header-voorgesoldeerd-3328?search=raspberry%20pi%20zero&page=2)
- [Raspberry Pi Zero camera](https://nl.aliexpress.com/item/32788881215.html?spm=a2g0s.9042311.0.0.27424c4dMKKQ5k)
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

## Requirements (Raspberry Pi)
- 

## Setup (Raspberry Pi)
```bash

```

## Requirements (Windows)
- conda
- Python 3
- cv2>=4.5.4-dev
- tensorflow==2.5.0
- [object_detection](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html#install-the-object-detection-api)
- numpy>=1.19.5

## Setup (Windows)
```bash
git clone --recurse-submodules git@github.com:SinglePaper/CharlesDRbt.git
```

## Usage
- 
