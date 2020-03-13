from tkinter import *
from time import *
from math import *
from random import *
import winsound
myInterface = Tk()
s = Canvas(myInterface, width=800, height=800, background="black")
s.pack()
r = 255
g = 0
b = 0
winsound.PlaySound("Jauz_and_Ephwurd_-_Rock_The_Party_Original_Mix_",winsound.SND_ASYNC)
alfonso = []
snoop = []
drake = []
for q in range(0,113,2):
    pic = "dance1/tmp-" + str(q)+".gif"
    alfonso.append(PhotoImage(file = pic))

for q in range(0,57,2):
    pic = "dance2/tmp-" + str(q)+"_50.gif"
    snoop.append(PhotoImage(file = pic))

for q in range(0,26,2):
    pic = "dance3/tmp-" + str(q)+".gif"
    drake.append(PhotoImage(file = pic))
s.create_rectangle(0,0,800,150,fill="grey10")
s.create_rectangle(0,600,800,800,fill = "grey10")
s.create_polygon(0,600,50,500,750,500,800,600, fill = "grey10")
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
xd = []
yd = []
zxc1 = []
zxc2= []
zxc3 = []
pp = []
p = []
y4 = []
y5 = []
y6 = []
num = 20
for q in range(num):
    pp.append(randint(1,9))
    p.append(randint(1,9))
    x1.append(randint(0,800))
    m =randint(600,800)
    y1.append(m)
    x2.append(randint(0,800))
    n =randint(600,800)
    y2.append(n)
    x3.append(randint(0,800))
    b = randint(600,800)
    y3.append(b)
    y4.append(m)
    y5.append(n)
    y6.append(b)
    zxc1.append(0)
    zxc2.append(0)
    zxc3.append(0)
    xd.append(0)
    yd.append(0)
f = 0
def colour(c):
    section = int(c / 255) % 6
    secnum = c % 255   
    if section == 0 or section == 6:
        r = str(hex(255))
        g = str(hex(0))
        b = str(hex(secnum))
    elif section == 1:
        r = str(hex(255 - secnum))
        g =str(hex(0))
        b =str(hex(255))
    elif section == 2:
        r =str(hex(0))
        g =str(hex(secnum))
        b =str(hex(255))
    elif section == 3:
        r =str(hex(0))
        g =str(hex(255))
        b =str(hex(255-secnum))
    elif section == 4:
        r = str(hex(secnum))
        g =str(hex(255))
        b =str(hex(0))
    else:
        r =str(hex(255))
        g =str(hex(255 - secnum))
        b =str(hex(0))
    if len(r) <4:
        r = "0" + r[-1:]
    if len(g) <4:
        g = "0" + g[-1:]
    if len(b) <4:
        b = "0" + b[-1:]
    return("#"+r[-2:]+g[-2:]+b[-2:])
while True:
    for f in range(f,f + 100):
        s.configure(background = colour(5*f))
        dance1 = s.create_image(400,420,image = alfonso[f%len(alfonso)])
        dance2 = s.create_image(200,400,image = snoop[f%len(snoop)])
        dance3 = s.create_image(600,400,image = drake[f%len(drake)])
        for i in range(num):
            xd[i] = 30*sin(pp[i]*0.1*f)
            yd[i] = 30*cos(p[i]*0.1*f)
            zxc1[i] = s.create_line(x1[i]+xd[i], y1[i]+yd[i], 100, 100, fill= colour(2*f), width=1)
            zxc2[i] = s.create_line(x2[i]+xd[i], y2[i]+yd[i], 400, 100, fill= colour(2*f), width=1)
            zxc3[i] = s.create_line(x3[i]+xd[i], y3[i]+yd[i], 700, 100, fill= colour(2*f), width=1)
        s.update()
        sleep(0.05)
        s.delete(dance1,dance2,dance3)
        for i in range(num):
            s.delete(zxc1[i],zxc2[i],zxc3[i])
    for f in range(f,f + 25):
        s.configure(background = colour(5*f))
        dance1 = s.create_image(400,420,image = alfonso[f%len(alfonso)])
        dance2 = s.create_image(200,400,image = snoop[f%len(snoop)])
        dance3 = s.create_image(600,400,image = drake[f%len(drake)])
        for i in range(num):
            if y1[i]+yd[i] < 900:
                y1[i] = y1[i] + 15
            if y2[i]+yd[i] < 900:
                y2[i] = y2[i] + 15
            if y3[i]+yd[i] < 900:
                y3[i] = y3[i] + 15
            zxc1[i] = s.create_line(x1[i]+xd[i], y1[i]+yd[i], 100, 100, fill= colour(2*f), width=1)
            zxc2[i] = s.create_line(x2[i]+xd[i], y2[i]+yd[i], 400, 100, fill= colour(2*f), width=1)
            zxc3[i] = s.create_line(x3[i]+xd[i], y3[i]+yd[i], 700, 100, fill= colour(2*f), width=1)
        s.update()
        sleep(0.05)
        s.delete(dance1,dance2,dance3)
        for i in range(num):
            s.delete(zxc1[i],zxc2[i],zxc3[i])
    for f in range(f,f + 100):
        s.configure(background = colour(5*f))
        dance1 = s.create_image(400,420,image = alfonso[f%len(alfonso)])
        dance2 = s.create_image(200,400,image = snoop[f%len(snoop)])
        dance3 = s.create_image(600,400,image = drake[f%len(drake)])
        for i in range(num):
            if y1[i]+yd[i] > -200:
                y1[i] = y1[i] -10
            if y2[i]+yd[i] > -200:
                y2[i] = y2[i] -10
            if y3[i]+yd[i] > -200:
                y3[i] = y3[i] -10
            zxc1[i] = s.create_line(x1[i]+xd[i], y1[i]+yd[i], 100, 100, fill= colour(2*f), width=1)
            zxc2[i] = s.create_line(x2[i]+xd[i], y2[i]+yd[i], 400, 100, fill= colour(2*f), width=1)
            zxc3[i] = s.create_line(x3[i]+xd[i], y3[i]+yd[i], 700, 100, fill= colour(2*f), width=1)
        s.update()
        sleep(0.05)
        s.delete(dance1,dance2,dance3)
        for i in range(num):
            s.delete(zxc1[i],zxc2[i],zxc3[i])
    for f in range(f,f + 100):
        s.configure(background = colour(5*f))
        dance1 = s.create_image(400,420,image = alfonso[f%len(alfonso)])
        dance2 = s.create_image(200,400,image = snoop[f%len(snoop)])
        dance3 = s.create_image(600,400,image = drake[f%len(drake)])
        for i in range(num):
            if y1[i]+yd[i] < 900:
                y1[i] = y1[i] +10
            if y2[i]+yd[i] < 900:
                y2[i] = y2[i] +10
            if y3[i]+yd[i] < 900:
                y3[i] = y3[i] +10
            zxc1[i] = s.create_line(x1[i]+xd[i], y1[i]+yd[i], 100, 100, fill= colour(2*f), width=1)
            zxc2[i] = s.create_line(x2[i]+xd[i], y2[i]+yd[i], 400, 100, fill= colour(2*f), width=1)
            zxc3[i] = s.create_line(x3[i]+xd[i], y3[i]+yd[i], 700, 100, fill= colour(2*f), width=1)
        s.update()
        sleep(0.05)
        s.delete(dance1,dance2,dance3)
        for i in range(num):
            s.delete(zxc1[i],zxc2[i],zxc3[i])
    for f in range(f,f + 25):
        s.configure(background = colour(5*f))
        dance1 = s.create_image(400,420,image = alfonso[f%len(alfonso)])
        dance2 = s.create_image(200,400,image = snoop[f%len(snoop)])
        dance3 = s.create_image(600,400,image = drake[f%len(drake)])
        for i in range(num):
            if y1[i]+yd[i] > y4[i]:
                y1[i] = y1[i] -15
            if y2[i]+yd[i] > y5[i]:
                y2[i] = y2[i] -15
            if y3[i]+yd[i] > y6[i]:
                y3[i] = y3[i] -15
            zxc1[i] = s.create_line(x1[i]+xd[i], y1[i]+yd[i], 100, 100, fill= colour(2*f), width=1)
            zxc2[i] = s.create_line(x2[i]+xd[i], y2[i]+yd[i], 400, 100, fill= colour(2*f), width=1)
            zxc3[i] = s.create_line(x3[i]+xd[i], y3[i]+yd[i], 700, 100, fill= colour(2*f), width=1)
        s.update()
        sleep(0.05)
        s.delete(dance1,dance2,dance3)
        for i in range(num):
            s.delete(zxc1[i],zxc2[i],zxc3[i])

