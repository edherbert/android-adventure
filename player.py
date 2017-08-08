from graphics import *
from map import *
from android import *
from gui import *
import math

#Whether the player is moving or not
playerMoving = False
#Just a housekeeping variable to do with the player moving
playerMovingTimer = 0
#The direction of the player
#0 up, 1 left, 2 right, 3 down
playerDirection = -1
#Used to compare the current direction and the previous to see if a graphical direction change is needed
#So that the function that switches android direction is not run every frame
previousPlayerDirection = -1
#The last android that was spoken to. Used to make the androids face forward after being spoken to
#-1 means no android was previously spoken to and is the default
spokenToAndroid = -1
#Used for the ice sections of the game
playerSliding = False
#Determines whether the player can move or not
playerCanMove = False
#The most important variable in the game
playerName = "Edward"
#Code for the fight scene
playerIsFighting = False

def playerInteract(player):
	#Check for androids, speech tiles, ran when the player presses the interact key
	global spokenToAndroid
	playerLookX = 0
	playerLookY = 0
	#Get the current android list
	androids = getAndroids()
	#A point is created a specific distance away from the centre of the player based on his/her direction
	if(playerDirection == 0):	playerLookY = -30
	if(playerDirection == 1):	playerLookX = -30
	if(playerDirection == 2):	playerLookX = 30
	if(playerDirection == 3):	playerLookY = 30

	playerPointX = player[0].getCenter().getX() + playerLookX
	playerPointY = player[0].getCenter().getY() + playerLookY
	#print(str(math.floor(playerPointX / tileSize)) + "   " + str(math.floor(playerPointY / tileSize)) + "   " + str(getSegmentX()) + "   " + str(getSegmentY()))
	#Check for androids first
	for i in range(0, len(androids), 17):
		if(androids[i + 13] == getSegmentX() and androids[i + 14] == getSegmentY()):
			#Loop through every android on the screen
			#If this android has nothing to say then skip it. 
			if(androids[i + 16] == ""):	continue
			if(playerPointX >= androids[i].getP1().getX() and playerPointY >= androids[i].getP1().getY() and playerPointX <= androids[i].getP2().getX() and playerPointY <= androids[i].getP2().getY()):
				#If the point is within the android then this talking code is run.
				#This changes the direction of the android based on the player's location
				if(playerDirection == 0):	changeAndroidDirection(androids[i:i + 17], 3)
				if(playerDirection == 1):	changeAndroidDirection(androids[i:i + 17], 2)
				if(playerDirection == 2):	changeAndroidDirection(androids[i:i + 17], 1)
				if(playerDirection == 3):	changeAndroidDirection(androids[i:i + 17], 0)
				#Make it the most recent spoken to android and show the gui
				spokenToAndroid = i
				guiSpeak(androids[i + 16])

	#Once the check for androids is run, check for gui tiles
	#CheckGuiTiles gives False if there is no tile, but returns a string to be spoken if there is.
	output = checkGuiTiles(math.floor(playerPointX / 48), math.floor(playerPointY / 48))
	if(output != False):
		guiSpeak(output)

def isPlayerSliding():
	return playerSliding

def setPlayerName(name):
	global playerName
	playerName = name

def getPlayerName():
	return playerName

def setIsFighting(val):
	global playerIsFighting
	playerIsFighting = val

def isPlayerFighting():
	return playerIsFighting

def playerUpdate(player):
	#House keeping functions for the player
	global playerMoving
	global playerMovingTimer
	global previousPlayerDirection
	global spokenToAndroid
	global playerSliding

	#If the player is done speaking and the spoken to android is not -1 then reset that androids direction to 3 (down)
	#print(spokenToAndroid)
	if(not isSpeaking() and spokenToAndroid >= 0):
		changeAndroidDirection(getAndroids()[spokenToAndroid:spokenToAndroid + 17], 3)
		#Reset the spoken to android
		spokenToAndroid = -1

	if(playerSliding):
		#0 up, 1 left, 2 right, 3 down
		if(playerDirection == 0):	movePlayer(player, 0, -6)
		if(playerDirection == 3):	movePlayer(player, 0, 6)
		if(playerDirection == 1):	movePlayer(player, -6, 0)
		if(playerDirection == 2):	movePlayer(player, 6, 0)


	#Used to determine whether the player is moving or not
	if(playerMovingTimer > 0):	playerMovingTimer -= 1
	else:
		playerMoving = False

	#If the previous direction is not equal to the current then that means the android has switched direction
	#This requires a call to the change android direction function
	if(playerMoving and previousPlayerDirection != playerDirection):
		changeAndroidDirection(player, playerDirection)
		previousPlayerDirection = playerDirection

def movePlayer(player, x, y):
	#A function to move the player and check collision and map boundaries
	#Saves processes in that collision is only checked when the player moves, not every frame
	#Also means animation is possible

	global playerMoving
	global playerMovingTimer
	global playerDirection
	playerMoving = True
	playerMovingTimer = 10

	map = getMap()

	#Find the direction for animation
	if(y < 0):
		playerDirection = 0
	elif(y > 0):
		playerDirection = 3

	if(x < 0):
		playerDirection = 1
	elif(x > 0):
		playerDirection = 2

	#Figure out if the player needs to switch the map segment 
	topLeft = player[0].getP1()
	bottomRight = player[0].getP2()

	#If the player is about to go off screen in a specific direction then the map segment is switched and the player is moved to the other side of the screen
	if(topLeft.getX() + x < 0):
		switchSegment(-1, 0)
		moveAndroid(player, winWidth - tileSize, 0)
	if(topLeft.getY() + y < 0):
		switchSegment(0, -1)
		moveAndroid(player, 0, winHeight - tileSize)
	if(bottomRight.getX() + x > winWidth):
		switchSegment(1, 0)
		moveAndroid(player, -winWidth + tileSize, 0)
	if(bottomRight.getY() + y > winHeight):
		switchSegment(0, 1)
		moveAndroid(player, 0, -winHeight + tileSize)

	if(not checkCollision(map, player, x, y) and not checkAndroidCollision(player, x, y)):
	#if(not checkAndroidCollision(player, x, y)):
		moveAndroid(player, x, y)

	#Now that the player has been moved, it can be checked whether it has moved onto a warp tile
	checkWarp(getMapMeta(), player)

	#Check to see if the player has finished certain parts of the story before entering areas
	#This would otherwise be in the android village update but it's more efficient to have it here
	if(getCurrentMapId() == 1):	
		if(getSegmentX() == 0 and getSegmentY() == 2 and player[0].getP1().getX() <= 48 * 2 and not isSightTrialDone()):
			moveAndroid(player, 50, 0)
			guiSpeak("You need to complete the trial of sight before you can go in here!")

		if(getSegmentX() == 2 and getSegmentY() == 2 and player[0].getP2().getX() >= 48 * 17 and player[0].getP2().getY() >= 48 * 7 and not isDeductionTrialDone()): #This might need fixing
			moveAndroid(player, -50, 0)
			guiSpeak("You need to complete both the trial of sight and the trial of deduction before you can go in here!")

def checkWarp(map, obj):
	#Checks whether the player is ontop of a warp tile as outlined in the map's meta file
	#If it is then the player will be moved to the correct location and possibly the map will change

	#Nine pieces of data make a warp tile, so increment the list in nines
	#Start at 4 because there are four pieces of data that help describe a map at the beginning of the list (map name, background colour, segwidth and segheight)
	for i in range(5, len(map), 9):
		warpTileSegX = map[i + 3]
		warpTileSegY = map[i + 4]

		if(warpTileSegX == getSegmentX() and warpTileSegY == getSegmentY()):
			targetMap = map[i + 0]
			warpTileX = map[i + 1]
			warpTileY = map[i + 2]

			currentTopLeft = compareWarpAndPosition(warpTileX, warpTileY, obj[0].getP1().getX() + 0.5, obj[0].getP1().getY() + 0.5)
			currentBottomRight = compareWarpAndPosition(warpTileX, warpTileY, obj[0].getP2().getX() - 0.5, obj[0].getP2().getY() - 0.5)
			currentTopRight = compareWarpAndPosition(warpTileX, warpTileY, obj[0].getP1().getX() + tileSize - 0.5, obj[0].getP1().getY() + 0.5)
			currentBottomLeft = compareWarpAndPosition(warpTileX, warpTileY, obj[0].getP2().getX() - tileSize + 0.5, obj[0].getP2().getY() - 0.5)

			warpDestinationX = map[i + 5]
			warpDestinationY = map[i + 6]
			warpDestinationSegX = map[i + 7]
			warpDestinationSegY = map[i + 8]

			#If any of the points are on that specific warp tile (true) then warp the player
			if(currentTopLeft or currentBottomRight or currentTopLeft or currentTopRight):
				warpToLocation(obj, targetMap, warpDestinationX, warpDestinationY, warpDestinationSegX, warpDestinationSegY, not(getSegmentX() == warpDestinationSegX and getSegmentY() == warpDestinationSegY))

def warpToLocation(obj, targetMap, destinationX, destinationY, segX, segY, redraw):
	#Warps the player to a location, either on the current map or off it

	#If the map is none, don't switch it, otherwise do
	if(targetMap != "None"):
		removeAndroids()
		setMap(processMap(readMap("maps/"+targetMap+".txt")), processMapMeta(readMap("maps/"+targetMap+"Meta.txt")))

	#The variable redraw determines whether to redraw the map or not
	#It means that if warping to a location on the same segment the map does not have to be redrawn
	if(redraw):	switchToSegment(segX, segY)
	#Move to the exact location of the destination x and y
	#obj.move(destinationX * tileSize - obj.getP1().getX(), destinationY * tileSize - obj.getP1().getY())
	moveAndroid(obj, destinationX * tileSize - obj[0].getP1().getX(), destinationY * tileSize - obj[0].getP1().getY())


def setCanPlayerMove(move):
	global playerCanMove
	playerCanMove = move

def canPlayerMove():
	return playerCanMove

def checkCollision(map, obj, x, y):
	global playerSliding
	#checks collision with a rectangle object for the tiles below

	#Basically the function checks where the player will be if it is moved
	#If any point of the player is going to be moved to an illegal (collision) tile it returns false and the player stays where it is
	#There is no point checking collision for the current tile, because at that point the player would be there anyway,
	#and would then just be stuck there forever.

	#Also, I set the bounding box of the player to be 0.5 pixels smaller that it actually is
	#This is because if moving forward, even if the player was to move onto the boundry of an illegal tile,
	#a collision would occur. Given how the player has four points this would always happen.
	#This is a problem with having the player the size of a tile,
	#the size of 0.5 does not matter though, as the player moves at a rate of 3 anyway and everything gets floored to the nearest tile

	#The graphics library provides each rectangle with two points, which can be retrieved like this
	currentTopLeft = obj[0].getP1()
	currentBottomRight = obj[0].getP2()

	#This returns the id of the tile underneath each x and y point
	topLeft = getTileAtXY(map, currentTopLeft.getX() + x + 0.5, currentTopLeft.getY() + y + 0.5)
	bottomRight = getTileAtXY(map, currentBottomRight.getX() + x - 0.5, currentBottomRight.getY() + y - 0.5)

	topRight = getTileAtXY(map, currentTopLeft.getX() + tileSize + x - 0.5, currentTopLeft.getY() + y + 0.5)
	bottomLeft = getTileAtXY(map, currentBottomRight.getX() - tileSize + x + 0.5, currentBottomRight.getY() + y - 0.5)

	#Check if the player has moved to an ice tile, to begin the sliding process
	if("f" in [topLeft, bottomRight, topRight, bottomLeft]):
		playerSliding = True
	else:
		playerSliding = False

	#If the value returned is equal to any of the pre-defined collision tiles then the function returns true (there has been a collision)
	for i in collisions:
		if(i in [topLeft, bottomRight, topRight, bottomLeft]):
			#If the player has collided then make them stop sliding (sliding logic for the ice part)
			playerSliding = False
			return True

def getTileAtXY(map, x, y):
	#A function that takes the coordinates of a point, rather than the point itself and returns the tile
	return getTile(math.floor(x / tileSize), math.floor(y / tileSize), getSegmentX(), getSegmentY())

def compareWarpAndPosition(warpTileX, warpTileY, x, y):
	#compares the position of a warp tile and an x and y. Returns true if there is an overlap
	collision = False
	if(math.floor(x / tileSize) == warpTileX and math.floor(y / tileSize) == warpTileY):	collision = True
	return collision