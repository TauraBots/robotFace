#!/usr/bin/env python

import pydynamixel as dxl
from time import sleep
from sys import exit

#PORT = "/dev/ttyUSB0" # Serial port
PORT = "/dev/ttyS0" # Serial port
BAUDNUM = 8    # 222kbps baudrate
TORQUE_ADDR = 0x18 # Address for torque enable
GOALPOS_ADDR = 0x1E # Address for goal position

# Initialize the socket
socket = dxl.initialize(PORT, BAUDNUM)
if not socket:
    exit("Failed to open socket")

# Define the target servos
servo_ids = [25,28,29,34,33]

# Enable torque
for servo_id in servo_ids:
    dxl.write_word(socket, servo_id, TORQUE_ADDR, 1)

# Set goal positions
for i in range(1023):
    values = [4*i for servo_id in servo_ids]
    dxl.sync_write_word(socket, GOALPOS_ADDR, servo_ids, values, len(servo_ids))
    sleep(0.001)

# Finish the connection with the socket
dxl.terminate(socket)

