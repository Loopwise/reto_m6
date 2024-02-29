#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    print(data.data)

def reto_sub():
    rospy.init_node('reto_sub', anonymous=True)

    rospy.Subscriber('Chat', String, callback)

    rospy.spin()

if __name__ == '__main__':
    reto_sub()