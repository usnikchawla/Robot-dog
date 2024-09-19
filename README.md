# Modeling and Dynamic Control of a Quadrupled

## Authors

- [@usnikchawla, @abdulmohammed]



## Dependencies to run the codes

1. Python 2  should be installed on your system.
2. ROS noetic full-desktop installation
3. PyQt4 should be installed along with SIP

    Run
```bash
  $ sudo apt-get install ros-noetic-ros-control ros-noetic-ros-controllers
```


## Instructions to build the package
1.Download the attachment on Canvas to your local machine

2.Unzip the attachment to find the "DreamWalker" package along with report, assembly files and video submissions.
    
3.Place the package in your catkin_ws
    
4.Open a new terminal and got to your catkin_ws by running $ cd ~/catkin_ws
    
5.Run $ catkin build or $ catkin_make to build the package.
    
6.To source ROS, make sure you run $ source ~/catkin_ws/devel/setup.bash in all the terminals you open

## Instructions to check leg movement of the robot using the custom designed Gui

1.Open a command prompt or terminal and source ROS.

2.Run $ roslaunch dreamwalker_simulation test.launch in the first terminal to spawn quadruple in the gazebo env.
    
3.Press 'Forward' to  synchronus gait sequence being implemented for forward motion.
    
4.Similary press other keys to the custom designed gaits.
    
6.The Manual and Automatic button at the button at the bottom are used to select the maual mode or the automatic trajectory follow mode for the robot.
Since Trajectory following could not be implemented so these buttons are redundant at the instant.
    

## Instructions to control the quadruple through Teleop 

1.Open a command prompt or terminals and source ROS.

2.Run $ roslaunch dreamwalker_simulation test2.launch in the terminal to spawn quadruple in the gazebo env.

3.After the above step a GUI launches which helps you control the robot.

4.The bot in the current configuration runs slow so please be patient.
# Robot-dog
# Robot-dog
