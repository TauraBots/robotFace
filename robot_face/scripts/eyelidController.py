#!/usr/bin/env python

from __future__ import division
import rospy
import time
import threading
from std_msgs.msg import (Int16MultiArray, Int16)


# Define angles for close eyelid
zeroTopLeft = 0
zeroTopRight = 0
zeroBottomLeft = 0
zeroBottomRIght = 0

# Define angles to open eyelid
maxTopLeft = 0
maxTopRight = 0
maxBottomLeft = 0
maxBottomRight = 0

# Define normal statics parameters
h = 30
frequency = 4 

# Define the output vector
output = Int16MultiArray()
output.data = []

#animationUpper = float(3)
animationUpper = 0
#animationDown = float (3)
animationDown = 0

class eyelidEnable():
    def __init__(self):
        pub = rospy.Publisher('eyelid', Int16MultiArray, queue_size=10)
        rospy.init_node('eyelidEnable', anonymous=False)
        self.sub_eyelid_st = rospy.Subscriber('emotion', Int16, self.getEyelid_st)
        self.sub_eyelid_dn = Int16MultiArray()
        self.sub_eyelid_dn.data = []   
        self.sub_eyelid_dn = rospy.Subscriber('eye', Int16MultiArray, self.getEyelid_dn)
        rate = rospy.Rate(80) # 80hz

        self.y = 0
        self.animation = 0
        self.upper = 0
        self.down = 0

        # Start blink thread
        blinkLoop = threading.Thread(name = 'blink', target = eyelidEnable.blink, args = (self,))
        blinkLoop.setDaemon(True)
        blinkLoop.start()

        while not rospy.is_shutdown():
            eyelidEnable.getOutput(self)
            output.data = []
            output.data = [self.upper, self.upper, self.down, self.down]
            rospy.loginfo(output)
            pub.publish(output)
            rate.sleep()
        
    def getOutput(self):
        if (self.animation == 1):
            print("Piscando...")
        elif(self.animation == 0): 
            eyelidEnable.setValues(self)

    def setValues(self):
        if(self.y > 50):
            self.upper = h + self.y*2 - 100
            self.down = h
        elif(self.y < 50):
            self.upper = h
            self.down = 100 - (h + self.y)
        elif(self.y == 50):
            self.upper = h
            self.down = h

    def getEyelid_dn(self, msg):
        self.data = msg.data
        self.y = self.data[1] - 50
        print(self.data)

    def getEyelid_st(self, msg):
        self.data = msg.data
        if(self.data == 0):
            self.h = 30
            self.frequency = 4
        elif(self.data == 1):
            self.h = 40
            self.frequency = 3
        elif(self.data == 2):
            self.h = 20
            self.frequency = 6
        elif(self.data == 3):
            self.h = 25
            self.frequency = 3
        elif(self.data == 4):
            self.h = 50
            self.frequency = 4
        #print(self.data)
    
    def blink(self):
        while(True):
            self.animation = 1
            eyelidEnable.setValues(self)
            x = 0
            if(self.y > 50):
                animationUpper = (h + self.y*2 - 100)/50
                animationDown = (h)/50
            elif(self.y < 50):
                animationUpper = (h)/50
                animationDown = (100-(h + self.y))/50
            elif(self.y == 50):
                animationUpper = (h)/50
                animationDown = (h)/50

            while(x<50):
                self.upper = self.upper - animationUpper
                self.down = self.down - animationDown
                #print("subtrai: "+str(self.upper))
                time.sleep(0.005)
                x = x + 1
            x = 0
            while(x<50):
                self.upper = self.upper + animationUpper
                self.down = self.down + animationDown
                #print("soma: "+str(self.upper))
                time.sleep(0.005)
                x = x + 1
            self.animation = 0
            time.sleep(frequency)  
            

if __name__ == '__main__':
    try:
        eyelidEnable()
    except rospy.ROSInterruptException:
        pass