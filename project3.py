#Project3.py
#Jinyang Wang
#This project is to create a game called Boiler Gold
# Hunt where the player has to search for a
# single gold Circle hidden within a 15 x 15 grid of black Circles with a radius of 15.

from time import sleep
from graphics import *
import random

#DrawControl function is used to draw a control panel, which will return the control panel and user's name box
def drawControl():
    win = GraphWin("Game Control", 250,400)
    win.setBackground("light grey")
    tittleBox = Rectangle(Point(0,0),Point(250,30))
    tittleBox.setFill("Black")
    tittleBox.draw(win)
#gold Tittle
    tittle1 = Text(Point(win.getWidth()/2,15), "BOILER GOLD HUNT!")
    tittle1.setFace("arial")
    tittle1.setSize(12)
    tittle1.setStyle("bold")
    tittle1.setTextColor("gold")
    tittle1.draw(win)
#black tittle   
    tittle2 = Text(Point(win.getWidth()/2,50), "PLAYER NAME")
    tittle2.setFace("arial")
    tittle2.setSize(12)
    tittle2.setTextColor("black")
    tittle2.setStyle("bold")
    tittle2.draw(win)

# Exit button
    list
    exitBox = Rectangle(Point(190,320),Point(240,390))
    exitBox.setFill("Black")
    exitBox.draw(win)
    exit_tittle = Text(Point(215,355), "EXIT")
    exit_tittle.setFace("arial")
    exit_tittle.setSize(12)
    exit_tittle.setTextColor("white")
    exit_tittle.setStyle("bold")
    exit_tittle.draw(win)
# Start box

    startBox = Rectangle(Point(10,320),Point(120,390))
    startBox.setFill("gold")
    startBox.draw(win)
    start_tittle = Text(Point(65,355), "NEW GAME")
    start_tittle.setFace("arial")
    start_tittle.setSize(12)
    start_tittle.setTextColor("black")
    start_tittle.setStyle("bold")
    start_tittle.draw(win)
    
    name = Entry(Point(win.getWidth()/2,90), 10)
    name.setFill("white")
    name.setSize(15)
    name.draw(win)

    tittle3 = Text(Point(win.getWidth()/2,120), "TOP SCORES")
    tittle3.setFace("arial")
    tittle3.setSize(12)
    tittle3.setStyle("bold")
    tittle3.setTextColor("black")
    tittle3.draw(win)
    
    
    return [win,name,exitBox,startBox]
#return the Player Name, New Game,
# Exit and Game Control Graphics window objects. 
#This function will interact with users to
# decide to start new game or quit

def Control(win,name):
#name box

   

#start or end
    cx,cy = 0,0
    
    click =win.checkMouse()
    try:    
        cx,cy = click.getX(),click.getY()
    except: pass
    RecordName = str(name.getText())
# If the name is empty, cannot start the game
    if cx <= 120 and cx >= 10 and cy <=390 and cy >= 320:
        if RecordName.isspace() or  RecordName == "":
            return 2
        else :
            return RecordName
    elif cx <= 240 and cx >= 190 and cy <=390 and cy >= 320:
        return 0
    else: return 2
        
#This function will Draw the game window, and return the window object
def GameBackground():
    win = GraphWin("GoldHunt", 480,520,autoflush = True)
    win.setBackground("white")
    tittleBox = Rectangle(Point(0,0),Point(480,40))
    tittleBox.setFill("Black")
    tittleBox.draw(win)
#Round tittle
    
    RoundTittle = Text(Point(50,20), "Round: ")
    RoundTittle.setFace("arial")
    RoundTittle.setSize(10)
    RoundTittle.setTextColor("gold")
    RoundTittle.draw(win)
    RoundTittle.setStyle("bold")
#Score tittle
    
    ClickTittle = Text(Point(430,20), "Clicks: ")
    ClickTittle.setFace("arial")
    ClickTittle.setSize(10)
    ClickTittle.setTextColor("gold")
    ClickTittle.draw(win)
    ClickTittle.setStyle("bold")

#Round, Clicks and GoldHunt Graphics window objects
    return [win,tittleBox,ClickTittle]

#This function will draw the balls, use random method to decide the hidden color,
# and it will also put the user name in to game panel,
# it will return list 0f ball object and the hidden colors for each ball

def make(NameTittle,GameWin):
    colors = "black"
    balls = []
    row = []
    bx = 30
    by = 70

#Set the "gold" to a random ball
    goldX = int(random.uniform(0, 14))
    goldY = int(random.uniform(0, 14))
    for i in range(15):
        for j in range (15):
            center = Point(bx,by)
            
#Set tan and grey color to near by balls, and white color to the rest.
            judge0 =  (i == goldY and j == goldX)
            judge1 = (i == goldY or i == goldY + 1 or i == goldY-1) and \
                     (j == goldX or j == goldX + 1 or j == goldX-1)and\
                         not (i == goldY and j == goldX)
            judge2 = (i == goldY or i == goldY + 1 or i == goldY-1 or i == goldY-2 or \
                      i == goldY+2) and (j == goldX or j == goldX + 1 or j == goldX-1 or \
                                         j == goldX-2 or j == goldX+2)
            if judge0:
                ball = [Circle(center,15), "gold"]
            elif judge1 and not judge0:
                ball = [Circle(center,15), "tan"]
            elif judge2 and not judge1 and not judge0:
                ball = [Circle(center,15), "grey"]
            else: ball = [Circle(center,15), "white"]

            row.append(ball)
            bx += 30
            ball[0].setFill("black")
        balls.append(row)
        bx = 30
        row = []
        by += 30

    redX = goldX
    redY = goldY
    while redX == goldX and redY == goldY:
        redX = int(random.uniform(0, 14))
        redY = int(random.uniform(0, 14))
    balls[redY][redX][1] = "red"
        
#Draw balls

    try:
        NameTittle.draw(GameWin)
        NameTittle.setStyle("bold")
    except:pass
    
    for i in range (15):
        for j in range(15):
            balls[i][j][0].draw(GameWin)
    return balls


#This function will return which ball is clicked by user,
# and return the coordinate of the ball, if no ball has been
# clicked, it will return -1

def ClickCheck(click,balls):
    if click == None:
        return -1
    
        
    try:
        for i in range (15):
            for j in range(15):
                bx,by = balls[i][j][0].getCenter().getX(), balls[i][j][0].getCenter().getY()
                cx,cy = click.getX(),click.getY()
                if ((bx-cx)**2+(by-cy)**2)**.5 < 15:
                    return [i,j]
    except: pass
    return -1

#This function will wash off all ball objects, so that a new round can start.

def WashBalls(balls):
    try:
        for i in range (15):
            for j in range(15):
                #if balls[i][j][1] != "gold":
                balls[i][j][0].undraw()
    except: pass

#This function will wash off old user's name and get the name of the new user.
    
def Initialize(GameWin,name,NameTittle):
    
    try:
        NameTittle.undraw()
            
    except:pass
    
    NameTittle = Text(Point(GameWin.getWidth()/2,20), "Player: " + str(name))
    NameTittle.setFace("arial")
    NameTittle.setSize(10)
    NameTittle.setTextColor("gold")
    NameTittle.setStyle("bold")

    return NameTittle

#These two functions will wash off old round
# and click numbers, then set new numbers

def RoundTittle(GameWin,Round,RoundCount):
    try:
        Round.undraw()
    except: pass   
    Round = Text(Point(80,20), str(RoundCount))
    Round.setFace("arial")
    Round.setSize(10)
    Round.setTextColor("gold")
    Round.setStyle("bold")
    Round.draw(GameWin)
    
    return Round
    
def scoreTittle(GameWin,score,ClickCount):
    try: 
        score.undraw()
    except: pass
    score = Text(Point(460,20), str(ClickCount))
    score.setFace("arial")
    score.setSize(10)
    score.setTextColor("gold")
    score.setStyle("bold")
    score.draw(GameWin)
    
    return score


def bounce(ball,dx,dy):         # Function 'bounces' ball off wall
    center=ball.getCenter()     # get center of ball
    if center.getX() not in range(15,475):   # within window?
        dx *= -1                            # change direction
    if center.getY() not in range(55,515):
        dy *= -1
    return dx,dy                            # return new values

# This function will decide whether the click is in the goldball
def inGold(click,goldball):
    if click == None:
        return False
    x = click.getX()
    y = click.getY()

    bx = goldball.getCenter().getX()
    by = goldball.getCenter().getY()
    r = goldball.getRadius()
    if bx - r <= x <= bx + r and by - r <= y <= by + r:
        return True
    else:
        return False


    
def sortScore(List):
    return List[1]


def topScore(win):
    topscoreList = []
    scoreObList = []
    
    i = 0
    file = open("scores.txt","r")
    
    for line in file:
        
        
        score = line.split(",")
            
            
        try:
            topscoreList.append([score[0],score[1][:-1]])
            i = i+1
        except:
            pass

    topscoreList.sort(key=sortScore)        
    try:
        topscoreList = topscoreList[0:3]
    
    except:
        pass

    return topscoreList






    
# main function
def main():

# Draw control penal and game penal

    Control_panel = drawControl()
    GameWin = GameBackground()[0]
    
# Initialize the round and score, should be 1 at the beginning.    
    Round = Text(Point(80,20), "0")
    Round.setFace("arial")
    Round.setSize(10)
    Round.setTextColor("gold")
    Round.setStyle("bold")
    Round.draw(GameWin)

            
    score = Text(Point(460,20), "0")
    score.setFace("arial")
    score.setSize(10)
    score.setTextColor("gold")
    score.setStyle("bold")            
    score.draw(GameWin)

# Initialize necessary variables    
    color = "white"
    ClickCount = 0
    RoundCount = 1
    name = 1
    NameTittle = ""
    WinWord1 = "You Win!"
    WinWord2 = "Click here to continue..."
    EndWord = ""
    x = 0
    clicked = []

#show the top scores    
    scoreObList = []
    topscoreList = topScore(Control_panel[0])
    
    for i in range(len(topscoreList)):
        scoreTxt = Text(Point(Control_panel[0].getWidth()/4,140+i*20), topscoreList[i][0])
        scoreTxt.setFace("arial")
        scoreTxt.setSize(10)
        scoreTxt.setTextColor("black")
        scoreTxt.draw(Control_panel[0])

        scoreNm = Text(Point(Control_panel[0].getWidth()*(3/4),140+i*20), topscoreList[i][1])
        scoreNm.setFace("arial")
        scoreNm.setSize(10)
        scoreNm.setTextColor("black")
        scoreNm.draw(Control_panel[0])
                       
        scoreObList.append([scoreTxt,scoreNm])
    
#situation is the variable can be assigned by for content
# 0 - shut down the program
# 1 - the program finished all step
# 2 - halt in the loop
# 3 - initialization successful, game can be start
# user name - restart the program, set this name on the top
# so that will can change the situation to decide what the program will do now

    situation = 2
    balls = 0

    while situation != 0:
        
        if situation != 0 and situation != 2 :
            
# Initialize the game            
            NameTittle = Initialize(GameWin,situation,NameTittle)
            WashBalls(balls)
            
            balls = make(NameTittle,GameWin)
            try:
                EndWord.undraw()
            except: pass
            

            
            situation = 3

        
        
        
        if situation == 3:
# start the game for 5 rounds
            for i in range (5):
                x = x + 1
                Round = RoundTittle(GameWin,Round,RoundCount)
                click = GameWin.checkMouse()
# User need to keep searching until find the "gold"            
                while color != "gold":
                    click = 0
                    
                    click = GameWin.checkMouse()
                    ClickedBall = ClickCheck(click,balls)
                    if ClickedBall != -1:
                        balls[ClickedBall[0]][ClickedBall[1]][0].setFill(balls[ClickedBall[0]][ClickedBall[1]][1])
                        color = balls[ClickedBall[0]][ClickedBall[1]][1]
                        if balls[ClickedBall[0]][ClickedBall[1]][0] not in clicked:
                            if balls[ClickedBall[0]][ClickedBall[1]][1] == "red":
                                ClickCount = ClickCount +5
                            else:
                                ClickCount = ClickCount +1
                        clicked.append(balls[ClickedBall[0]][ClickedBall[1]][0])
                        
                        score = scoreTittle(GameWin,score,ClickCount)
# Monitoring the situation at any part allowes the user to shut down will restart program at any time                         
                    
                    
                    
                    situation = Control(Control_panel[0],Control_panel[1])
                    if situation != 2 and situation != 3:
                        break
                clicked = []
# This nest loop will let all ball objects to drop at the end of each round                    
                if situation == 2 or situation == 3:    
                    while balls[0][14][0].getCenter().getY() < 550:
                        for i in range (15):
                            for j in range(15):
                                if balls[i][j][1] != "gold":
                                    balls[i][j][0].move(0,20)
                                else:
                                    gi = i
                                    gj = j
                                
                        situation = Control(Control_panel[0],Control_panel[1])
                        if situation != 2 and situation != 3:
                            break
                    

                    WashBalls(balls)   
                if situation != 2 and situation != 3:

                    break



# bouncing animation

                dir1 = random.choice([-1,1])
                dir2 = random.choice([-1,1])
                dx = dir1*4
                dy = dir2*6
                gR = 15
                while gR > 0.5:
                    situation = Control(Control_panel[0],Control_panel[1])
                    if situation != 2 and situation != 3:
                        break
                    gX = balls[gi][gj][0].getCenter().getX()
                    gY = balls[gi][gj][0].getCenter().getY()
                    gR = balls[gi][gj][0].getRadius()
                    
                    
                    balls[gi][gj][0].undraw()
                    
                    balls[gi][gj][0] = Circle(Point(gX + dx, gY + dy),gR-0.2)
                    balls[gi][gj][0].setFill("gold")
                    balls[gi][gj][0].draw(GameWin)
                    sleep(0.1)

                    click = GameWin.checkMouse()
                    if inGold(click,balls[gi][gj][0]):
                        ClickCount = ClickCount - 1
                        score = scoreTittle(GameWin,score,ClickCount)
                    
                    dx,dy = bounce(balls[gi][gj][0],dx,dy) 

                WashBalls(balls)
                balls[gi][gj][0].undraw()





                
# show the congratulation to the user at the end of each round                    
                WinWord1Ob = Text(Point(GameWin.getWidth()/2,GameWin.getHeight()/2-15), str(WinWord1))
                WinWord1Ob.setFace("arial")
                WinWord1Ob.setSize(12)
                WinWord1Ob.setTextColor("black")
                WinWord1Ob.setStyle("bold")            
                WinWord1Ob.draw(GameWin)
    
                WinWord2Ob = Text(Point(GameWin.getWidth()/2,GameWin.getHeight()/2+15), str(WinWord2))
                WinWord2Ob.setFace("arial")
                WinWord2Ob.setSize(10)
                WinWord2Ob.setTextColor("black")
                WinWord2Ob.setStyle("italic")            
                WinWord2Ob.draw(GameWin)
                        
# click to continue, but can also shut down and restart                        
                Continue = None
                while Continue == None:
                    if situation != 2 and situation != 3:
                    
                        break
                    
                    Continue = GameWin.checkMouse()
                    situation = Control(Control_panel[0],Control_panel[1])
                    
                    
                        

                WinWord1Ob.undraw()
                WinWord2Ob.undraw()
                
                
                
                    
                if situation != 2 and situation != 3:
                    
                        break
                    
                
                
                
                WashBalls(balls)
                if x != 5:
                    balls =  make(NameTittle,GameWin)
                color = "white"
                RoundCount += 1
                situation = 1

                
            x = 0

# if situation get the order of restart and shut down, this loop will wash off everything and initialize            
        if  situation != 1 and situation != 2 and situation != 3:    
            ClickCount = 0
            color = "white"
            WashBalls(balls)
            RoundCount = 1
            score.undraw()
            Round.undraw()

            Round = Text(Point(80,20), "0")
            Round.setFace("arial")
            Round.setSize(10)
            Round.setTextColor("gold")
            Round.setStyle("bold")
            Round.draw(GameWin)

            
            score = Text(Point(460,20), "0")
            score.setFace("arial")
            score.setSize(10)
            score.setTextColor("gold")
            score.setStyle("bold")            
            score.draw(GameWin)
            
# If situation is 1, which means game has compeleted, so that the score will be recorded, and it will show the top scores on control panel                       
        if situation == 1:
            color = "white"
            Record = open("scores.txt", "a")
            Record.write("{},{}\n".format(NameTittle.getText()[8:],ClickCount))
            Record.close()
            ClickCount = 0
            WashBalls(balls)
            RoundCount = 1
            score.undraw()
            Round.undraw()
            situation = 2
            NameTittle.undraw()

            Round = Text(Point(80,20), "0")
            Round.setFace("arial")
            Round.setSize(10)
            Round.setTextColor("gold")
            Round.setStyle("bold")
            Round.draw(GameWin)

            
            score = Text(Point(460,20), "0")
            score.setFace("arial")
            score.setSize(10)
            score.setTextColor("gold")
            score.setStyle("bold")            
            score.draw(GameWin)

            EndWord = Text(Point(GameWin.getWidth()/2,GameWin.getHeight()/2), "GOOD GAME WELL PLAY")
            EndWord.setFace("arial")
            EndWord.setSize(12)
            EndWord.setTextColor("black")
            EndWord.setStyle("bold")            
            EndWord.draw(GameWin)
            situation = 2

            for i in scoreObList:
                i[0].undraw()
                i[1].undraw()
            topscoreList = topScore(Control_panel[0])
            scoreObList = []
            for i in range(len(topscoreList)):
                scoreTxt = Text(Point(Control_panel[0].getWidth()/4,140+i*20), topscoreList[i][0])
                scoreTxt.setFace("arial")
                scoreTxt.setSize(10)
                scoreTxt.setTextColor("black")
                scoreTxt.draw(Control_panel[0])

                scoreNm = Text(Point(Control_panel[0].getWidth()*(3/4),140+i*20), topscoreList[i][1])
                scoreNm.setFace("arial")
                scoreNm.setSize(10)
                scoreNm.setTextColor("black")
                scoreNm.draw(Control_panel[0])
                       
                scoreObList.append([scoreTxt,scoreNm])
                
            Record.close()    
            
        if situation == 2 or situation == 3 or situation == 1:
            situation = Control(Control_panel[0],Control_panel[1])
        
# Close the windows when "Exit" has been clicked        
    GameWin.close()
    Control_panel[0].close()
    
        
    
       
  
    
        

main()

        




























