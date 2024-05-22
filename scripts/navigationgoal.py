#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():


    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

   
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = 3.864808
    goal.target_pose.pose.position.y = 4.232503
    goal.target_pose.pose.orientation.w = 0.01
    
    


    client.send_goal(goal)

if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal finished!")
    except rospy.ROSInterruptException:
        rospy.loginfo("The End")
