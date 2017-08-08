from graphics import *
from player import *
from map import *
from android import *

trialSiteStoryCount = 0
#0 up, 1 left, 2 right, 3 down

def trialSiteUpdate(win, player, currentTrialId):
	global trialSiteStoryCount
	if(trialSiteStoryCount == 0):
		setCanPlayerMove(False)
		trialSiteStoryCount += 1
	elif(trialSiteStoryCount == 1):
		trialSiteStoryCount = guiStory("dum dee dum.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 2):
		trialSiteStoryCount = guiStory("What a lovely day it is to be old and decrepit.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 3):
		changeAndroidDirection(getAndroidById(0), 1)
		trialSiteStoryCount = guiStory("Oh? Is that somebody at the door?", trialSiteStoryCount)
	elif(trialSiteStoryCount == 4):
		if(getAndroidById(0)[0].getP2().getY() >= player[0].getP1().getY()):
			trialSiteStoryCount += 1
		else:
			changeAndroidDirection(getAndroidById(0), 3)
			moveAndroid(getAndroidById(0), 0, 12)
	elif(trialSiteStoryCount == 5):
		trialSiteStoryCount = guiStory("THUD!!!", trialSiteStoryCount)
	elif(trialSiteStoryCount == 6):
		time.sleep(1)
		trialSiteStoryCount += 1
	elif(trialSiteStoryCount == 7):
		trialSiteStoryCount = guiStory("Oh! Did I run into something?", trialSiteStoryCount)
	elif(trialSiteStoryCount == 8):
		trialSiteStoryCount = guiStory("Is that another person? Let me get a good look at you.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 9):
		trialSiteStoryCount = guiStory("*The older looking android leans in to try to look at you.*", trialSiteStoryCount)
	elif(trialSiteStoryCount == 10):
		trialSiteStoryCount = guiStory("*If he is the trial master of the trial of sight, then that is quite ironic, as apparently he is rather blind.*", trialSiteStoryCount)
	elif(trialSiteStoryCount == 11):
		trialSiteStoryCount = guiStory("Hmmmmmm. You must be a trial goer. Come in, come in.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 12):
		trialSiteStoryCount = guiStory("Welcome to the trial of sight, a daunting challenge that will trial your ability to see, or something along those lines.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 13):
		trialSiteStoryCount = guiStory("My name is Eggplant.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 14):
		trialSiteStoryCount = guiStory("Most likely because I am the colour of an egg plant.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 15):
		trialSiteStoryCount = guiStory("Are you ready to take on my trial? Yes? Excellent!", trialSiteStoryCount)
	elif(trialSiteStoryCount == 16):
		trialSiteStoryCount = guiStory("Then, let us begin!", trialSiteStoryCount)
	elif(trialSiteStoryCount == 17):
		rolldown(win)
		trialSiteStoryCount += 1
		return 2
	elif(trialSiteStoryCount == 18):
		time.sleep(1)
		removeRolldown()
		trialSiteStoryCount += 1
	elif(trialSiteStoryCount == 19):
		time.sleep(1)
		trialSiteStoryCount += 1
	elif(trialSiteStoryCount == 20):
		trialSiteStoryCount = guiStory("You have done well, young one.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 21):
		trialSiteStoryCount = guiStory("Not many people have passed my trail.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 22):
		trialSiteStoryCount = guiStory("You might just have a chance.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 23):
		trialSiteStoryCount = guiStory("Well, good luck with the rest of your trials.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 24):
		changeAndroidDirection(getAndroidById(0), 0)
		if(getAndroidById(0)[0].getP1().getY() > 4 * 48):
			moveAndroid(getAndroidById(0), 0, -4)
		else:	trialSiteStoryCount += 1
	elif(trialSiteStoryCount == 25):
		changeAndroidDirection(getAndroidById(0), 3)
		setSightTrialDone(True)
		setCanPlayerMove(True)
		trialSiteStoryCount += 1
	#Trial of deduction
	elif(trialSiteStoryCount == 26):
		if(getSegmentX() == 1 and getSegmentY() == 0):	trialSiteStoryCount += 1
	elif(trialSiteStoryCount == 27):
		time.sleep(2)
		changeAndroidDirection(getAndroidById(1), 3)
		trialSiteStoryCount += 1
	elif(trialSiteStoryCount == 28):
		setCanPlayerMove(False)
		trialSiteStoryCount = guiStory("Welcome challenger. Welcome to the trial of deduction.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 29):
		trialSiteStoryCount = guiStory("This trial is designed to test your metal capabilities, your ability to deduce fact from information.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 30):
		trialSiteStoryCount = guiStory("My name is Charcoal and I have been trial master for a number of years.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 31):
		trialSiteStoryCount = guiStory("I see you made it past my desert maze. Congratulations.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 32):
		trialSiteStoryCount = guiStory("That experience should prepare you well for what is to come.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 33):
		trialSiteStoryCount = guiStory("Now, let us begin the trial of deduction!", trialSiteStoryCount)
	elif(trialSiteStoryCount == 34):
		rolldown(win)
		trialSiteStoryCount += 1
	elif(trialSiteStoryCount == 35):
		if(isRolldownComplete()):
			time.sleep(1)
			trialSiteStoryCount += 1
			return 3
	elif(trialSiteStoryCount == 36):
		time.sleep(1)
		trialSiteStoryCount += 1
	elif(trialSiteStoryCount == 37):
		trialSiteStoryCount = guiStory("CONGRATULATIONS!", trialSiteStoryCount)
	elif(trialSiteStoryCount == 38):
		trialSiteStoryCount = guiStory(getPlayerName().upper() + ".", trialSiteStoryCount)
	elif(trialSiteStoryCount == 39):
		trialSiteStoryCount = guiStory("WELL DONE.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 40):
		trialSiteStoryCount = guiStory("YOU CAN LEAVE NOW.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 41):
		time.sleep(1)
		changeAndroidDirection(getAndroidById(1), 0)
		trialSiteStoryCount += 1
	elif(trialSiteStoryCount == 42):
		trialSiteStoryCount = guiStory("*Charcoal turns away from you and starts shouting again.*", trialSiteStoryCount)
	elif(trialSiteStoryCount == 43):
		trialSiteStoryCount = guiStory("*You should probably leave now.*", trialSiteStoryCount)
	elif(trialSiteStoryCount == 44):
		trialSiteStoryCount += 1
		setCanPlayerMove(True)
		setDeductionTrialDone(True)

	#Strength trial
	elif(trialSiteStoryCount == 45):
		if(getSegmentX() == 0 and getSegmentY() == 1):	trialSiteStoryCount += 1
	elif(trialSiteStoryCount == 46):
		setCanPlayerMove(False)
		time.sleep(1)
		changeAndroidDirection(getAndroidById(2), 3)
		trialSiteStoryCount += 1
	elif(trialSiteStoryCount == 47):
		trialSiteStoryCount = guiStory("Welcome challenger. My name is Sage.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 48):
		trialSiteStoryCount = guiStory("You know, I don't get many visitors out here. Not many make it as far as you have.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 49):
		trialSiteStoryCount = guiStory("Not many have the strength.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 50):
		trialSiteStoryCount = guiStory("Furthermore, not many can withstand the cold.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 51):
		trialSiteStoryCount = guiStory("They also lack strength.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 52):
		trialSiteStoryCount = guiStory("Do you understand?", trialSiteStoryCount)
	elif(trialSiteStoryCount == 53):
		trialSiteStoryCount = guiStory("The fact that you've even made it this far shows strength.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 54):
		trialSiteStoryCount = guiStory("However, that is not enough.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 55):
		trialSiteStoryCount = guiStory("You will need more than strength to complete this trial. You will need grit and determination.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 56):
		trialSiteStoryCount = guiStory("Do you have those?", trialSiteStoryCount)
	elif(trialSiteStoryCount == 57):
		trialSiteStoryCount = guiStory("After all, what is strength without the will to utilise it?", trialSiteStoryCount)
	elif(trialSiteStoryCount == 58):
		trialSiteStoryCount = guiStory("And what is determination without the strength to fulfil it?", trialSiteStoryCount)
	elif(trialSiteStoryCount == 59):
		trialSiteStoryCount = guiStory("That is the purpose of this trial.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 60):
		trialSiteStoryCount = guiStory("Not to provide you with strength, but to give you the means to acquire it.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 61):
		changeAndroidDirection(getAndroidById(2), 1)
		time.sleep(2)
		trialSiteStoryCount += 1
	elif(trialSiteStoryCount == 62):
		trialSiteStoryCount = guiStory("Perhaps you are wondering why there is a tree in here.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 63):
		trialSiteStoryCount = guiStory("Did you know that this is the only tree in the entire wastelands.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 64):
		trialSiteStoryCount = guiStory("I have always felt more comfortable around nature.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 65):
		trialSiteStoryCount = guiStory("But I also like the wastelands. They are my home.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 66):
		trialSiteStoryCount = guiStory("You might also be wondering why I'm telling you all this, given that you are here for the trial, not for talk.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 67):
		changeAndroidDirection(getAndroidById(2), 3)
		trialSiteStoryCount += 1
	elif(trialSiteStoryCount == 68):
		trialSiteStoryCount = guiStory("Well there is nothing stronger than the will of nature. Let me show you. Come! Let us start the trial!", trialSiteStoryCount)
	elif(trialSiteStoryCount == 69):
		rolldown(win)
		trialSiteStoryCount += 1
	elif(trialSiteStoryCount == 70):
		if(isRolldownComplete()):
			time.sleep(1)
			trialSiteStoryCount += 1
			return 4

	elif(trialSiteStoryCount == 71):
		trialSiteStoryCount = guiStory("Good work!", trialSiteStoryCount)
	elif(trialSiteStoryCount == 72):
		trialSiteStoryCount = guiStory("I must say, not many people finish all three trials. You have excelled yourself.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 73):
		trialSiteStoryCount = guiStory("So have you learned any lessons from this experience?", trialSiteStoryCount)
	elif(trialSiteStoryCount == 74):
		trialSiteStoryCount = guiStory("Remember that while your journey is nearing it's end, there are still things to learn.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 75):
		trialSiteStoryCount = guiStory("I assume you will be heading for the abyss next. Please be careful.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 76):
		changeAndroidDirection(getAndroidById(2), 1)
		trialSiteStoryCount = guiStory("Once again I must apologise for that tree attacking.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 77):
		changeAndroidDirection(getAndroidById(2), 3)
		trialSiteStoryCount = guiStory("Now, I'll let you get on.", trialSiteStoryCount)
	elif(trialSiteStoryCount == 78):
		setCanPlayerMove(True)
		setStrengthTrialDone(True)
		trialSiteStoryCount += 1

	return currentTrialId

def trialSiteInit():
	trialSiteEggPlant = createAndroid("#614051")
	changeAndroidDirection(trialSiteEggPlant, 0)
	setAndroidSpeech(trialSiteEggPlant, "Well done completing the trial of sight, young'un.")
	addAndroid(trialSiteEggPlant, 10 * 48, 4 * 48, 0, 0)

	trialSiteCharcoal = createAndroid("#36454f")
	changeAndroidDirection(trialSiteCharcoal, 0)
	setAndroidSpeech(trialSiteCharcoal, "I said it should be a CIRCLE!")
	addAndroid(trialSiteCharcoal, 10 * 48, 4 * 48, 1, 0)

	trialSiteCharcoal = createAndroid("#9C9F84")
	changeAndroidDirection(trialSiteCharcoal, 1)
	setAndroidSpeech(trialSiteCharcoal, "Congratulations.")
	addAndroid(trialSiteCharcoal, 10 * 48, 5 * 48, 0, 1)
