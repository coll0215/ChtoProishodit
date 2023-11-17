#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16

rospy.init_node('prikolist')
pub = rospy.Publisher('my_cringe_topic', Int16, queue_size=10)
cringepub = rospy.Publisher('my_clueless_topic', Int16, queue_size=10)
rate = rospy.Rate(10)
chislo = 0
nextchislo = 0

def start_prikolist():
    msg = Int16()
    global chislo
    while chislo <=98 and not rospy.is_shutdown(): 
        chislo = chislo+2
        rospy.loginfo(chislo)
        msg.data = chislo
        pub.publish(msg)
        rate.sleep()
        
    while chislo >=100 and not rospy.is_shutdown(): 
        global nextchislo
        nextchislo = nextchislo+2
        rospy.loginfo(nextchislo)
        msg.data = nextchislo
        cringepub.publish(msg)
        rate.sleep()
    
try:
    start_prikolist()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
