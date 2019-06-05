#!/usr/bin/env python

import pyjoints as pj
from math import pi
from time import sleep

# Open a port object (you can have
# several of these)
port0 = pj.DxlComm('/dev/ttyS0', 8)

# Create two joints
right_elbow = pj.Joint(40)
left_elbow = pj.Joint(41)

# Attach joints to the port
port0.attachJoint(right_elbow)
port0.attachJoint(left_elbow)

# Set and send the maximum torques
port0.sendMaxTorques(250)

# Enable torque in all joints
port0.enableTorques()

# Set goal angles to the joints
right_elbow.setGoalAngle(pi/2)
left_elbow.setGoalAngle(pi/2)

# Send the goal angles to all
# joints using sync_write
port0.sendGoalAngles()
sleep(1)

# Send the goal angle to a
# single joint
right_elbow.setGoalAngle(0)
right_elbow.sendGoalAngle()
sleep(1)

# Sending to a single joint
# can also be done this way
left_elbow.sendGoalAngle(0)
sleep(1)

# To read the current angle
# of a joint use this
angle = left_elbow.receiveAngle()

# The value read last time can
# be accessed using this
# (caution, this does not
#  make new communication)
angle = left_elbow.getAngle()

# To read all angles of a port
port0.receiveAngles()

# Then later the angles can
# be used like before
angle = left_elbow.getAngle()

# Close the port when finished
port0.release()

