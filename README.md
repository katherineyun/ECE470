# ECE470 Robot Simulation Project

The goal of this project is to simulate a robot using program written in python (or programming language of your choice) to perform a specific task. This README file will include instructions on how to install a simulation platform and program a robot to move its joints.


## Getting Started

The instructions written in this file are specifically for running the simulation on Linux system (Ubuntu 16.04).

### Prerequisites

The simulation platform we used in this project is V-rep and all programming code will be written in Python3.

### installing V-REP

Step 1. Download V-REP
  You can download V-REP for Linux system by following this link http://www.coppeliarobotics.com/downloads.html.

Step 2. Install V-REP
  Next, after the V-REP zip is downloaded, you can unzip the file by entering the followings in a terminal
  ```
  cd Downloads
  sh V-REP_PRO_EDU_V3_5_0_Linux.sh
  ```
Step 3. Launch V-REP
  You can run v-rep from its own directory by enter the followings in a terminal
  ```
  cd V-REP_PRO_EDU_V3_5_0_Linux
  ./vrep.sh
  ```
### Run Python Project

You can create a folder in parallel to the v-rep folder and run your python code from there. However, in order to successfully import vrep package, you also need to add vrep.py, vrepConst.py and remoteApi.so to the folder, which can all be found in the V-REP folder that you have just unziped.

```
  cd ECE470_Final
  python ./cp1.py
  ```

## Authors

* **Katherine Yun**
* **Sophie Jin**


## Acknowledgments

* We used Prof. Bretl's test code as a starter to implement our project.
