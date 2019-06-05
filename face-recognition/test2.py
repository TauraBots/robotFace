#(0 - 5)(1 - 4)(2 - 2)(3 - 3)(4 - 6)(5 - 7)(6 - 8)(7 - 9)(8 - 10)(9 - 11)
#git clone git@github.com:TauraBots/robot-face.git RostoAnimatronico
import time
from PyDynamixel.pyjoints import DxlComm, Joint

ardbus = DxlComm("/dev/ttyACM2")

arduino = Joint(128)

ardbus.attachJoint(arduino)

#10 - 180 / 60 - 130

while(True):
    arduino.writeValue(5, 60)
    arduino.writeValue(4, 130)
    #arduino.writeValue(3, 105)
    #arduino.writeValue(2, 105)
    arduino.writeValue(7, 90) # Giro
    arduino.writeValue(6, 90) # Giro
    arduino.writeValue(5, 30)
    arduino.writeValue(4, 160)
    #arduino.writeValue(3, 105)
    #arduino.writeValue(2, 105)
    arduino.writeValue(7, 40) # Giro
    arduino.writeValue(6, 140) # Giro
    time.sleep(2)


#arduino.writeValue(6, 180)
#arduino.writeValue(7, 100)
#arduino.writeValue(5, 60)
#arduino.writeValue(4, 120)
#while(1):
#    arduino.writeValue(6, 180)
#    arduino.writeValue(7, 110)
#    arduino.writeValue(5, 60)
#    arduino.writeValue(4, 120)
#    time.sleep(.1)
#    arduino.writeValue(6, 160)
#    arduino.writeValue(7, 130)
#    arduino.writeValue(5, 120)
#    arduino.writeValue(4, 60)
#    time.sleep(.1)
#    arduino.writeValue(6, 180)
#    arduino.writeValue(7, 110)
#    arduino.writeValue(5, 80)
#    arduino.writeValue(4, 100)
#    time.sleep(.1)
#    arduino.writeValue(6, 180)
#    arduino.writeValue(7, 110)
#    arduino.writeValue(5, 120)
#    arduino.writeValue(4, 60)


# base da rotacao da sombrancelha
#eyeB_left = 180
#eyeB_right =  0
#rotacao = 30

#def sombrancelha (eyeB_left, eyeB_right, rotacao):
#    arduino.writeValue(8, eyeB_left+rotacao)
#    arduino.writeValue(9, eyeB_right+rotacao)

#i = 5
#while(1):
#    while(i<150):
#        i = i + 1
#        arduino.writeValue(4, i) #EyeBrown
#        arduino.writeValue(5, 185-i) #EyeBrown
#        arduino.writeValue(6, i)
#        arduino.writeValue(7, i)
#    while(i>5):
#        i = i - 1
#        arduino.writeValue(4, i) #EyeBrown
#        arduino.writeValue(5, 185-i) #EyeBrown
#        arduino.writeValue(6, i)
#        arduino.writeValue(7, i)