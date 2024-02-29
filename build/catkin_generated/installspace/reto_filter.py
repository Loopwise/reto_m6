#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import PointCloud2, PointField
from sensor_msgs import point_cloud2
from std_msgs.msg import Header
import numpy as np

def callback(data):
    gen = point_cloud2.read_points(data, skip_nans=True)
    point_list = list(gen)
    point_list = [list(point) for point in point_list]

    fields = [PointField('x', 0, PointField.FLOAT32, 1),
            PointField('y', 4, PointField.FLOAT32, 1),
            PointField('z', 8, PointField.FLOAT32, 1),
            PointField('rgb', 12, PointField.UINT32, 1)]
    header = Header()
    header.frame_id = "base_link"

    r = 3.5
    for i in range(len(point_list)):
        x = point_list[i][0]
        y = point_list[i][1]
        if x**2 + y**2 <= r**2:
            point_list[i][3] = 0xFF0000
        else:
            point_list[i][3] = 0x00FFFF

    cloud = point_cloud2.create_cloud(header, fields, point_list)

    pub.publish(cloud)
    rospy.loginfo("Nube de puntos publicada")

if __name__ == '__main__':
    try:
        rospy.init_node('pointcloud_filter', anonymous=True)
        pub = rospy.Publisher('pointcloud_topic', PointCloud2, queue_size=10)
        rospy.Subscriber('pointcloud_unfiltered_topic', PointCloud2, callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
