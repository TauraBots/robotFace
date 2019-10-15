#!/usr/bin/env python

import rospy
import time
import threading
from std_msgs.msg import (Int16MultiArray, Int16)
from PyDynamixel import DxlComm, Joint

# Define the output vector
motors = [50] * 12
refinedMotors = [90] * 12

class dataflowEnable():
    def __init__(self):
        rospy.init_node('dataController', anonymous=False)
        
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
        #rospy.spin()

    def getMouth(self, msg):
        global motors
        self.data = msg.data
        motors[0] = int(0.3059*self.data[0])
        motors[1] = int(0.3059*self.data[1])

    def getEye(self, msg):
        global motors
        self.data = msg.data
        motors[2] = self.data[0]
        motors[3] = self.data[1]
    
    def getEyelid(self, msg):
        global motors
        self.data = msg.data
        motors[4] = self.data[0]
        motors[5] = self.data[1]
        motors[6] = self.data[2]
        motors[7] = self.data[3]

    def getEyebrown(self, msg):
        global motors
        self.data = msg.data
        motors[8] = self.data[0]
        motors[9] = self.data[1]
        motors[10] = self.data[2]
        motors[11] = self.data[3]

    #def getNeck(self, msg):
    #    self.data = msg.data
    #    motors[12] = self.data[0]
    #    motors[13] = self.data[1]

    def sendArduino(self):
        while(True):
            global motors
            '''
            Joint0.writeValue(motors[0])
            Joint1.writeValue(motors[1])
            Joint2.writeValue(motors[2])
            Joint3.writeValue(motors[3])
            Joint4.writeValue(motors[4])
            Joint5.writeValue(motors[5])
            Joint6.writeValue(motors[6])
            Joint7.writeValue(motors[7])
            Joint8.writeValue(motors[8])
            Joint9.writeValue(motors[9])
            Joint10.writeValue(motors[10])
            Joint11.writeValue(motors[11])
            '''
            
            time.sleep(0.05)

if __name__ == '__main__':
    try:
        dataflowEnable()
    except rospy.ROSInterruptException:
        pass