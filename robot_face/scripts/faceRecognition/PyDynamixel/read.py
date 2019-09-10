#!/usr/bin/env python

import pydynamixel as dxl
from time import sleep
from sys import exit

LLEG_PORT = "/dev/ttyS6" # Serial port
RLEG_PORT = "/dev/ttyS5" # Serial port
#SEA_PORT = "/dev/ttyS4" # Serial port
TORSO_PORT = "/dev/ttyS11" # Serial port

BAUDNUM = 8    # 222kbps baudrate
TORQUE_ADDR = 0x18 # Address for torque enable
GOALPOS_ADDR = 0x1E # Address for goal position
CURRPOS_ADDR = 0x24 # Address for the current pos

# Initialize the socket
lleg_socket = dxl.initialize(LLEG_PORT, BAUDNUM)
if not lleg_socket:
    exit("Failed to open lleg_socket")
rleg_socket = dxl.initialize(RLEG_PORT, BAUDNUM)
if not rleg_socket:
    exit("Failed to open rleg_socket")
torso_socket = dxl.initialize(TORSO_PORT, BAUDNUM)
if not torso_socket:
    exit("Failed to open torso_socket")
#sea_socket = dxl.initialize(SEA_PORT, BAUDNUM)
#if not sea_socket:
#    exit("Failed to open sea_socket")


# Define the target servos
lleg_servo_ids = [26,28,24,22,16,14,12]
rleg_servo_ids = [11,13,15,21,23,25,27]
torso_servo_ids = [31,32,33,34,35,36,41,42,51,52,53,61,62]

# Get current positions
for i in range(1023):
    print "lleg:",
    for servo_id in lleg_servo_ids:
        print str(servo_id)+":"+str(dxl.read_word(lleg_socket, \
				servo_id, CURRPOS_ADDR)),
    print "rleg:",
    for servo_id in rleg_servo_ids:
        print str(servo_id)+":"+str(dxl.read_word(rleg_socket, \
				servo_id, CURRPOS_ADDR)),
    print "torso:",
    for servo_id in torso_servo_ids:
        print str(servo_id)+":"+str(dxl.read_word(torso_socket, \
				servo_id, CURRPOS_ADDR)),
    print
    sleep(0.001)

# Finish the connection with the socket
dxl.terminate(lleg_socket)
dxl.terminate(rleg_socket)
dxl.terminate(torso_socket)

