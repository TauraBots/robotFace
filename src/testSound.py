#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty, Int16, Bool

def callback(msg):
    data = msg.data
    print (data)

rospy.init_node('sendEnable', anonymous=False)
sub_finish = rospy.Subscriber('finishedSound', Bool, callback)
pub = rospy.Publisher('sendSound', Int16, queue_size=1)
send = 10
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    pub.publish(send)
    rate.sleep()
    pass
