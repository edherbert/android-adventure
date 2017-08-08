from graphics import *
from map import *
from gui import *
import random

deductionTrialCount = 0

deductionTrialShape = []
deductionTrialAttemptsLeft = 10
deductionTrialCounter = Text(Point(120, 25), "Attempts left: " + str(deductionTrialAttemptsLeft))
deductionTrialIndicator = Text(Point(120, 50), " " + str(deductionTrialAttemptsLeft))
deductionTrialPreviousDistance = -1

def deductionTrialUpdate(win, currentTrial):
	global deductionTrialCount

	if(deductionTrialCount == 0):
		time.sleep(1)
		deductionTrialCount += 1
	elif(deductionTrialCount == 1):
		deductionTrialCount = guiStory("Let me explain my trial.", deductionTrialCount)
	elif(deductionTrialCount == 2):
		deductionTrialCount = guiStory("I have hidden a number of shapes around the screen. You must click on the screen at the place you think the shape is hidden.", deductionTrialCount)
	elif(deductionTrialCount == 3):
		deductionTrialCount = guiStory("Once you have clicked twice I will tell you if your previous click was closer or further away to the shape, based on a hot and cold system.", deductionTrialCount)
	elif(deductionTrialCount == 4):
		deductionTrialCount = guiStory("From this system you must deduce the location of the shape.", deductionTrialCount)
	elif(deductionTrialCount == 5):
		deductionTrialCount = guiStory("You will have ten attempts to find the shape. If you do not find it then you lose the trial.", deductionTrialCount)
	elif(deductionTrialCount == 6):
		deductionTrialCount = guiStory("Are you ready?", deductionTrialCount)
	elif(deductionTrialCount == 7):
		deductionTrialCount = guiStory("Then start searching when you're ready.", deductionTrialCount)
	elif(deductionTrialCount == 8):
		deductionTrialCount += 1
		deductionTrialAddCircle(100, win)

		deductionTrialCounter.draw(win)
		deductionTrialCounter.setSize(20)

		deductionTrialIndicator.draw(win)
		deductionTrialIndicator.setSize(20)
		deductionTrialIndicator.setText("")
		win.checkMouse()
	elif(deductionTrialCount == 9):
		searchForShape(win.checkMouse(), win)
	elif(deductionTrialCount == 10):
		deductionTrialCount = guiStory("Well done, you found the first shape.", deductionTrialCount)
	elif(deductionTrialCount == 11):
		deductionTrialCount = guiStory("Now try to find another circle, but this time, the radius of the circle will be smaller!", deductionTrialCount)
	elif(deductionTrialCount == 12):
		deductionTrialCount += 1
		resetShape()
		deductionTrialAddCircle(60, win)
		win.checkMouse()
	elif(deductionTrialCount == 13):
		searchForShape(win.checkMouse(), win)
	elif(deductionTrialCount == 14):
		deductionTrialCount = guiStory("Good work!", deductionTrialCount)
	elif(deductionTrialCount == 15):
		deductionTrialCount = guiStory("I'll make the circle smaller once again. If you can find this one, then your attempt at the trial of deduction will be a success.", deductionTrialCount)
	elif(deductionTrialCount == 16):
		deductionTrialCount += 1
		resetShape()
		deductionTrialAddRect(win, 100, 100)
		win.checkMouse()
	elif(deductionTrialCount == 17):
		searchForShape(win.checkMouse(), win)
	elif(deductionTrialCount == 18):
		deductionTrialCount = guiStory("Well Done! You've found all th... Wait, is that a square!?", deductionTrialCount)
	elif(deductionTrialCount == 19):
		deductionTrialCount = guiStory("That was supposed to be a circle!", deductionTrialCount)
	elif(deductionTrialCount == 20):
		deductionTrialCount = guiStory("Well, whatever, let's just pretend that didn't happen.", deductionTrialCount)
	elif(deductionTrialCount == 21):
		deductionTrialCount = guiStory("Have another go! Find a Circle.", deductionTrialCount)
	elif(deductionTrialCount == 22):
		deductionTrialCount += 1
		resetShape()
		deductionTrialAddRect(win, 150, 100)
		win.checkMouse()
	elif(deductionTrialCount == 23):
		searchForShape(win.checkMouse(), win)
	elif(deductionTrialCount == 24):
		deductionTrialCount = guiStory("Congratul..... WHY IS IT A RECTANGLE.", deductionTrialCount)
	elif(deductionTrialCount == 25):
		deductionTrialCount = guiStory("I SAID BE A CIRCLE!! I remember saying CIRCLE!!!", deductionTrialCount)
	elif(deductionTrialCount == 26):
		deductionTrialCount = guiStory("Oh! Apologies for shouting. I don't mean to be rude to our challengers.", deductionTrialCount)
	elif(deductionTrialCount == 27):
		deductionTrialCount = guiStory("Try to find a circle again.", deductionTrialCount)
	elif(deductionTrialCount == 28):
		deductionTrialCount += 1
		resetShape()
	elif(deductionTrialCount == 29):
		mouse = win.checkMouse()
		if(mouse != None):
			text = Text(mouse, "A Circle")
			text.setSize(20)
			text.draw(win)
			deductionTrialAddShape(text)
			deductionTrialCount += 1

	elif(deductionTrialCount == 30):
		time.sleep(2)
		deductionTrialCount += 1
	elif(deductionTrialCount == 31):
		deductionTrialCount = guiStory("What.", deductionTrialCount)
	elif(deductionTrialCount == 32):
		deductionTrialCount = guiStory("What.", deductionTrialCount)
	elif(deductionTrialCount == 33):
		deductionTrialCount = guiStory("WHAT!!!", deductionTrialCount)
	elif(deductionTrialCount == 34):
		deductionTrialCount = guiStory("IS THIS SOME SORT OF JOKE!!", deductionTrialCount)
	elif(deductionTrialCount == 35):
		deductionTrialCount = guiStory("*Charcoal keeps screaming. You begin to wonder if she has issues.*", deductionTrialCount)
	elif(deductionTrialCount == 36):
		deductionTrialCount = guiStory("Oh! I'm sorry for shouting, sometimes I let myself get a bit too heated.", deductionTrialCount)
	elif(deductionTrialCount == 37):
		deductionTrialCount = guiStory("Anyway, no matter! Have another look for the circle. I guarantee it will be there this time.", deductionTrialCount)
	elif(deductionTrialCount == 38):
		deductionTrialCount += 1
		resetShape()
		mouse = win.checkMouse()
	elif(deductionTrialCount == 39):
		mouse = win.checkMouse()
		if(mouse != None):
			deductionTrialAddParollelogram(win, mouse)
			deductionTrialCount += 1

	elif(deductionTrialCount == 40):
		time.sleep(1)
		deductionTrialCount += 1
	elif(deductionTrialCount == 41):
		deductionTrialCount = guiStory("Is that a Parallelogram?", deductionTrialCount)
	elif(deductionTrialCount == 42):
		deductionTrialCount = guiStory("A Parallelogram.", deductionTrialCount)
	elif(deductionTrialCount == 43):
		deductionTrialCount = guiStory("Not a circle.", deductionTrialCount)
	elif(deductionTrialCount == 44):
		deductionTrialCount = guiStory("A Parallelogram.", deductionTrialCount)
	elif(deductionTrialCount == 45):
		deductionTrialCount = guiStory("Ok.", deductionTrialCount)
	elif(deductionTrialCount == 46):
		deductionTrialCount = guiStory("That's the end of the trial, you pass.", deductionTrialCount)
	elif(deductionTrialCount == 47):
		resetShape()
		deductionTrialCounter.undraw()
		deductionTrialIndicator.undraw()
		removeRolldown()
		return 0

	return currentTrial

def deductionTrialAddParollelogram(win, point):
	x = point.getX()
	y = point.getY()
	point1 = Point(x - 50, y - 25)
	point2 = Point(x + 50, y - 25)
	point3 = Point(x + 50 - 40, y + 25)
	point4 = Point(x - 50 - 40, y + 25)

	shape = Polygon([point1, point2, point3, point4])
	shape.draw(win)
	deductionTrialAddShape(shape)

def deductionTrialAddRect(win, width, height):
	x = random.random() * (winWidth - width)
	y = random.random() * (winHeight - height)
	shape = Rectangle(Point(x, y), Point(x + width, y + height))
	deductionTrialAddShape(shape)	

def deductionTrialAddCircle(radius, win):
	shape = Circle(Point(random.random() * (winWidth - (radius * 2)) + radius, random.random() * (winHeight - (radius * 2)) + radius), radius)
	deductionTrialAddShape(shape)

def deductionTrialAddShape(shape):
	deductionTrialShape.append(shape)

def searchForShape(point, win):
	global deductionTrialCount
	global deductionTrialPreviousDistance
	if(point != None):
		useAttempt()
		distance = distanceBetweenPoints(point, deductionTrialShape[0].getCenter())
		if(deductionTrialShape[0] == Circle):
			if(distance <= deductionTrialShape[0].getRadius() or deductionTrialAttemptsLeft <= 0):
				deductionTrialShape[0].move(point.getX() - deductionTrialShape[0].getCenter().getX(), point.getY() - deductionTrialShape[0].getCenter().getY())
				deductionTrialShape[0].draw(win)
				deductionTrialCount += 1
		else:
			if((point.getX() >= deductionTrialShape[0].getP1().getX() and point.getY() >= deductionTrialShape[0].getP1().getY() and point.getX() <= deductionTrialShape[0].getP2().getX() and point.getY() <= deductionTrialShape[0].getP2().getY()) or deductionTrialAttemptsLeft <= 0):
				deductionTrialShape[0].move(point.getX() - deductionTrialShape[0].getCenter().getX(), point.getY() - deductionTrialShape[0].getCenter().getY())
				deductionTrialShape[0].draw(win)
				deductionTrialCount += 1
		#If it's -1 then this is the first click
		if(deductionTrialPreviousDistance >= 0):
			if(distance >= deductionTrialPreviousDistance):
				deductionTrialIndicator.setText("Colder")
			else:
				deductionTrialIndicator.setText("Warmer")

		deductionTrialPreviousDistance = distance

def distanceBetweenPoints(p1, p2):
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    return math.sqrt(((y2 - y1) ** 2) + ((x2 - x1) ** 2))

def useAttempt():
	global deductionTrialAttemptsLeft
	deductionTrialAttemptsLeft -= 1
	deductionTrialCounter.setText("Attempts left: " + str(deductionTrialAttemptsLeft))

def resetShape():
	global deductionTrialShape
	global deductionTrialPreviousDistance
	global deductionTrialAttemptsLeft

	deductionTrialShape[0].undraw()
	deductionTrialPreviousDistance = -1
	deductionTrialShape = []

	deductionTrialAttemptsLeft = 10
	deductionTrialCounter.setText("Attempts left: " + str(deductionTrialAttemptsLeft))
