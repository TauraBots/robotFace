#!/usr/bin/env python

import os
os.system("rosrun robot_face recognize_video.py --detector faceDoris/src/robot_face/scripts/face_detection_model --embedding-model faceDoris/src/robot_face/scripts/openface_nn4.small2.v1.t7 --recognizer faceDoris/src/robot_face/scripts/output/recognizer.pickle --le faceDoris/src/robot_face/scripts/output/le.pickle")