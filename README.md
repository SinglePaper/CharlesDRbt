# Charles D. Robot
Charles D. Robot can detect objects and center them in the frame. This guide can be used to recreate the results as seen in this [YouTube video](https://youtu.be/6JhAzuDE4sk).

## Building the robot
### Electronics
The following electronics are required for the build. If any are unavailable, try to find an identical alternative.
- []

### 3D-printed parts
All 3D-printed parts can be found on [Thingiverse](https://www.thingiverse.com/thing:5167214). All of the files' names are prefixed with the material it should be printed with and, if applicable, the amount required.

## Requirements
- 

## Setup
```bash
git clone --recurse-submodules git@git.liacs.nl:s2619369/ea-a2.git
cd ea-a2
git submodule update --init --recursive
cd IOHexperimenter
mkdir build
mkdir INSTALL
cd build
cmake .. && sudo make install
mkdir ../external/fmt/build
cd ../external/fmt/build
cmake .. && sudo make install
```

## Usage
- 
