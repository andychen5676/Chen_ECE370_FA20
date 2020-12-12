rosservice call gazebo/delete_model cc_robot
rosrun gazebo_ros spawn_model -file model.sdf -sdf -model cc_robot -y 0.0 -x 0.0 -z 5.0