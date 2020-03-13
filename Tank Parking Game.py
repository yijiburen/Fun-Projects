#IMPORTS
from tkinter import *
from math import *
from time import *
from random import *

#SET UP
root = Tk()
s = Canvas(root, width=800, height=800)

#SETS INITIAL VALUES
def initial():
    global regen,delay,boxes,xBoxes,word,easy,medium,hard,difficulty,goaly,goalx,q,win,AIstart,AIend,AIhit,start,end,hit,x1Wall,y1Wall,x2Wall,y2Wall,health,healthbar,frames, xMouse,yMouse,speed,xTank,yTank,tankSpeed,r,turret,hull,xSpeed,ySpeed,mouseAngle,bullet,xBullet,yBullet,bulletDirection,bulletSpeed,xTurret,yTurret,AIsize,AIx,AIy,AIbase,AIgun,AIr
    xTank,yTank = 775,775
    speed,xSpeed,ySpeed,bulletSpeed = 3,0,0,3
    AIr,r = 75,50
    xTurret,yTurret,turret,hull = 0,0,0,0
    mouseAngle = 0
    AIbase = [0,0,0,0,0,0,0,0,0,0,0,0]
    AIgun = [0,0,0,0,0,0,0,0,0,0,0,0]
    AIhit = [False,False,False,False,False,False,False,False,False,False,False,False]
    xBullet = []
    yBullet = []
    AIx = [385,215,75,25,345,530,715,randint(100,550),randint(100,550),randint(100,550),randint(100,550),randint(100,550)]
    AIy = [740,575,575,305,405,405,405,randint(50,200),randint(50,200),randint(50,200),randint(50,200),randint(50,200)]
    bullet = []
    bulletDirection = []
    AIsize = 25
    xMouse,yMouse = 0,0
    frames = 0
    health = 3
    healthbar = [0,0,0]
    x1Wall = [730,50,660,460,410,290,50,0,390,50,240,430,610,610]
    y1Wall = [600,530,550,730,660,550,640,260,660,395,330,280,330,80]
    x2Wall = [750,800,680,660,610,310,240,750,410,240,260,450,630,630]
    y2Wall = [800,550,750,750,680,750,660,280,800,415,415,480,530,180]
    hit = False
    end = 0
    start = 0
    AIend = [0,0,0,0,0,0,0,0,0,0,0,0]
    AIstart = [0,0,0,0,0,0,0,0,0,0,0,0]
    q = False
    win = False
    goalx = 30
    goaly = 30
    difficulty = 0
    boxes = [0,0,0]
    xBoxes = [170,260,360]
    word,easy,medium,hard = 0,0,0,0
    delay = 100
    regen = 5

#DRAWS WALLS
def drawWall():
    i = 0
    while i < len(x1Wall):
        s.create_rectangle(x1Wall[i],y1Wall[i],x2Wall[i],y2Wall[i],fill = "black")
        i = i + 1

#DRAWS DIFFICULTY BARS
def drawDifficulty():
    global boxes,word,easy,medium,hard
    s.delete(word,boxes[0],boxes[1],boxes[2],easy,medium,hard)
    word = s.create_text(120,10,text = "DIFFICULTY:", font = "Courier 10")
    i = 0
    while i < 3:
        if i == difficulty:
            colour = "red"
        else:
            colour = "white"
        boxes[i] = s.create_rectangle(xBoxes[i],0,xBoxes[i]+75,20,fill = colour)
        i = i + 1
    easy = s.create_text(200,10,text = "1.EASY",font = "Courier 10")
    medium = s.create_text(300,10,text = "2.MEDIUM",font = "Courier 10")
    hard = s.create_text(400,10,text = "3.HARD",font = "Courier 10")

#DRAWS HEALTH BAR
def drawHealth():
    global healthbar
    healthbar[0] = s.create_rectangle(500,0,550,20,fill = "red")
    healthbar[1] = s.create_rectangle(550,0,600,20,fill = "red")
    healthbar[2] = s.create_rectangle(600,0,650,20,fill = "red")
    s.create_text(470,10,text = "HEALTH:",font = "Courier 10")

#DRAWS GOAL (YELLOW SQUARE)
def drawGoal():
    s.create_rectangle(goalx-25,goaly-25,goalx+25,goaly+25,fill = "yellow")

#SPAWNS BULLET WHEN MOUSE IS CLICKED
def mouseClick( event ):
    global bullet, xBullet, yBullet,bulletDirection
    xBullet.append(xTurret)
    yBullet.append(yTurret)
    bullet.append(0)
    bulletDirection.append(getAngle(yTank,yMouse,xMouse,xTank))

#UPDATES BULLET POSITION
def moveBullet():
    global bullet,xBullet,yBullet,bulletDirection,health,hit,start
    i = 0
    while i < len(bullet):
        j = 0
        #BULLET HITS WALL OR TURRET
        if hitObject(i) == True:
            s.delete(bullet[i])
            xBullet.pop(i)
            yBullet.pop(i)
            bullet.pop(i)
            bulletDirection.pop(i)
        #BULLET GOES OFF SCREEN
        elif xBullet[i] > 850 or xBullet[i] < -50 or yBullet[i] > 850 or yBullet[i] < -50:
            s.delete(bullet[i])
            xBullet.pop(i)
            yBullet.pop(i)
            bullet.pop(i)
            bulletDirection.pop(i)
        #BULLET HITS TANK
        elif sqrt((xBullet[i] - xTank)**2 + (yBullet[i] - yTank)**2) < 25:
            s.delete(bullet[i])
            xBullet.pop(i)
            yBullet.pop(i)
            bullet.pop(i)
            bulletDirection.pop(i)
            health = health - 1
            s.delete(healthbar[health])
            hit = True
            start = time()
            #print("Hit detected on tank")
        #MOVES BULLET
        else:
            xBullet[i] = xBullet[i] + bulletSpeed*sin(radians(bulletDirection[i]))
            yBullet[i] = yBullet[i] + bulletSpeed*cos(radians(bulletDirection[i]))
            s.delete(bullet[i])
            bullet[i] = s.create_oval( xBullet[i]-5,yBullet[i]-5,xBullet[i]+5,yBullet[i]+5,fill="red")
            i = i + 1

#IF BULLET HITS WALL OR TURRET
def hitObject(i):
    global bullet,xBullet,yBullet,bulletDirection,AIhit,AIstart
    j = 0
    k = 0
    while j < len(AIgun):
        if (AIx[j] - AIsize - 5) <= xBullet[i] <= (AIx[j] + AIsize + 5) and (AIy[j] - AIsize - 5) <= yBullet[i] <= (AIy[j] + AIsize + 5):
            #print("Hit detected on turret num", j)
            AIhit[j] = True
            AIstart[j] = time()
            return True
        j = j + 1
    while k < len(x1Wall):
        if (x1Wall[k] - 5) <= xBullet[i] <= (x2Wall[k] + 5) and (y1Wall[k] - 5) <= yBullet[i] <= (y2Wall[k] + 5):
            #print("Hit detected on wall num", k)
            return True
        k = k + 1

#UPDATE AI TURRETS
def moveAI():
    global AIbase, AIgun
    i = 0
    while i < len(AIbase):
        angle = getAngle(AIy[i],yTank,xTank,AIx[i])
        x = AIx[i] + AIr * sin(radians(angle))
        y = AIy[i] + AIr * cos(radians(angle))
        s.delete(AIbase[i], AIgun[i])
        AIend[i] = time()
        #CHECK IF TURRET IS HIT (CHANGE COLOUR)
        if (AIhit[i] == True) or (AIend[i] - AIstart[i]) < regen:
            colour = "red"
        else:
            colour = "blue"
        AIbase[i] = s.create_rectangle(AIx[i]-AIsize,AIy[i]-AIsize,AIx[i]+AIsize,AIy[i]+AIsize,fill = colour)
        AIgun[i] = s.create_line(AIx[i],AIy[i],x,y,width = 15)
        AIhit[i] = False
        i = i + 1
        #SETS DELAY FOR FIRING AND SPAWNS BULLET
        if frames % delay == 0 and colour == "blue":
            xBullet.append(x)
            yBullet.append(y)
            bullet.append(0)
            bulletDirection.append(angle)

#WHEN KEYS ARE PRESSED
def keyDown( event ):
    global xSpeed,ySpeed,q,difficulty,speed,bulletSpeed,regen,delay
    if event.keysym == "w" or event.keysym == "W":
        ySpeed =  -speed
    elif event.keysym == "s" or event.keysym == "S":
        ySpeed =  speed
    elif event.keysym == "a" or event.keysym == "A":
        xSpeed = -speed
    elif event.keysym == "d" or event.keysym == "D":
        xSpeed = speed
    elif event.keysym == "q" or event.keysym == "Q":
        q = True
    elif event.keysym == "1":
        difficulty = 0
        speed,bulletSpeed,regen,delay = 3,3,5,100
    elif event.keysym == "2":
        difficulty = 1
        speed,bulletSpeed,regen,delay = 3,4,4,70
    elif event.keysym == "3":
        difficulty = 2
        speed,bulletSpeed,regen,delay = 4,8,2,30
    elif event.keysym == "r" or event.keysym == "R":
        s.delete("all")
        s.update()
        runGame()
    elif event.keysym == "e" or event.keysym == "E":
        root.destroy()

#WHEN KEYS ARE RELEASED
def keyUpW(event):
    global ySpeed
    ySpeed = 0
def keyUpA(event):
    global xSpeed
    xSpeed = 0
def keyUpS(event):
    global ySpeed
    ySpeed = 0
def keyUpD(event):
    global xSpeed
    xSpeed = 0
def mouseMotion( event ):
    global xMouse, yMouse
    xMouse = event.x
    yMouse = event.y

#UPDATES TANK POSITION
def moveHull():
    global hull,xTank,yTank,turret,hit,end,win
    xTank = xTank + xSpeed
    yTank = yTank + ySpeed
    j = 0
    k = 0
    #CHECK IF GOAL IS REACHED
    if sqrt((goalx - xTank)**2 + (goaly - yTank)**2) < 10:
        win = True
    #PREVENTS TANK FROM GOING OFFSCREEN
    if xTank > 785 or xTank < 15 or yTank > 785 or yTank < 15:
        xTank = xTank - xSpeed
        yTank = yTank - ySpeed
    #CHECKS COLLISION WITH TURRETS
    while j < len(AIgun):
        if (AIx[j] - AIsize - 20) <= xTank <= (AIx[j] + AIsize + 20) and (AIy[j] - AIsize - 20) <= yTank <= (AIy[j] + AIsize + 20):
            #print("Collision with turret num", j)
            xTank = xTank - xSpeed
            yTank = yTank - ySpeed
        j = j + 1
    #CHECKS COLLISION WITH WALLS
    while k < len(x1Wall):
        if (x1Wall[k] - 20) <= xTank <= (x2Wall[k] + 20) and (y1Wall[k] - 20) <= yTank <= (y2Wall[k] + 20):
            #print("Collision with wall num", k)
            xTank = xTank - xSpeed
            yTank = yTank - ySpeed
        k = k + 1
    end = time()
    #CHECK IF TANK IS HIT (CHANGE COLOUR)
    if hit == True or (end - start) < 0.5:
        colour = "red"
    else:
        colour = "white"
    hull = s.create_oval(xTank-20,yTank-20,xTank+20,yTank+20,fill = colour)
    hit = False

#UPDATES TANK TURRET TO FOLLOW MOUSE
def moveTurret():
    global turret,xTurret,yTurret
    mouseAngle = getAngle(yTank,yMouse,xMouse,xTank)
    xTurret = xTank + (r*sin(radians(mouseAngle)))
    yTurret = yTank + (r*cos(radians(mouseAngle)))
    turret = s.create_line(xTank,yTank,xTurret,yTurret,fill = "black",width = 20)

#GETS ANGLE OF TWO POINTS
def getAngle(y1,y2,x2,x1):
    dy = y1 - y2
    dx = x2 - x1
    if dx==0:
        if dy >= 0:
            return 180
        else:
            return 360 
    else:
        radianAngle = atan2(dy,dx)
        return degrees( radianAngle ) + 90

#MAIN
def runGame():
    global turret,hull,frames,gtext
    initial()
    drawWall()
    drawHealth()
    drawGoal()
    #MAIN LOOP
    while (health > 0) and q == False and win == False:
        s.delete(turret,hull)
        drawDifficulty()
        if len(bullet) > 0:
            moveBullet()
        moveTurret()
        moveHull()
        moveAI()
        s.update()
        sleep(0.001)
        frames = frames + 1
    if health < 1:
        gtext = "TANK DESTROYED"
    elif q == True:
        gtext = "YOU QUIT THE GAME"
    else:
        gtext = "YOU WON"
    gameOver()

#GAME OVER ANIMATION
def gameOver():
    x,y = 400,-50
    for f in range(100):
        text1 = s.create_text(x,y,text = gtext,font = "Courier 50",fill = "red")
        text2 = s.create_text(x,y + 50,text = "GAME OVER",font = "Courier 50",fill = "red")
        text3 = s.create_text(x,y + 130,text = "PRESS R TO RESTART OR E TO EXIT",font = "Courier 25",fill = "red")
        y = y + 4
        s.update()
        sleep(0.05)
        if f < 99:
            s.delete(text1,text2,text3)

#SETUP
root.after(0, runGame)
s.bind( "<Button-1>", mouseClick )
s.bind( "<Key>", keyDown)
s.bind( "<KeyRelease-w>", keyUpW)
s.bind( "<KeyRelease-a>", keyUpA)
s.bind( "<KeyRelease-s>", keyUpS)
s.bind( "<KeyRelease-d>", keyUpD)
s.bind( "<Motion>", mouseMotion)

s.focus_set() 
s.pack() 
root.mainloop()
