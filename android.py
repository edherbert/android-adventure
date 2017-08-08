from map import *

#A list of android information
androids = []

def checkAndroidCollision(player, x, y):
	#Checks collision between the player and the androids in the map
	px1 = player[0].getP1().getX() + x
	px2 = player[0].getP2().getX() + x
	py1 = player[0].getP1().getY() + y
	py2 = player[0].getP2().getY() + y

	for i in range(0, len(androids), 17):
		if(androids[i + 13] == getSegmentX() and androids[i + 14] == getSegmentY()):
			ax1 = androids[i].getP1().getX()
			ax2 = androids[i].getP2().getX()
			ay1 = androids[i].getP1().getY()
			ay2 = androids[i].getP2().getY()
			if(px1 < ax2 and px2 > ax1 and py1 < ay2 and py2 > ay1):
				return True

	return False

def setAndroidSpeech(android, speech):
	#Sets the speech of an android
	android[16] = speech

def addAndroid(android, x, y, segX, segY):
	#Adds an android to the androids list
	global androids
	android[13] = segX
	android[14] = segY

	#Move the android to it's correct location on the map
	moveAndroid(android, x, y)
	for i in android:
		androids.append(i)

def drawAndroids(win):
	global androids
	#draws all the androids in the list relevant to this map segment
	#Loop through the entire list in 15s for each android
	for i in range(0, len(androids), 17):
		#Loop over the body parts to draw them,
		#The first part is the bounding box used to make collisions nicer, so don't draw that
		if(androids[i + 13] == getSegmentX() and androids[i + 14] == getSegmentY()):
			androids[i + 15] = True
			for part in range(1, 12):
				androids[i + part].draw(win)

def undrawAndroids():
	#Just the draw function, but this one undraws
	global androids
	for i in range(0, len(androids), 17):
		if(androids[i + 15] == False):	continue
		androids[i + 15] = False
		for part in range(1, 12):
			androids[i + part].undraw()

def removeAndroids():
	#Removes every android from the list before a map switch
	global androids
	undrawAndroids()
	androids = []

def createAndroid(colour):
	#Create android without scale
	return createAndroidWithScale(colour, 1)

def createAndroidWithScale(colour, scale):
	#Returns a list of graphical objects and other bits that represents an android, with scale

	#This object is for collision detection and other logic, it just makes the code simpler
	boundingBox = Rectangle(Point(0 * scale, 0 * scale), Point(48 * scale, 48 * scale))

	head = Circle(Point(24 * scale, 16 * scale), 16 * scale)
	body = Rectangle(Point(8 * scale, 16 * scale), Point(40 * scale, 40 * scale))

	leg1 = Rectangle(Point(10 * scale, 40 * scale), Point(15 * scale, 48 * scale))
	leg2 = Rectangle(Point(33 * scale, 40 * scale), Point(38 * scale, 48 * scale))

	arms = Rectangle(Point(4 * scale, 16 * scale), Point(44 * scale, 34 * scale))

	eye1 = Circle(Point(16 * scale, 13 * scale), 3 * scale)
	eye2 = Circle(Point(32 * scale, 13 * scale), 3 * scale)

	armSide = Rectangle(Point(19 * scale, 17 * scale), Point(27 * scale, 32 * scale))

	#These covers hide the black outlines of the other body pieces
	#I wanted the androids to have outlines around their bodies but not the insides,
	#This was the best option to achieve that
	bodyCover = Rectangle(Point(9 * scale, 16 * scale), Point(39 * scale, 30 * scale))
	coverLeft = Rectangle(Point(11 * scale, 39 * scale), Point(14 * scale, 47 * scale))
	coverRight = Rectangle(Point(34 * scale, 40 * scale), Point(37 * scale, 47 * scale))

	android = [boundingBox, head, arms, body, leg1, leg2, coverLeft, coverRight, bodyCover, eye1, eye2, armSide]
	for i in android:
		if(i == eye1 or i == eye2):
			i.setFill("white")
			i.setOutline("white")
		elif(i == bodyCover or i == coverLeft or i == coverRight):
			i.setOutline(colour)
			i.setFill(colour)
		elif(i == boundingBox):
			pass
		elif(i == armSide):
			i.setOutline(colour)
		else:
			i.setFill(colour)
			i.setOutline("black")

	#give the android other values, such as colour and the segX and segY
	android.append(colour)
	#These 0s are just placeholders
	android.append(0)
	android.append(0)
	#A boolean to tell if the android has already been drawn
	android.append(False)
	#A string that is used when talking to an android
	android.append("")
	return android

def drawAndroid(win, android):
	#Draw androids. -5 because 
	for i in range(1, len(android) - 5):
		android[i].draw(win)

def undrawAndroid(android):
	for i in range(1, len(android) - 5):
		android[i].undraw()

def moveAndroid(android, x, y):
	for i in range(0, len(android) - 5):
		android[i].move(x, y)

def getAndroids():
	return androids

def getAndroidById(id):
	return androids[id*17:id*17+17]

def changeAndroidDirection(android, direction):
	#A function that changes the look of the android depending on it's direction
	#0 up, 1 left, 2 right, 3 down
	#You can tell what each section of the array is by checking the list in the create android function
	colour = android[12]
	if(direction == 0):
		android[9].setFill(colour)
		android[10].setFill(colour)
		android[9].setOutline(colour)
		android[10].setOutline(colour)
	if(direction == 3):
		android[9].setFill("white")
		android[10].setFill("white")
		android[9].setOutline("white")
		android[10].setOutline("white")

	if(direction == 1 or direction == 2):
		#move the arms somewhere off screen
		#You can't redraw and undraw because:
		#A, it leads to layering issues
		#B, it would require win to be passed in as an arguement, which I don't want to do
		android[2].move(-1000, -1000)
		android[11].setOutline("black")
	else:
		#This works out the exact ammount that the arms need to move to be back to the correct position
		android[2].move(android[3].getP1().getX() - android[2].getP1().getX() - 4, android[3].getP1().getY() - android[2].getP1().getY())
		android[11].setOutline(colour)

	if(direction == 1):
		android[9].setFill("white")
		android[9].setOutline("white")
		android[10].setFill(colour)
		android[10].setOutline(colour)
	if(direction == 2):
		android[9].setFill(colour)
		android[9].setOutline(colour)
		android[10].setFill("white")
		android[10].setOutline("white")
