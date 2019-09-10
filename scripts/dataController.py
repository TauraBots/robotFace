#!/usr/bin/env python

import rospy
import time
import threading
from std_msgs.msg import (Int16MultiArray, Int16)

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

        #Todos os dados serão convertidos em angulos e enviados para o arduino por aqui...
        print("Em desenvolvimento")

        updateLoop = threading.Thread(name = 'send2Arduino', target = dataflowEnable.sendArduino, args = (self,))
        updateLoop.setDaemon(True)
        updateLoop.start()
        #rospy.spin()

    def getMouth(self, msg):
        self.data = msg.data
        motors[0] = int(0.3059*self.data[0])
        motors[1] = int(0.3059*self.data[1])
        print(self.data)

    def getEye(self, msg):
        self.data = msg.data
        motors[2] = self.data[0]
        motors[3] = self.data[1]
        print(self.data)
    
    def getEyelid(self, msg):
        self.data = msg.data
        motors[4] = self.data[0]
        motors[5] = self.data[1]
        motors[6] = self.data[2]
        motors[7] = self.data[3]
        print(self.data)

    def getEyebrown(self, msg):
        self.data = msg.data
        motors[8] = self.data[0]
        motors[9] = self.data[1]
        motors[10] = self.data[2]
        motors[11] = self.data[3]

    def sendArduino(self):
        while(True):
            time.sleep(0.05)

if __name__ == '__main__':
    try:
        dataflowEnable()
    except rospy.ROSInterruptException:
        pass