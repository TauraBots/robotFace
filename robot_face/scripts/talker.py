#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16MultiArray
import math
import numpy as np

def talker():
    pub = rospy.Publisher('chatter', Int16MultiArray, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(5) # 10hz

    hello_array = Int16MultiArray()
    hello_array.data = []
    x = 0

    while not rospy.is_shutdown():
        hello_array.data = [conta(x+0),conta(x+1),conta(x+2),conta(x+3),conta(x+4),conta(x+5),conta(x+6),conta(x+7),conta(x+8),
        conta(x+9),conta(x+10),conta(x+11),]
        x = x + 1
        rospy.loginfo(hello_array)
        pub.publish(hello_array)
        rate.sleep()

def conta(n):
    return int(50 + 25*(np.sin(n / 8.3)) + 10*(np.sin(n / 7.5)) - 5*(np.sin(n / 1.5)))
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
