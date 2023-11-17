#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray

rospy.init_node('req')
pub = rospy.Publisher('req_topic', Float64MultiArray, queue_size=10, latch = True)
rate = rospy.Rate(10) 


def start_req():
    one = rospy.get_param('/req/one')
    anotherone = rospy.get_param('/req/anotherone')
    andanotherone = rospy.get_param('/req/andanotherone')
    req_to_send = Float64MultiArray()
    req_to_send.data = [one, anotherone, andanotherone]
    pub.publish(req_to_send)
    rate.sleep()
    
def callback(msg):
    rospy.loginfo(msg.data)  
    
    
rospy.Subscriber('summ_topic', Float64, callback, queue_size=10)    

    
try:
    start_req()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
