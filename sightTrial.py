from graphics import *
from gui import *
from map import *
from player import *
import math

sightTrialCount = 0

sightTrialShotsLeft = 5
sightTrialScore = 0
sightTrialMovingCount = 0
sightTrialTargetDirection = False
sightTrialTargetMoving = False
sightTrialTargetMoveRate = 4

sightTrialScoreCounter = Text(Point(80, 30), "")

targetSegments = []
targetShots = []

def sightTrialUpdate(win, trialId):
	global sightTrialCount

	global sightTrialTargetDirection
	global sightTrialMovingCount
	global sightTrialTargetMoveRate
	global sightTrialTargetMoving
	global sightTrialShotsLeft
	global sightTrialScore
	if(sightTrialTargetMoving):
		sightTrialMovingCount += 0.01
		for i in targetSegments:
			if(not sightTrialTargetDirection):
				i.move(sightTrialTargetMoveRate, 0)
			else:
				i.move(-sightTrialTargetMoveRate, 0)
		if(targetSegments[0].getP1().getX() <= 0 or targetSegments[0].getP2().getX() >= winWidth):	sightTrialTargetDirection = not sightTrialTargetDirection


	if(sightTrialCount == 0):
		if(isRolldownComplete()):	sightTrialCount += 1
	elif(sightTrialCount == 1):
		time.sleep(1)
		sightTrialCount += 1
	elif(sightTrialCount == 2):
		sightTrialCount = guiStory("Well then, let me explain my trial.", sightTrialCount)
	elif(sightTrialCount == 3):
		sightTrialCount = guiStory("When I say it's based around sight, I mean aim, like in archery.", sightTrialCount)
	elif(sightTrialCount == 4):
		for i in targetSegments:
			i.draw(win)
			time.sleep(0.5)
		sightTrialCount += 1
	elif(sightTrialCount == 5):
		sightTrialCount = guiStory("Use your mouse to aim at the different sections of the target.", sightTrialCount)
	elif(sightTrialCount == 6):
		sightTrialCount = guiStory("Try to hit the centre. Red is 10 points. Yellow is 5 points. Blue is 2. If it doesn't hit the target you get nothing!", sightTrialCount)
	elif(sightTrialCount == 7):
		sightTrialCount = guiStory("I'll give you 10 shots. If you can reach 1000 points with that then you pass!", sightTrialCount)
	elif(sightTrialCount == 8):
		sightTrialCount = guiStory("Capiche.", sightTrialCount)
	elif(sightTrialCount == 9):
		sightTrialCount = guiStory("Right off you go.", sightTrialCount)
		win.checkMouse()
	elif(sightTrialCount == 10):
		mouse = win.checkMouse()
		if(mouse != None):
			shootArrow(win, mouse.getX(), mouse.getY())
	elif(sightTrialCount == 11):
		sightTrialShotsLeft = 5
		sightTrialCount = guiStory("Ok. You seem to be getting the hang of it.", sightTrialCount)
	elif(sightTrialCount == 12):
		sightTrialCount = guiStory("Now let's see how you cope if I add wind resistance.", sightTrialCount)
	elif(sightTrialCount == 13):
		sightTrialCount = guiStory("*Eggplant stands to your side and starts blowing out of his mouth.*", sightTrialCount)
	elif(sightTrialCount == 14):
		mouse = win.checkMouse()
		if(mouse != None):
			shootArrow(win, mouse.getX() + (random.random() * 50) - 25, mouse.getY() + (random.random() * 50) - 25)
	elif(sightTrialCount == 15):
		sightTrialCount = guiStory("Well now that that's out of the way, let's try something different.", sightTrialCount)
	elif(sightTrialCount == 16):
		sightTrialTargetMoving = True
		for i in range(len(targetShots)):
			targetShots[0].undraw()
			targetShots.pop(0)
		sightTrialCount += 1
	elif(sightTrialCount == 17):
		sightTrialCount = guiStory("Let's see how you fare against this!", sightTrialCount)
		sightTrialShotsLeft = 5
		win.checkMouse()
	elif(sightTrialCount == 18):
		mouse = win.checkMouse()
		if(mouse != None):
			shootArrow(win, mouse.getX(), mouse.getY())
	elif(sightTrialCount == 19):
		resetShoot(8, win)
		sightTrialCount = guiStory("Faster!", sightTrialCount)
	elif(sightTrialCount == 20):
		mouse = win.checkMouse()
		if(mouse != None):
			shootArrow(win, mouse.getX(), mouse.getY())
	elif(sightTrialCount == 21):
		resetShoot(16, win)
		sightTrialCount = guiStory("FASTER!", sightTrialCount)
	elif(sightTrialCount == 22):
		mouse = win.checkMouse()
		if(mouse != None):
			shootArrow(win, mouse.getX(), mouse.getY())
	elif(sightTrialCount == 23):
		resetShoot(32, win)
		sightTrialCount = guiStory("FASTER!!!!!!!!!!!!!!", sightTrialCount)
	elif(sightTrialCount == 24):
		mouse = win.checkMouse()
		if(mouse != None):
			shootArrow(win, mouse.getX(), mouse.getY())
	elif(sightTrialCount == 25):
		sightTrialCount = guiStory("FAS ... Wait that's too fast.", sightTrialCount)
	elif(sightTrialCount == 26):
		sightTrialTargetMoveRate = 64
		sightTrialCount = guiStory("Stop!! Stop!!", sightTrialCount)
	elif(sightTrialCount == 27):
		sightTrialCount = guiStory("Right stand back please.", sightTrialCount)
	elif(sightTrialCount == 28):
		sightTrialCount = guiStory("*Eggplant starts blowing at the target in an attempt to slow it.*", sightTrialCount)
	elif(sightTrialCount == 29):
		sightTrialTargetMoveRate = 84
		sightTrialCount = guiStory("*Ironically, the target just gets faster.*", sightTrialCount)
	elif(sightTrialCount == 30):
		for i in range(len(targetShots)):
			targetShots[0].undraw()
			targetShots.pop(0)
		sightTrialCount += 1
	elif(sightTrialCount == 31):
		sightTrialCount = guiStory("We seem to be having some technical difficulties here.", sightTrialCount)
	elif(sightTrialCount == 32):
		sightTrialTargetMoveRate = 64
		sightTrialCount = guiStory("It's too bad because that's my only moving target.", sightTrialCount)
	elif(sightTrialCount == 33):
		sightTrialTargetMoveRate = 32
		sightTrialCount = guiStory("We'll probably have to postpone the trial.", sightTrialCount)
	elif(sightTrialCount == 34):
		sightTrialTargetMoveRate = 16
		sightTrialCount = guiStory("Wait is it getting slower?", sightTrialCount)
	elif(sightTrialCount == 35):
		sightTrialTargetMoveRate = 8
		sightTrialCount = guiStory("Excellent! in that case we can continue.", sightTrialCount)
	elif(sightTrialCount == 36):
		sightTrialTargetMoving = False
		if(targetSegments[0].getCenter().getX() < winWidth / 2):
			for i in targetSegments:
				i.move(1, 0)
		if(targetSegments[0].getCenter().getX() > winWidth / 2):
			for i in targetSegments:
				i.move(-1, 0)

		if(targetSegments[0].getCenter().getX() == winWidth / 2):	sightTrialCount += 1
	elif(sightTrialCount == 37):
		time.sleep(1)
		for i in range(len(targetSegments), 0, -1):
			targetSegments[i - 1].undraw()
			time.sleep(0.5)

		for i in range(len(targetSegments)):
			targetSegments.pop(0)
		time.sleep(1)
		sightTrialCount += 1
	elif(sightTrialCount == 38):
		sightTrialCount = guiStory("Oh.", sightTrialCount)
	elif(sightTrialCount == 39):
		sightTrialCount = guiStory("Apparently it broke.", sightTrialCount)
	elif(sightTrialCount == 40):
		sightTrialCount = guiStory("Well this isn't the optimum situation, not going to lie.", sightTrialCount)
	elif(sightTrialCount == 41):
		sightTrialCount = guiStory("It looks like you won't be able to complete the trial.", sightTrialCount)
	elif(sightTrialCount == 42):
		sightTrialCount = guiStory("So far you have " + str(sightTrialScore) + " points.", sightTrialCount)
	elif(sightTrialCount == 43):
		if(sightTrialScore <= 0):
			sightTrialCount = guiStory("You clearly aren't particularly gifted are you?", sightTrialCount)	
		elif(sightTrialScore > 0 and sightTrialScore <= 10):
			sightTrialCount = guiStory("Honestly I've seen better.", sightTrialCount)	
		elif(sightTrialScore > 10 and sightTrialScore <= 30):
			sightTrialCount = guiStory("That's a respectable figure.", sightTrialCount)
		elif(sightTrialScore > 30):
			sightTrialCount = guiStory("That's a decent figure.", sightTrialCount)	
	elif(sightTrialCount == 44):
		if(sightTrialScore <= 0):
			sightTrialCount = guiStory("That score is no where close to getting you through this trial.", sightTrialCount)	
		elif(sightTrialScore > 0 and sightTrialScore <= 10):
			sightTrialCount = guiStory("That score isn't going to get you through the trial.", sightTrialCount)	
		elif(sightTrialScore > 10 and sightTrialScore <= 30):
			sightTrialCount = guiStory("Even though the score is good, it's not enough to get you through the trial", sightTrialCount)
		elif(sightTrialScore > 30):
			sightTrialCount = guiStory("Even though your score is high, it's still not enough to get you through the trial.", sightTrialCount)	
	elif(sightTrialCount == 45):
		sightTrialCount = guiStory("I know you might be upset that you failed given that the trial broke, however there wasn't much left to the trial anyway.", sightTrialCount)
	elif(sightTrialCount == 46):
		sightTrialCount = guiStory("All that happens is the target does a sick loop-de-loop and then a back flip.", sightTrialCount)
	elif(sightTrialCount == 47):
		sightTrialCount = guiStory("You aren't even allowed to shoot at it, I just think it looks cool.", sightTrialCount)
	elif(sightTrialCount == 48):
		sightTrialCount = guiStory("You need 1000 points to pass the trial remember.", sightTrialCount)
	elif(sightTrialCount == 49):
		sightTrialCount = guiStory("Therefore, I, the great Eggplant rule that the 9999th attempt at the trial of sight is a fai....", sightTrialCount)
	elif(sightTrialCount == 50):
		sightTrialCount = guiStory("Wait a minute, the 9999th attempt?", sightTrialCount)
	elif(sightTrialCount == 51):
		sightTrialCount = guiStory("You know what that means folks!", sightTrialCount)
	elif(sightTrialCount == 52):
		sightTrialCount = guiStory("That means that " + getPlayerName() + " here is entitled to a fabulous prize!", sightTrialCount)
	elif(sightTrialCount == 53):
		sightTrialCount = guiStory("For being the 9999th challenger to the trial of sight, you win the fabulous prize of: " + str(1000 - sightTrialScore) + " points!", sightTrialCount)
	elif(sightTrialCount == 54):
		sightTrialCount = guiStory("Let's add your prize points on now!", sightTrialCount)
	elif(sightTrialCount == 55):
		sightTrialScore += 1000 - sightTrialScore
		sightTrialScoreCounter.setText("Score: " + str(sightTrialScore))
		sightTrialCount += 1
	elif(sightTrialCount == 56):
		sightTrialCount = guiStory("OhmyGosh. Those extra points have just put you up to the 1000 point threshold.", sightTrialCount)
	elif(sightTrialCount == 57):
		sightTrialCount = guiStory("In a dramatic turn of events it seems you have actually passed the trial!", sightTrialCount)
	elif(sightTrialCount == 58):
		sightTrialCount = guiStory("What a shocking conclusion.", sightTrialCount)
	elif(sightTrialCount == 59):
		sightTrialScoreCounter.undraw()
		time.sleep(1)
		return 0

	return trialId

def resetShoot(shoot, win):
		global sightTrialShotsLeft
		global sightTrialTargetMoveRate
		sightTrialShotsLeft = 5
		sightTrialTargetMoveRate = shoot
		win.checkMouse()

def shootArrow(win, x, y):
	global sightTrialShotsLeft
	global sightTrialScore
	sightTrialScoreCounter.setText("Score: " + str(sightTrialScore))
	mouse = Point(x, y)
	distance = distanceBetweenPoints(targetSegments[0].getCenter(), mouse)
	if(distance < 40):	sightTrialScore += 10
	elif(distance >= 40 and distance < 120):	sightTrialScore += 5
	elif(distance >= 120 and distance < 200):	sightTrialScore += 2

	sightTrialScoreCounter.setText("Score: " + str(sightTrialScore))
	shot = Circle(mouse, 5)
	shot.setFill("black")
	shot.draw(win)
	targetShots.append(shot)
	sightTrialShotsLeft -= 1
	if(sightTrialShotsLeft <= 0):
		global sightTrialCount
		sightTrialCount += 1

def distanceBetweenPoints(p1, p2):
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    return math.sqrt(((y2 - y1) ** 2) + ((x2 - x1) ** 2))

def sightTrialInit(win):
	blueSegment = Circle(Point(winWidth / 2, winHeight / 2), 200)
	blueSegment.setFill("blue")
	yellowSegment = Circle(Point(winWidth / 2, winHeight / 2), 120)
	yellowSegment.setFill("yellow")
	redSegment = Circle(Point(winWidth / 2, winHeight / 2), 40)
	redSegment.setFill("red")

	sightTrialScoreCounter.setSize(20)
	sightTrialScoreCounter.draw(win)

	for i in [blueSegment, yellowSegment, redSegment]:
		targetSegments.append(i)
