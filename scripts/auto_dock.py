#!/usr/bin/env python
import rospy
import actionlib
from fetch_auto_dock_msgs.msg import DockAction, DockGoal

# Create a ROS node
rospy.init_node("dock_the_robot")

# Create an action client
client = actionlib.SimpleActionClient("/dock", DockAction)
client.wait_for_server()

# Create and send a goal
goal = DockGoal()
goal.dock_pose.header.frame_id = "base_link"
goal.dock_pose.pose.position.x = 1.0
goal.dock_pose.pose.orientation.z = 0.0
client.send_goal(goal)
