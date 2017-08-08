from graphics import *
from map import *
from android import *
from player import *
from gui import *
import time
import random
import math

#A list of graphics objects for the intro
introWindowGUI = []

#To cover up the intro screen
cover = Rectangle(Point(0, 0), Point(winWidth, winHeight))

redApples = []
badApples = []

playerIntro = createAndroid("green")
playerMoveX = 0
playerMoveY = 0

magentaIntro = createAndroid("#D80073")

storySection = 0
currentAppleCount = 0
#The direction the apple runs away from the player in
#0 up, 1 left, 2 right, 3 down
appleDirection = 0

def updateIntro(win, key, currentTrial):
	global storySection
	if(storySection == 0):
		name = introWindowGUI[3].getText()
		if(name != ""):
			introWindowGUI[4].setFill("green")
			mouse = win.checkMouse()
			if(mouse != None):
				if(mouse.getX() >= introWindowGUI[4].getP1().getX() and mouse.getY() >= introWindowGUI[4].getP1().getY() and mouse.getX() <= introWindowGUI[4].getP2().getX() and mouse.getY() <= introWindowGUI[4].getP2().getY()):
					name = introWindowGUI[3].getText()
					setPlayerName(name)
					storySection += 1
					for i in range(4):
						introWindowGUI[0].undraw()
						introWindowGUI.pop(0)
					if(name.upper() == "Edward".upper() or name.upper() == "Ed".upper()):	introWindowGUI[2].setText("That's a great name!")
					if(name.upper() == "Magenta".upper()):	win.close()
					for i in range(2, len(introWindowGUI)):
						introWindowGUI[i].draw(win)
					introWindowGUI[1].setText("ok")
		else:
			introWindowGUI[4].setFill("red")
	elif(storySection == 1):
		mouse = win.getMouse()
		if(mouse.getX() >= introWindowGUI[0].getP1().getX() and mouse.getY() >= introWindowGUI[0].getP1().getY() and mouse.getX() <= introWindowGUI[0].getP2().getX() and mouse.getY() <= introWindowGUI[0].getP2().getY()):
			storySection += 1
			for i in range(len(introWindowGUI)):
				introWindowGUI[0].undraw()
				introWindowGUI.pop(0)
			countText = Text(Point(30, 20), "0/3")
			countText.setSize(20)
			countText.draw(win)
			introWindowGUI.append(countText)
	elif(storySection == 2):
		time.sleep(0.5)
		drawAndroid(win, playerIntro)
		time.sleep(0.5)
		for i in redApples:
			i.draw(win)
			time.sleep(0.3)
		time.sleep(1)
		for i in badApples:
			i.draw(win)
			time.sleep(0.1)

		storySection += 1
	elif(storySection == 3):
		global playerMoveX
		global playerMoveY
		if(key == "Up"):	playerMoveY -= 1
		if(key == "Down"):	playerMoveY += 1
		if(key == "Left"):	playerMoveX -= 1
		if(key == "Right"):	playerMoveX += 1
		moveAndroid(playerIntro, playerMoveX, playerMoveY)
		if(playerIntro[0].getCenter().getX() <= 0 or playerIntro[0].getCenter().getY() <= 0 or playerIntro[0].getCenter().getX() >= winWidth or playerIntro[0].getCenter().getY() >= winHeight):
			#if the player goes outside the window then reset them to the center of the window
			moveAndroid(playerIntro, winWidth / 2 - playerIntro[0].getCenter().getX(), winHeight / 2 - playerIntro[0].getCenter().getY())
			playerMoveX = 0
			playerMoveY = 0
		for i in redApples:
			if(androidAppleCollision(playerIntro[0].getCenter(), i.getCenter())):
				global currentAppleCount
				if(currentAppleCount <= 1):
					currentAppleCount += 1
					introWindowGUI[0].setText(str(currentAppleCount) + "/3")
					i.undraw()
					redApples.remove(i)
				else:
					storySection += 1

		for i in badApples:
			if(androidAppleCollision(playerIntro[0].getCenter(), i.getCenter())):
				#Move the android back to the center of the screen
				moveAndroid(playerIntro, winWidth / 2 - playerIntro[0].getCenter().getX(), winHeight / 2 - playerIntro[0].getCenter().getY())
				#Remove the bad apple they collided with
				playerMoveX = 0
				playerMoveY = 0
				i.undraw()
				badApples.remove(i)
	elif(storySection == 4):
		#This is quite a dirty way to center the text but it works
		introWindowGUI[0].setText("                           Press Z to continue")
		storySection = guiStory("Wait!", storySection)
	elif(storySection == 5):
		introWindowGUI[0].setText(str(currentAppleCount) + "/3")
		storySection = guiStory("What do you think you're doing!", storySection)
	elif(storySection == 6):
		storySection = guiStory("You can't just eat me like that!", storySection)
	elif(storySection == 7):
		for i in range(0, len(badApples)):
			badApples[0].undraw()
			badApples.pop(0)
			time.sleep(0.1)
		storySection += 1
	elif(storySection == 8):
		#Figure out which direction to move the player on the x axis
		if(playerIntro[0].getCenter().getX() < winWidth / 2):
			moveAndroid(playerIntro, 6, 0)
			redApples[0].move(6, 0)
		else:
			moveAndroid(playerIntro, -6, 0)
			redApples[0].move(-6, 0)
		#If they're within a certain boundary of the center then switch and do the same thing for the y axis.
		if(playerIntro[0].getCenter().getX() > abs(winWidth / 2) - 6 and playerIntro[0].getCenter().getX() < abs(winWidth / 2) + 6):	storySection += 1

	elif(storySection == 9):
		if(playerIntro[0].getCenter().getY() < winHeight / 2):
			redApples[0].move(0, 6)
			moveAndroid(playerIntro, 0, 6)
		else:
			moveAndroid(playerIntro, 0, -6)
			redApples[0].move(0, -6)

		if(playerIntro[0].getCenter().getY() > abs(winHeight / 2) - 6 and playerIntro[0].getCenter().getY() < abs(winHeight / 2) + 6):	storySection += 1
	elif(storySection == 10):
		#Figure out which direction the apple needs to move
		global appleDirection
		time.sleep(0.5)
		if(redApples[0].getCenter().getY() > playerIntro[0].getCenter().getY()):	appleDirection = 3
		if(redApples[0].getCenter().getY() < playerIntro[0].getCenter().getY()):	appleDirection = 0
		storySection += 1

	elif(storySection == 11):
		#Move the apple
			if(appleDirection == 0):
				redApples[0].move(0, -3)
				changeAndroidDirection(playerIntro, 0)
				if(redApples[0].getCenter().getY() < winHeight / 2 - 60):	storySection += 1
			else:
				redApples[0].move(0, 3)
				if(redApples[0].getCenter().getY() > winHeight / 2 + 60):	storySection += 1

	elif(storySection == 12):
		storySection = guiStory("What? Just because I'm an apple means you can just eat me?", storySection)
	elif(storySection == 13):
		storySection = guiStory("You monster!", storySection)
	elif(storySection == 14):
		storySection = guiStory("Don't I have just as much right to life as you do?", storySection)
	elif(storySection == 15):
		storySection = guiStory("Get... Get away from me!", storySection)
	elif(storySection == 16):
		if(appleDirection == 0):
			redApples[0].move(0, -3)
		else:
			redApples[0].move(0, 3)
		#Apple runs away
		if(redApples[0].getCenter().getY() < -10 or redApples[0].getCenter().getY() > winHeight + 10):	
			redApples[0].undraw()
			redApples.pop(0)
			time.sleep(3)
			drawAndroid(win, magentaIntro)
			changeAndroidDirection(magentaIntro, 1)
			storySection += 1

	#Magenta appears
	elif(storySection == 17):
		moveAndroid(magentaIntro, -2, 0)
		if(magentaIntro[0].getP1().getX() <= winWidth / 2 + 48):	storySection += 1
	elif(storySection == 18):
		time.sleep(3)
		changeAndroidDirection(magentaIntro, appleDirection)
		time.sleep(2)
		changeAndroidDirection(magentaIntro, 1)
		time.sleep(2)
		changeAndroidDirection(magentaIntro, appleDirection)
		storySection += 1
	elif(storySection == 19):
		storySection = guiStory("Dear me.", storySection)
	elif(storySection == 20):
		storySection = guiStory("It seems like you've run into a bit of a situation.", storySection)
	elif(storySection == 21):
		time.sleep(1)
		changeAndroidDirection(magentaIntro, 1)
		storySection += 1
	elif(storySection == 22):
		storySection = guiStory("Let's get the formalities out of the way first.", storySection)
	elif(storySection == 23):
		storySection = guiStory("My name is Magenta. We androids are named after our colours!", storySection)
	elif(storySection == 24):
		storySection = guiStory("So what can I call you, Green perhaps?", storySection)
	elif(storySection == 25):
		changeAndroidDirection(playerIntro, 2)
		storySection = guiStory("Hmmm. " + getPlayerName() + " is it? That's a bit unconventional but it's a good name.", storySection)
	elif(storySection == 26):
		storySection = guiStory("Well " + getPlayerName() + ", I hate to be the bearer of bad news but I'm afraid you're going to have to go after that apple.", storySection)
	elif(storySection == 27):
		storySection = guiStory("See, at some point the apples became sentient, cognitively aware and so on. Apparently they didn't take too kindly to the thought of being eaten.", storySection)
	elif(storySection == 28):
		storySection = guiStory("Some of the apples just accepted their fate, but then again there were those that didn't.", storySection)
	elif(storySection == 29):
		storySection = guiStory("The problem is that you need to eat all three apples to win this game, otherwise it will never end.", storySection)
	elif(storySection == 30):
		storySection = guiStory("My third apple ran away as well and believe me, being trapped inside a game for the rest of time is not ideal.", storySection)
	elif(storySection == 31):
		storySection = guiStory("I've been here for so long, I can't remember who I was back in the real world.", storySection)
	elif(storySection == 32):
		storySection = guiStory("That's why I want to help you! I know where that apple ran off to.", storySection)
	elif(storySection == 33):
		storySection = guiStory("North of the Android Village is a place named the Eternal Abyss.", storySection)
	elif(storySection == 34):
		storySection = guiStory("That's where the apples always run away to. You're going to have to go in there and find it.", storySection)
	elif(storySection == 35):
		changeAndroidDirection(playerIntro, 0)
		changeAndroidDirection(magentaIntro, 0)
		storySection += 1
	elif(storySection == 36):
		storySection = guiStory("Otherwise that counter is going to be stuck at 2/3 forever.", storySection)
	elif(storySection == 37):
		changeAndroidDirection(magentaIntro, 1)
		storySection += 1
	elif(storySection == 38):
		storySection = guiStory("Here, let me show you the way.", storySection)
	elif(storySection == 39):
		changeAndroidDirection(magentaIntro, 0)
		time.sleep(0.5)
		storySection += 1
	elif(storySection == 40):
		moveAndroid(magentaIntro, 0, -3)
		if(magentaIntro[0].getCenter().getY() <= 200):
			changeAndroidDirection(magentaIntro, 3)
			time.sleep(1)
			storySection += 1
	elif(storySection == 41):
		storySection = guiStory("This way.", storySection)
	elif(storySection == 42):
		changeAndroidDirection(magentaIntro, 0)
		moveAndroid(magentaIntro, 0, -2)
		if(magentaIntro[0].getCenter().getY() <= -30):
			undrawAndroid(magentaIntro)
			storySection += 1
	elif(storySection == 43):
		time.sleep(1)
		changeAndroidDirection(playerIntro, 3)
		time.sleep(2)
		changeAndroidDirection(playerIntro, 0)
		time.sleep(1)
		storySection += 1
	elif(storySection == 44):
		moveAndroid(playerIntro, 0, -1)
		if(playerIntro[0].getCenter().getY() <= 150):
			undrawAndroid(playerIntro)
			introWindowGUI[0].undraw()
			introWindowGUI.pop(0)

			title = Text(Point(winWidth / 2, winHeight / 2), "Android Adventure")
			title.setSize(36)
			title.setFill("black")
			title.draw(win)
			introWindowGUI.append(title)

			underTitleText = Text(Point(winWidth / 2, winHeight / 2 + 50), "By Edward Herbert")
			underTitleText.setSize(12)
			underTitleText.setFill("black")
			introWindowGUI.append(underTitleText)
			storySection += 1

	elif(storySection == 45):
		time.sleep(2)
		introWindowGUI[1].draw(win)
		time.sleep(4)
		storySection += 1
	elif(storySection == 46):
		for i in range(2):
			introWindowGUI[0].undraw()
			introWindowGUI.pop(0)
		cover.setFill("black")
		cover.setOutline("black")
		time.sleep(2)
		storySection += 1
	elif(storySection == 47):
		setCanPlayerMove(True)
		setMap(processMap(readMap("maps/androidVillage.txt")), processMapMeta(readMap("maps/androidVillageMeta.txt")))
		switchSegment(0, 0)
		cover.undraw()
		return 0

	return currentTrial

def androidAppleCollision(circlePoint, rectPoint):
    circleDistanceX = abs(circlePoint.getX() - rectPoint.getX())
    circleDistanceY = abs(circlePoint.getY() - rectPoint.getY())

    if (circleDistanceX > (48/2 + 10)):	return False
    if (circleDistanceY > (48/2 + 10)):	return False

    if (circleDistanceX <= (48/2)):	return True
    if (circleDistanceY <= (48/2)):	return True

    cornerDistance_sq = (circleDistanceX - 48/2)**2 + (circleDistanceY - 48/2)**2

    return (cornerDistance_sq <= (10**2))



def initIntro(win):
	moveAndroid(playerIntro, winWidth / 2 - 24, winHeight / 2 - 24)
	moveAndroid(magentaIntro, winWidth + 10, winHeight / 2 - 24)

	cover.setFill("white")
	cover.setOutline("white")
	cover.draw(win)

	title = Text(Point(winWidth / 2, winHeight / 2 - 100), "Android Adventure")
	title.setSize(36)
	title.setFill("black")

	underTitleText = Text(Point(winWidth / 2, winHeight / 2 - 50), "By Edward Herbert")
	underTitleText.setSize(12)
	underTitleText.setFill("black")

	nameText = Text(Point(winWidth / 2, winHeight / 2 + 20), "Please enter your name:")
	nameText.setSize(20)
	nameText.setFill("black")

	nameInput = Entry(Point(winWidth / 2, winHeight / 2 + 80), 20)
	nameInput.setFill("#bcbcbc")

	nameConfirmBox = Rectangle(Point(winWidth / 2 - 50, winHeight / 2 + 140), Point(winWidth / 2 + 50, winHeight / 2 + 170))
	nameConfirmBox.setFill("red")

	nameConfirmBoxText = Text(Point(winWidth / 2, winHeight / 2 + 155), "Confirm")
	nameConfirmBoxText.setSize(16)
	nameConfirmBoxText.setFill("black")

	for i in [title, underTitleText, nameText, nameInput, nameConfirmBox, nameConfirmBoxText]:
		i.draw(win)
		introWindowGUI.append(i)

	#Gui bits for the second screen
	gloatText = Text(Point(winWidth / 2, 30 + 40), "")
	lineFirst = Text(Point(winWidth / 2, 30 + 130), "Move the android around with the arrow keys!")
	lineSecond = Text(Point(winWidth / 2, 80 + 130), "Press Z to interact with objects!")
	lineThird = Text(Point(winWidth / 2, 130 + 130), "Eat the red apples!")
	lineFourth = Text(Point(winWidth / 2, 180 + 130), "Don't eat the bad apples!")
	lineFifth = Text(Point(winWidth / 2, 230 + 130), "Eat all three red apples to win the game!")
	lineFifth.setStyle("bold")

	for i in [gloatText, lineFirst, lineSecond, lineThird, lineFourth, lineFifth]:
		i.setSize(20)
		introWindowGUI.append(i)

	gloatText.setSize(15)

	for i in range(3):
		apple = Circle(Point(random.random() * (winWidth - 20) + 10, random.random() * (winHeight - 20) + 10), 10)
		apple.setFill("red")
		redApples.append(apple)

	for i in range(10):
		apple = Circle(Point(random.random() * (winWidth - 20) + 10, random.random() * (winHeight - 20) + 10), 10)
		apple.setFill("black")
		badApples.append(apple)
