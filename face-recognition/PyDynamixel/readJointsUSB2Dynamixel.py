#!/usr/bin/env python

from pyjoints import DxlComm, Joint

port = DxlComm('/dev/ttyUSB0',8)

lleg_joints = [Joint(i) for i in [12,14,16,22,24,26,28]]
port.attachJoints(lleg_joints)
rleg_joints = [Joint(i) for i in [11,13,15,21,23,25,27]]
port.attachJoints(rleg_joints)
torso_joints = [Joint(i) for i in [31,32,33,34,35,36,41,42,51,52,53,61,62]]
port.attachJoints(torso_joints)

for i in range(1023):
    port.receiveCurrAngles()
    print 'lleg',
    for joint in lleg_joints:
        print str(joint.servo_id)+":"+str(joint.currValue),
    print 'rleg',
    for joint in rleg_joints:
        print str(joint.servo_id)+":"+str(joint.currValue),
    print 'trunk',
    for joint in torso_joints:
        print str(joint.servo_id)+":"+str(joint.currValue),
    print

