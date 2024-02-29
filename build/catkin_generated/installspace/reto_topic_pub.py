#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def reto_pub():
    pub = rospy.Publisher('Chat', String, queue_size=10)
    rospy.init_node('reto_pub', anonymous=True)
    rate = rospy.Rate(10) # Frecuencia 10 Hz

    while not rospy.is_shutdown():
        msg_str = 'M6 Reto'
        pub.publish(msg_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        reto_pub()
    except rospy.ROSInterruptException:
        pass