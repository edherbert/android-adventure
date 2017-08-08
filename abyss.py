from graphics import *
from android import *
from map import *
from gui import *
from player import *

abyssCover = Rectangle(Point(0, 0), Point(winWidth, winHeight))

titleAbyss = Text(Point(winWidth / 2, winHeight / 2 - 100), "Android Adventure")
underTitleTextAbyss = Text(Point(winWidth / 2, winHeight / 2 - 50), "By Edward Herbert")

abyssCount = 0

abyssCoverDrawn = False

tileDetails = []

abyssPlayer = createAndroid("green")
abyssMagenta = createAndroid("#D80073")
abyssSlate = createAndroid("#778899")

abyssApple = Circle(Point(0, 0), 10)
abyssChild = Circle(Point(0, 0), 8)

abyssChoiceArrow = Polygon([Point(0, 0), Point(10, 10), Point(0, 20)])
#Eat, true
currentChoiceSelection = True

abyssPlayerX = 0
abyssPlayerY = 0

#Player shaking animation variables
abyssPlayerShaking = False
abyssPlayerShakingCount = 0
abyssPlayerShakingDirection = True
abyssPlayerShakingRate = 2

def abyssUpdate(win, key, currentTrial):
	global abyssCount
	global abyssGuiCount

	abyssPlayerShakeUpdate()

	if(abyssCount == 0):
		setCanPlayerMove(False)
		time.sleep(2)
		abyssCount += 1
	elif(abyssCount == 1):
		abyssCount = guiStory("It's us or them.", abyssCount)
	elif(abyssCount == 2):
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 3):
		moveAbyssPlayer(winWidth / 2 - 24, winHeight / 2 - 24 + 48)
		moveAndroid(abyssPlayer, abyssPlayerX, abyssPlayerY)
		createAbyssMap()
		moveAbyssPlayer(winWidth + winWidth / 4, 0)
		changeAndroidDirection(abyssPlayer, 3)
		drawAbyssMap(win)
		drawAndroid(win, abyssPlayer)
		abyssCount += 1
	elif(abyssCount == 4):
		checkAbyssKeys(key)
		if(abyssPlayerX < 1530):	abyssCount += 1
	elif(abyssCount == 5):
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 6):
		abyssCount = guiStory("It's us or them.", abyssCount)
	elif(abyssCount == 7):
		checkAbyssKeys(key)
		if(abyssPlayerX < 1330):	abyssCount += 1
	elif(abyssCount == 8):
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 9):
		abyssCount = guiStory("It's us or them.", abyssCount)
	elif(abyssCount == 10):
		checkAbyssKeys(key)
		if(abyssPlayerX < 1000):	abyssCount += 1
	elif(abyssCount == 11):
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 12):
		abyssCount = guiStory("It's us or...", abyssCount)
	elif(abyssCount == 13):
		time.sleep(2)
		abyssApple.setFill("red")
		abyssApple.move(-2 * 48, abyssPlayer[0].getP2().getY() - 10)
		abyssApple.draw(win)
		abyssCount += 1
	elif(abyssCount == 14):
		if(abyssPlayer[0].getP2().getX() < winWidth - 3 * 48):
			moveAndroid(abyssPlayer, 6, 0)
			moveAbyssMap(6, 0)
			abyssApple.move(6, 0)
		else:
			abyssCount += 1
	elif(abyssCount == 15):
		time.sleep(2)
		abyssCount += 1
	elif(abyssCount == 16):
		abyssCount = guiStory("So... You made it.", abyssCount)
	elif(abyssCount == 17):
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 18):
		abyssCount = guiStory("You came all this way to eat me.", abyssCount)
	elif(abyssCount == 19):
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 20):
		#Code that moves the apple that was slightly broken.
		#I ran out of time so I just removed it.
		'''
		if(abyssApple.getP1().getY() < abyssPlayerY + 48 * 2):
			abyssApple.move(0, 1)
			if(abyssApple.getP1().getY() + 10 >= tileSize * 9):	abyssCount += 1
		else:	abyssCount += 1'''
		abyssCount += 1
	elif(abyssCount == 21):
		abyssCount += 1
	elif(abyssCount == 22):
		abyssCount = guiStory("I'm sorry for what I did. I must have caused you a lot of trouble.", abyssCount)
	elif(abyssCount == 23):
		abyssCount = guiStory("I wasn't thinking properly.", abyssCount)
	elif(abyssCount == 24):
		abyssCount = guiStory("I was scared that it was all going to end just like that.", abyssCount)
	elif(abyssCount == 25):
		abyssCount = guiStory("But seeing that you made it down here... You must really want to leave.", abyssCount)
	elif(abyssCount == 26):
		abyssCount = guiStory("Condemning someone to stay here for eternity. I could never do that. No matter what the cost.", abyssCount)
	elif(abyssCount == 27):
		abyssCount = guiStory("You want to move on I suppose. You probably have friends and family back in the real world.", abyssCount)
	elif(abyssCount == 28):
		if(abyssApple.getP1().getY() > abyssPlayer[0].getP1().getY() + 28):
			abyssApple.move(0, -1)
		else:	abyssCount += 1
	elif(abyssCount == 29):
		abyssCount = guiStory("So do it. I'll let you go back.", abyssCount)
	elif(abyssCount == 30):
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 31):
		if(abyssPlayer[0].getP1().getX() > winWidth - 48 * 5):
			moveAndroid(abyssPlayer, -2, 0)
		else:
			abyssCount += 1
	elif(abyssCount == 32):
		abyssCount = guiStory("Daddy!", abyssCount)
	elif(abyssCount == 33):
		abyssChild.setFill("red")
		abyssChild.move(-2 * 48,  abyssPlayer[0].getP2().getY() - 8)
		abyssChild.draw(win)
		abyssCount += 1
	elif(abyssCount == 34):
		if(abyssChild.getP1().getX() < 48 * 2):
			abyssChild.move(4, 0)
		else:
			abyssCount += 1
	elif(abyssCount == 35):
		abyssCount = guiStory("Are you done yet? You said you would leave for a bit but I didn't think you would be THIS long.", abyssCount)
	elif(abyssCount == 36):
		for i in range(6):
			time.sleep(0.01)
			abyssApple.move(-1, 0)
		abyssCount += 1
	elif(abyssCount == 37):
		abyssCount = guiStory("Not yet, son. Now please go back to where I told you to wait.", abyssCount)
	elif(abyssCount == 38):
		abyssCount = guiStory("Uuuuhhhhh. Ok. How long do you think you'll be?", abyssCount)
	elif(abyssCount == 39):
		time.sleep(2)
		abyssCount += 1
	elif(abyssCount == 40):
		abyssCount = guiStory("I might be a while.", abyssCount)
	elif(abyssCount == 41):
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 42):
		abyssCount = guiStory("Ok then. See you in a bit.", abyssCount)
	elif(abyssCount == 43):
		if(abyssChild.getP1().getX() > - 20):
			abyssChild.move(-4, 0)
		else:
			abyssChild.undraw()
			abyssCount += 1
	elif(abyssCount == 44):
		for i in range(6):
			time.sleep(0.01)
			abyssApple.move(1, 0)
		time.sleep(0.5)
		abyssCount += 1
	elif(abyssCount == 45):
		abyssCount = guiStory("Sorry about that.", abyssCount)
	elif(abyssCount == 46):
		abyssCount = guiStory("He can be very attentive sometimes.", abyssCount)
	elif(abyssCount == 47):
		abyssCount = guiStory("But he's a good kid.", abyssCount)
	elif(abyssCount == 48):
		time.sleep(2)
		abyssCount += 1
	elif(abyssCount == 49):
		abyssCount = guiStory("Ok, I'm ready.", abyssCount)
	elif(abyssCount == 50):
		abyssCount = guiStory("Do what you must.", abyssCount)
	elif(abyssCount == 51):
		if(abyssPlayer[0].getP2().getX() < winWidth - 5 * 48):
			moveAndroid(abyssPlayer, 6, 0)
			moveAbyssMap(6, 0)
			abyssApple.move(6, 0)
		else:
			abyssCount += 1
	elif(abyssCount == 52):
		showChoice(win)
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 53):
		updateChoiceGui(key)
	elif(abyssCount == 54):
		if(currentChoiceSelection):
			abyssCount += 1
		else:
			abyssCount = 133

	#Apple eaten
	elif(abyssCount == 55):
		time.sleep(1)
		for i in range(10):
			moveAndroid(abyssPlayer, -24, 0)
			time.sleep(0.01)
		time.sleep(0.1)
		abyssApple.undraw()
		for i in range(10):
			moveAndroid(abyssPlayer, 24, 0)
		time.sleep(2)
		abyssCount += 1
	elif(abyssCount == 56):
		if(abyssPlayer[0].getP2().getX() > winWidth / 2):
			moveAndroid(abyssPlayer, -6, 0)
			moveAbyssMap(-6, 0)
		else:	abyssCount += 1
	elif(abyssCount == 57):
		changeAndroidDirection(abyssMagenta, 1)
		abyssCount = guiStory("Well done.", abyssCount)
	elif(abyssCount == 58):
		abyssCount = guiStory(getPlayerName() + ".", abyssCount)
	elif(abyssCount == 59):
		moveAndroid(abyssMagenta, winWidth + 48, abyssPlayer[0].getCenter().getY() - 24)
		drawAndroid(win, abyssMagenta)
		abyssCount += 1
	elif(abyssCount == 60):
		if(abyssPlayer[0].getP2().getX() > 2 * 48):
			moveAndroid(abyssPlayer, -6, 0)
			moveAbyssMap(-6, 0)
			moveAndroid(abyssMagenta, -6, 0)
		else:	abyssCount += 1
	elif(abyssCount == 61):
		if(abyssMagenta[0].getP1().getX() > winWidth - 5 * 48):
			moveAndroid(abyssMagenta, -4, 0)
		else:
			abyssCount += 1
	elif(abyssCount == 62):
		changeAndroidDirection(abyssPlayer, 2)
		abyssCount = guiStory("He he he.", abyssCount)
	elif(abyssCount == 63):
		abyssCount = guiStory("You know, I really didn't think you would make it this far.", abyssCount)
	elif(abyssCount == 64):
		abyssCount = guiStory("It was an effort, let me tell you.", abyssCount)
	elif(abyssCount == 65):
		abyssCount = guiStory("Like your little performance outside of the abyss.", abyssCount)
	elif(abyssCount == 66):
		abyssCount = guiStory("But that doesn't matter.", abyssCount)
	elif(abyssCount == 67):
		abyssCount = guiStory("Because now you've eaten that apple, any moment now you'll disappear.", abyssCount)
	elif(abyssCount == 68):
		abyssCount = guiStory("But before that...", abyssCount)
	elif(abyssCount == 69):
		setTextSpeed(16)
		abyssCount = guiStory("I'll eat you.", abyssCount)
	elif(abyssCount == 70):
		setTextSpeed(getDefaultTextSpeed())
		abyssCount = guiStory("That's right, I figured it out.", abyssCount)
	elif(abyssCount == 71):
		abyssCount = guiStory("If I'm the one who eats you before you disappear then I'll be the one to leave this place, not you.", abyssCount)
	elif(abyssCount == 72):
		if(abyssMagenta[0].getP1().getX() > winWidth - 6 * 48):
			moveAndroid(abyssMagenta, -4, 0)
		else:
			abyssCount += 1
	elif(abyssCount == 73):
		abyssCount = guiStory("What's that look in your eyes? Are you upset?", abyssCount)
	elif(abyssCount == 74):
		abyssCount = guiStory("Did you not expect to meet your end like this?", abyssCount)
	elif(abyssCount == 75):
		abyssCount = guiStory("Well tough, kid, you didn't seem too averted to murder just then.", abyssCount)
	elif(abyssCount == 76):
		abyssCount = guiStory("I've spent so long in this game. You can serve some time for me.", abyssCount)
	elif(abyssCount == 77):
		abyssCount = guiStory("Are you ready? No? Too bad! Here I come!", abyssCount)
	elif(abyssCount == 78):
		rolldown(win)
		abyssCount += 1
	elif(abyssCount == 79):
		if(abyssMagenta[0].getP1().getX() > abyssPlayer[0].getP2().getX() + 48):
			moveAndroid(abyssMagenta, -4, 0)
		else:	abyssCount += 1
	elif(abyssCount == 80):
		if(isRolldownComplete()):
			abyssCount += 1
	elif(abyssCount == 81):
		time.sleep(1)
		abyssCount += 1
		return 6

	elif(abyssCount == 82):
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 83):
		abyssCount = guiStory("Please.", abyssCount)
	elif(abyssCount == 84):
		abyssCount = guiStory("Please.", abyssCount)
	elif(abyssCount == 85):
		removeRolldown()
		abyssCount += 1
	elif(abyssCount == 86):
		setTextSpeed(getDefaultTextSpeed())
		abyssCount = guiStory("I...", abyssCount)
	elif(abyssCount == 87):
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 88):
		undrawAndroid(abyssMagenta)
		setTextSpeed(getDefaultTextSpeed())
		abyssCount += 1
	elif(abyssCount == 89):
		time.sleep(3)
		abyssCount += 1
	elif(abyssCount == 90):
		abyssCount = guiStory("Hello, " + getPlayerName() + ".", abyssCount)
	elif(abyssCount == 91):
		moveAndroid(abyssSlate, winWidth + 48, abyssPlayer[0].getP1().getY())
		changeAndroidDirection(abyssSlate, 1)
		drawAndroid(win, abyssSlate)
		abyssCount += 1
	elif(abyssCount == 92):
		if(abyssSlate[0].getP1().getX() > 48 * 15):
			moveAndroid(abyssSlate, -2, 0)
		else:
			abyssCount += 1
	elif(abyssCount == 93):
		abyssCount = guiStory("I see you're off then.", abyssCount)
	elif(abyssCount == 94):
		time.sleep(2)
		changeAndroidDirection(abyssSlate, 2)
		time.sleep(2)
		changeAndroidDirection(abyssSlate, 1)
		time.sleep(2)
		abyssCount += 1
	elif(abyssCount == 95):
		abyssCount = guiStory("Don't worry about it. You did what you had to.", abyssCount)
	elif(abyssCount == 96):
		abyssCount = guiStory("I suppose you're wondering what happened with Magenta.", abyssCount)
	elif(abyssCount == 97):
		abyssCount = guiStory("He seemed to be very afraid to die right?", abyssCount)
	elif(abyssCount == 98):
		abyssCount = guiStory("You see, androids cannot die, they simply reappear in the same area they were in when they died.", abyssCount)
	elif(abyssCount == 99):
		abyssCount = guiStory("But that's why the abyss is guarded. Why it's so difficult to get in.", abyssCount)
	elif(abyssCount == 100):
		abyssCount = guiStory("It's infinite. If someone dies in the abyss they will be lost forever.", abyssCount)
	elif(abyssCount == 101):
		abyssCount = guiStory("Magenta will probably re-awaken soon, somewhere off in these dark tunnels.", abyssCount)
	elif(abyssCount == 102):
		abyssCount = guiStory("He's lost forever.", abyssCount)
	elif(abyssCount == 103):
		abyssCount = guiStory("Magenta...", abyssCount)
	elif(abyssCount == 104):
		abyssCount = guiStory("A name that says suffering.", abyssCount)
	elif(abyssCount == 105):
		abyssCount = guiStory("He didn't deserve what happened to him. I would wish it on no one.", abyssCount)
	elif(abyssCount == 106):
		abyssCount = guiStory("Eternity is a long time, but someone had to live it.", abyssCount)
	elif(abyssCount == 107):
		abyssCount = guiStory("If he did succeed in eating you, you would have been reborn in the abyss instead.", abyssCount)
	elif(abyssCount == 108):
		abyssCount = guiStory("Of course Magenta knew this.", abyssCount)
	elif(abyssCount == 109):
		abyssCount = guiStory("I must ask you not to think badly of him. Magenta used to be such a nice person.", abyssCount)
	elif(abyssCount == 110):
		abyssCount = guiStory("Time wore away at him. He's been here for the longest.", abyssCount)
	elif(abyssCount == 111):
		abyssCount = guiStory("Originally, he made friends with his final apple, after he took pity on it.", abyssCount)
	elif(abyssCount == 112):
		abyssCount = guiStory("But once it reached the end of it's life, he was stuck.", abyssCount)
	elif(abyssCount == 113):
		abyssCount = guiStory("Existence wore him down. ", abyssCount)
	elif(abyssCount == 114):
		abyssCount = guiStory("But enough of that! You must be pretty excited to be going back to the real world!", abyssCount)
	elif(abyssCount == 115):
		abyssCount = guiStory("I wish I was you pal. I'm Jealous.", abyssCount)
	elif(abyssCount == 116):
		abyssCount = guiStory("You see, all I really wanted to say was I hope you're happy with how things turned out.", abyssCount)
	elif(abyssCount == 117):
		abyssCount = guiStory("I know you're probably upset you had to eat that final apple.", abyssCount)
	elif(abyssCount == 118):
		abyssCount = guiStory("I just want you to know that if I was in your situation, I would have done the same thing.", abyssCount)
	elif(abyssCount == 119):
		abyssCount = guiStory("Also, don't worry about that apple's child, I'll take care of him.", abyssCount)
	elif(abyssCount == 120):
		abyssCount = guiStory("The important thing is that you're happy with your choices, as you are the one who will have to live with them.", abyssCount)
	elif(abyssCount == 121):
		abyssCount = guiStory("Even in the real world, the choices you made here still happened.", abyssCount)
	elif(abyssCount == 122):
		abyssCount = guiStory("But with all that being said, please enjoy the rest of your life in the real world.", abyssCount)
	elif(abyssCount == 123):
		abyssCount = guiStory("Enjoy every second, in case you end up in another situation like this.", abyssCount)
	elif(abyssCount == 124):
		makePlayerShake()
		abyssCount = guiStory("Well, it looks like it's time.", abyssCount)
	elif(abyssCount == 125):
		abyssCount = guiStory("It's been a pleasure knowing you, " + getPlayerName() + ".", abyssCount)
	elif(abyssCount == 126):
		abyssCount = guiStory("Have a safe journey back! Good bye.", abyssCount)
	elif(abyssCount == 127):
		changeAndroidDirection(abyssSlate, 2)
		if(abyssSlate[0].getP1().getX() < winWidth + 100):
			moveAndroid(abyssSlate, 2, 0)
		else:
			abyssCount += 1
	elif(abyssCount == 128):
		if(abyssPlayer[0].getCenter().getX() < winWidth / 2):
			moveAndroid(abyssPlayer, 12, 0)
			moveAbyssMap(12, 0)
		else:
			abyssCount += 1
	elif(abyssCount == 129):
		changeAndroidDirection(abyssPlayer, 3)
		abyssCount += 1
	elif(abyssCount == 130):
		abyssIncrementShakingRate()
		if(abyssPlayerShakingRate >= 100):	abyssCount += 1
	elif(abyssCount == 131):
		undrawAbyssMap()
		undrawAndroid(abyssPlayer)
		abyssCover.setFill("white")
		abyssCover.setOutline("white")
		abyssCount += 1
	elif(abyssCount == 132):
		time.sleep(2)
		titleAbyss.draw(win)
		time.sleep(2)
		underTitleTextAbyss.draw(win)
		time.sleep(4)
		closeGame()

	#Apple not eaten
	elif(abyssCount == 133):
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 134):
		abyssCount = guiStory("What?", abyssCount)
	elif(abyssCount == 135):
		abyssCount = guiStory("You... you aren't going to eat me?", abyssCount)
	elif(abyssCount == 136):
		abyssCount = guiStory("But... you came all this way...", abyssCount)
	elif(abyssCount == 137):
		abyssCount = guiStory("You really are peculiar, " + getPlayerName() + ".", abyssCount)
	elif(abyssCount == 138):
		abyssCount = guiStory("You know that if you don't eat me, you'll be trapped here forever, right?", abyssCount)
	elif(abyssCount == 139):
		abyssCount = guiStory("But if you're not willing to eat me, then I suppose I don't have to worry any more.", abyssCount)
	elif(abyssCount == 140):
		abyssCount = guiStory("I donno but, maybe we could be friends?", abyssCount)
	elif(abyssCount == 141):
		time.sleep(1)
		setTextSpeed(16)
		abyssCount += 1
	elif(abyssCount == 142):
		abyssCount = guiStory(getPlayerName() + ".", abyssCount)
	elif(abyssCount == 143):
		setTextSpeed(12)
		abyssCount = guiStory("What are you doing?", abyssCount)
	elif(abyssCount == 144):
		setTextSpeed(8)
		abyssCount = guiStory("Why did you not heed my advice?", abyssCount)
	elif(abyssCount == 145):
		if(abyssPlayer[0].getP2().getX() > winWidth / 2):
			moveAndroid(abyssPlayer, -12, 0)
			moveAbyssMap(-12, 0)
			abyssApple.move(-12, 0)
		else:	abyssCount += 1
	elif(abyssCount == 146):
		moveAndroid(abyssMagenta, winWidth + 48, abyssPlayer[0].getCenter().getY() - 24)
		drawAndroid(win, abyssMagenta)
		changeAndroidDirection(abyssMagenta, 1)
		abyssCount += 1
	elif(abyssCount == 147):
		if(abyssPlayer[0].getP2().getX() > 5 * 48):
			moveAndroid(abyssPlayer, -12, 0)
			moveAbyssMap(-12, 0)
			moveAndroid(abyssMagenta, -12, 0)
			abyssApple.move(-12, 0)
		else:	abyssCount += 1
	elif(abyssCount == 148):
		if(abyssMagenta[0].getP1().getX() > winWidth - 5 * 48):
			moveAndroid(abyssMagenta, -4, 0)
		else:
			abyssCount += 1
	elif(abyssCount == 149):
		setTextSpeed(getDefaultTextSpeed())
		abyssCount = guiStory("YOU!", abyssCount)
	elif(abyssCount == 150):
		changeAndroidDirection(abyssPlayer, 2)
		abyssCount = guiStory("After EVERYTHING I've done for you.", abyssCount)
	elif(abyssCount == 151):
		abyssCount = guiStory("You've ruined it!", abyssCount)
	elif(abyssCount == 152):
		abyssCount = guiStory("You've ruined your only chance!", abyssCount)
	elif(abyssCount == 153):
		if(abyssApple.getP1().getX() < 48 * 2):
			abyssApple.move(8, 0)
		else:	abyssCount += 1
	elif(abyssCount == 154):
		abyssCount = guiStory("What's going on? Who are you?", abyssCount)
	elif(abyssCount == 155):
		abyssCount = guiStory(getPlayerName() + "...", abyssCount)
	elif(abyssCount == 156):
		abyssCount = guiStory("You're going to eat that apple and then...", abyssCount)
	elif(abyssCount == 157):
		setTextSpeed(16)
		abyssCount = guiStory("I'm going to eat you.", abyssCount)
	elif(abyssCount == 158):
		setTextSpeed(getDefaultTextSpeed())
		abyssCount = guiStory("I figured it out. If I'm the one to eat you before you disappear then I'll leave instead of you.", abyssCount)
	elif(abyssCount == 159):
		abyssCount = guiStory("This was all my plan. You would eat the apple without complaining.", abyssCount)
	elif(abyssCount == 160):
		abyssCount = guiStory("You RUINED it. You fool.", abyssCount)
	elif(abyssCount == 161):
		abyssCount = guiStory("But I don't care any more.", abyssCount)
	elif(abyssCount == 162):
		abyssCount = guiStory("You're going to eat that apple, whether you like it or not.", abyssCount)
	elif(abyssCount == 163):
		for i in range(10):
			abyssApple.move(1, 0)
			time.sleep(0.01)
		abyssCount += 1
	elif(abyssCount == 164):
		abyssCount = guiStory("Wait! You can't just choose what " + getPlayerName() + " does!", abyssCount)
	elif(abyssCount == 165):
		abyssCount = guiStory("SHUT UP APPLE!", abyssCount)
	elif(abyssCount == 166):
		abyssCount = guiStory("If you hadn't given that little speech to gain sympathy this never would have happened!", abyssCount)
	elif(abyssCount == 167):
		abyssCount = guiStory("Now get ready " + getPlayerName() + "... you're going to eat that apple whether you want to or not!", abyssCount)
	elif(abyssCount == 168):
		rolldown(win)
		abyssCount += 1
	elif(abyssCount == 169):
		if(abyssMagenta[0].getP1().getX() > abyssPlayer[0].getP2().getX() + 48):
			moveAndroid(abyssMagenta, -4, 0)
		else:	abyssCount += 1
	elif(abyssCount == 170):
		if(isRolldownComplete()):
			abyssCount += 1
	elif(abyssCount == 171):
		time.sleep(1)
		abyssCount += 1
		return 6

	elif(abyssCount == 172):
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 173):
		abyssCount = guiStory("Please.", abyssCount)
	elif(abyssCount == 174):
		abyssCount = guiStory("Please.", abyssCount)
	elif(abyssCount == 175):
		removeRolldown()
		abyssCount += 1
	elif(abyssCount == 176):
		abyssCount = guiStory("I...", abyssCount)
	elif(abyssCount == 177):
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 178):
		undrawAndroid(abyssMagenta)
		setTextSpeed(getDefaultTextSpeed())
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 179):
		abyssCount = guiStory("Is it over?", abyssCount)
	elif(abyssCount == 180):
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 181):
		changeAndroidDirection(abyssPlayer, 1)
		abyssCount = guiStory("Who was that? Did you know him?", abyssCount)
	elif(abyssCount == 182):
		abyssCount = guiStory("I suppose you weren't friends? Or were you?", abyssCount)
	elif(abyssCount == 183):
		abyssCount = guiStory("Either way, you killed him.", abyssCount)
	elif(abyssCount == 184):
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 185):
		changeAndroidDirection(abyssPlayer, 2)
		abyssCount = guiStory("Hello again, " + getPlayerName() + ".", abyssCount)
	elif(abyssCount == 186):
		moveAndroid(abyssSlate, winWidth + 48, abyssPlayer[0].getP1().getY())
		changeAndroidDirection(abyssSlate, 1)
		drawAndroid(win, abyssSlate)
		abyssCount += 1
	elif(abyssCount == 187):
		if(abyssSlate[0].getP1().getX() > 48 * 15):
			moveAndroid(abyssSlate, -2, 0)
		else:
			abyssCount += 1
	elif(abyssCount == 188):
		abyssCount = guiStory("It looks like you've been busy.", abyssCount)
	elif(abyssCount == 189):
		time.sleep(1)
		changeAndroidDirection(abyssSlate, 2)
		time.sleep(1)
		changeAndroidDirection(abyssSlate, 1)
		time.sleep(1)
		abyssCount += 1
		#Some of this is a copy and paste
		#I ran out of time at the end and couldn't come up with a more elegant solution :s
	elif(abyssCount == 190):
		abyssCount = guiStory("So this is your final apple?", abyssCount)
	elif(abyssCount == 191):
		abyssCount = guiStory("Hm. You chose to spare him, how interesting.", abyssCount)
	elif(abyssCount == 192):
		abyssCount = guiStory("I suppose you both are wondering what happened with Magenta.", abyssCount)
	elif(abyssCount == 193):
		abyssCount = guiStory("He seemed to be very afraid to die, right?", abyssCount)
	elif(abyssCount == 194):
		abyssCount = guiStory("You see, androids cannot die, they simply reappear in the same area they were in when they died.", abyssCount)
	elif(abyssCount == 195):
		abyssCount = guiStory("But that's why the abyss is guarded. Why it's so difficult to get in.", abyssCount)
	elif(abyssCount == 196):
		abyssCount = guiStory("It's infinite. If someone dies in the abyss they will be lost forever.", abyssCount)
	elif(abyssCount == 197):
		abyssCount = guiStory("Magenta will probably re-awaken soon, somewhere off in these dark tunnels.", abyssCount)
	elif(abyssCount == 198):
		abyssCount = guiStory("He's lost forever.", abyssCount)
	elif(abyssCount == 199):
		abyssCount = guiStory("Magenta...", abyssCount)
	elif(abyssCount == 200):
		abyssCount = guiStory("A name that says suffering.", abyssCount)
	elif(abyssCount == 201):
		abyssCount = guiStory("He didn't deserve what happened to him. I would wish it on no one.", abyssCount)
	elif(abyssCount == 202):
		abyssCount = guiStory("Eternity is a long time, but someone had to live it.", abyssCount)
	elif(abyssCount == 203):
		abyssCount = guiStory("If he did succeed in eating you, you would have been reborn in the abyss instead.", abyssCount)
	elif(abyssCount == 204):
		abyssCount = guiStory("Of course Magenta knew this.", abyssCount)
	elif(abyssCount == 205):
		abyssCount = guiStory("I must ask you not to think badly of him. Magenta used to be such a nice person.", abyssCount)
	elif(abyssCount == 206):
		abyssCount = guiStory("Time wore away at him. He's been here for the longest.", abyssCount)
	elif(abyssCount == 207):
		abyssCount = guiStory("But enough about that. The real reason I came here was to talk about your choice.", abyssCount)
	elif(abyssCount == 208):
		abyssCount = guiStory("You chose compassion, even if it means you are forced to stay here.", abyssCount)
	elif(abyssCount == 209):
		abyssCount = guiStory("Hey, I can't help but feel admiration for you kid.", abyssCount)
	elif(abyssCount == 210):
		abyssCount = guiStory("Did you know that that was the choice Magenta chose?", abyssCount)
	elif(abyssCount == 211):
		abyssCount = guiStory("Long ago he made friends with his apple too. But once it died he was forced to linger here.", abyssCount)
	elif(abyssCount == 212):
		abyssCount = guiStory("But let's not make any assumptions about your future, you still have to live it.", abyssCount)
	elif(abyssCount == 213):
		abyssCount = guiStory("The important thing is that you're happy with your choices, as you are the one who will have to live them.", abyssCount)
	elif(abyssCount == 214):
		abyssCount = guiStory("In this world or the other, your choices matter, so always stand by them.", abyssCount)
	elif(abyssCount == 215):
		abyssCount = guiStory("Anyway, we should head back to the village. The apple will be safe as the others won't be able to eat it and leave, only you can do that.", abyssCount)
	elif(abyssCount == 216):
		abyssCount = guiStory("Well, I'll go on ahead. We have an eternity to fill, how about a game of cards?", abyssCount)
	elif(abyssCount == 217):
		time.sleep(1)
		changeAndroidDirection(abyssSlate, 2)
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 218):
		if(abyssSlate[0].getP1().getX() < winWidth + 48 * 2):
			moveAndroid(abyssSlate, 4, 0)
		else:	abyssCount += 1
	elif(abyssCount == 219):
		if(abyssPlayer[0].getP1().getX() < winWidth / 2):
			moveAndroid(abyssPlayer, 4, 0)
		else:	abyssCount += 1
	elif(abyssCount == 220):
		abyssCount = guiStory(getPlayerName() + "...", abyssCount)
	elif(abyssCount == 221):
		changeAndroidDirection(abyssPlayer, 1)
		abyssCount = guiStory("Thanks...", abyssCount)
	elif(abyssCount == 222):
		time.sleep(2)
		changeAndroidDirection(abyssPlayer, 2)
		time.sleep(1)
		abyssCount += 1
	elif(abyssCount == 223):
		if(abyssApple.getP1().getX() < winWidth + 48):
			moveAndroid(abyssPlayer, 4, 0)
			abyssApple.move(4, 0)
		else:	abyssCount += 1
	elif(abyssCount == 224):
		time.sleep(1)
		abyssChild.draw(win)
		abyssCount += 1
	elif(abyssCount == 225):
		if(abyssChild.getP1().getX() < winWidth + 48):
			abyssChild.move(8, 0)
		else:
			abyssCount += 1
	elif(abyssCount == 226):
		time.sleep(3)
		abyssCount += 1
	elif(abyssCount == 227):
		undrawAbyssMap()
		undrawAndroid(abyssPlayer)
		abyssCover.setFill("white")
		abyssCover.setOutline("white")
		abyssCount += 1
	elif(abyssCount == 228):
		time.sleep(2)
		titleAbyss.draw(win)
		time.sleep(2)
		underTitleTextAbyss.draw(win)
		time.sleep(4)
		closeGame()


	return currentTrial

def abyssIncrementShakingRate():
	global abyssPlayerShakingRate
	abyssPlayerShakingRate += 1

def	abyssPlayerShakeUpdate():
	if(not abyssPlayerShaking):	return
	global abyssPlayerShakingDirection
	global abyssPlayerShakingCount

	abyssPlayerShakingCount += 1
	if(abyssPlayerShakingCount % 2 == 0):
		abyssPlayerShakingDirection = not abyssPlayerShakingDirection

	if(abyssPlayerShakingDirection):
		moveAndroid(abyssPlayer, abyssPlayerShakingRate, 0)
	else:
		moveAndroid(abyssPlayer, -abyssPlayerShakingRate, 0)


def makePlayerShake():
	global abyssPlayerShaking
	abyssPlayerShaking = True


def showChoice(win):
	drawGuiBox(win)
	comp = getGuiComponents()
	comp[3].setText("Eat")
	comp[4].setText("Do Not Eat")

	abyssChoiceArrow.draw(win)

def updateChoiceGui(key):
	global currentChoiceSelection
	if(key == "Up" and not currentChoiceSelection):
		currentChoiceSelection = True
		moveChoiceArrow()

	if(key == "Down" and currentChoiceSelection):
		currentChoiceSelection = False
		moveChoiceArrow()

	if(key == "z" or key == "Return"):
		global abyssCount
		abyssCount += 1

		comp = getGuiComponents()
		comp[3].setText("")
		comp[4].setText("")

		undrawGuiBox()
		abyssChoiceArrow.undraw()
		
def moveChoiceArrow():
	if(currentChoiceSelection):
		abyssChoiceArrow.move(55, -40)
	else:
		abyssChoiceArrow.move(-55, 40)

def checkAbyssKeys(key):
	if(key == "Up"):	moveAbyssPlayer(0, -12)
	if(key == "Down"):	moveAbyssPlayer(0, 12)
	if(key == "Left"):	moveAbyssPlayer(-12, 0)
	if(key == "Right"):	moveAbyssPlayer(12, 0)

def abyssInit(win):
	global abyssCoverDrawn
	if(not abyssCoverDrawn):
		abyssCover.setFill("black")
		abyssCover.draw(win)
		abyssCoverDrawn = True

	abyssChoiceArrow.setFill("red")
	#abyssChoiceArrow.move(385, winHeight - 55)
	abyssChoiceArrow.move(440, winHeight - 95)

	titleAbyss.setSize(36)
	titleAbyss.setFill("black")

	underTitleTextAbyss.setSize(12)
	underTitleTextAbyss.setFill("black")

def moveAbyssPlayer(x, y):
	global abyssPlayerX
	global abyssPlayerY

	if(y < 0):
		playerDirection = 0
	elif(y > 0):
		playerDirection = 3

	if(x < 0):
		playerDirection = 1
	elif(x > 0):
		playerDirection = 2

	changeAndroidDirection(abyssPlayer, playerDirection)

	#Collision detection for the tunnel bit
	if(abyssPlayerX + x > winWidth * 2 - 48):	return
	if(abyssPlayerY + y < tileSize * 6):	return
	if(abyssPlayerY + y > tileSize * 9 - 48):	return

	abyssPlayerX += x
	abyssPlayerY += y

	moveAbyssMap(-x, -y)

def moveAbyssMap(x, y):
	for i in tileDetails:
		i.move(x, y)

def undrawAbyssMap():
	for i in tileDetails:
		i.undraw()

def drawAbyssMap(win):
	for i in tileDetails:
		i.draw(win)

def createAbyssMap():
	back = Rectangle(Point(0, 6 * 48), Point(2 * tileWinWidth * tileSize, 9 * 48))
	back.setFill("#C7EBFB")
	back.setOutline("#C7EBFB")
	tileDetails.append(back)
	for y in range(6, 9):
		for x in range(tileWinWidth * 2):
			addAbyssTile(x * tileSize, y * tileSize)

def addAbyssTile(x, y):
	for i in range(10):
		xx = grassValues[i * 2]
		yy = grassValues[(i * 2) + 1]
		spec = Rectangle(Point(xx + x, yy + y), Point(xx + x + 2, yy + y + 1))
		spec.setFill("#7E959E")
		spec.setOutline("#7E959E")
		tileDetails.append(spec)
