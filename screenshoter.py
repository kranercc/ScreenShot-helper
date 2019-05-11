#take screen shots but have a moving box on your desktop so you can resize it and take a screen shot there

from PIL import ImageGrab, Image
import pygame, sys, os
from pygame.locals import *
import time
import keyboard
import mouse
from time import sleep
import cv2
import numpy as np
import tempfile

#1 args since it needs to start systray
def main(aa):
	def takeSS():
		img = ImageGrab.grab((0,0,1920,1080));
		img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
		cv2.imwrite("temp.jpg", img);
		return img;

	takeSS();
	screenshot = Image.open("temp.jpg");


	def regionOfInterest(img, verticies):
		mask = np.zeros_like(img);
		cv2.fillPoly(mask, verticies, 255);
		masked = cv2.bitwise_and(img, mask);
		return masked;


	def saver(bbox):
		imageToCrop = Image.open("temp.jpg");

		startx, starty = bbox[0][0], bbox[0][1];
		endx, endy = bbox[1][0], bbox[1][1];



		bbox = ((startx, starty, endx, endy));
		area = imageToCrop.crop(bbox)
		area.save("screenShot.jpg");
		imageToCrop.close();



	#draw lines
	storeValues = [];
	def liner(storeValues):
		mC = mouse.get_position();
		mCx,mCy = mC[0], mC[1];

		#select a point
		if len(storeValues) != 2:
			if keyboard.is_pressed("+"):
				storeValues.append((mCx,mCy));
		
			for i in range(len(storeValues)-1):
				if storeValues[i] == storeValues[i+1]:
					storeValues.pop(i+1);


		#for coords in range(len(storeValues)-1):			
			#pygame.draw.line(screen, (0,255,100), (storeValues[coords][0],storeValues[coords][1]), (storeValues[coords+1][0],storeValues[coords+1][1]), 2)
		print(storeValues);
		return storeValues;
	pygame.init()

	screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
	#pygame.display.set_caption("ScreenShot@krane");

	background = pygame.image.load("temp.jpg").convert()





	Running = True
	while Running:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				Running = False
				sys.exit()
				break
		if keyboard.is_pressed("q"):
			exit();

		screen.blit(background,(0,0))
		drawer = liner(storeValues);

		if len(drawer) == 2:
			saver(drawer);
			screenshot.close();
			os.system("del temp.jpg");
			exit();

			pygame.display.update()


while 1:
	sleep(1/100)
	if keyboard.is_pressed("print screen"):
		main(1);
	#exiting the program
	if keyboard.is_pressed("ctrl") and keyboard.is_pressed("alt") and keyboard.is_pressed("+"):
		exit();
#menu_options = (("ScreenShot", None, main),)
#systray = SysTrayIcon("icon.ico", "ScreenShot @krane", menu_options)