#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseResult
from geometry_msgs.msg import PoseStamped

class MoveBaseServer(object):
    def __init__(self):
        # Initialize the action server
        self.server = actionlib.SimpleActionServer('move_base', MoveBaseAction, self.execute, False)
        self.server.start()

    def execute(self, goal):
        # Create a goal position from the input message
        goal_position = goal.goal

        # Move the robot to the goal position
        # (This is where you would implement your robot's motion control algorithm)
        rospy.loginfo("Moving robot to goal position: %s", goal_position)

        # Send a success message to the client when the task is complete
        result = MoveBaseResult()
        result.success = True
        self.server.set_succeeded(result)

if __name__ == '__main__':
    rospy.init_node('move_base_server')
    server = MoveBaseServer()
    rospy.spin()
