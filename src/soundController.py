#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty, Int16
import subprocess as sp

def getSound(msg):
    data = msg.data
    sp.call('mplayer', 'media/{}.mp3'.format(str(data)))
    pub.publish(empty)

rospy.init_node('soundEnable', anonymous=False)
sub_sound = rospy.Subscriber('sendSound', Int16, getSound)
pub = rospy.Publisher('finishedSound', Empty)
empty = Empty()
rospy.spin()


