#!/usr/bin/python

from PyDynamixel import DxlComm, Joint
import alsaaudio, time, audioop
import rospy
from std_msgs.msg import Int16MultiArray
import math
import numpy as np

# Define the output vector
output = Int16MultiArray()
output.data = []

class mouthEnable():
    pub = rospy.Publisher('mouth', Int16MultiArray, queue_size=10)
    rospy.init_node('mouthEnable', anonymous=False)
    rospy.Rate(100) # 100hz
    
    #port = DxlComm('/dev/ttyACM0')
    #joint = Joint(128)
    #port.attachJoint(joint)

    #bus = DxlComm('/dev/ttyUSB0')
    #j = Joint(128)
    #bus.attachJoint(j)
    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)

    # Set attributes: Mono, 8000 Hz, 16 bit little endian samples
    inp.setchannels(1)
    inp.setrate(8000)
    inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    inp.setperiodsize(160)

    while not rospy.is_shutdown():
        l,data = inp.read()
        if l:
            vlr = (audioop.max(data,2) - 200) * 180 / 20000
            #j.writeValue(4,vlr)
            #print(audioop.max(data, 2)/100)
            value = audioop.max(data, 2)/100
            value = int(0.3059*value)
            output.data = []
            output.data = [value, abs(100 - value)]
            #joint.writeValue(10, int(abs(100-value)))
            rospy.loginfo(output)
            pub.publish(output)
            #rate.sleep()
        #time.sleep(.001)

if __name__ == '__main__':
    try:
        mouthEnable()
    except rospy.ROSInterruptException:
        pass
