cmake_minimum_required(VERSION 3.0.2)
project(move_taleb)

find_package(catkin REQUIRED COMPONENTS
  rospy
  roscpp
  actionlib_msgs
  std_msgs
)

add_action_files(
  DIRECTORY action
  FILES move.action
)

generate_messages(
  DEPENDENCIES
  actionlib_msgs std_msgs
)

catkin_package(
  CATKIN_DEPENDS rospy roscpp actionlib_msgs std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(move_taleb_server src/move_taleb_server.cpp)
target_link_libraries(move_taleb_server ${catkin_LIBRARIES})
add_dependencies(move_taleb_server ${move_taleb_EXPORTED_TARGETS})

add_executable(move_taleb_client src/move_taleb_client.cpp)
target_link_libraries(move_taleb_client ${catkin_LIBRARIES})
add_dependencies(move_taleb_client ${move_taleb_EXPORTED_TARGETS})

