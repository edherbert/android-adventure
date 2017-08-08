from graphics import *
from map import *
from android import *

def desertInit():
	red = createAndroid("red")
	setAndroidSpeech(red, "This desert is so complicated. I think I'm lost.")
	addAndroid(red, 4 * 48, 7 * 48, 3, 1)

	orange = createAndroid("orange")
	setAndroidSpeech(orange, "Maybe the desert isn't the best place for a first date.")
	addAndroid(orange, 14 * 48, 3 * 48, 1, 1)

	pink = createAndroid("pink")
	setAndroidSpeech(pink, "I love the desert!")
	addAndroid(pink, 15 * 48, 3 * 48, 1, 1)

def desertUpdate():
	pass