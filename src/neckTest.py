#!/usr/bin/env python

import cv2
import rospy
import numpy as np
from std_msgs.msg import Float64MultiArray
import imutils

def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))

rospy.init_node("faceDetect", anonymous = False)

face_cascade = cv2.CascadeClassifier("/home/victor_kich/faceDoris/src/robotFace/src/haar_cascade_face_default.xml")
cap = cv2.VideoCapture(2)

pub = rospy.Publisher("updateEyes", Float64MultiArray, queue_size = 1)

while not rospy.is_shutdown():
	ret, img = cap.read()
	# loop over the rotation angles
	for angle in np.arange(0, 360, 15):
		rotated = imutils.rotate(img, 10)

	img = rotated
	#img = rotate_bound(img, -10)
	height, width, layers = img.shape
	img_center = [width/2, height/2]

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	# A larger rectangle area means that the person face is closer to the robot face
	larger_area = 0
	larger_area_center = [np.nan, np.nan, width, height]
	for(x,y,w,h) in faces:
		center = [(x+x+w)/2, (y+y+h)/2]
		area = w*h

		if area > larger_area:
			larger_area = area
			larger_area_center[0] = center[0]
			larger_area_center[1] = center[1]

		cv2.rectangle(img, (x,y),(x+w, y+h), (255,0,0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]

	msg = Float64MultiArray()
	msg.data = larger_area_center
	
	if not np.isnan(larger_area_center[0]) or not np.isnan(larger_area_center[1]):
		pub.publish(msg)

	cv2.imshow("screen", img)

	k = cv2.waitKey(30) & 0xff

	if k == 26:
		break


cap.release()
cv2.destroyAllWindows()
