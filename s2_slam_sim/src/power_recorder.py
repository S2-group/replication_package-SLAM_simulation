#!/usr/bin/env python3

import rospy
import rosbag
from datetime import datetime
import time
import os
import subprocess


#slam_gmapping
#hector_mapping
#sync_slam_toolb
#slam_karto

PATH_TO_BAG = os.environ["PATH_TO_BAG"]
bag = rosbag.Bag(PATH_TO_BAG)
MISSION_TIME = bag.get_end_time()-bag.get_start_time()

var1=str(time.time())
# var1=str(datetime.now())
var2= MISSION_TIME

# subprocess.call("sleep.sh", shell=True)

def recordPower():
    # subprocess.call("~/catkin_ws/src/s2_slam/src/record_power.sh", shell=True)
    os.system("sudo /home/parallels/catkin_ws/src/s2_slam_sim/src/record_power.sh {} {}".format(var1, var2))

if __name__ == "__main__":
    rospy.init_node("power_recorder")
    recordPower()
