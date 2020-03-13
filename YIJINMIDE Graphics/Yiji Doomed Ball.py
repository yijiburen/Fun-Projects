from tkinter import *
from time import *
from random import *
wide = int(input("Input width of screen: "))
tall = int(input("Input height of screen: "))
myInterface = Tk()
s = Canvas(myInterface, width=wide, height=tall, background="black")
s.pack()
x = wide
y = tall
ballx = randint(0,wide)
bally = randint(0,tall)
speedx = 5
speedy = 5
f = 0
while x > 0 and y > 0:
    f = f + 1
    x = wide - 0.5 *f
    y = tall - 0.5 *f
    ballx = ballx + speedx
    bally = bally + speedy
    if x > 10 and y > 10:    
        if ballx >= x - 10:
            speedx = speedx * -1
            ballx = x - 10
        if ballx <= 10:
            speedx = speedx * -1
            ballx = 10
        if bally >= y - 10:
            speedy = speedy * -1
            bally = y - 10
        if bally <= 10:
            speedy = speedy * -1
            bally =  10
        line1 = s.create_line(x,0,x,y,fill = "blue")
        line2 = s.create_line(0,y,x,y,fill = "blue")
        ball = s.create_oval(ballx-10,bally-10,ballx+10,bally+10,fill = "red")
        s.update()
        sleep(.005)
        s.delete(line1,line2,ball)
    else:
        line1 = s.create_line(x,0,x,y,fill = "blue")
        line2 = s.create_line(0,y,x,y,fill = "blue")
        s.update()
        sleep(.005)
        s.delete(line1,line2)
