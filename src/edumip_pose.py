#!/usr/bin/python

import rospy
from fiducial_msgs.msg import *
from turtlesim.msg import Pose
from tf.transformations import euler_from_quaternion

rospy.init_node("edumip_aruco_pose")

def CallBack(data):

    n = len(data.transforms)
    msg = Pose() 
    i = 0
    while i < n:
     k = data.transforms[i].fiducial_id
     p = rospy.Publisher("edumip"+str(k)+"/pose", Pose, queue_size=10)
     msg.x = data.transforms[i].transform.translation.x 
     msg.y = data.transforms[i].transform.translation.y
     euler = euler_from_quaternion([data.transforms[i].transform.rotation.x, data.transforms[i].transform.rotation.y, data.transforms[i].transform.rotation.z, data.transforms[i].transform.rotation.w])
     msg.theta = euler[2]
     p.publish(msg)
     i=i+1

def listener():

	s = rospy.Subscriber("/fiducial_transforms", FiducialTransformArray, CallBack)

	rospy.spin()

if __name__ == '__main__':

     listener()



