#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import PointCloud2, PointField
from sensor_msgs import point_cloud2
from std_msgs.msg import Header
import numpy as np

def generate_point_cloud_square():
    fields = [PointField('x', 0, PointField.FLOAT32, 1),
            PointField('y', 4, PointField.FLOAT32, 1),
            PointField('z', 8, PointField.FLOAT32, 1),
            PointField('rgba', 12, PointField.UINT32, 1)]
    header = Header()
    header.frame_id = "base_link"

    # Creamos la nube de puntos en forma de cuadrado
    length = 10
    n = 7
    point_list = []
    for i in np.linspace(-length/2, length/2, n):
        for j in np.linspace(-length/2, length/2, n):
            point_list.append([i, j, 0, 0xFFFFFF]) 

    cloud = point_cloud2.create_cloud(header, fields, point_list)

    return cloud

def main():
    rospy.init_node('pointcloud_publisher_node', anonymous=True)
    pub = rospy.Publisher('pointcloud_unfiltered_topic', PointCloud2, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        cloud = generate_point_cloud_square()
        pub.publish(cloud)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass