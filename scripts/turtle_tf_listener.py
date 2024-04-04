#!/usr/bin/env python3
import rospy

import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('turtle_tf_listener')

    listener = tf.TransformListener()

    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(5, 5, 0, 'turtle2')

    turtle_vel = rospy.Publisher('turtle2/cmd_vel', geometry_msgs.msg.Twist, queue_size=1)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans, rot) = listener.lookupTransform('/turtle2', '/turtle1', rospy.Time())
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        def calculate_circular_movement(center_x, center_y, radius, angle):
            x = center_x + radius * math.cos(math.radians(angle))
            y = center_y + radius * math.sin(math.radians(angle))
            return x, y
        center_x = trans[0]
        center_y = trans[1]
        radius = 5
        angle = 0
        angle += 10
        if angle >359:
            angle = 0
        x, y = calculate_circular_movement(center_x, center_y, radius, angle)
        msg = geometry_msgs.msg.Twist()
        msg.linear.x = math.sqrt(x ** 2 + y ** 2)
        msg.angular.z = 2 * math.atan2(trans[1], trans[0])
        turtle_vel.publish(msg)
        rate.sleep()
