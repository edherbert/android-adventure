from graphics import *
from map import *
from android import *
from gui import *
from player import *

forestStoryCount = 0

forestSlate = createAndroid("#778899")

def forestInit():
	red = createAndroid("red")
	setAndroidSpeech(red, "I love the forest! The air is so fresh!")
	addAndroid(red, 12 * 48, 4 * 48, 2, 0)

	orange = createAndroid("orange")
	setAndroidSpeech(orange, "You know, when my final apple ran away, I chased it as far as this lake. I wasn't incredibly fit at the time. But it's strange to think about it. If I had been able to chase it for longer maybe I wouldn't be stuck here.")
	addAndroid(orange, 14 * 48, 2 * 48, 1, 0)

	pink = createAndroid("pink")
	setAndroidSpeech(pink, "Are you going to take on the trial of sight? I'll be rooting for you <3")
	addAndroid(pink, 6 * 48, 4 * 48, 1, 3)

	brown = createAndroid("brown")
	setAndroidSpeech(brown, "This river is so picturesque, I could almost paint it, that is if I was artistically talented.")
	addAndroid(brown, 8 * 48, 7 * 48, 1, 3)

def forestUpdate(win, player):
	global forestStoryCount

	if(forestStoryCount == 0):
		if(getSegmentX() == 2 and getSegmentY() == 3 and isSightTrialDone()):
			forestStoryCount += 1
	elif(forestStoryCount == 1):
		setCanPlayerMove(False)
		drawAndroid(win, forestSlate)
		moveAndroid(forestSlate, 15 * 48, 8 * 48)
		forestStoryCount += 1
	elif(forestStoryCount == 2):
		time.sleep(1)
		changeAndroidDirection(forestSlate, 1)
		forestStoryCount += 1
		time.sleep(0.5)
	elif(forestStoryCount == 3):
		forestStoryCount = guiStory("Hey.", forestStoryCount)
	elif(forestStoryCount == 4):
		changeAndroidDirection(player, 2)
		if(forestSlate[0].getP1().getX() <= player[0].getP2().getX() + 5):
			forestStoryCount += 1
		else:
			moveAndroid(forestSlate, -2, 0)
	elif(forestStoryCount == 5):
		time.sleep(1)
		changeAndroidDirection(forestSlate, 0)
		time.sleep(1)
		changeAndroidDirection(forestSlate, 1)
		forestStoryCount += 1
	elif(forestStoryCount == 6):
		forestStoryCount = guiStory("I see you've just passed the trial of sight.", forestStoryCount)
	elif(forestStoryCount == 7):
		forestStoryCount = guiStory("That's impressive pal, good on you!", forestStoryCount)
	elif(forestStoryCount == 8):
		forestStoryCount = guiStory("I can only think of one other person who finished that trial.", forestStoryCount)
	elif(forestStoryCount == 9):
		forestStoryCount = guiStory("If you're doing the trials, then that means you must be looking for entry into the abyss.", forestStoryCount)
	elif(forestStoryCount == 10):
		forestStoryCount = guiStory("And why might you want that?", forestStoryCount)
	elif(forestStoryCount == 11):
		forestStoryCount = guiStory("An apple? Huh that's interesting.", forestStoryCount)
	elif(forestStoryCount == 12):
		forestStoryCount = guiStory("I see your hurry. Those things don't stick around for long.", forestStoryCount)
	elif(forestStoryCount == 13):
		forestStoryCount = guiStory("I suppose you'll be heading to the desert next. The trial of deduction is a good one.", forestStoryCount)
	elif(forestStoryCount == 14):
		forestStoryCount = guiStory("Use the sink holes to reach the trial site.", forestStoryCount)
	elif(forestStoryCount == 15):
		forestStoryCount = guiStory("Anyway, I'll let you get on.", forestStoryCount)
	elif(forestStoryCount == 16):
		time.sleep(0.5)
		changeAndroidDirection(forestSlate, 2)
		forestStoryCount += 1
	elif(forestStoryCount == 17):
		if(forestSlate[0].getP1().getX() <= 13 * 48):
			moveAndroid(forestSlate, 2, 0)
		else:
			forestStoryCount += 1
	elif(forestStoryCount == 18):
		time.sleep(1)
		changeAndroidDirection(forestSlate, 1)
		time.sleep(0.5)
		forestStoryCount += 1
	elif(forestStoryCount == 19):
		forestStoryCount = guiStory("By the way kid, what's your name?", forestStoryCount)
	elif(forestStoryCount == 20):
		forestStoryCount = guiStory(getPlayerName() + ", huh?", forestStoryCount)
	elif(forestStoryCount == 21):
		forestStoryCount = guiStory("Nice to meet you " + getPlayerName() +". I'm Slate.", forestStoryCount)
	elif(forestStoryCount == 22):
		forestStoryCount = guiStory("You've got a good name. You can tell a lot about a person from their name.", forestStoryCount)
	elif(forestStoryCount == 23):
		forestStoryCount = guiStory("Your name tells me that you're soon to meet with destiny.", forestStoryCount)
	elif(forestStoryCount == 24):
		forestStoryCount = guiStory("I wonder what form it will take?", forestStoryCount)
	elif(forestStoryCount == 25):
		forestStoryCount = guiStory("Anyway. See you later. I'll be sure to keep an eye on you.", forestStoryCount)
	elif(forestStoryCount == 26):
		changeAndroidDirection(forestSlate, 0)
		if(forestSlate[0].getP1().getY() > 3 * 48):
			moveAndroid(forestSlate, 0, -2)
		else:
			forestStoryCount += 1
	elif(forestStoryCount == 27):
		changeAndroidDirection(forestSlate, 1)
		if(forestSlate[0].getP1().getX() > 11 * 48):
			moveAndroid(forestSlate, -2, 0)
		else:
			forestStoryCount += 1
	elif(forestStoryCount == 28):
		changeAndroidDirection(forestSlate, 0)
		if(forestSlate[0].getP1().getY() > -50):
			moveAndroid(forestSlate, 0, -2)
		else:
			forestStoryCount += 1
	elif(forestStoryCount == 29):
		changeAndroidDirection(player, 3)
		setCanPlayerMove(True)
		forestStoryCount += 1
