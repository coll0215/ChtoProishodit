#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray

rospy.init_node('summ')
pub2 = rospy.Publisher('summ_topic', Float64, queue_size=10, latch = True)

def callback(msg):
    oxxymiron = msg.data[0] + msg.data[1] + msg.data[2]
    pub2.publish(oxxymiron)

rospy.init_node('summ')
rospy.Subscriber('poly_topic', Float64MultiArray, callback, queue_size=10)
rospy.spin()
