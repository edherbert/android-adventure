from graphics import *
from map import *
from android import *
from player import *
from gui import *

androidVillageStoryCount = 0

androidVillageMagenta = createAndroid("#D80073")
androidVillageAzure = createAndroid("#007fff")

def androidVillageInit():
	red = createAndroid("red")
	setAndroidSpeech(red, "Hi! I'm Red. Also my name is Red. Did you know you can press the left shift to toggle running?")
	addAndroid(red, 11 * 48, 7 * 48, 1, 1)

	orange = createAndroid("orange")
	setAndroidSpeech(orange, "Did your apple run away as well? Don't worry about it pal. Two of mine ran away. It's not that bad here once you get used to it.")
	addAndroid(orange, 8 * 48, 9 * 48, 0, 1)

	blue = createAndroid("blue")
	setAndroidSpeech(blue, "The desert is too hot for me. I'd prefer it if it was colder, but the icy place to the east is far too cold. What a conundrum.")
	addAndroid(blue, 8 * 48, 8 * 48, 0, 2)

	purple = createAndroid("purple")
	setAndroidSpeech(purple, "I like this tree. There are lots more trees down in the south.")
	addAndroid(purple, 13 * 48, 5 * 48, 1, 2)

	brown = createAndroid("brown")
	setAndroidSpeech(brown, "Hey! That shade of green looks good on you!")
	addAndroid(brown, 16 * 48, 3 * 48, 2, 2)

	#Non default yellow because the default looked a bit weird
	yellow = createAndroid("#ccc543")
	setAndroidSpeech(yellow, "Isn't the water pretty.")
	addAndroid(yellow, 8 * 48, 2 * 48, 2, 1)

	setAndroidSpeech(androidVillageAzure, "I'm Azure. I'm the guard for the abyss.")
	addAndroid(androidVillageAzure, 16 * 48, 6 * 48, 1, 0)

def resetMagenta():
	global androidVillageMagenta
	androidVillageMagenta = createAndroid("#D80073")

def androidVillageUpdate(win, player, currentTrial):
	global androidVillageStoryCount

	if(androidVillageStoryCount == 0):
		setCanPlayerMove(False)
		drawAndroids(win)
		androidVillageStoryCount+=1
	elif(androidVillageStoryCount == 1):
		changeAndroidDirection(player, 1)
		moveAndroid(androidVillageMagenta, 48 * 14, 48 * 8)
		changeAndroidDirection(androidVillageMagenta, 1)
		drawAndroid(win, androidVillageMagenta)
		androidVillageStoryCount += 1
	elif(androidVillageStoryCount == 2):
		if(androidVillageMagenta[0].getP1().getX() > 11 * 48):
			moveAndroid(androidVillageMagenta, -1, 0)
		else:
			time.sleep(1)
			changeAndroidDirection(androidVillageMagenta, 3)
			time.sleep(0.5)
			changeAndroidDirection(androidVillageMagenta, 2)
			time.sleep(0.5)
			androidVillageStoryCount += 1
		if(player[0].getP1().getX() > 13 * 48):
			moveAndroid(player, -1, 0)

	elif(androidVillageStoryCount == 3):
		androidVillageStoryCount = guiStory("Well, here we are! Welcome to Android Village!", androidVillageStoryCount)
	elif(androidVillageStoryCount == 4):
		androidVillageStoryCount = guiStory("We've done our best to carve out a living in this world.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 5):
		androidVillageStoryCount = guiStory("I suppose you're wondering when this game became an RPG.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 6):
		androidVillageStoryCount = guiStory("Well to be honest this place isn't even supposed to exist.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 7):
		androidVillageStoryCount = guiStory("As I said, the apples aren't supposed to run away.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 8):
		androidVillageStoryCount = guiStory("The best thing you can do is to try to find that final apple, so you don't end up trapped here.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 9):
		androidVillageStoryCount = guiStory("Everyone who lives here also had their final apple run away, and are now stuck in this game for the rest of eternity.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 10):
		androidVillageStoryCount = guiStory("Everyone is very friendly, so feel free to talk to them!", androidVillageStoryCount)
	elif(androidVillageStoryCount == 11):
		androidVillageStoryCount = guiStory("Now, as I've already said you'll be able to find that apple in the eternal abyss, the place to the north.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 12):
		androidVillageStoryCount = guiStory("However, before you can go into the abyss, you'll need to complete the three trials.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 13):
		androidVillageStoryCount = guiStory("The abyss is quite a dangerous place you see, so because of that we only let those who are worthy into it.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 14):
		androidVillageStoryCount = guiStory("The trials shouldn't be too difficult for you though!", androidVillageStoryCount)
	elif(androidVillageStoryCount == 15):
		androidVillageStoryCount = guiStory("There are three in total.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 16):
		changeAndroidDirection(androidVillageMagenta, 1)
		androidVillageStoryCount = guiStory("The Trial of Deduction in the west.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 17):
		changeAndroidDirection(androidVillageMagenta, 3)
		androidVillageStoryCount = guiStory("The Trial of Sight in the south.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 18):
		changeAndroidDirection(androidVillageMagenta, 2)
		androidVillageStoryCount = guiStory("Finally, the Trial of Strength in the east.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 19):
		androidVillageStoryCount = guiStory("I would recommend you start with the trial of sight in the south.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 20):
		androidVillageStoryCount = guiStory("Once you have completed all three trials, head to the north and you'll be granted entry into the abyss.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 21):
		androidVillageStoryCount = guiStory("I'll let you get on then!", androidVillageStoryCount)
	elif(androidVillageStoryCount == 22):
		androidVillageStoryCount = guiStory("Good luck, see you soon!", androidVillageStoryCount)
	elif(androidVillageStoryCount == 23):
		if(androidVillageMagenta[0].getP2().getX() <= 0):
			undrawAndroid(androidVillageMagenta)
			changeAndroidDirection(player, 3)
			androidVillageStoryCount+=1
		else:
			changeAndroidDirection(androidVillageMagenta, 1)
			moveAndroid(androidVillageMagenta, -3, 0)
	elif(androidVillageStoryCount == 24):
		time.sleep(1)
		setCanPlayerMove(True)
		androidVillageStoryCount+=1
	elif(androidVillageStoryCount == 25):
		if(getSegmentY() == 0):
			if(player[0].getP1().getY() < 6 * 48):
				if(not isStrengthTrialDone()):
					changeAndroidDirection(androidVillageAzure, 1)
					setCanPlayerMove(False)
					androidVillageStoryCount = guiStory("Hey! You need to complete all three trials before you can go in there!", androidVillageStoryCount)
				else:
					androidVillageStoryCount += 2
	elif(androidVillageStoryCount == 26):
		changeAndroidDirection(player, 3)
		if(player[0].getP1().getY() < 8 * 48):
			moveAndroid(player, 0, 2)
		else:
			setCanPlayerMove(True)
			changeAndroidDirection(androidVillageAzure, 3)
			androidVillageStoryCount -= 1
	elif(androidVillageStoryCount == 27):
		setCanPlayerMove(False)
		resetMagenta()
		moveAndroid(androidVillageMagenta, player[0].getCenter().getX() - 24, winHeight + 48)
		changeAndroidDirection(androidVillageMagenta, 0)
		drawAndroid(win, androidVillageMagenta)
		time.sleep(1)
		androidVillageStoryCount += 1
	elif(androidVillageStoryCount == 28):
		androidVillageStoryCount = guiStory("Hey! " + getPlayerName() + "!", androidVillageStoryCount)
	elif(androidVillageStoryCount == 29):
		changeAndroidDirection(player, 3)
		if(androidVillageMagenta[0].getP1().getY() > 7 * 48):
			moveAndroid(androidVillageMagenta, 0, -2)
		else:
			androidVillageStoryCount += 1
	elif(androidVillageStoryCount == 30):
		androidVillageStoryCount = guiStory("You did it! I'm proud of you.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 31):
		androidVillageStoryCount = guiStory("You took control of a bad situation. You have my respect.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 32):
		androidVillageStoryCount = guiStory("Now there is only one thing left to do.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 33):
		androidVillageStoryCount = guiStory("Are you nervous? I am.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 34):
		androidVillageStoryCount = guiStory("You'll finally meet that apple, the one that started all of this.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 35):
		changeAndroidDirection(player, 0)
		if(player[0].getP1().getY() > 4 * 48):
			moveAndroid(player, 0, -2)
		if(androidVillageMagenta[0].getP1().getY() > 5 * 48):
			moveAndroid(androidVillageMagenta, 0, -2)
		else:
			androidVillageStoryCount += 1
	elif(androidVillageStoryCount == 36):
		androidVillageStoryCount = guiStory("So, are you ready.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 37):
		time.sleep(1)
		changeAndroidDirection(player, 3)
		time.sleep(1)
		changeAndroidDirection(player, 2)
		time.sleep(1)
		androidVillageStoryCount += 1
	elif(androidVillageStoryCount == 38):
		androidVillageStoryCount = guiStory("What? Are you scared?", androidVillageStoryCount)
	elif(androidVillageStoryCount == 39):
		androidVillageStoryCount = guiStory("What is there to be scared of? You're about to be free.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 40):
		androidVillageStoryCount = guiStory("The real thing to be afraid of is being stuck here for the rest of time. Believe me.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 41):
		androidVillageStoryCount = guiStory("That's the way it is.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 42):
		time.sleep(1)
		changeAndroidDirection(player, 1)
		time.sleep(1)
		androidVillageStoryCount += 1
	elif(androidVillageStoryCount == 43):	
		if(androidVillageMagenta[0].getP1().getY() > player[0].getP2().getY() - 10):
			moveAndroid(androidVillageMagenta, 0, -1)
		else:	androidVillageStoryCount += 1
	elif(androidVillageStoryCount == 44):
		changeAndroidDirection(player, 3)
		androidVillageStoryCount = guiStory("Listen to me. You need to go in there and find that apple. Understand?", androidVillageStoryCount)
	elif(androidVillageStoryCount == 45):
		time.sleep(1)
		changeAndroidDirection(player, 1)
		time.sleep(1)
		androidVillageStoryCount += 1
	elif(androidVillageStoryCount == 46):
		androidVillageStoryCount = guiStory(getPlayerName() + " just stop and think about this.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 47):
		androidVillageStoryCount = guiStory("If that apple had just stayed where it was and let you eat it then this never would have happened.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 48):
		changeAndroidDirection(player, 3)
		androidVillageStoryCount = guiStory("It put it's life ahead of yours. Every apple has a limited lifespan, whereas androids do not.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 49):
		androidVillageStoryCount = guiStory("My apple died long ago, now I am forced to linger here.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 50):
		androidVillageStoryCount = guiStory("If you do not eat it, time will eat away at you too.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 51):
		androidVillageStoryCount = guiStory("Understand? Please take my advice. I want what's best for you.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 52):
		time.sleep(1)
		changeAndroidDirection(player, 2)
		time.sleep(1)
		androidVillageStoryCount += 1
	elif(androidVillageStoryCount == 53):
		if(androidVillageMagenta[0].getP1().getY() > player[0].getP2().getY() - 20):
			moveAndroid(androidVillageMagenta, 0, -1)
		else:	androidVillageStoryCount += 1
	elif(androidVillageStoryCount == 54):
		changeAndroidDirection(player, 3)
		androidVillageStoryCount = guiStory(getPlayerName().upper() + "!", androidVillageStoryCount)
	elif(androidVillageStoryCount == 55):
		androidVillageStoryCount = guiStory("It's us or them.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 56):
		androidVillageStoryCount = guiStory("Now get in.", androidVillageStoryCount)
	elif(androidVillageStoryCount == 57):
		changeAndroidDirection(player, 0)
		if(player[0].getP1().getY() > 3 * 48 - 24):
			moveAndroid(player, 0, -2)
			moveAndroid(androidVillageMagenta, 0, -2)
		else:
			androidVillageStoryCount += 1
	elif(androidVillageStoryCount == 58):
		changeAndroidDirection(player, 2)
		time.sleep(0.2)
		changeAndroidDirection(player, 1)
		time.sleep(0.2)
		changeAndroidDirection(player, 3)
		androidVillageStoryCount += 1
		time.sleep(0.5)
	elif(androidVillageStoryCount == 59):
		undrawAndroid(player)
		androidVillageStoryCount += 1
	elif(androidVillageStoryCount == 60):
		time.sleep(1)
		undrawAndroid(androidVillageMagenta)
		return 5

	return currentTrial
