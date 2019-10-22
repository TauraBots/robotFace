#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty, Int16, Bool
import os

def getSound(msg):
    data = msg.data
    print (data)
    data = 'mpv /home/victor_kich/faceDoris/src/robotFace/src/media/'+str(data)+'.mp3'
    os.system(data)
    pub.publish(True)

rospy.init_node('soundEnable', anonymous=False)
sub_sound = rospy.Subscriber('sendSound', Int16, getSound)
pub = rospy.Publisher('finishedSound', Bool, queue_size=1)
#empty = Empty()
rospy.spin()
