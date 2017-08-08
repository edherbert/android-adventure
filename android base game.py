#-------------------------------------------------------------------------------
# android.py - in-class demonstration of program design
# Use the arrow keys to move. Collect all the red apples to win. 
# Game over if you hit a black apple or an edge of the play area.
#-------------------------------------------------------------------------------

from graphics import *

def getInputs():
    numberRed = eval(input("Enter number of red apples: "))
    numberBlack = eval(input("Enter number of black apples: "))
    return numberRed, numberBlack

def drawAndroid(win):
    head = Circle(Point(0.5, 0.5), 0.03)
    body = Rectangle(Point(0.47, 0.45), Point(0.53, 0.5))
    leg1 = Rectangle(Point(0.48, 0.42), Point(0.49, 0.45))
    leg2 = Rectangle(Point(0.52, 0.42), Point(0.51, 0.45))
    arm1 = Rectangle(Point(0.53, 0.46), Point(0.54, 0.5))
    arm2 = Rectangle(Point(0.46, 0.46), Point(0.47, 0.5))
    eye1 = Circle(Point(0.49, 0.51), 0.005)
    eye2 = Circle(Point(0.51, 0.51), 0.005)
    android = [head, body, leg1, leg2, arm1, arm2, eye1, eye2]
    for part in android:
        if part == eye1 or part == eye2:
            colour = "white"
        else:
            colour = "green"
        part.setFill(colour)
        part.setOutline(colour)
        part.draw(win)
    return android

def drawApples(win, colour, numberOfApples):
    from random import random
    apples = []
    for i in range(numberOfApples):
        x = random()
        y = random()
        apple = Circle(Point(x, y), 0.02) 
        apple.setFill(colour)
        apple.setOutline(colour)
        apple.draw(win)
        apples.append(apple)
    return apples
        
def drawScene(numberRed, numberBlack):
    win = GraphWin("Android", 500, 500)
    win.setCoords(0, 0, 1, 1)
    android = drawAndroid(win)
    redApples = drawApples(win, "red", numberRed)
    blackApples = drawApples(win, "black", numberBlack)  
    return win, android, redApples, blackApples 

def playGame(win, android, redApples, blackApples):
    won = False
    lost = False
    speedX = 0
    speedY = 0
    speedChange = 0.00001
    while not won and not lost:
        
        # handle speed change
        key = win.checkKey()
        if key == "Left":
            speedX = speedX - speedChange
        elif key == "Right":
            speedX = speedX + speedChange
        elif key == "Down":
            speedY = speedY - speedChange
        elif key == "Up":
            speedY = speedY + speedChange
                
        # move android
        for part in android:
            part.move(speedX, speedY)
         
        # test whether crashed into edge
        androidCentre = android[0].getCenter() 
        if androidCentre.getX() < 0 or androidCentre.getX() > 1 or \
           androidCentre.getY() < 0 or androidCentre.getY() > 1:
            lost = True
            
        # test whether hit black apple
        for black in blackApples:
            if distanceBetweenPoints(black.getCenter(), androidCentre) < 0.02:
                lost = True
      
        # test whether hit red apple
        for red in redApples:
            if distanceBetweenPoints(red.getCenter(), androidCentre) < 0.02:
                red.undraw()
                redApples.remove(red)
        
        # test whether won
        if len(redApples) == 0:
            won = True
         
    message = Text(Point(0.5, 0.5), "")
    message.setSize(20)
    if won:
        message.setText("You've won!")
    else:
        message.setText("Game over!")
    message.draw(win)
        
def distanceBetweenPoints(p1, p2):
    import math
    return math.sqrt((p1.getX() - p2.getX()) ** 2 + 
                     (p1.getY() - p2.getY()) ** 2)
    
def main():
    numberRed, numberBlack = getInputs()
    win, android, redApples, blackApples = drawScene(numberRed, numberBlack)
    playGame(win, android, redApples, blackApples)
    
main()