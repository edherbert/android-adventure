from graphics import *
from map import *
from player import *
from fightScene import *
from android import *
import random

strengthTrialCount = 0

sageStrengthAnim = createAndroid("#9C9F84")

def initStrengthTrial(win):
	pass

def strengthTrialUpdate(win, currentTrial, key):
	global strengthTrialCount

	if(strengthTrialCount == 0):
		startFight(win, createTree(winWidth / 2 - 24, winHeight / 2 - 24 - 20), "tree", 100)
		playerCanInteractFight(False)
		setCanPlayerMove(False)
		setOpponentCanAttack(False)
		strengthTrialCount += 1
	elif(strengthTrialCount == 1):
		time.sleep(1)
		strengthTrialCount += 1
	elif(strengthTrialCount == 2):
		strengthTrialCount = guiStory("I don't suppose you were expecting this.", strengthTrialCount)
	elif(strengthTrialCount == 3):
		strengthTrialCount = guiStory("I'm going to teach you how to fight, and I'm going to use this tree to demonstrate.", strengthTrialCount)
	elif(strengthTrialCount == 4):
		strengthTrialCount = guiStory("This is the trial of strength.", strengthTrialCount)
	elif(strengthTrialCount == 5):
		strengthTrialCount = guiStory("I said previously that there is nothing stronger than the will of nature, so let me demonstrate that.", strengthTrialCount)
	elif(strengthTrialCount == 6):
		strengthTrialCount = guiStory("When fighting you have two options, fight or heal.", strengthTrialCount)
	elif(strengthTrialCount == 7):
		strengthTrialCount = guiStory("Fighting will deal damage to your opponent, and healing will heal yourself.", strengthTrialCount)
	elif(strengthTrialCount == 8):
		strengthTrialCount = guiStory("Let's start with healing.", strengthTrialCount)
	elif(strengthTrialCount == 9):
		strengthTrialCount = guiStory("You see that green bar down the bottom? Watch it closely.", strengthTrialCount)
	elif(strengthTrialCount == 10):
		time.sleep(1)
		strengthTrialCount += 1
	elif(strengthTrialCount == 11):
		strengthTrialCount = guiStory("*Sage hits you over the head with a shovel*", strengthTrialCount)
	elif(strengthTrialCount == 12):
		changePlayerHealth(win, -playerMaxHealth / 2)
		time.sleep(1)
		strengthTrialCount += 1
	elif(strengthTrialCount == 13):
		strengthTrialCount = guiStory("See? That bar is your health. If it reaches 0 then you lose.", strengthTrialCount)
	elif(strengthTrialCount == 14):
		strengthTrialCount = guiStory("Now try to heal that damage. Move over to the heal button with the arrow keys and push z or enter to heal.", strengthTrialCount)
	elif(strengthTrialCount == 15):
		if(key == "z" or key == "Return"):
			if(not isFightSelected()):
				strengthTrialCount = guiStory("Clicking heal will bring up a set of keys. Press them fast to heal a higher amount.", strengthTrialCount)

	elif(strengthTrialCount == 16):
		playerHeal(win)
		strengthTrialCount += 1
	elif(strengthTrialCount == 17):
		if(not playerIsHealing()):
			strengthTrialCount += 1
	elif(strengthTrialCount == 18):
		strengthTrialCount = guiStory("Excellent! Remember, the faster you type the keys the more you will heal.", strengthTrialCount)
	elif(strengthTrialCount == 19):
		playerCanInteractFight(True)
		strengthTrialCount = guiStory("Actually, the same mechanic works for attacking. Try it now.", strengthTrialCount)
	elif(strengthTrialCount == 20):
		if(getIsAttacking()):	strengthTrialCount += 1
	elif(strengthTrialCount == 21):
		if(not getIsAttacking()):	strengthTrialCount += 1
	elif(strengthTrialCount == 22):
		playerCanInteractFight(False)
		strengthTrialCount = guiStory("Well done! You've mastered the basics of combat.", strengthTrialCount)
	elif(strengthTrialCount == 23):
		strengthTrialCount = guiStory("Now that you've got the hang of that, let's start the ...", strengthTrialCount)
	elif(strengthTrialCount == 24):
		for i in range(50):
			moveOpponent(8, 0)
			time.sleep(0.01)
			moveOpponent(-8, 0)
			time.sleep(0.01)

		strengthTrialCount += 1
		time.sleep(1)
	elif(strengthTrialCount == 25):
		strengthTrialCount = guiStory("Wait, what was that?", strengthTrialCount)
	elif(strengthTrialCount == 26):
		for i in range(2):
			opponentAttackPlayer(win, 10)
			time.sleep(0.2)

		strengthTrialCount += 1

	elif(strengthTrialCount == 27):
		strengthTrialCount = guiStory("Ahhhh, the tree's come to life!", strengthTrialCount)
	elif(strengthTrialCount == 28):
		strengthTrialCount = guiStory("What the hell. That wasn't supposed to happen.", strengthTrialCount)
	elif(strengthTrialCount == 29):
		strengthTrialCount = guiStory("I was just supposed to give you an axe and that would be some metaphor about acquiring strength.", strengthTrialCount)
	elif(strengthTrialCount == 30):
		strengthTrialCount = guiStory("I didn't even know trees could come to life like that!", strengthTrialCount)
	elif(strengthTrialCount == 31):
		for i in range(2):
			opponentAttackPlayer(win, 10)
			time.sleep(0.2)

		strengthTrialCount += 1
	elif(strengthTrialCount == 32):
		strengthTrialCount = guiStory("All right lads, he doesn't look best pleased. But don't worry, I'll stop him!", strengthTrialCount)
	elif(strengthTrialCount == 33):
		drawAndroid(win, sageStrengthAnim)
		moveAndroid(sageStrengthAnim, -48, winHeight / 2 - 24)
		changeAndroidDirection(sageStrengthAnim, 2)
		strengthTrialCount += 1
	elif(strengthTrialCount == 34):
		moveAndroid(sageStrengthAnim, 8, 0)
		if(sageStrengthAnim[0].getP2().getX() >= winWidth / 2 - 24):	
			strengthTrialCount += 1
	elif(strengthTrialCount == 35):
		moveAndroid(sageStrengthAnim, -8, 6)
		changeAndroidDirection(sageStrengthAnim, int(random.random() * 15))
		if(sageStrengthAnim[0].getP1().getY() >= winHeight):	strengthTrialCount += 1
	elif(strengthTrialCount == 36):
		strengthTrialCount = guiStory("Ow my head.", strengthTrialCount)
	elif(strengthTrialCount == 37):
		playerCanInteractFight(True)
		setOpponentCanAttack(True)
		strengthTrialCount = guiStory("Ok plan B, you take care of him. If you can stop him then I'll pass your trial attempt. I've taught you what you need to know, good luck.", strengthTrialCount)
	elif(strengthTrialCount == 38):
		if(getOpponentHealth() <= 0):	strengthTrialCount += 1
		if(getPlayerHealth() <= 50):	strengthTrialCount = 45
	elif(strengthTrialCount == 39):
		for i in range(50):
			moveOpponent(8, 0)
			time.sleep(0.01)
			moveOpponent(-8, 0)
			time.sleep(0.01)

		strengthTrialCount += 1
		time.sleep(1)
	elif(strengthTrialCount == 40):
		strengthTrialCount = guiStory("You... You did it.", strengthTrialCount)
	elif(strengthTrialCount == 41):
		strengthTrialCount = guiStory("To tell you the truth, I didn't expect you to actually be able to stop it.", strengthTrialCount)
	elif(strengthTrialCount == 42):
		strengthTrialCount = guiStory("You sure showed me up.", strengthTrialCount)
	elif(strengthTrialCount == 43):
		strengthTrialCount = guiStory("Well as you managed to stop it, it looks like you've passed my trial.", strengthTrialCount)
	elif(strengthTrialCount == 44):
		strengthTrialCount = 50
	elif(strengthTrialCount == 45):		
		playerCanInteractFight(False)
		setOpponentCanAttack(False)
		time.sleep(2)
		strengthTrialCount += 1
	elif(strengthTrialCount == 46):
		strengthTrialCount = guiStory("*The tree stopped moving, maybe it doesn't want to attack any more.*", strengthTrialCount)
	elif(strengthTrialCount == 47):
		strengthTrialCount = guiStory("Wait? It stopped?", strengthTrialCount)
	elif(strengthTrialCount == 48):
		strengthTrialCount = guiStory("Did it take pity on you because you were hurt. Maybe it just wanted to make itself clear that it doesn't like being hit.", strengthTrialCount)
	elif(strengthTrialCount == 49):
		strengthTrialCount = guiStory("Well I did say that if you stopped it then I would pass your trial attempt.", strengthTrialCount)
	elif(strengthTrialCount == 50):
		endFight()
		removeRolldown()
		return 0

	return currentTrial
