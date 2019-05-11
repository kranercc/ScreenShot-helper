'''
Icon used is from google images, source: https://duckduckgo.com/?q=barry+bee+benson&atb=v161-1&iax=images&ia=images&iai=https%3A%2F%2Fpbs.twimg.com%2Fprofile_images%2F696766954409893888%2FLFx7rcQE.jpg
Author: "@Krane"
GMail: "kranehecaru@gmail.com"


Keep in mind:

If you are downloading the source code, you are not allowed to do edit the code in anyway shape or form.
If you are going to sell this code as your own, contact me first and we can talk about it, if i don't respond you are not allowed to sell it

'''

from PIL import ImageGrab, Image
import pygame, sys, os
from pygame.locals import *
import time
import keyboard
import mouse
from time import sleep
import cv2
import numpy as np


def takeSS():
	img = ImageGrab.grab((0,0,1920,1080));
	img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
	cv2.imwrite("temp.jpg", img);
	return img;


def saver(bbox):
		imageToCrop = Image.open("temp.jpg");

		startx, starty = bbox[0][0], bbox[0][1];
		endx, endy = bbox[1][0], bbox[1][1];

		#in case the user does it reverse for some reason

		reverse1 = False
		if startx >= endx:
			endxNew = startx;
			startx = endx;
			reverse1 = True;
		if starty >= endy:
			endyNew = starty+1;
			starty = endy+1;
			reverse1 = True;

		

		if reverse1:
			bbox = ((startx, starty, endxNew, endyNew));
		else:
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
	return storeValues;

Running = True;
def main():
	global Running

	takeSS();
	screenshot = Image.open("temp.jpg");

	pygame.init()

	screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
	#pygame.display.set_caption("ScreenShot@krane");

	background = pygame.image.load("temp.jpg").convert()
	pygame.font.init() 
	myfont = pygame.font.SysFont('Comic Sans MS', 30)
	textsurface = myfont.render('You are in the cropping process', False, (255, 255, 255))

	while Running:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				Running = False
				sys.exit()
				break
		screen.blit(background,(0,0))
		drawer = liner(storeValues);

		if len(drawer) == 2:
			saver(drawer);
			screenshot.close();
			os.system("del temp.jpg");
			Running = False;
			pygame.quit();
		if Running != False:
			
			screen.blit(textsurface,(mouse.get_position()[0],mouse.get_position()[1]))
			pygame.display.update()



while 1:
	sleep(1/100)
	if keyboard.is_pressed("print screen"):
		Running = True;
		storeValues = [];
		main();
	#exiting the program
	if keyboard.is_pressed("ctrl") and keyboard.is_pressed("alt") and keyboard.is_pressed("+"):
		exit();
