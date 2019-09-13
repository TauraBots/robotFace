#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int16MultiArray

output = Int16MultiArray()

class neck():
    def __init__(self):
        rospy.init_node('neckController', anonymous=False)
        self.sub_eyes = rospy.Subscriber('eyes', Int16MultiArray, self.getEyes)

        pub = rospy.Publisher('neck', Int16MultiArray, queue_size=10)
        rate = rospy.Rate(50) # 50hz

        self.xPosition = 50
        self.yPosition = 50

        while not rospy.is_shutdown():
            neck.updateValues(self)
            output.data = [self.xPosition , self.yPosition]
            rospy.loginfo(output)
            pub.publish(output)
            rate.sleep()

    def getEyes(self, msg):
        self.data = msg.data
        self.xImage = self.data[0]
        self.yImage = self.data[1]

    def updateValues(self):
        print("Trabalhando nisso")
