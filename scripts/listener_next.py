#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16

def callback(msg):
    rospy.loginfo(msg.data)

rospy.init_node('roflerzhostkiy')
rospy.Subscriber('my_clueless_topic', Int16, callback, queue_size=10)
rospy.spin()
