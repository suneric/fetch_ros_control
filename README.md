# fetch_ros_control
ros cotnrol fetch freight100

## Robots
- Freight100-1568 ipv4: 192.168.1.11 (hostname:freight1568)
- Freight100-1814 ipv4: 198.168.1.16 (hostname:freight1814)

## Remote computer configuration
1. configure static ip address on robot
2. configure ssh hostname in /etc/hosts (add the remote computer hostname and ip address)
3. In your remote computer, repeat step 2 to add the fetch robot hostname
4. configure [ros network](http://wiki.ros.org/ROS/NetworkSetup), use ROS_HOSTNAME as mentioned in [Fetch Manual](https://docs.fetchrobotics.com/computer.html)
5. install fetch ros packages (assume ros melodic and ubuntu 18.04)
```
sudo apt install ros-melodic-fetch-description ros-melodic-freight-bringup ros-melodic-fetch-tools
```

## Visualize
```
rosrun rviz rviz
```
- add robot model
- change fixed frame to odom


## Control

### teleop control
```
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```

### build a map
```
roslaunch fetch_navigation build_map.launch
```
teleop the robot to build the map of your environment and visualize in rviz

### navigation
clone this repo and run
```
roslaunch fetch_ros_control navigation_test.launch
```
or follow [fetch navigation](https://docs.fetchrobotics.com/navigation.html) toturial

### auto dock
drive the robot to the dock station, make sure the robot is facing to the dock and within 1 meter.
```
python scripts/auto_dock.py
```
