#!/usr/bin/env python

import rospy
from std_msgs.msg import (Int16, Int16MultiArray)

# Define output vector
output = Int16MultiArray()
output.data = []

class eyebrownEnable():
    def __init__(self):
        pub = rospy.Publisher('eyebrown', Int16MultiArray, queue_size=10)
        rospy.init_node('eyebrownEnable', anonymous=False)
        self.sub_eyebrown_st = rospy.Subscriber('emotion', Int16, self.getEyebrown_st)
        rate = rospy.Rate(50) # 50hz

        # Set normal emotion on eyebrown
        self.emotion = 0
        self.rightY = 20
        self.leftY = 20
        self.rightRotation = 50
        self.leftRotation = 50

        while not rospy.is_shutdown():
            eyebrownEnable.getOutput(self)
            output.data = []
            output.data = [self.rightY, self.leftY, self.rightRotation, self.leftRotation]
            rospy.loginfo(output)
            pub.publish(output)
            rate.sleep()
        
    def getOutput(self):
        if(self.emotion == 0):
            self.rightY = 20
            self.leftY = 20
            self.rightRotation = 50
            self.leftRotation = 50
        elif(self.emotion == 1):
            self.rightY = 30
            self.leftY = 30
            self.rightRotation = 40
            self.leftRotation = 40
        elif(self.emotion == 2):
            self.rightY = 15
            self.leftY = 15
            self.rightRotation = 0
            self.leftRotation = 0
        elif(self.emotion == 3):
            self.rightY = 20
            self.leftY = 20
            self.rightRotation = 100
            self.leftRotation = 100
        elif(self.emotion == 4):
            self.rightY = 70
            self.leftY = 70
            self.rightRotation = 30
            self.leftRotation = 30

    def getEyebrown_st(self, msg):
        self.data = msg.data
        self.emotion = self.data

if __name__ == '__main__':
    try:
        eyebrownEnable()
    except rospy.ROSInterruptException:
        pass