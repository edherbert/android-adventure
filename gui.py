from graphics import *
from player import *
#The text that needs to be spoken
guiSpeakText = []
#A variable used to animate the gui
guiCount = 0
#Whether the gui is currently shown, for the entire text.
guiSpeaking = False
#Whether the scrolling text animation is done for that portion of text or not
guiDoneSpeaking = False
#The graphical objects that make up the gui
guiSpeakComponents = []
#Determines whether to draw on the first line or the second
firstGuiLine = True
#The current ammount of text on the screen (used for the text animation)
currentTextLength = 0
#Whether the gui has been drawn or not
shouldDrawGui = False
#Whether the gui arrow is up or down (used for animation)
guiArrowDown = False
#Whether the gui arrow has been drawn or not
guiArrowDrawn = False
#The time before the player can next bring up a gui using the z key
playerInteractCooldown = 0
#A variable to determine if the player 
storySpoken = False

#The default text speed
defaultTextSpeed = 2
#The current text speed
currentTextSpeed = defaultTextSpeed

def guiInit(win):
	#Create all the gui components and add them to a list
	global guiSpeakComponents
	outer = Rectangle(Point(48 * 3, win.getHeight() - 120), Point(win.getWidth() - 48 * 3, win.getHeight() - 10))
	outer.setFill("#265784")
	outer.setOutline("#265784")

	band = Rectangle(Point(outer.getP1().getX() + 5, outer.getP1().getY() + 5), Point(outer.getP2().getX() - 5, outer.getP2().getY() - 5))
	band.setFill("white")
	band.setOutline("white")

	inner = Rectangle(Point(band.getP1().getX() + 5, band.getP1().getY() + 5), Point(band.getP2().getX() - 5, band.getP2().getY() - 5))
	inner.setFill("#265784")
	inner.setOutline("#265784")

	contentFirst = Text(Point(inner.getCenter().getX(), inner.getCenter().getY() - 20), "")
	contentFirst.setFill("white")
	contentFirst.setFace("arial")
	contentFirst.setSize(23)

	contentSecond = Text(Point(inner.getCenter().getX(), inner.getCenter().getY() + 20), "")
	contentSecond.setFill("white")
	contentSecond.setFace("arial")
	contentSecond.setSize(23)

	arrowBox = Rectangle(Point(outer.getP2().getX() - 40, outer.getP2().getY() - 20), Point(outer.getP2().getX() - 20, outer.getP2().getY()))
	arrowBox.setFill("#265784")
	arrowBox.setOutline("#265784")

	arrowP1 = Point(outer.getP2().getX() - 40, outer.getP2().getY() - 20)
	arrowP2 = Point(outer.getP2().getX() - 20, outer.getP2().getY() - 20)
	arrowP3 = Point(outer.getP2().getX() - 30, outer.getP2().getY() - 5)
	arrow = Polygon([arrowP1, arrowP2, arrowP3])
	arrow.setFill("red")

	for i in [outer, band, inner, contentFirst, contentSecond, arrowBox, arrow]:
		guiSpeakComponents.append(i)

def getDefaultTextSpeed():
	return defaultTextSpeed

def setTextSpeed(speed):
	global currentTextSpeed
	currentTextSpeed = speed

def guiSpeak(text):
	#Populates the guiSpeakText list with values
	global guiSpeaking
	global guiSpeakText
	global shouldDrawGui

	if(guiSpeaking):	return

	guiSpeaking = True

	#Blank the speak text
	guiSpeakText = []

	shouldDrawGui = True

	#Holds the current line of text
	textCurrent = ""
	#The input split by words
	#If a word pushes the string length over 40 then it is pushed to the next line
	splitText = text.split()
	for i in range(0, len(splitText)):
		#+1 to each of these due to spaces
		#If the current size of text current and split text are less than 40 then add them
		if(len(textCurrent) + len(splitText[i]) + 1 <= 40):
			textCurrent += splitText[i] + " "
		else:
			#Otherwise append to the list and reset textCurrent
			guiSpeakText.append(textCurrent)
			textCurrent = ""
			textCurrent += splitText[i] + " "

		if(i >= len(splitText) - 1):
			#Finally, if the end of the string is reached, add the rest of the characters to the list
			guiSpeakText.append(textCurrent)

def updateGui(win, key):
	global guiCount
	global currentTextLength
	global firstGuiLine
	global guiSpeaking
	global guiDoneSpeaking
	global shouldDrawGui
	global guiArrowDown
	global playerInteractCooldown
	guiCount += 1
	#If the gui has yet to be drawn, then draw it.
	if(shouldDrawGui):
		shouldDrawGui = False
		drawGuiBox(win)

	#A variable used to determine if the text that needs to be drawn only takes up one line
	oneLine = False
	if(guiSpeaking and guiCount % currentTextSpeed == 0):
		#If the list of text only contains one value then one line is set to true
		if(len(guiSpeakText) <= 1):	oneLine = True

		if(oneLine):
			#If there is only one line draw it and then set gui done speaking to true
			guiSpeakComponents[3].setText(guiSpeakText[0][0:currentTextLength])
			if(currentTextLength >= len(guiSpeakText[0])):	guiDoneSpeaking = True
		else:
			#If there is more than one line then first gui line is used to determine which line to draw to
			if(firstGuiLine):
				guiSpeakComponents[3].setText(guiSpeakText[0][0:currentTextLength])
				if(currentTextLength >= len(guiSpeakText[0])):
					#Once the end of the first line has been reached, drop to the next
					currentTextLength = 0
					firstGuiLine = False
			else:
				#Animate the second line and then gui done speaking is true
				guiSpeakComponents[4].setText(guiSpeakText[1][0:currentTextLength])
				if(currentTextLength >= len(guiSpeakText[1])):	guiDoneSpeaking = True

		currentTextLength += 1

	#Only show the continue arrow if gui done speaking is true
	if(guiDoneSpeaking):
		showArrow(win)
	else:
		hideArrow()

	if(playerInteractCooldown > 0):
		playerInteractCooldown -= 1

	if(key == "z" and guiSpeaking and guiDoneSpeaking):
		#Code to push the next set of strings or close the gui
		guiSpeakComponents[3].setText("")
		guiSpeakComponents[4].setText("")
		guiDoneSpeaking = False
		firstGuiLine = True
		currentTextLength = 0
		#Remove values from the text list
		#If there is only one, then remove the first, if there is two remove two
		if(oneLine):
			if(len(guiSpeakText) > 0):	guiSpeakText.pop(0)
		else:
			#Two separate if statements just incase one pop removed the last value, the other one should not run
			if(len(guiSpeakText) > 0):	guiSpeakText.pop(0)
			if(len(guiSpeakText) > 0):	guiSpeakText.pop(0)

		if(len(guiSpeakText) <= 0):
			#If there are no more values in the list then remove the gui and set speaking to false
			removeGui()

	#code to move the gui arrow up and down
	if(guiSpeaking and guiCount % 40 == 0 and guiArrowDrawn):
		if(guiArrowDown):
			guiSpeakComponents[6].move(0, -5)
		else:
			guiSpeakComponents[6].move(0, 5)
		guiArrowDown = not guiArrowDown

def getGuiComponents():
	return guiSpeakComponents

def removeGui():
	global guiSpeaking
	setPlayerInteractCooldown(10)
	guiSpeaking = False
	undrawGuiBox()
	hideArrow()

def removeGuiDone():
	#remove the gui Completely
	global guiDoneSpeaking
	guiDoneSpeaking = False
	removeGui()

def guiStory(speech, incrementCounter):
	global storySpoken
	if(storySpoken == False):
		guiSpeak(speech)
		storySpoken = True
	if(not isSpeaking() and storySpoken):
		storySpoken = False
		return incrementCounter + 1
	else:
		return incrementCounter


def isSpeaking():
	return guiSpeaking

def drawGuiBox(win):
	#Draws the gui box except for the red arrow
	for i in range(0, 5):
		guiSpeakComponents[i].draw(win)

def undrawGuiBox():
	#Does the same except this one undraws it
	for i in range(0, 5):
		guiSpeakComponents[i].undraw()

def showArrow(win):
	#Draw the red animation arrow
	global guiArrowDrawn
	if(not guiArrowDrawn):
		guiSpeakComponents[5].draw(win)
		guiSpeakComponents[6].draw(win)
		guiArrowDrawn = True

def removeArrow():
	#removes the arrow, without caring if it's been drawn or not.
	global guiArrowDrawn
	guiSpeakComponents[5].undraw()
	guiSpeakComponents[6].undraw()
	guiArrowDrawn = False

def hideArrow():
	#Undraw the animation arrow
	global guiArrowDrawn
	if(guiArrowDrawn):
		guiSpeakComponents[5].undraw()
		guiSpeakComponents[6].undraw()
		guiArrowDrawn = False

def setPlayerInteractCooldown(time):
	#Used to make sure that there is a wait between player interactions
	#If this was not there then the player could press z to close the dialogue
	#and immediately be brought back to it (due to another interaction)
	global playerInteractCooldown
	playerInteractCooldown = time

def playerCanInteract():
	#Returns whether or not the player can interact (if the interact cooldown has not finished)
	if(playerInteractCooldown <= 0):	return True
	else:	return False
