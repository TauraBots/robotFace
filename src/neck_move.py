#!/usr/bin/env python

import rospy
import numpy as np
import sys
from PyDynamixel import DxlComm, Joint
from std_msgs.msg import Float64MultiArray

face_center = [150,150]

def move_neck():
	'''
	Centro motor vertical (id 61):  3.141592653589793 rad
	Cento motor horizontal (id 62): 3.141592653589793 rad

	angulo maximo de rotacao: 
		O horizontal nao mexe mais que 60 graus para cada lado (1,0472 rad)
		O vertical nao mexe mais que 30 graus para baixo ou para cima (0,523599 rad)

		vertical: [2.617993, 3.665193]
		horizontal: [2.0943926, 4.188792]

	'''
	global face_center

	rospy.Subscriber("face_center", Float64MultiArray, callback_coordinates)

	# Inicia comunicacao da porta serial
	port = DxlComm("/dev/ttyUSB0")

	neck_h = Joint(62)
	neck_v = Joint(61)

	port.attachJoint(neck_v)
	port.attachJoint(neck_h)
	neck_h.enableTorque()
	neck_v.enableTorque()

	tolerance = 0.2

	rate = rospy.Rate(50)
	while not rospy.is_shutdown():

		# Receive the neck motors angles
		theta_x = neck_h.receiveCurrAngle()
		theta_y = neck_v.receiveCurrAngle()

		# O calculo dos limites da tela para o pescoco se mover dependem do tamanho da tela
		width = 300
		height = 300
		width_limits = [0.3*width, 0.7*width, 0.3*height, 0.7*height]

		step = 0.08

		if face_center[0] > width_limits[1] and  theta_x > 2.0943926:
			while face_center[0] > width/2:
				# Significa que a pessoa esta muito para a esquerda na imagem
				if theta_x - step < 2.0943926 + tolerance: theta_x = 2.0943926
				neck_h.sendGoalAngle(theta_x - step)

		if face_center[0] < width_limits[0] and  theta_x < 4.188792:
			while face_center[0] < width/2:
				# Significa que a pessoa esta muito para a direita na imagem
				if theta_x + step > 4.188792 - tolerance: theta_x = 4.188792
				neck_h.sendGoalAngle(theta_x + step)

		if face_center[1] > width_limits[3] and  theta_y < 3.665193:
		 	while face_center[1] > height/2:
		 		# Significa que a pessoa esta muito para baixo na imagem
				if theta_x - step < 2.617993 + tolerance: theta_x = 2.617993
				neck_v.sendGoalAngle(theta_y + step)

		if face_center[1] < width_limits[2] and  theta_y > 2.617993:
			while face_center[1] < height/2:
				# Significa que a pessoa esta muito para cima na image
				if theta_x + step > 3.665193 - tolerance: theta_x = 3.665193
				neck_v.sendGoalAngle(theta_y - step)

		rate.sleep()


def callback_coordinates(msg):
	global face_center

	face_center = msg.data

if __name__ == "__main__":
	rospy.init_node('neck_mover', anonymous = False)
	move_neck()