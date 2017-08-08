from graphics import *
from map import *
from android import *
from fightScene import *

magentaFightCount = 0

#Basically the fight with Magenta. I named it ending to avoid spoilers

#Used to determine if magenta has said anything this turn
FightSpoken = False
speechCount = 0

#Whether to do the magenta shaking animation.
magentaShaking = False
#A count to animate the shake
magentaShakeCount = 0
#The shake direction
magentaShakeDirection = True
#The speed at which magenta shakes
magentaShakeSpeed = 1

#An array to allow animation of the smaller eyes that magenta has when you beat him.
smallerEyes = []

magentaSpeech = [
"Stop struggling! This doesn't have to take long.",
"Do you really think you can beat me! I'm Magenta!",
"You know you're only here because I needed you to be.",
"Did you really think the trials would be that easy?",
"The trial masters might have said, but I was the only person to ever beat them.",
"So I knew the best way to get you through them.",
"Did you like that Parallelogram I slipped into the deduction trial?",
"Obviously without me you would have lost the sight trial as well.",
"Eggplant is blind, all I had to do was write 9999 on his trial form.",
"That living tree was the hardest thing to do.",
"In the end I just stood behind it and moved it around.",
"It was fun getting to fling Sage across the room though.",
"That fool always talks about strength like he knows what pain is.",
"I've been here the longest!",
"I know what solitude feels like. I know what sheer time feels like!",
"You could NEVER understand what I've been through.",
"I can't even remember what my name was back in the real world.",
"How do you forget your own name?",
"We've all been here for so long. Our colours are the only thing that we can remember.",
"I need to be free of Magenta! I need to be free from this broken world!",
"Sorry kid, but I would rather eat you than spend another minute here!",
"Everything that has happened to you since the start of this game has been planned by me.",
"All I had to do was wait for some idiot to have an apple run away on them.",
"I would just slide in and give them the sweet talk.",
"\"I want to help you!\" Don't make me laugh.",
"I can't believe you bought that.",
"But then again, it's not like you had anyone else who was willing to help.",
"You were doomed from the start!",
"And that idiot that's been following you around, Slate.",
"What? Did you not think that I knew about that.",
"I was forced to keep an eye on her.",
"She could have blown this entire thing if she told you my plan.",
"I'm not entirely sure why she didn't tell you though.",
"I'm sure she could tell what I was planning as well.",
"She's always been able to tell!",
"But no matter! I won't have to worry about her soon.",
"I won't have to worry about her or anyone else!",
"This is the end " + getPlayerName() + ".",
"You never stood a chance.",
"So just give up and let me win!",
"...",
"Why are you still fighting!?",
"YOU CAN'T BEAT ME!!!",
"I know everything of this world. I know every inch!",
"Did you not think that I planned for you to fight back?",
"I've been waiting for an eternity for this opportunity!",
"I planned this. I planned for you to fight back!",
"But you know, I didn't plan for you to win!",
"Now stand still!",
"And let me end you!",
]

def initMagentaFight(win):
	pass

def makeMagentaShake():
	global magentaShaking
	magentaShaking = True

def magentaFightUpdate(win, key, currentTrial):
	global magentaFightCount

	if(magentaShaking):
		global magentaShakeDirection
		global magentaShakeCount
		magentaShakeCount += 1
		if(magentaShakeCount % 3 == 0):	magentaShakeDirection = not magentaShakeDirection

		if(magentaShakeDirection):
			for i in getOpponentData():
				i.move(-magentaShakeSpeed, 0)
			for i in smallerEyes:
				i.move(-magentaShakeSpeed, 0)
		else:
			for i in getOpponentData():
				i.move(magentaShakeSpeed, 0)
			for i in smallerEyes:
				i.move(magentaShakeSpeed, 0)

	if(magentaFightCount == 0):
		fightMagenta = createAndroidWithScale("#D80073", 2)
		moveAndroid(fightMagenta, winWidth / 2 - 48, winHeight / 2 - 48)
		startFight(win, fightMagenta[0:12], "Magenta", 600)
		redrawPlayerHealth(win)
		magentaFightCount += 1
	elif(magentaFightCount == 1):
		if(getOpponentHealth() <= 0):
			magentaFightCount +=1
		updateMagentaSpeech()
	elif(magentaFightCount == 2):
		#make magenta's eyes smaller for atmosphere and things
		leftEyeOld = getOpponentData()[9]
		rightEyeOld = getOpponentData()[10]
		leftEye = Circle(leftEyeOld.getCenter(), 3)
		rightEye = Circle(rightEyeOld.getCenter(), 3)
		for i in [leftEye, rightEye]:
			i.setFill("white")
			i.setOutline("white")
			i.draw(win)
			smallerEyes.append(i)
		getOpponentData()[9].undraw()
		getOpponentData()[10].undraw()
		magentaFightCount += 1
	elif(magentaFightCount == 3):
		magentaFightCount = guiStory("Wait...", magentaFightCount)
	elif(magentaFightCount == 4):
		magentaFightCount = guiStory("Th... This...", magentaFightCount)
	elif(magentaFightCount == 5):
		magentaFightCount = guiStory("Can't be right...", magentaFightCount)
	elif(magentaFightCount == 6):
		magentaFightCount = guiStory("What did you do? What have you done?", magentaFightCount)
	elif(magentaFightCount == 7):
		magentaFightCount = guiStory(getPlayerName() + "... STOP IT.", magentaFightCount)
	elif(magentaFightCount == 8):
		magentaFightCount = guiStory("You.. You can't beat me. I CAN'T DIE LIKE THIS!!", magentaFightCount)
	elif(magentaFightCount == 9):
		makeMagentaShake()
		magentaFightCount += 1
	elif(magentaFightCount == 10):
		magentaFightCount = guiStory(getPlayerName().upper() + "!", magentaFightCount)
	elif(magentaFightCount == 11):
		magentaFightCount = guiStory("Please!", magentaFightCount)
	elif(magentaFightCount == 12):
		incrementShakeSpeed(1)
	elif(magentaFightCount == 13):
		magentaFightCount = guiStory("I know I did you wrong but you can't let me go like this!", magentaFightCount)
	elif(magentaFightCount == 14):
		incrementShakeSpeed(2)
	elif(magentaFightCount == 15):
		magentaFightCount = guiStory("I... I'm sorry!", magentaFightCount)
	elif(magentaFightCount == 16):
		magentaFightCount = guiStory("I'll make it up to you.", magentaFightCount)
	elif(magentaFightCount == 17):
		incrementShakeSpeed(3)
	elif(magentaFightCount == 18):
		magentaFightCount = guiStory("PLEASE!", magentaFightCount)
	elif(magentaFightCount == 19):
		incrementShakeSpeed(6)
	elif(magentaFightCount == 20):
		magentaFightCount = guiStory("I'M SORRY!!!", magentaFightCount)
	elif(magentaFightCount == 21):
		for i in smallerEyes:
			i.undraw()
		endFight()
		return 5

	return currentTrial

def incrementShakeSpeed(num):
	global magentaShakeSpeed
	global magentaFightCount
	magentaShakeSpeed += num
	magentaFightCount += 1

def updateMagentaSpeech():
	if(getOpponentHealth() <= 0):	return
	global speechCount
	if(getPlayerHealth() <= 0):
		speechCount = 0
	global FightSpoken
	if(not FightSpoken and not getIsAttacking()):
		FightSpoken = True
		if(speechCount < len(magentaSpeech)):
			guiSpeak(magentaSpeech[speechCount])
			speechCount += 1
		else:
			guiSpeak("...")

	if(getIsAttacking() and FightSpoken):
		FightSpoken = False
	
