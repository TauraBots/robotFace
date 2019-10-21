#!/usr/bin/env python

import rospy
import time
import threading
from std_msgs.msg import (Int16MultiArray, Int16)
from PyDynamixel import DxlComm, Joint

class dataflowEnable():
    def __init__(self):
        rospy.init_node('dataController', anonymous=False)
        rospy.Rate(100) # 100hz

        # Define the output vector
        self.motors = [50] * 12

        self.port = DxlComm('/dev/ttyACM0')
        self.joint = Joint(128)
        self.port.attachJoint(self.joint)

        self.sub_mouth = Int16MultiArray()
        self.sub_mouth.data = []  
        self.sub_mouth = rospy.Subscriber('mouth', Int16MultiArray, self.getMouth)

        self.sub_eye = Int16MultiArray()
        self.sub_eye.data = []  
        self.sub_eye = rospy.Subscriber('eye', Int16MultiArray, self.getEye)

        self.sub_eyelid = Int16MultiArray()
        self.sub_eyelid.data = []  
        self.sub_eyelid = rospy.Subscriber('eyelid', Int16MultiArray, self.getEyelid)

        self.sub_eyebrown = Int16MultiArray()
        self.sub_eyebrown.data = []  
        self.sub_eyebrown = rospy.Subscriber('eyebrown', Int16MultiArray, self.getEyebrown)

        #self.sub_neck = Int16MultiArray()
        #self.sub_neck.data = []  
        #self.sub_neck = rospy.Subscriber('neck', Int16MultiArray, self.getNeck)


        updateLoop = threading.Thread(name = 'send2Arduino', target = dataflowEnable.sendArduino, args = (self,))
        updateLoop.setDaemon(True)
        updateLoop.start()

        rospy.spin()

    def getMouth(self, msg):
        data = msg.data
        #motors[0] = int(0.3059*self.data[0])
        #self.motors[10] = abs(100-data[0])
        self.motors[10] = int(0.3059*data[0])
        #motors[1] = data[1]

    def getEye(self, msg):
        data = msg.data
        self.motors[8] = data[0]
        self.motors[9] = data[1]
    
    def getEyelid(self, msg):
        data = msg.data
        self.motors[4] = data[0]
        self.motors[5] = data[1]
        self.motors[6] = data[2]
        self.motors[7] = data[3]

    def getEyebrown(self, msg):
        data = msg.data
        self.motors[0] = data[0]
        self.motors[1] = data[1]
        self.motors[2] = data[2]
        self.motors[3] = data[3]

        

    #def getNeck(self, msg):
    #    data = msg.data
    #    motors[12] = data[0]
    #    motors[13] = data[1]

    def sendArduino(self):
        while(True):
            # 0 - EyebrowRightHeight
            # 1 - EyebrowLeftHeight
            # 2 - EyebrowRightAngle
            # 3 - EyebrowLeftAngle
            # 4 - EyelidRightUp
            # 5 - EyelidLeftUp
            # 6 - EyelidRightDown
            # 7 - EyelidLeftDown
            # 8 - EyeHorizontal
            # 9 - EyeVertical
            # 10 - Mouth

            print (self.motors)
            
            self.joint.writeValue(4, int(self.motors[4]))
            self.joint.writeValue(5, int(self.motors[5]))
            self.joint.writeValue(6, int(self.motors[6]))
            self.joint.writeValue(7, int(self.motors[7]))
            self.joint.writeValue(10, int(self.motors[10]))
            self.joint.writeValue(0, int(self.motors[0]))
            self.joint.writeValue(1, int(self.motors[1]))
            self.joint.writeValue(2, int(self.motors[2]))
            self.joint.writeValue(3, int(self.motors[3]))
            self.joint.writeValue(8, int(self.motors[8]))
            self.joint.writeValue(9, int(self.motors[9]))
            #self.joint.writeValue(10, int(self.motors[10]))
            
            time.sleep(0.01)

if __name__ == '__main__':
    try:
        dataflowEnable()
    except rospy.ROSInterruptException:
        pass