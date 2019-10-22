#!/usr/bin/env python

import rospy
import numpy as np
import sys
from PyDynamixel import DxlComm, Joint
from std_msgs.msg import Float64MultiArray

face_center = [np.nan,np.nan]

def move_neck():
	'''
	Funcao que recebe a posicao do centro da face do usuario em relacao a tela, e move os motores
	para que o rosto robotico olhe diretamente para a face da pessoa mais proxima dele.

	Parametros:

	Centro motor vertical (id 61):  3.141592653589793 rad
	Centro motor horizontal (id 62): 3.141592653589793 rad

	angulo maximo de rotacao: 
		O horizontal nao mexe mais que 60 graus para cada lado (1,0472 rad)
		O vertical nao mexe mais que 30 graus para baixo ou para cima (0,523599 rad)

		vertical: [2.617993, 3.665193]
		horizontal: [2.0943926, 4.188792]

	'''
	global face_center

	# Se inscreve no topico "face_center", que informa as coordenadas dp centro da face mais proxima ao robo
	rospy.Subscriber("updateEyes", Float64MultiArray, callback_coordinates)

	# Inicia comunicacao dos motores dynamixel pela porta serial /dev/ttyUSB0
	port = DxlComm("/dev/ttyUSB0")

	# Inicia as juntas de rotacao com os respectivos IDs dos motores
	neck_h = Joint(62)			# Junta responsavel pelo movimento horizontal da cabeca, motor ID 62
	neck_v = Joint(61)			# Junta responsavel pelo movimento vertical da cabeca, motor ID 61

	port.attachJoint(neck_v)
	port.attachJoint(neck_h)

	# Ativa o torque dos motores, por seguranca
	neck_h.enableTorque()
	neck_v.enableTorque()

	# Seta a taxa de envio de dados do ros
	rate = rospy.Rate(50)
	while not rospy.is_shutdown():
		# O calculo dos limites da tela para o pescoco se mover dependem do tamanho da tela
		# Provavelmente, as dimencoes da camera usada pela Doris sao 300 por 300.
		width = 400
		height = 300

		# A tolerancia representa a regiao da tela que ativa os movimentos do robo
		# Tolerance = 0.3 significa que se a face mais proxima estiver nos 30% mais 
		# da direita da tela, o motor deve rotacionar para a esquerda
		tolerance = 0.12

		width_limits = [tolerance*width, (1-tolerance)*width]
		height_limits = [tolerance*height, (1-tolerance)*height]

		# Step eh o angulo em radianos que cada motor gira em cada iteracao
		step = 0.004

		# Verifica se a face mais proxima esta muito para a esquerda
		if face_center[0] < width_limits[0]:
			# Guarda o angulo inicial registrado
			theta_h = neck_h.receiveCurrAngle()
			init_theta_h = theta_h
			if theta_h != 0:
				while theta_h < 4.188792 - step and theta_h < init_theta_h + 0.1:
					# Move o rosto ate no maximo 4.188792 radianos
					theta_h += step
					neck_h.sendGoalAngle(theta_h)
		
		# Verifica se a face mais proxima esta muito para a direita
		if face_center[0] > width_limits[1]:
			# Guarda o angulo inicial registrado
			theta_h = neck_h.receiveCurrAngle()
			init_theta_h = theta_h
			if theta_h != 0:
				while theta_h > 2.0943926 + step and theta_h > init_theta_h - 0.1:
					# Move o rosto ate no minimo 2.0943926 radianos
					theta_h -= step
					neck_h.sendGoalAngle(theta_h)
				

		# Verifica se a face mais proxima esta muito para cima
		if face_center[1] < height_limits[0]:
			# Guarda o angulo inicial registrado
			theta_v = neck_v.receiveCurrAngle()
			init_theta_v = theta_v
			if theta_v != 0:
				while theta_v < 3.665193 - step and theta_v < init_theta_v + 0.1:
					# Move o rosto ate no maximo 3.665193 radianos
					theta_v += step
					neck_v.sendGoalAngle(theta_v)

		# Verifica se a face mais proxima esta muito para baixo
		if face_center[1] > height_limits[1]:
			# Guarda o angulo inicial registrado
			theta_v = neck_v.receiveCurrAngle()
			init_theta_v = theta_v
			if theta_v != 0:
				while theta_v > 2.617993 + step and theta_v > init_theta_v - 0.1:
					# Move o rosto ate no minimo 2.617993 radianos
					theta_v -= step
					neck_v.sendGoalAngle(theta_v)
		
		rate.sleep()


def callback_coordinates(msg):
	'''
	Funcao de retorno para o Subscriber
	Recebe as coordenadas do centro da face mais proxima a camera e altera o valor da variavel face_center
	'''
	global face_center
	face_center = msg.data

if __name__ == "__main__":
	rospy.init_node('neckController', anonymous = False)
	move_neck()
