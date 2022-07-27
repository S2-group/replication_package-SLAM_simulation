# replication_package-SLAM_simulation

Replication package of SLAM Simutalion - Kwame's Thesis.

## Setup

This setup assumes you are running the experiment on Ubuntu 20.0.4 and have ROS 1 installed (full desktop noetic) on your laptop.
https://wiki.ros.org/Installation/Ubuntu

You can test if all these were installed properly by sourcing ROS (source /opt/ros/noetic/setup.bash) and running roscore.

In order to run the missions you will need to follow the following tutorials for setting up the robot in simulation:

<!-- You can test if all these were installed properly by sourcing ROS (source /opt/ros/noetic/setup.bash), running roscore, running bringup on the robot, and then running the teleoperation node from your computer as per this tutorial: https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_operation/ -->

Install TurtleBot3 dependent packages for noetic
https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup

Build the TurtleBot3 packages from source in catkin_ws <br/>

```bash
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src/
$ git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3.git
$ git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations
```

After this is done, place the s2_slam_sim package from the repo into the catkin_ws/src folder. Once you've done this, run:

```bash
$ cd ~/catkin_ws && catkin_make
$ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
```

Add the following arena configuration into the turtlebot3_simulations folder

- In folder /catkin_ws/src/turtlebot3_simulations/turtlebot3_gazebo/worlds add the turtlebot3_arena.world file from the repo
- In folder /catkin_ws/src/turtlebot3_simulations/turtlebot3_gazebo/models add turtlebot3_arena2 folder from the repo
- In folder /catkin_ws/src/turtlebot3_simulations/turtlebot3_gazebo/launch add turtlebot3_arena.launch from the repo

You will also need to install the following ROS packages on your remote PC for Gazebo simulation:

And the following ROS SLAM packages on your laptop:

- `$ sudo apt-get install ros-noetic-gmapping`
- `$ sudo apt-get install ros-noetic-hector-slam`
- `$ sudo apt-get install ros-noetic-slam-karto`
- `$ sudo apt-get install ros-noetic-slam-toolbox`

You will also need to install the following ROS packages on your remote PC for Gazebo simulation:

In order for the python files to run correctly, you'll need to install:

- `$ pip3 install psutil` (cpu memory profiler)
- `$ sudo apt install wireshark` (network profiler) - answer yes to "should non-superusers be able to capture packets

Now the folders for the data collection should be created.

Remote PC:

- A folder for your rosbag files (can be anywhere)
- A folder for your network data - simply create the folder "Robot_Data" in your /home/[username]/ directory.
- A folder for your cpu/mem profiler data named Robot_Data (should have the path /home/[username]/Robot_Data)

- export TURTLEBOT3_MODEL=burger
- export PATH_TO_BAG=/path/to/where/bagfile/should/be/stored/SLAM.bag

## Running

For testing purposes:
Change the values in /catkin_ws/src/turtlebot3_simulations/turtlebot3_gazebo/launch/turtlebot3_arena.launch:

```bash
    <arg name="gui" value="true"/>
    <arg name="headless" value="false"/>
```

Open new terminal and run this command to see the arena and TurttleBOT3: <br/>

```bash
$ roslaunch turtlebot3_gazebo turtlebot3_arena.launch
```

When done testing, change it back to

```bash
    <arg name="gui" value=“false”/>
    <arg name="headless" value=“true”/>
```

First you need to source ROS on the remote PC to run roscore: <br/>

````bash
$ source /opt/ros/noetic/setup.bash
$ roscore
``

Now you can run the setup launch file on the remote PC (this can be skipped for replication):

```bash
$ roslaunch s2_slam_sim SLAM_mission_setup.launch
```

With this running, you can teleoperate the robot to record the path it will take. Once the map on RVIZ is complete, you can kill the running nodes on the remote PC to stop recording to the bag file.

Now you can run the mission controller on the remote PC:

```bash
$ rosrun s2_slam_sim remote_SLAM_controller.py
```

Once running, fill in all fields polled by the programs. Once you've done this, terminal should say "Press enter key to begin mission 1" <br/>
![alt text](https://i.imgur.com/1cmvOLS.png)'

retrieve the files manually on the remote PC.
````
