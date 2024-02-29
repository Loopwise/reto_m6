cmake_minimum_required(VERSION 3.0.2)
project(reto_m6)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  joint_state_publisher
  joint_state_publisher_gui
  roscpp
  rospy
  rviz
  sensor_msgs
  std_msgs
  tf2
  urdf
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES reto_m6
#  CATKIN_DEPENDS roscpp rospy rviz sensor_msgs std_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS src/reto_topic_pub.py src/reto_topic_sub.py src/reto_pointcloud.py src/reto_filter_pub.py src/reto_filter.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)