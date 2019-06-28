import cv2 as cv
from imutils.video import VideoStream
import imutils
import numpy as np
import wx

class camera(object):
	def __init__(self):
		#use cv2
		#self.cam = cv.VideoCapture(0)
		# on PC camera
		#self.vs = VideoStream(src=0).start()
		# on pi camera
		self.vs = VideoStream(usePiCamera=False).start()
	def has_webcam(self):
		#_,frame = self.cam.read()
		frame = self.vs.read()
		#frame = imutils.resize(frame, width=500)
		if (isinstance(frame,np.ndarray)):
			return True
		return False
	def get_image(self,w=None,h=None):
		#_,frame = self.cam.read()2
		frame = self.vs.read()
		#if w != None and h != None:
		#   frame = cv.resize(frame,(w,h))
		#   frame = imutils.resize(frame, width=w,height=h)
		frame = imutils.resize(frame, width=500)
		return cv.cvtColor(frame,cv.COLOR_BGR2RGB)
	def get_size(self):
		#_,frame = self.cam.read()		
		frame = self.vs.read()
		frame = imutils.resize(frame, width=500)
		return frame.shape[:2]
	def release(self):
		#self.cam.release()
		self.vs.stop()