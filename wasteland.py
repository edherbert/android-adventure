from graphics import *
from gui import *
from player import *
from map import *
from android import *

wastelandStoryCount = 0

wastelandSlate = createAndroid("#778899")

def wastelandUpdate(win, player):
	global wastelandStoryCount

	if(wastelandStoryCount == 0):
		if(getSegmentX() == 0 and getSegmentY() == 3):
			setCanPlayerMove(False)
			wastelandStoryCount += 1
	elif(wastelandStoryCount == 1):
		moveAndroid(wastelandSlate, 5 * 48, 7 * 48)
		changeAndroidDirection(wastelandSlate, 2)
		drawAndroid(win, wastelandSlate)
		wastelandStoryCount += 1
	elif(wastelandStoryCount == 2):
		#0 up, 1 left, 2 right, 3 down
		changeAndroidDirection(wastelandSlate, 1)
		time.sleep(1)
		wastelandStoryCount += 1
	elif(wastelandStoryCount == 3):
		wastelandStoryCount = guiStory("Hello again, " + getPlayerName() + ".", wastelandStoryCount)
	elif(wastelandStoryCount == 4):
		wastelandStoryCount = guiStory("It's me, Slate!", wastelandStoryCount)
	elif(wastelandStoryCount == 5):
		wastelandStoryCount = guiStory("Good to see you. You seem to be doing well with your trials.", wastelandStoryCount)
	elif(wastelandStoryCount == 6):
		wastelandStoryCount = guiStory("I just thought I would show you something cool about the wastelands.", wastelandStoryCount)
	elif(wastelandStoryCount == 7):
		wastelandStoryCount = guiStory("Here, watch this.", wastelandStoryCount)
	elif(wastelandStoryCount == 8):
		time.sleep(1)
		changeAndroidDirection(wastelandSlate, 2)
		time.sleep(1)
		wastelandStoryCount += 1
	elif(wastelandStoryCount == 9):
		if(wastelandSlate[0].getP2().getX() < 14 * 48):
			moveAndroid(wastelandSlate, 6, 0)
		else:
			wastelandStoryCount += 1
	elif(wastelandStoryCount == 10):
		time.sleep(1)
		changeAndroidDirection(wastelandSlate, 1)
		time.sleep(1)
		wastelandStoryCount += 1
	elif(wastelandStoryCount == 11):
		wastelandStoryCount = guiStory("See? When you step on ice patches you'll slide!", wastelandStoryCount)
	elif(wastelandStoryCount == 12):
		wastelandStoryCount = guiStory("It's pretty cool right?", wastelandStoryCount)
	elif(wastelandStoryCount == 13):
		changeAndroidDirection(wastelandSlate, 3)
		if(wastelandSlate[0].getP2().getY() < 9 * 48):
			moveAndroid(wastelandSlate, 0, 6)
		else:
			wastelandStoryCount += 1
	elif(wastelandStoryCount == 14):
		time.sleep(1)
		changeAndroidDirection(wastelandSlate, 1)
		time.sleep(1)
		wastelandStoryCount += 1
	elif(wastelandStoryCount == 15):
		wastelandStoryCount = guiStory("There's quite a bit of ice further into the wastelands, so watch out for that!", wastelandStoryCount)
	elif(wastelandStoryCount == 16):
		wastelandStoryCount = guiStory("You're nearly there pal. Soon you'll be free from this place.", wastelandStoryCount)
	elif(wastelandStoryCount == 17):
		wastelandStoryCount = guiStory("I bet you're excited.", wastelandStoryCount)
	elif(wastelandStoryCount == 18):
		wastelandStoryCount = guiStory("The final apple... But never forget, you still have a choice.", wastelandStoryCount)
	elif(wastelandStoryCount == 19):
		wastelandStoryCount = guiStory("You must always follow your head when making choices, as you are the one who has to live with them.", wastelandStoryCount)
	elif(wastelandStoryCount == 20):
		wastelandStoryCount = guiStory("Just remember that before the end. Only you can choose what is right, so choose well.", wastelandStoryCount)
	elif(wastelandStoryCount == 21):
		wastelandStoryCount = guiStory("We'll meet again. Before the end. I can tell by your name.", wastelandStoryCount)
	elif(wastelandStoryCount == 22):
		wastelandStoryCount = guiStory(getPlayerName() + "...", wastelandStoryCount)
	elif(wastelandStoryCount == 23):
		time.sleep(1)
		changeAndroidDirection(wastelandSlate, 2)
		time.sleep(1)
		wastelandStoryCount += 1
	elif(wastelandStoryCount == 24):
		if(wastelandSlate[0].getP2().getX() < 17 * 48):
			moveAndroid(wastelandSlate, 2, 0)
		else:
			time.sleep(1)
			wastelandStoryCount += 1
	elif(wastelandStoryCount == 25):
		wastelandStoryCount = guiStory("I'm sorry for what is to come.", wastelandStoryCount)
	elif(wastelandStoryCount == 26):
		if(wastelandSlate[0].getP2().getX() < 22 * 48):
			moveAndroid(wastelandSlate, 1, 0)
		else:
			wastelandStoryCount += 1
	elif(wastelandStoryCount == 27):
		setCanPlayerMove(True)
