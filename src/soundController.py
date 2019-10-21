#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty, Int
import subprocess as sp

rospy.init_node('soundEnable', anonymous=False)
sub_sound = rospy.Subscriber('sendSound', Int, getSound)
pub = rospy.Publisher('finishedSound', Empty)
empty = Empty()
rospy.spin()

def getSound(msg):
    data = msg.data
    sp.call('mplayer', '{}.mp3'.format(str(data)))
    pub.publish(empty)
