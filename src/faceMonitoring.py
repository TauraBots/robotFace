#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt5 import (QtGui, QtCore, QtWidgets)
from PyQt5.QtWidgets import (QLineEdit, QVBoxLayout, QGridLayout, QHBoxLayout, QLabel)
import functools
import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.figure import Figure
from matplotlib.animation import TimedAnimation
from matplotlib.lines import Line2D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import time
import threading
import rospy
from std_msgs.msg import (Int16MultiArray, Int16)

def setCustomSize(x, width, height):
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(x.sizePolicy().hasHeightForWidth())
    x.setSizePolicy(sizePolicy)
    x.setMinimumSize(QtCore.QSize(width, height))
    x.setMaximumSize(QtCore.QSize(width, height))

emotion = 0
motors = [50]*12

class Env():
    def __init__(self):
        rospy.init_node('faceMonitoring', anonymous=False)
        
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

        # Start blink thread
        blinkLoop = threading.Thread(name = 'publishEmotion', target = Env.publishEmotion, args = (self,))
        blinkLoop.setDaemon(True)
        blinkLoop.start()

    def publishEmotion(self):
        pub = rospy.Publisher('updateEmotion', Int16, queue_size=10)
        rate = rospy.Rate(50) # 50hz
        while not rospy.is_shutdown():
            rospy.loginfo(emotion)
            pub.publish(emotion)
            rate.sleep()

    def getMouth(self, msg):
        self.data = msg.data
        motors[0] = int(0.3059*self.data[0])
        motors[1] = int(0.3059*self.data[1])
        print(self.data)

    def getEye(self, msg):
        self.data = msg.data
        motors[2] = self.data[0] - 50
        motors[3] = self.data[1] - 50
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

class CustomMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CustomMainWindow, self).__init__()

        # Define the geometry of the main window
        self.setGeometry(200, 200, 1120, 700)
        self.setWindowTitle("Doris Face")

        # Create frame and set principal layout
        self.frame = QtWidgets.QFrame(self)
        self.principalBox = QHBoxLayout()
        self.frame.setLayout(self.principalBox)
        self.frame.setStyleSheet("background-color:white;")
        self.setCentralWidget(self.frame)

        # Create and set left principal layout
        self.leftLayout = QVBoxLayout()
        self.principalBox.addLayout(self.leftLayout)
 
        # Create and set right principal layout
        self.rightLayout = QVBoxLayout()
        self.principalBox.addLayout(self.rightLayout)

        # Place the button
        self.buttonExit = QtWidgets.QPushButton(text = 'Exit')
        setCustomSize(self.buttonExit, 100, 50)
        self.buttonExit.clicked.connect(self.buttonActionExit)
        self.leftLayout.addWidget(self.buttonExit)

        # Create and set force angles tab and button division layout
        self.forceAnglesTab = QHBoxLayout()
        self.rightLayout.addLayout(self.forceAnglesTab)
        self.buttonDivision = QHBoxLayout()
        self.forceAnglesTab.addLayout(self.buttonDivision)
        self.forceAnglesTab.setSpacing(15)

        # Create and set graph's tab layout
        self.graphTab = QGridLayout()
        self.rightLayout.addLayout(self.graphTab)

        # Create and set button's left layout
        self.buttonsLeft = QVBoxLayout()
        self.leftLayout.addLayout(self.buttonsLeft)
        self.leftLabels = QVBoxLayout()
        self.leftLayout.addLayout(self.leftLabels)
        
        # Create the force angles button
        self.buttonForce = QtWidgets.QPushButton(text = 'Force Angles')
        setCustomSize(self.buttonForce, 100, 50)
        self.buttonForce.clicked.connect(self.buttonActionForce)
        self.buttonDivision.addWidget(self.buttonForce)
        
        # Create and set labels and text area tabs layout
        self.rightLabels = QHBoxLayout()
        self.buttonDivision.addLayout(self.rightLabels)
        self.rightLabels.setSpacing(10)
        self.tab1 = QVBoxLayout()
        self.rightLabels.addLayout(self.tab1)
        self.tab2 = QVBoxLayout()
        self.rightLabels.addLayout(self.tab2)
        self.tab3 = QVBoxLayout()
        self.rightLabels.addLayout(self.tab3)
        self.tab4 = QVBoxLayout()
        self.rightLabels.addLayout(self.tab4)
        self.tab5 = QVBoxLayout()
        self.rightLabels.addLayout(self.tab5)
        self.tab6 = QVBoxLayout()
        self.rightLabels.addLayout(self.tab6)
        self.tab7 = QVBoxLayout()
        self.rightLabels.addLayout(self.tab7)
        self.tab8 = QVBoxLayout()
        self.rightLabels.addLayout(self.tab8)
        self.tab9 = QVBoxLayout()
        self.rightLabels.addLayout(self.tab9)
        self.tab10 = QVBoxLayout()
        self.rightLabels.addLayout(self.tab10)
        self.tab11 = QVBoxLayout()
        self.rightLabels.addLayout(self.tab11)
        self.tab12 = QVBoxLayout()
        self.rightLabels.addLayout(self.tab12)

        # Create right label's
        self.rlabel1 = QLabel('Motor 1:', self)
        self.tab1.addWidget(self.rlabel1)
        self.rlabel2 = QLabel('Motor 2:', self)
        self.tab2.addWidget(self.rlabel2)
        self.rlabel3 = QLabel('Motor 3:', self)
        self.tab3.addWidget(self.rlabel3)
        self.rlabel4 = QLabel('Motor 4:', self)
        self.tab4.addWidget(self.rlabel4)
        self.rlabel5 = QLabel('Motor 5:', self)
        self.tab5.addWidget(self.rlabel5)
        self.rlabel6 = QLabel('Motor 6:', self)
        self.tab6.addWidget(self.rlabel6)
        self.rlabel7 = QLabel('Motor 7:', self)
        self.tab7.addWidget(self.rlabel7)
        self.rlabel8 = QLabel('Motor 8:', self)
        self.tab8.addWidget(self.rlabel8)
        self.rlabel9 = QLabel('Motor 9:', self)
        self.tab9.addWidget(self.rlabel9)
        self.rlabel10 = QLabel('Motor 10:', self)
        self.tab10.addWidget(self.rlabel10)
        self.rlabel11 = QLabel('Motor 11:', self)
        self.tab11.addWidget(self.rlabel11)
        self.rlabel12 = QLabel('Motor 12:', self)
        self.tab12.addWidget(self.rlabel12)

        # Create left label's
        self.llabel1 = QLabel('Motor 1: 50', self)
        self.leftLabels.addWidget(self.llabel1)
        self.llabel2 = QLabel('Motor 2: 50', self)
        self.leftLabels.addWidget(self.llabel2)
        self.llabel3 = QLabel('Motor 3: 50', self)
        self.leftLabels.addWidget(self.llabel3)
        self.llabel4 = QLabel('Motor 4: 50', self)
        self.leftLabels.addWidget(self.llabel4)
        self.llabel5 = QLabel('Motor 5: 50', self)
        self.leftLabels.addWidget(self.llabel5)
        self.llabel6 = QLabel('Motor 6: 50', self)
        self.leftLabels.addWidget(self.llabel6)
        self.llabel7 = QLabel('Motor 7: 50', self)
        self.leftLabels.addWidget(self.llabel7)
        self.llabel8 = QLabel('Motor 8: 50', self)
        self.leftLabels.addWidget(self.llabel8)
        self.llabel9 = QLabel('Motor 9: 50', self)
        self.leftLabels.addWidget(self.llabel9)
        self.llabel10 = QLabel('Motor 10: 50', self)
        self.leftLabels.addWidget(self.llabel10)
        self.llabel11 = QLabel('Motor 11: 50', self)
        self.leftLabels.addWidget(self.llabel11)
        self.llabel12 = QLabel('Motor 12: 50', self)
        self.leftLabels.addWidget(self.llabel12)
        
        # Create button's
        self.buttonNormal = QtWidgets.QPushButton(text = 'Normal')
        setCustomSize(self.buttonNormal, 100, 50)
        self.buttonNormal.clicked.connect(self.buttonActionNormal)
        self.buttonsLeft.addWidget(self.buttonNormal)

        self.buttonHappy = QtWidgets.QPushButton(text = 'Happy')
        setCustomSize(self.buttonHappy, 100, 50)
        self.buttonHappy.clicked.connect(self.buttonActionHappy)
        self.buttonsLeft.addWidget(self.buttonHappy)

        self.buttonSad = QtWidgets.QPushButton(text = 'Sad')
        setCustomSize(self.buttonSad, 100, 50)
        self.buttonSad.clicked.connect(self.buttonActionSad)
        self.buttonsLeft.addWidget(self.buttonSad)

        self.buttonRage = QtWidgets.QPushButton(text = 'Rage')
        setCustomSize(self.buttonRage, 100, 50)
        self.buttonRage.clicked.connect(self.buttonActionRage)
        self.buttonsLeft.addWidget(self.buttonRage)

        self.buttonScared = QtWidgets.QPushButton(text = 'Scared')
        setCustomSize(self.buttonScared, 100, 50)
        self.buttonScared.clicked.connect(self.buttonActionScared)
        self.buttonsLeft.addWidget(self.buttonScared)

        # Create textbox's
        self.textbox1 = QLineEdit(self)
        setCustomSize(self.textbox1, 65, 30)
        self.tab1.addWidget(self.textbox1)

        self.textbox2 = QLineEdit(self)
        setCustomSize(self.textbox2, 65, 30)
        self.tab2.addWidget(self.textbox2)

        self.textbox3 = QLineEdit(self)
        setCustomSize(self.textbox3, 65, 30)
        self.tab3.addWidget(self.textbox3)

        self.textbox4 = QLineEdit(self)
        setCustomSize(self.textbox4, 65, 30)
        self.tab4.addWidget(self.textbox4)

        self.textbox5 = QLineEdit(self)
        setCustomSize(self.textbox5, 65, 30)
        self.tab5.addWidget(self.textbox5)

        self.textbox6 = QLineEdit(self)
        setCustomSize(self.textbox6, 65, 30)
        self.tab6.addWidget(self.textbox6)

        self.textbox7 = QLineEdit(self)
        setCustomSize(self.textbox7, 65, 30)
        self.tab7.addWidget(self.textbox7)

        self.textbox8 = QLineEdit(self)
        setCustomSize(self.textbox8, 65, 30)
        self.tab8.addWidget(self.textbox8)

        self.textbox9 = QLineEdit(self)
        setCustomSize(self.textbox9, 65, 30)
        self.tab9.addWidget(self.textbox9)

        self.textbox10 = QLineEdit(self)
        setCustomSize(self.textbox10, 65, 30)
        self.tab10.addWidget(self.textbox10)

        self.textbox11 = QLineEdit(self)
        setCustomSize(self.textbox11, 65, 30)
        self.tab11.addWidget(self.textbox11)

        self.textbox12 = QLineEdit(self)
        setCustomSize(self.textbox12, 65, 30)
        self.tab12.addWidget(self.textbox12)

        # Place the matplotlib figure's
        self.Motor1 = CustomFigCanvas()
        self.graphTab.addWidget(self.Motor1, *(0,0))
        self.Motor2 = CustomFigCanvas()
        self.graphTab.addWidget(self.Motor2, *(0,1))
        self.Motor3 = CustomFigCanvas()
        self.graphTab.addWidget(self.Motor3, *(0,2))
        self.Motor4 = CustomFigCanvas()
        self.graphTab.addWidget(self.Motor4, *(1,0))
        self.Motor5 = CustomFigCanvas()
        self.graphTab.addWidget(self.Motor5, *(1,1))
        self.Motor6 = CustomFigCanvas()
        self.graphTab.addWidget(self.Motor6, *(1,2))
        self.Motor7 = CustomFigCanvas()
        self.graphTab.addWidget(self.Motor7, *(2,0))
        self.Motor8 = CustomFigCanvas()
        self.graphTab.addWidget(self.Motor8, *(2,1))
        self.Motor9 = CustomFigCanvas()
        self.graphTab.addWidget(self.Motor9, *(2,2))
        self.Motor10 = CustomFigCanvas()
        self.graphTab.addWidget(self.Motor10, *(3,0))
        self.Motor11 = CustomFigCanvas()
        self.graphTab.addWidget(self.Motor11, *(3,1))
        self.Motor12 = CustomFigCanvas()
        self.graphTab.addWidget(self.Motor12, *(3,2))

        # Add the callbackfunc to ..
        myDataLoop = threading.Thread(name = 'myDataLoop', target = dataSendLoop, args = (self.addData_callbackFunc,))
        myDataLoop.setDaemon(True)
        myDataLoop.start()

        self.show()

    def buttonActionExit(self):
        print("Exit")
        exit()

    def buttonActionForce(self):
        print("Force Angles")

    def buttonActionNormal(self):
        global emotion
        emotion = 0
        print("Normal")

    def buttonActionHappy(self):
        global emotion
        emotion = 1
        print("Happy")

    def buttonActionSad(self):
        global emotion
        emotion = 2
        print("Sad")

    def buttonActionRage(self):
        global emotion
        emotion = 3
        print("Rage")

    def buttonActionScared(self):
        global emotion
        emotion = 4
        print("Scared")

    def addData_callbackFunc(self, value):
        self.Motor1.addData(value[0])
        self.Motor2.addData(value[1])
        self.Motor3.addData(value[2])
        self.Motor4.addData(value[3])
        self.Motor5.addData(value[4])
        self.Motor6.addData(value[5])
        self.Motor7.addData(value[6])
        self.Motor8.addData(value[7])
        self.Motor9.addData(value[8])
        self.Motor10.addData(value[9])
        self.Motor11.addData(value[10])
        self.Motor12.addData(value[11])
        self.llabel1.setText("Motor 1: "+str(value[0]))
        self.llabel2.setText("Motor 2: "+str(value[1]))
        self.llabel3.setText("Motor 3: "+str(value[2]))
        self.llabel4.setText("Motor 4: "+str(value[3]))
        self.llabel5.setText("Motor 5: "+str(value[4]))
        self.llabel6.setText("Motor 6: "+str(value[5]))
        self.llabel7.setText("Motor 7: "+str(value[6]))
        self.llabel8.setText("Motor 8: "+str(value[7]))
        self.llabel9.setText("Motor 9: "+str(value[8]))
        self.llabel10.setText("Motor 10: "+str(value[9]))
        self.llabel11.setText("Motor 11: "+str(value[10]))
        self.llabel12.setText("Motor 12: "+str(value[11]))
        
class CustomFigCanvas(FigureCanvas, TimedAnimation):
    def __init__(self):
        self.addedData = []
        print(matplotlib.__version__)

        # The data
        self.xlim = 250
        self.n = np.linspace(0, self.xlim - 1, self.xlim)
        a = []
        b = []
        a.append(2.0)
        a.append(4.0)
        a.append(2.0)
        b.append(4.0)
        b.append(3.0)
        b.append(4.0)
        self.y = (self.n * 0.0) + 50

        # The window
        self.fig = Figure(figsize=(5,5), dpi=65)
        self.ax1 = self.fig.add_subplot(111)

        # self.ax1 settings
        self.ax1.set_ylabel('Angle')
        self.line1 = Line2D([], [], color='blue')
        self.line1_tail = Line2D([], [], color='red', linewidth=2)
        self.line1_head = Line2D([], [], color='red', marker='o', markeredgecolor='r')
        self.ax1.add_line(self.line1)
        self.ax1.add_line(self.line1_tail)
        self.ax1.add_line(self.line1_head)
        self.ax1.set_xlim(0, self.xlim - 1)
        self.ax1.set_ylim(0, 100)
        self.ax1.set_frame_on(False)
        self.ax1.get_xaxis().tick_bottom()
        self.ax1.axes.get_xaxis().set_visible(False)
        self.ax1.yaxis.tick_right()
        #self.ax1.yaxis.set_label_position('right')

        FigureCanvas.__init__(self, self.fig)
        TimedAnimation.__init__(self, self.fig, interval = 10, blit = True)

    def new_frame_seq(self):
        return iter(range(self.n.size))

    def _init_draw(self):
        lines = [self.line1, self.line1_tail, self.line1_head]
        for l in lines:
            l.set_data([], [])

    def addData(self, value):
        self.addedData.append(value)

    def zoomIn(self, value):
        bottom = self.ax1.get_ylim()[0]
        top = self.ax1.get_ylim()[1]
        bottom += value
        top -= value
        self.ax1.set_ylim(bottom,top)
        self.draw()

    def _step(self, *args):
        try:
            TimedAnimation._step(self, *args)
        except Exception as e:
            self.abc += 1
            print(str(self.abc))
            TimedAnimation._stop(self)
            pass

    def _draw_frame(self, framedata):
        margin = 1
        while(len(self.addedData) > 0):
            self.y = np.roll(self.y, -1)
            self.y[-1] = self.addedData[0]
            del(self.addedData[0])

        self.line1.set_data(self.n[ 0 : self.n.size - margin ], self.y[ 0 : self.n.size - margin ])
        self.line1_tail.set_data(np.append(self.n[-10:-1 - margin], self.n[-1 - margin]), np.append(self.y[-10:-1 - margin], self.y[-1 - margin]))
        self.line1_head.set_data(self.n[-1 - margin], self.y[-1 - margin])
        self._drawn_artists = [self.line1, self.line1_tail, self.line1_head]

class Communicate(QtCore.QObject):
    data_signal = QtCore.pyqtSignal(list)

def dataSendLoop(addData_callbackFunc):
    mySrc = Communicate()
    mySrc.data_signal.connect(addData_callbackFunc)
    
    while(True):
        time.sleep(0.1)
        mySrc.data_signal.emit(motors)

if __name__== '__main__':
    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Plastique'))
    myGUI = CustomMainWindow()
    ROS = Env()

    sys.exit(app.exec_())