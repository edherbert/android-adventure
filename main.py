from graphics import *
import os
import time
from datetime import datetime
from random import random

from map import *
from player import *
from android import *
from gui import *
from story import *
from fightScene import *

from random import randint

import math

#Things that I would change if I could to re-make the game:
#Some of the story code is quite repetitive
#Add saving functionality

def main():
	running = True

	speed = 6

	win = GraphWin("Android Adventure", winWidth, winHeight)

	#Set the map data for both tile data and map meta data
	setMap(processMap(readMap("maps/blank.txt")), processMapMeta(readMap("maps/blankMeta.txt")))

	#To reset the game:
	#set the map to blank
	#set story trial to 1
	#Set the map coordinates to 1, 1
	#Draw the map in main
	#Reset the trial site count to 0
	#Make it so the player cannot move
	#reset the player position to 15, 8

	drawMap(win, segX, segY)
	#setCanPlayerMove(True)
	#setStoryTrial(6)

	guiInit(win)
	initFightScene()

	player = createAndroid("green")
	#moveAndroid(player, 48 * 15, 48 * 8)
	moveAndroid(player, 48 * 15, 48 * 8)
	drawAndroid(win, player)
	playerRunning = False

	#Code for the popup that appears when entering a new map
	mapNameContainer.setFill("white")
	mapNameContainer.setFace("arial")
	mapNameContainer.setSize(36)
	#mapNameContainer.setText(getMapNameText())
	mapNameContainer.draw(win)

	prev = getTime()
	while running:
		current = getTime()
		#The human eye can only see 24 fps anyway
		if(current - prev >= 1000 / 60):
			prev = current

			if(win.isClosed()):	running = False
			key = win.checkKey()
			if(key == "Escape"):	running = False

			if(shouldGameClose()):	running = False

			fightSceneUpdate(win, key)

			updateGui(win, key)

			if(not isSpeaking() and not isPlayerSliding() and canPlayerMove() and not isPlayerFighting()):
				#Left shift tooggles player running.
				if(key == "Shift_L"):
					playerRunning = not playerRunning
					if(playerRunning):	speed = 24
					else:	speed = 6
				if(key == "Up"):	movePlayer(player, 0, -speed)
				if(key == "Down"):	movePlayer(player, 0, speed)
				if(key == "Left"):	movePlayer(player, -speed, 0)
				if(key == "Right"):	movePlayer(player, speed, 0)
				if(key == "z"):
					if(playerCanInteract()):
						playerInteract(player)

			playerUpdate(player)
			updateStory(getCurrentMapId(), win, key, player)
			updateMap()

			#Checks if the map needs to be redrawn and which segment
			if(mapShouldRedraw()):
				#Certain objects are undrawn and then drawn again. This is to create correct object layering
				undrawAndroid(player)
				undrawAndroids()
				mapNameContainer.undraw()

				#Draw the map and the player
				drawMap(win, getSegmentX(), getSegmentY())
				drawAndroids(win)
				drawAndroid(win, player)

				#Change the map title container's text and re-draw it.
				mapNameContainer.setText(getMapNameText())
				mapNameContainer.draw(win)


def getTime():
	#Get the time since the 1970 epoch in milliseconds
    return int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)

main()
