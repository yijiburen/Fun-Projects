from tkinter import *
myInterface = Tk()
s = Canvas(myInterface, width=800, height=800, background="black")
s.pack()
x1 = 10
y1 = 300
x2 = 600
y2 = 10
x3 = 700
y3 = 790
num = int(input("How many triangles would you like to see? "))
for q in range(0,num):
    if q % 2 == 0:
        color = "blue"
    else:
        color = "red"
    s.create_polygon(x1,y1,x2,y2,x3,y3,fill = color)
    z = x1
    a = y1
    x1 = (x1 + x2) /2
    y1 = (y1 + y2) /2
    x2 = (x2 + x3) /2
    y2 = (y2 + y3) /2
    x3 = (x3 + z) /2
    y3 = (y3 + a) /2
