from tkinter import *
from time import *
from random import *
myInterface = Tk()
s = Canvas(myInterface, width= 800, height= 800, background="black")
s.pack()
x1 = 400
y1 = 400
num = 0
for f in range(1,159):
    num = num + 1
    if num == 1:
        x2 = x1 + 5*f
        y2 = y1
        s.create_line(x1,y1,x2,y2,fill = "yellow")
    elif num == 2:
        x2 = x1
        y2 = y1 - 5*f
        s.create_line(x1,y1,x2,y2,fill = "blue")
    elif num == 3:
        x2 = x1 - 5*f
        y2 = y1
        s.create_line(x1,y1,x2,y2,fill = "red")
    else:
        x2 = x1
        y2 = y1 + 5*f
        s.create_line(x1,y1,x2,y2,fill = "green")
        num = 0
    x1 = x2
    y1 = y2
    s.update()
    sleep(0.05)
