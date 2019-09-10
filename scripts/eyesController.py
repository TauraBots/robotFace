#!/usr/bin/env python
import rospy
import time
import threading
import os
from std_msgs.msg import Int16MultiArray

output = Int16MultiArray()
output.data = []

class emotionEnable():
    def __init__(self):
        pub = rospy.Publisher('eye', Int16MultiArray, queue_size=10)
        rospy.init_node('eyesEnable', anonymous=False)
        self.sub_eyelid_st = rospy.Subscriber('updateEyes', Int16MultiArray, self.getEmotion)
        rate = rospy.Rate(50) # 50hz

        self.xPosition = 50
        self.yPosition = 50

        updateLoop = threading.Thread(name = 'startVideo', target = emotionEnable.startVideo, args = (self,))
        updateLoop.setDaemon(True)
        updateLoop.start()

        while not rospy.is_shutdown():
            output.data = [self.xPosition , self.yPosition]
            rospy.loginfo(output)
            pub.publish(output)
            rate.sleep()

    def getEmotion(self, msg):
        # Receive [startX, startY, endX, endY]
        self.data = msg.data
        startX = self.data[0]
        startY = self.data[1]
        endX = self.data[2]
        endY = self.data[3]
        self.xPosition = int(abs(100 - ((((endX-startX)/2.0)+startX)/6.1538)+55))
        self.yPosition = int(((((endY-startY)*0.2)+startY)/4.6154)+55)

        print(self.data)

    def startVideo(self):
        os.system("rosrun robotFace recognize_video.py --detector faceDoris/src/robotFace/scripts/face_detection_model --embedding-model faceDoris/src/robotface/scripts/openface_nn4.small2.v1.t7 --recognizer faceDoris/src/robotFace/scripts/output/recognizer.pickle --le faceDoris/src/robotFace/scripts/output/le.pickle")

if __name__ == '__main__':
    try:
        emotionEnable()
    except rospy.ROSInterruptException:
        pass



