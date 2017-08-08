from androidVillage import *
from desert import *
from forest import *
from Intro import *
from trialSite import *
from sightTrial import *
from deductionTrial import *
from strengthTrial import *
from wasteland import *
from abyss import *
from ending import *
#Used to determine if the map needs to have it's objects re-created
previousMapId = 0
#The same as before, but for trials
previousTrialId = 0
#Used to determine which trial the player is currently doing
#0 means no trial
currentTrial = 1
#1 - game intro
#2 - Sight trial
#3 - Deduction trial
#4 - Strength trial
#5 - The bit in the abyss

def updateStory(mapId, win, key, player):
	#Update the story
	global previousMapId
	global previousTrialId
	if(mapId != previousMapId):
		#If the map that is being updated is different from the previous one then there has been a change, so re-create the entities
		previousMapId = mapId
		initStory(mapId)
	if(currentTrial != previousTrialId):
		previousTrialId = currentTrial
		initTrial(currentTrial, win)

	if(currentTrial == 0):
		if(mapId == 1):	setStoryTrial(androidVillageUpdate(win, player, currentTrial))
		if(mapId == 3):	desertUpdate()
		if(mapId == 4):	forestUpdate(win, player)
		if(mapId == 5):	wastelandUpdate(win, player)
		if(mapId == 7):	setStoryTrial(trialSiteUpdate(win, player, currentTrial))
	else:
		if(currentTrial == 1):	setStoryTrial(updateIntro(win, key, currentTrial))
		if(currentTrial == 2):	setStoryTrial(sightTrialUpdate(win, currentTrial))
		if(currentTrial == 3):	setStoryTrial(deductionTrialUpdate(win, currentTrial))
		if(currentTrial == 4):	setStoryTrial(strengthTrialUpdate(win, currentTrial, key))
		if(currentTrial == 5):	setStoryTrial(abyssUpdate(win, key, currentTrial))
		if(currentTrial == 6):	setStoryTrial(magentaFightUpdate(win, key, currentTrial))

def initStory(mapId):
	if(mapId == 1):	androidVillageInit()
	if(mapId == 3):	desertInit()
	if(mapId == 4):	forestInit()
	if(mapId == 7):	trialSiteInit()

def initTrial(trialId, win):
	if(trialId == 1):	initIntro(win)
	if(trialId == 2):	sightTrialInit(win)
	if(trialId == 4):	initStrengthTrial(win)
	if(trialId == 5):	abyssInit(win)

def setStoryTrial(trialId):
	global currentTrial
	currentTrial = trialId
