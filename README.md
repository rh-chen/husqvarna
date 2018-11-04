# ROS project with Husqvarna Research package
The project was developed during the MMKF15 course at LTH. This is a very simple package which can be used quite early during your project to give a brief understanding of how ROS, and HRP works.

## Installing
1. Clone the project into catkin/src.
2. 'catkin_make' in the catkin_ws folder. Make sure you have installed the HRP packages before.
3. If you write 'rospack find husqvarna', the terminal should return the location of the installed package.
4. Go to the husqvarna folder, should be catkin_ws/src/husqvarna.
5. Run 'roslaunch husqvarna launch_drive.launch' and gazebo should start with an empty world, and the husqvarna mower.

## Making the mower move
1. Open a new terminal, go to catkin_ws
2. Run 'rostopic pub /target geometry_msgs/Pose '{position: {x: 2, y: 1}}' to make it move to (2, 1).
