#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseStamped

def movebase_client():
    # Initialize the ROS node
    rospy.init_node('movebase_client')

    # Create an action client for move_base
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    # Create a goal object and set its position
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = 1.0
    goal.target_pose.pose.position.y = 2.0
    goal.target_pose.pose.orientation.w = 1.0

    # Send the goal to move_base
    client.send_goal(goal)

    # Wait for move_base to complete the task
    client.wait_for_result()

    # Check if the task was successful
    if client.get_state() == actionlib.GoalStatus.SUCCEEDED:
        rospy.loginfo("Goal reached successfully")
        return True
    else:
        rospy.loginfo("Failed to reach the goal")
        return False

if __name__ == '__main__':
    movebase_client()
