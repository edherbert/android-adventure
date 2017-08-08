from graphics import *
import random
import math

#Map segments are the number of tiles that can fit on a screen at once

#The number of map segments in the map for the width and height
#These numbers also include 0 by the way, so 2 = 3
#This is just so you can't say segWidth = 0 because then you would have nothing to draw
segWidth = 2
segHeight = 2
#The current map segment
segX = 1
segY = 1
#Wheather or not the map should be redrawn (after segment change)
mapShouldRedrawBool = False
#The number of tiles that can fit on the window for width and height
tileWinWidth = 20
tileWinHeight = 12
#The size of each tile in pixels
tileSize = 48
#Width and height for the window
winWidth = tileWinWidth * tileSize
winHeight = tileWinHeight * tileSize
#A list of tile ids that respond to collision
collisions = [0, 2, 3, 4, 5, 7, 9, "g", "e", "j", "c"]
#A list of places to draw dots on the grass tile
grassValues = [6, 30, 46, 17, 33, 42, 33, 27, 20, 5, 18, 23, 4, 45, 22, 24, 23, 5, 45, 33]
#A similar list for water details
waterValues = [45, 41, 24, 9, 17, 22, 38, 23, 7, 4, 25, 46, 10, 40, 40, 8]

#The tile data for the map
map = []
#The meta data for the map, containing warp tile details
mapMeta = []
#The ammount of time the map name has left on the screen
mapNameTime = 0
mapNameText = ""
#a text object to contain the map name
mapNameContainer = Text(Point(winWidth / 2, winHeight / 2), mapNameText)
#The current background of the window
windowBackground = "558032"
#The id of the current map. Used for story programming.
currentMapId = 0

#An array that will contain every graphical object required to draw a map segment
#This is more for correct removal of graphical objects from the window than anything
mapContent = []
#A list of houses to make sure that houses are drawn last, to avoid graphical issues
houses = []
#A list of gui Tiles. I didn't want to put those in meta data
guiTiles = []
#A list containing the elements for the rolldown effect
rolldownBands = []
#A variable to determine if the rolldown effect has completed
rolldownCompelete = True
#A variable to tell if the sight trial has been completed
sightTrialDone = False
#A variable to tell if the deduction trial has been completed
deductionTrialDone = False
#A variable to tell if the strength trial has been completed
strengthTrialDone = False
#If true the game will close
gameShouldClose = False

def readMap(path):
	#loads in a map from a txt file
	file = open(path, "r")
	contents = file.read()
	file.close()
	return contents

def rolldown(win):
	global rolldownCompelete
	global rolldownBands
	rolldownBands = []
	rolldownCompelete = False
	for i in range(48):
		band = Rectangle(Point(i * 48, -winHeight - 50), Point(i * 48 + 48, 0))
		band.setFill("white")
		band.setOutline("white")
		band.move(0, random.random() * -300)
		band.draw(win)
		rolldownBands.append(band)

def removeRolldown():
	for i in range(len(rolldownBands)):
		rolldownBands[0].undraw()
		rolldownBands.pop(0)

def shouldGameClose():
	return gameShouldClose

def closeGame():
	global gameShouldClose
	gameShouldClose = True

def setSightTrialDone(state):
	global sightTrialDone
	sightTrialDone = state

def isSightTrialDone():
	return sightTrialDone

def isDeductionTrialDone():
	return deductionTrialDone

def setDeductionTrialDone(state):
	global deductionTrialDone
	deductionTrialDone = state

def isStrengthTrialDone():
	return strengthTrialDone

def setStrengthTrialDone(state):
	global strengthTrialDone
	strengthTrialDone = state

def isRolldownComplete():
	return rolldownCompelete

def drawMap(win, mapX, mapY):
	#Draws a map segment on the screen.
	global mapShouldRedrawBool
	mapShouldRedrawBool = False

	#Change the background colour of the window on each draw of the map
	win.setBackground("#" + windowBackground)

	#If the map mapX is higher than the allowed size, the size is set to the allowed size
	if(mapX >= segWidth):	mapX = segWidth
	if(mapY >= segHeight):	mapY = segWidth

	for y in range(tileWinHeight):
		for x in range(tileWinWidth):
			#Get the id of the tile to draw
			tileVal = getTile(x, y, mapX, mapY)
			#Draw the tile based on id
			if(tileVal == 1):	drawGrass(win, x * tileSize, y * tileSize, "64a42c")
			elif(tileVal == 2):	drawWater(win, x * tileSize, y * tileSize)
			elif(tileVal == 3):	drawTree(win, x * tileSize, y * tileSize)
			#Houses get rendered later to prevent graphical bugs, so they're added to a temporary list
			elif(tileVal == 4):	addHouse(x * tileSize, y * tileSize)
			elif(tileVal == 5):	drawSign(win, x * tileSize, y * tileSize)
			elif(tileVal == 6):	drawPath(win, x * tileSize, y * tileSize)
			elif(tileVal == 7):	drawRock(win, x * tileSize, y * tileSize, "9D9C9B", "48585F")
			elif(tileVal == 8):	drawFloor(win, x * tileSize, y * tileSize)
			elif(tileVal == 9):	drawCactus(win, x * tileSize, y * tileSize)
			elif(tileVal == "s"):	drawGrass(win, x * tileSize, y * tileSize, "D0B068")
			elif(tileVal == "a"):	drawSinkHole(win, x * tileSize, y * tileSize, "BDA05E")
			elif(tileVal == "b"):	drawGrass(win, x * tileSize, y * tileSize, "A38A52")
			elif(tileVal == "c"):	drawRock(win, x * tileSize, y * tileSize, "729DAF", "406473")
			elif(tileVal == "d"):	drawGrass(win, x * tileSize, y * tileSize, "BBDDEA")
			elif(tileVal == "e"):	drawStone(win, x * tileSize, y * tileSize, "729DAF", "406473")
			elif(tileVal == "f"):	drawIce(win, x * tileSize, y * tileSize)
			elif(tileVal == "g"):	drawIceStone(win, x * tileSize, y * tileSize,  "729DAF", "406473")
			elif(tileVal == "h"):	drawSinkHole(win, x * tileSize, y * tileSize,  "729DAF")
			elif(tileVal == "i"):	drawGrass(win, x * tileSize, y * tileSize, "7E959E")
			elif(tileVal == "j"):	drawArcheryTarget(win, x * tileSize, y * tileSize)
			elif(tileVal == "k"):	drawBlankTileColoured(win, x * tileSize, y * tileSize, "000")
			elif(tileVal == "l"):	drawAbyssPit(win, x * tileSize, y * tileSize)

	for i in range(0, len(houses), 2):
		drawHouse(win, houses[i], houses[i + 1])


def processMap(mapString):
	#Creates the map list from the loaded map data, only caring about digits and not about whitespace
	map = []
	for i in mapString.splitlines():
		if(i[0] == "#"):	continue
		for a in i:
			if(a.isdigit()):
				map.append(eval(a))
			else:
				map.append(a)


	return map

def processMapMeta(mapString):
	global guiTiles
	#Clear the gui tiles before adding new values to them
	#Gui tiles don't go in the meta data list, because they are separate kinds of values entirely.
	guiTiles = []
	#Processes the meta file for a map
	mapMeta = []
	#Split the input into lines
	for l in mapString.splitlines():
		#Split the lines into individual words
		if(l==""):	continue
		if(l[0] == "$"):
			mapMeta.append(l[2:])
			continue
		if(l[0] == "!"):
			#Values to find the start of the string and the end of the string
			startStringIndex = 0
			endStringIndex = 0
			for i in range(len(l)):
				if(l[i] == "\"" and startStringIndex == 0):
					startStringIndex = i
				if(l[i] == "\"" and startStringIndex != 0):
					endStringIndex = i

			guiTiles.append(l[startStringIndex + 1:endStringIndex])
			for i in l.split():
				if(i.isdigit()):
					guiTiles.append(eval(i))

		for i in l.split():
			#A # in the meta file is a comment, so skip the entire line
			if(i[0] == "#"):	break
			if(i[0] == "!"):	break
			if(i.isdigit()):
				#Only if i is a digit eval it. Because it is possible to have strings
				mapMeta.append(eval(i))
			else:
				mapMeta.append(i)

	return mapMeta

def getTile(x, y, mapX, mapY):
	#returns a tile from the map list based on the current map segment and coordinates
	return map[x + (tileWinWidth * tileWinHeight * mapX) + (y * tileWinWidth) + (tileWinWidth * tileWinHeight * mapY * (segWidth + 1))]

def checkGuiTiles(x, y):
	#Loop over all the tiles in the list
	for i in range(0, len(guiTiles), 5):
		#If the tile is in the same map segment, then proceed.
		if(guiTiles[i + 3] == segX and guiTiles[i + 4] == segY and guiTiles[i + 1] == x and guiTiles[i + 2] == y):
			#If the tile is on the same map segment and the same x and y coordinates then return true
			return guiTiles[i]

	return False


def mapShouldRedraw():
	#called by main every frame
	return mapShouldRedrawBool

def switchSegment(x, y):
	#Switches the segment by a certain ammount, for example + 3 segments on x and 0 on y
	#basically just calls switch to segment
	if(segX + x > segWidth or segY + y > segHeight or segX + x < 0 or segY + y < 0):	return
	switchToSegment(segX + x, segY + y)

def switchToSegment(x, y):
	#Switches the map segment
	#The main loop will redraw it later as it has access to win
	#and I wanted this function to be callable from entities without win
	global segX
	global segY
	global mapShouldRedrawBool
	global mapContent
	global houses

	if(x > segWidth or y > segHeight or x < 0 or y < 0):	return
	segX = x
	segY = y
	mapShouldRedrawBool = True

	for i in mapContent:
		i.undraw()

	#Clear the houses and map content lists. They'll be repopulated when the next map segment is drawn
	houses = []
	mapContent = []

def getSegmentX():
	return segX

def getSegmentY():
	return segY

def setMap(mapData, mapMetaData):
	#Sets the current map and map meta
	global map
	global mapMeta
	global segWidth
	global segHeight
	global mapNameTime
	global mapNameContainer
	global mapNameText
	global currentMapId
	map = mapData
	mapMeta = mapMetaData
	segWidth = eval(mapMeta[2])
	segHeight = eval(mapMeta[3])
	#How long the map name will appear on the screen
	mapNameTime = 100
	mapNameText = mapMeta[0]
	#Change the background colour of the window
	setWindowBackground(mapMeta[1])
	#Set the current map for the story code
	currentMapId = eval(mapMeta[4])

def getMap():
	return map

def getGuiTiles():
	return guiTiles

def getMapMeta():
	return mapMeta

def addObjectToMap(object):
	#add a single object to the map
	#Things are added to the map so they can be cleared later
	mapContent.append(object)

def addObjectsToMap(objects):
	#add multiple objects to the map
	for i in objects:
		mapContent.append(i)

def getMapNameText():
	return mapNameText

def getCurrentMapId():
	return currentMapId

def updateMap():
	#A function to update aspects of the map
	global mapNameTime
	if(mapNameTime > 0):	mapNameTime -= 1
	else:	mapNameContainer.setText("")

	global rolldownCompelete
	if(not rolldownCompelete):
		rolldownDone = True
		for i in rolldownBands:
			if(i.getP2().getY() < winHeight):
				i.move(0, 8)
				rolldownDone = False
		if(rolldownDone):	rolldownCompelete = True

def setWindowBackground(colour):
	global windowBackground
	windowBackground = colour

def drawGrass(win, x, y, specColour):
	#Draw grass has no background rectangle because it's background colour is the default window
	#The colour of the grass specs is defined as a parameter. This just means less tiles have to be defined.
	for i in range(10):
		xx = grassValues[i * 2]
		yy = grassValues[(i * 2) + 1]
		spec = Rectangle(Point(xx + x, yy + y), Point(xx + x + 2, yy + y + 1))
		spec.setFill("#" + specColour)
		spec.setOutline("#" + specColour)
		spec.draw(win)
		addObjectToMap(spec)

def drawWater(win, x, y):
	rect = Rectangle(Point(x, y), Point(x + tileSize, y + tileSize))
	rect.setFill("#00bff3")
	rect.setOutline("#00bff3")
	rect.draw(win)
	addObjectToMap(rect)

	for i in range(8):
		xx = waterValues[i * 2]
		yy = waterValues[(i * 2) + 1]
		spec = Rectangle(Point(xx + x, yy + y), Point(xx + x + 4, yy + y + 1))
		spec.setFill("#00aeef")
		spec.setOutline("#00aeef")
		spec.draw(win)
		addObjectToMap(spec)

def createTree(x, y):
	#I seperated this because I needed it for the strength trial
	stump = Rectangle(Point(x + tileSize - 5, y + tileSize * 2 - 5), Point(x + tileSize + 5, y + tileSize * 2 - 40))
	stump.setFill("#8c6239")
	stump.setOutline("#754c24")

	first = Rectangle(Point(x + 10, y + 8), Point(x + 47, y + 61))
	second = Rectangle(Point(x + 85, y + 68), Point(x + 38, y + 21))

	for i in [first, second]:
		i.setFill("#00a651")
		i.setOutline("#007236")

	return [stump, first, second]

def drawTree(win, x, y):
	#The tree spans four tiles (2x2)
	#These for loops draw grass underneath
	for yy in range(2):
		for xx in range(2):
			drawGrass(win, x + xx * tileSize, y + yy * tileSize, "64a42c")

	tree = createTree(x, y)
	for i in tree:
		addObjectToMap(i)
		i.draw(win)

def addHouse(x, y):
	#Add the location of a house to a list
	#Houses are drawn after the rest of the tiles to prevent graphical errors
	houses.append(x)
	houses.append(y)

def drawHouse(win, x, y):
	#The house spans six tiles (2x3) and looks very nice
	point1 = Point(x, y + tileSize - 10)
	point2 = Point(x + tileSize - 10, y)
	point3 = Point(x + tileSize * 2 + 10, y)
	point4 = Point(x + tileSize * 3, y + tileSize - 10)
	point5 = Point(x + tileSize * 3, y + tileSize)
	point6 = Point(x, y + tileSize)

	roof = Polygon([point1, point2, point3, point4, point5, point6])
	roof.setFill("#8c6239")
	roof.setOutline("#603913")

	houseBody = Rectangle(Point(x, y + tileSize), Point(x + tileSize * 3, y + tileSize * 2))
	houseBody.setFill("#a09994")
	houseBody.setOutline("#665f59")

	win1 = Rectangle(Point(x + 14, y + tileSize + 14), Point(x + tileSize - 14, y + tileSize * 2 - 14))
	win1.setFill("#1996bf")
	win1.setOutline("#174add")

	win2 = Rectangle(Point(x + tileSize * 2 + 14, y + tileSize + 14), Point(x + tileSize + tileSize * 2 - 14, y + tileSize * 2 - 14))
	win2.setFill("#1996bf")
	win2.setOutline("#174add")

	door = Rectangle(Point(x + tileSize + 10, y + tileSize + 10), Point(x + tileSize * 2 - 10, y + tileSize * 2))
	door.setFill("#8a8179")
	door.setOutline("#665f59")

	for i in [houseBody, roof, win1, win2, door]:
		i.draw(win)
		addObjectToMap(i)

def drawSign(win, x, y):
	board = Rectangle(Point(x, y), Point(x + tileSize, y + 30))
	board.setFill("#8c6239")
	board.setOutline("#603913")

	stand = Rectangle(Point(x + tileSize / 2 - 5, y), Point(x + tileSize / 2 + 5, y + 48))
	stand.setFill("#8c6239")
	stand.setOutline("#603913")

	line1 = Rectangle(Point(x + 5, y + 6), Point(x + tileSize - 5, y + 11))
	line1.setFill("#1c1a18")
	line1.setOutline("#1c1a18")

	line2 = Rectangle(Point(x + 5, y + 20), Point(x + tileSize - 5, y + 25))
	line2.setFill("#1c1a18")
	line2.setOutline("#1c1a18")

	for i in [stand, board, line1, line2]:
		i.draw(win)
		addObjectToMap(i)

def drawPath(win, x, y):
	background = Rectangle(Point(x, y), Point(x + tileSize, y + tileSize))
	background.setFill("#DAC782")
	background.setOutline("#DAC782")
	background.draw(win)
	addObjectToMap(background)
	for i in range(8):
		xx = waterValues[i * 2]
		yy = waterValues[(i * 2) + 1]
		spec = Rectangle(Point(xx + x, yy + y), Point(xx + x + 4, yy + y + 1))
		spec.setFill("#bfa840")
		spec.setOutline("#bfa840")
		spec.draw(win)
		addObjectToMap(spec)

def drawRock(win, x, y, fill, outline):
	point1 = Point(x + 10, y  + tileSize * 2 - 10)
	point2 = Point(x + 20, y  + tileSize * 2 - 30)
	point3 = Point(x + 30, y  + tileSize * 2 - 30)
	point4 = Point(x + 60, y  + 20)
	point5 = Point(x + 80, y  + 25)
	point6 = Point(x + 86, y  + tileSize * 2 - 10)

	point7 = Point(x + 35,  y + tileSize * 2 - 10)
	point8 = Point(x + 40,  y + tileSize * 2 - 20)
	point9 = Point(x + 60,  y + tileSize * 2 - 25)
	point10 = Point(x + 70,  y + tileSize * 2 - 35)
	point11 = Point(x + 80,  y + tileSize * 2 - 10)

	rock = Polygon([point1, point2, point3, point4, point5, point6])
	rockFront = Polygon([point7, point8, point9, point10, point11])
	for i in [rock, rockFront]:
		i.setFill("#" + fill)#9D9C9B
		i.setOutline("#" + outline)#48585F
		i.draw(win)
		addObjectToMap(i)


def drawFloor(win, x, y):
	board = Rectangle(Point(x, y), Point(x + tileSize, y + tileSize))
	board.setFill("#8C623A")
	board.setOutline("#825830")
	board.draw(win)
	addObjectToMap(board)

def drawCactus(win, x, y):
	for yy in range(2):
		for xx in range(2):
			drawGrass(win, x + xx * tileSize, y + yy * tileSize, "D0B068")
	
	point1 = Point(x + tileSize - 15, y + tileSize * 2 - 20)
	point2 = Point(x + tileSize - 15, y + tileSize)
	point3 = Point(x + 10, y + tileSize)
	point4 = Point(x + 10, y + 10)
	point5 = Point(x + 25, y + 10)
	point6 = Point(x + 25, y + tileSize - 10)
	point7 = Point(x + tileSize - 15, y + tileSize - 10)
	point8 = Point(x + tileSize - 15, y + 20)
	point9 = Point(x + tileSize + 15, y + 20)
	point10 = Point(x + tileSize + 15, y + tileSize)
	point11 = Point(x + tileSize * 2 - 20, y + tileSize)
	point12 = Point(x + tileSize * 2 - 20, y + 30)
	point13 = Point(x + tileSize * 2 - 10, y + 30)
	point14 = Point(x + tileSize * 2 - 10, y + tileSize + 10)
	point15 = Point(x + tileSize + 15, y + tileSize + 10)
	point16 = Point(x + tileSize + 15, y + tileSize * 2 - 20)

	polyCactus = Polygon([point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16])
	polyCactus.setFill("#00a651")
	polyCactus.setOutline("#007236")
	polyCactus.draw(win)
	addObjectToMap(polyCactus)

def drawSinkHole(win, x, y, colour):
	hole = Oval(Point(x, y + tileSize / 2), Point(x + tileSize, y + tileSize))
	hole.setFill("#" + colour)

	hole.draw(win)
	addObjectToMap(hole)

def drawStone(win, x, y, fill, outline):
	point1 = Point(x, y + tileSize)
	point2 = Point(x + 10, y + tileSize - 20)
	point3 = Point(x + 20, y + tileSize - 30)
	point4 = Point(x + 30, y + 5)
	point5 = Point(x + tileSize, y + tileSize)

	stone = Polygon([point1, point2, point3, point4, point5])
	stone.setFill("#" + fill)
	stone.setOutline("#" + outline)

	stone.draw(win)
	addObjectToMap(stone)

def drawIce(win, x, y):
	background = Rectangle(Point(x, y), Point(x + tileSize, y + tileSize))
	background.setFill("#ABFFFA")
	background.setOutline("#ABFFFA")

	background.draw(win)
	addObjectToMap(background)

	point1 = Point(x, y + tileSize - 7)
	point2 = Point(x + tileSize - 7, y)
	point3 = Point(x + tileSize, y)
	point4 = Point(x + tileSize, y + 7)
	point5 = Point(x + 7, y + tileSize)
	point6 = Point(x, y + tileSize)

	point7 = Point(x, y)
	point8 = Point(x + 7, y)
	point9 = Point(x, y + 7)

	point10 = Point(x + tileSize, y + tileSize)
	point11 = Point(x + tileSize - 7, y + tileSize)
	point12 = Point(x + tileSize, y + tileSize - 7)

	mainStreak = Polygon([point1, point2, point3, point4, point5, point6])
	topStreak = Polygon([point7, point8, point9])
	bottomStreak = Polygon([point10, point11, point12])

	for i in [mainStreak, topStreak, bottomStreak]:
		i.setFill("white")
		i.setOutline("white")
		i.draw(win)
		addObjectToMap(i)

def drawIceStone(win, x, y, stoneFill, stoneOutline):
	drawIce(win, x, y)
	drawStone(win, x, y, stoneFill, stoneOutline)

def drawArcheryTarget(win, x, y):
	drawFloor(win, x, y)
	stand = Rectangle(Point(x + 8, y + 24), Point(x + 48 - 8, y + 48))
	stand.setFill("brown")
	blueCircle = Circle(Point(x + 24, y + 24), 24)
	blueCircle.setFill("blue")
	yellowCircle = Circle(Point(x + 24, y + 24), 18)
	yellowCircle.setFill("yellow")
	redCircle = Circle(Point(x + 24, y + 24), 8)
	redCircle.setFill("red")

	for i in [stand, blueCircle, yellowCircle, redCircle]:
		i.draw(win)
		addObjectToMap(i)

def drawBlankTileColoured(win, x, y, colour):
	bottom = Rectangle(Point(x, y), Point(x + tileSize, y + tileSize))
	bottom.setFill("#" + colour)
	bottom.setOutline("#" + colour)
	bottom.draw(win)
	addObjectToMap(bottom)

def drawAbyssPit(win, x, y):
	for i in range(4):
		drawGrass(win, x + 48 * i, y, "64a42c")
	pit = Oval(Point(x, y + tileSize / 2), Point(x + tileSize * 4, y + tileSize * 2))
	pit.setFill("black")
	pit.draw(win)
	addObjectToMap(pit)