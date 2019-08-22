# sensehat_driver
**A ROS driver for the Raspberry Pi Sense HAT.**
## Overview
The Sense HAT is an affordable and easy-to-use add-on board for the Raspberry Pi. It is equipped with a multitude of useful sensors including a 9-DoF IMU and various environmental sensors, which makes it an ideal asset for personal robotic projects. This ROS package provides an interface to access the functionalities of the board, and includes a set of ROS nodes and launch files to immediately start extracting sensor data.
## Sense HAT Setup 
- The Sense HAT installation and calibration instructions can be found [here](https://www.raspberrypi.org/documentation/hardware/sense-hat/).
## Installation
### Install from Git Repository
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone --single-branch --branch kinetic-devel https://github.com/joeyjyyang/sensehat_driver.git #kinetic-devel (default branch)
cd .. 
catkin build sensehat_driver
source devel/setup.bash
```
### Example Usage
```
roslaunch sensehat_driver sensehat_imu_compass.launch
```
## Contents
### Nodes 
**Publishers, subscribers, servers, and clients.**
- sensehat_imu_publisher_node(.py)
- sensehat_environment_publisher_node(.py)
- sensehat_compass_display(.py)
- sensehat_temp_diff_server(.py)
- sensehat_imu_subscriber_node(.cpp)
- sensehat_temp_diff_client(.cpp)
### Services
- calc_temp_diff
### Launch Files
- sensehat_imu_compass.launch
	- Publishes 9-DoF IMU data and displays the onboard compass based on heading (yaw) readings. Also runs the generic subscriber which logs orientation in quaternions.
- sensehat_environment.launch
	- Publishes data from environmental sensors, including temperature, relative humidity, pressure, and magnetic field vectors.
### Topics
- /air_pressure
- /magnetic_field
- /imu_orientation_euler
- /imu_orientation_quaternion
- /relative_humidity
- /temperature_celsius
- /temperature_fahrenheit
### Messages
- sensor_msgs/FluidPressure
- sensor_msgs/MagneticField
- sensor_msgs/Imu
- sensehat_driver/IMUOrientationEuler
- sensor_msgs/RelativeHumidity
- sensor_msgs/Temperature
- sensehat_driver/TemperatureFahrenheit
## References
- The Sense HAT API Reference can be found [here](https://pythonhosted.org/sense-hat/api/).
- The sensor_msgs Msg/Srv Documentation can be found [here](http://docs.ros.org/kinetic/api/sensor_msgs/html/index-msg.html).
