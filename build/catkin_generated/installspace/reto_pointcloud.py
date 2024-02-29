#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import PointCloud2, PointField
from sensor_msgs import point_cloud2
from std_msgs.msg import Header
import numpy as np

def point_list_square():
    length = 10
    n = 7
    point_list = []
    for i in np.linspace(-length, length, n):
        for j in np.linspace(-length, length, n):
            if i == -length or i == length or j == -length or j == length:
                point_list.append([i, j, 0, 0xFF0000]) 

    return point_list

def point_list_circle():
    r = 10
    n = 16
    point_list = []
    for i in range(n):
        theta = 2 * np.pi * i / n
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        point_list.append([x, y, 0, 0xFF0000])

    return point_list

def generate_point_cloud(i):
    fields = [PointField('x', 0, PointField.FLOAT32, 1),
            PointField('y', 4, PointField.FLOAT32, 1),
            PointField('z', 8, PointField.FLOAT32, 1),
            PointField('rgb', 12, PointField.UINT32, 1)]
    header = Header()
    header.frame_id = "base_link"

    point_list = point_list_circle() if i%2 else point_list_square()

    cloud = point_cloud2.create_cloud(header, fields, point_list)

    return cloud

def main():
    i = 0
    rospy.init_node('pointcloud_publisher_node', anonymous=True)
    pub = rospy.Publisher('pointcloud_topic', PointCloud2, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        cloud = generate_point_cloud(i)
        pub.publish(cloud)
        rate.sleep()
        i += 1

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
