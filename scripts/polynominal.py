#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray
pub1 = rospy.Publisher('poly_topic', Float64MultiArray, queue_size=10, latch = True)
 

def callback(msg):
    morgen = msg.data[1]**2
    slawamerlou = msg.data[2]**3
    poly_to_send = Float64MultiArray()
    poly_to_send.data = [msg.data[0], morgen, slawamerlou]
    rospy.loginfo(poly_to_send.data)
    pub1.publish(poly_to_send)
 
    
rospy.init_node('poly')
rospy.Subscriber('req_topic', Float64MultiArray, callback, queue_size=10)
rospy.spin()

