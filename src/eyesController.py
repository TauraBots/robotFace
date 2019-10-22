#!/usr/bin/env python
import rospy
import time
import threading
import os
from std_msgs.msg import Int16MultiArray, Float64MultiArray
import map as mp

output = Int16MultiArray()
output.data = []

class eyesEnable():
    def __init__(self):
        pub = rospy.Publisher('eye', Int16MultiArray, queue_size=10)
        rospy.init_node('eyesEnable', anonymous=False)
        self.sub_eye = rospy.Subscriber('updateEyes', Float64MultiArray, self.getEyes)
        rate = rospy.Rate(50) # 50hz

        self.xPosition = 50
        self.yPosition = 50

        while not rospy.is_shutdown():
            output.data = [self.xPosition , self.yPosition]
            rospy.loginfo(output)
            pub.publish(output)
            rate.sleep()

    def getEyes(self, msg):
        self.data = msg.data
        self.x = self.data[0]
        self.y = self.data[1]
        self.width = self.data[3]
        self.height = self.data[2]

        self.xPosition = abs(100 - mp.map(0, self.width, 0, 100, self.x))
        self.yPosition = mp.map(0, self.height, 0, 100, self.y)

if __name__ == '__main__':
    try:
        eyesEnable()
    except rospy.ROSInterruptException:
        pass
