from tkinter import *
from time import *
from math import *
from random import *
myInterface = Tk()
s = Canvas(myInterface, width=800, height=800, background="black")
s.pack()
command = int(input("Would you like to etch the standard pattern (1), or a random pattern (2)? "))
while command != 1 and command != 2:
    command = int(input("Invalid input! Would you like to etch the standard pattern (1), or a random pattern (2)? "))
if command == 1:
    r = 1
    p = 1
else:
    r = randint(1,9)
    p = randint(1,9)
s.create_rectangle(150,140,650,670,fill = "blanched almond")
s.create_line(0,400,100,400,width = 100, fill = "sky blue")
s.create_text(50,380,text = "Laser",font = "papyrus 18")
s.create_text(50,420,text = "Etching",font = "papyrus 18")
l = [400,400]
for f in range(0,400):
    x = 400 + 0.5*f*sin( 0.1*r*f)
    y = 400 + 0.5*f*cos( 0.1*p*f)
    l.append(x)
    l.append(y)
    laser = s.create_line(x, y, 100, 400, fill= "red", width=1)
    line = s.create_line(l,fill = "black",smooth = True)
    s.update()
    if f < 399:
        s.delete(laser,line)
    else:
        s.delete(laser)
    sleep(0.03)
