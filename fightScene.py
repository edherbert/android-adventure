from graphics import *
from map import *
from gui import *
from player import *
import random
#Object in the center of the screen
#Bar down the bottom to select
#The player just gets given dialogue each turn
#They can't lose the trial.
#They can lose to magenta
#The trial acts as usual

#Menu components are fight and heal, 

menuComponents = []

fightCover = Rectangle(Point(0, 0), Point(winWidth, winHeight))

#A rectangle to cover the opponent when they get damaged
opponentDamageCover = Rectangle(Point(winWidth / 2 - 100, winHeight / 2 - 100), Point(winWidth / 2 + 100, winHeight / 2 + 100))

#The name of the opponent
fightingOpponentName = ""
#The base health of the player
baseOpponentHealth = 10
#The health of the opponent
opponentHealth = baseOpponentHealth
#The gui objects of the opponent
opponentData = []

#Whether the fight button is the currently selected button
fightSelected = True
#A timer to make sure that the player switches buttons reasonably
fightSelectionToggleCount = 5
#An array that contains all the keys that need to be pressed to complete the attack
fightKeys = []
#To tell if the player has clicked the fight button, and is still fighting
isAttacking = False
#To tell if the player has started healing
isHealing = False
#A variable to work out how long the player took to enter all the numbers
attackCount = 0
#A list of player effects
playerAttackEffects = []
#A variable to tell if the player can interact with the fight gui
#Mostly used by the strength trial
playerCanInteractFight = True
#Determines if the opponent can attack
opponentCanAttack = True

#A health variable for the player
playerMaxHealth = 800
playerHealth = playerMaxHealth
#A rectangle to show the current key that needs to be pressed
currentKeyBackground = Rectangle(Point(winWidth - 100, winHeight - 200), Point(winWidth, winHeight - 100))

def initFightScene():
	fightCover.setFill("black")
	opponentDamageCover.setFill("black")

	currentKeyBackground.setFill("grey")

	boxWidth = 150
	boxHeight = 50
	boxPadding = 20

	fightBox = Rectangle(Point(winWidth / 2 - boxWidth - boxPadding, winHeight - boxPadding - boxHeight), Point(winWidth / 2 - boxPadding, winHeight - boxPadding))
	healBox = Rectangle(Point(winWidth / 2 + boxWidth + boxPadding, winHeight - boxPadding - boxHeight), Point(winWidth / 2 + boxPadding, winHeight - boxPadding))

	fightText = Text(fightBox.getCenter(), "Fight")
	healText = Text(healBox.getCenter(), "Heal")

	opponentNameText = Text(Point(80, 40), fightingOpponentName)

	opponentHealthContainer = Rectangle(Point(30, 60), Point(300, 100))
	opponentHealthContainer.setFill("white")

	opponentHealthIndicator = Rectangle(Point(opponentHealthContainer.getP1().getX() + 10, opponentHealthContainer.getP1().getY() + 10), Point(opponentHealthContainer.getP2().getX() - 10, opponentHealthContainer.getP2().getY() - 10))
	opponentHealthIndicator.setFill("red")

	playerHealthIndicator = Rectangle(Point(0, winHeight - 10), Point(winWidth * (playerHealth / playerMaxHealth), winHeight))
	playerHealthIndicator.setFill("green")

	for i in [fightText, healText, opponentNameText]:
		i.setSize(20)
		i.setTextColor("white")

	for i in [fightBox, healBox]:
		i.setOutline("white")
		i.setWidth(3)

	for i in [fightBox, healBox, fightText, healText, opponentNameText, opponentHealthContainer, opponentHealthIndicator, playerHealthIndicator]:
		menuComponents.append(i)

def playerCanInteractFight(val):
	global playerCanInteractFight
	playerCanInteractFight = val

def isFightSelected():
	return fightSelected

def setOpponentCanAttack(val):
	global opponentCanAttack
	opponentCanAttack = val

def playerHeal(win):
	global isHealing
	isHealing = True
	populateKeysList(9)
	drawKeysList(win)
	currentKeyBackground.setFill("green")

def getOpponentHealth():
	return opponentHealth

def getPlayerHealth():
	return playerHealth

def changePlayerHealth(win, ammount):
	global playerHealth
	playerHealth += ammount
	if(playerHealth < 0):
		playerHealth = 0
		#endFight()

	if(playerHealth > playerMaxHealth):
		playerHealth = playerMaxHealth

	redrawPlayerHealth(win)

def redrawPlayerHealth(win):
	global menuComponents
	menuComponents[7].undraw()
	playerRect = Rectangle(Point(0, winHeight - 10), Point(winWidth * (playerHealth / playerMaxHealth), winHeight))
	playerRect.setFill("green")
	playerRect.draw(win)
	menuComponents[7] = playerRect


def addToAttackCount():
	global attackCount
	attackCount += 1

def getIsAttacking():
	return isAttacking

def moveOpponent(x, y):
	for i in opponentData:
		i.move(x, y)

def getOpponentData():
	return opponentData

def fightSceneUpdate(win, key):
	if(not isPlayerFighting()):	return
	global fightSelectionToggleCount
	global playerHealth

	if(fightSelectionToggleCount > 0):	fightSelectionToggleCount -= 1

	#Debug and things, probably remove this before submission
	#if(key == "3"):	takeHealthOpponent(win, 10000)

	if(not isSpeaking() and not isAttacking and not isHealing):
		if(key == "z" or key == "Return"):
			if(playerCanInteractFight):
				if(fightSelected):
					startAttack(win)
				else:
					playerHeal(win)

		if(key == "Left" or key == "Right"):
			toggleFightSelection()

	if(playerHealth <= 0):
		newCover = Rectangle(Point(0, 0), Point(winWidth, winHeight))
		newCover.setFill("black")
		newCover.setOutline("black")
		global opponentHealth
		playerHealth = playerMaxHealth
		opponentHealth = baseOpponentHealth
		drawOpponentHealth(win)
		redrawPlayerHealth(win)
		newCover.draw(win)
		time.sleep(1)
		newCover.undraw()

	#If attacking check for attack keys
	if(isAttacking or isHealing):
		addToAttackCount()
		currentKey = getCurrentFightKey()
		if(currentKey != None):
			if(key == currentKey[1].getText()):
				removeCurrentKey()
		else:
			ammountToTake = 0
			if(attackCount <= 150):	ammountToTake = 50
			elif(attackCount > 150 and attackCount <= 170):	ammountToTake = 40
			elif(attackCount > 170 and attackCount <= 190):	ammountToTake = 30
			elif(attackCount > 190 and attackCount <= 210):	ammountToTake = 20
			else:	ammountToTake = 15
			currentKeyBackground.undraw()
			if(isAttacking):				
				attackOpponent(win, ammountToTake)
			if(isHealing):
				changePlayerHealth(win, ammountToTake * 3)
			stopAttack()
			stopHealing()
			time.sleep(0.5)
			if(opponentCanAttack and opponentHealth > 0):
				opponentAttackPlayer(win, ammountToTake)

	if(fightSelected):
		menuComponents[0].setFill("grey")
		menuComponents[1].setFill("black")
	else:
		menuComponents[0].setFill("black")
		menuComponents[1].setFill("grey")

def opponentAttackPlayer(win, ammountToTake):
	#The opponent attacks the player depending on how badly they did in the key pressing bit
	playerDamage = (55 - ammountToTake) * 0.6
	for i in range(2):
		for i in opponentData:
			i.move(0, 20)

	changePlayerHealth(win, -playerDamage)
	for i in range(10):
		time.sleep(0.01)
		for i in opponentData:
			i.move(0, -4)


def attackOpponent(win, ammount):
	global playerAttackEffects
	playerAttackEffects = []
	for i in range(int(ammount / 2)):
		effect = Circle(Point(winWidth / 2 - 48 + 96 * random.random(), winHeight / 2 - 48 + 96 * random.random()), 5)
		effect.setFill("grey")
		time.sleep(0.05)
		effect.draw(win)
		playerAttackEffects.append(effect)

	for i in playerAttackEffects:
		i.undraw()

	for i in range(3):
		opponentDamageCover.draw(win)
		time.sleep(0.1)
		opponentDamageCover.undraw()
		time.sleep(0.1)

	takeHealthOpponent(win, ammount)

def stopAttack():
	global isAttacking
	isAttacking = False

def stopHealing():
	global isHealing
	isHealing = False

def playerIsHealing():
	return isHealing

def removeCurrentKey():
	fightKeys[0].undraw()
	fightKeys[1].undraw()
	fightKeys.pop(0)
	fightKeys.pop(0)
	for i in fightKeys:
		i.move(100, 0)

def startAttack(win):
	global isAttacking
	if(isAttacking):	return
	global attackCount
	attackCount = 0

	currentKeyBackground.setFill("grey")

	isAttacking = True
	populateKeysList(9)
	drawKeysList(win)

def getCurrentFightKey():
	if(len(fightKeys) <= 1):	return None
	return fightKeys[0:2]

def drawKeysList(win):
	currentKeyBackground.draw(win)
	for i in fightKeys:
		i.draw(win)

def populateKeysList(numKeys):
	global fightKeys
	fightKeys = []
	keyBoxY = winHeight - 200
	keys = "abcdefghijklmnopqrstuvwxyz"
	for i in range(numKeys):
		keyBoxX = i * 100
		keyBox = Rectangle(Point(winWidth - keyBoxX, keyBoxY), Point(winWidth - keyBoxX - 100, keyBoxY + 100))
		keyBox.setWidth(3)
		keyBox.setOutline("white")

		text = Text(keyBox.getCenter(), keys[math.floor(random.random() * 26)])
		text.setTextColor("white")
		text.setSize(30)

		fightKeys.append(keyBox)
		fightKeys.append(text)

def toggleFightSelection():
	global fightSelected
	global fightSelectionToggleCount
	if(fightSelectionToggleCount <= 0):
		fightSelected = not fightSelected
		fightSelectionToggleCount = 5


def endFight():
	fightCover.undraw()
	setIsFighting(False)
	for i in menuComponents:
		i.undraw()
	for i in opponentData:
		i.undraw()

def startFight(win, data, opponentName, health):
	global fightingOpponentName
	global opponentHealth
	global menuComponents
	global opponentData
	global baseOpponentHealth
	global playerHealth
	playerHealth = playerMaxHealth
	baseOpponentHealth = health
	setIsFighting(True)
	fightingOpponentName = opponentName
	opponentHealth = health
	opponentData = data

	menuComponents[4].setText(fightingOpponentName)

	opponentHealthContainer = Rectangle(Point(30, 60), Point(30 + health + 30, 100))
	opponentHealthContainer.setFill("white")
	menuComponents[5] = opponentHealthContainer

	opponentHealthIndicator = Rectangle(Point(opponentHealthContainer.getP1().getX() + 10, opponentHealthContainer.getP1().getY() + 10), Point(opponentHealthContainer.getP2().getX() - 10, opponentHealthContainer.getP2().getY() - 10))
	opponentHealthIndicator.setFill("red")
	menuComponents[6] = opponentHealthIndicator

	fightCover.draw(win)
	for i in menuComponents:
		i.draw(win)

	for i in opponentData:
		i.draw(win)

def takeHealthOpponent(win, ammount):
	global opponentHealth
	opponentHealth -= ammount
	if(opponentHealth <= 0):
		opponentHealth = 0
		menuComponents[6].undraw()
		return

	drawOpponentHealth(win)

def drawOpponentHealth(win):
	global menuComponents
	opponentHealthContainer = menuComponents[5]

	opponentHealthIndicator = Rectangle(Point(opponentHealthContainer.getP1().getX() + 10, opponentHealthContainer.getP1().getY() + 10), Point(opponentHealthContainer.getP1().getX() + 10 + opponentHealth, opponentHealthContainer.getP2().getY() - 10))
	opponentHealthIndicator.setFill("red")
	menuComponents[6].undraw()
	menuComponents[6] = opponentHealthIndicator
	menuComponents[6].draw(win)
