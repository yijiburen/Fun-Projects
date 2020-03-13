from tkinter import *
from random import *
#Prep
grassColours = ["dark olive green","yellow green", "dark green","forest green","dark olive green"]
desertColours = ["khaki","khaki","dark khaki","khaki2","khaki3","black"]
snowColours = ["snow","ghost white","white smoke","ivory","gray85","gray84"]
skinColours = ["saddle brown","moccasin","peach puff", "sandy brown", "peru", "light goldenrod","navajo white","bisque","blanched almond"]
#Theme
theme = choice([1,2,3])
if theme == 1:
    myInterface = Tk()
    screen = Canvas(myInterface, width=700, height=800, background="dark olive green")
    screen.pack()
    #Hill and Sky
    p1 = randint(150,250)
    p2 = randint(150,250)
    p3 = randint(150,250)
    p4 = randint(150,250)
    p5 = randint(150,250)
    p6 = randint(150,250)
    for g3 in range(1,100001):
        grass = choice(grassColours)
        x = randint(0,700)
        y = randint(150,310)
        x2 = randint(x - 1,x + 1)
        screen.create_line(x,y,x2,y - 5, fill = grass)
    for g4 in range(100000):
        grass = choice(grassColours)
        x = randint(0,700)
        y = randint(300,500)
        x2 = randint(x - 2,x + 2)
        screen.create_line(x,y,x2,y - 8, fill = grass)
    screen.create_polygon(-100,300,0,p1,140,p2,280,p3,420,p4,560,p5,700,p6,800,300,1000,-100,-300,-100,smooth = True,fill = "sky blue")
    #Sun
    screen.create_oval(450,50,500,100,fill = "yellow")
    #Soldiers
    for s in range(1,6):
        skin = choice(skinColours)
        x = randint(0,140)
        m = (p2-p1)/140
        b = p1 - m * x
        eq = int(m * x + b)
        y = randint(eq,300)
        helmet = screen.create_polygon(x-7,y-9,x-6,y-15,x,y-17,x+6,y-15,x+7,y-9,fill = "forest green",outline = "black")
        face = screen.create_polygon(x-6,y-9,x-4,y-2,x,y,x+4,y-2,x+6,y-9,fill = skin,outline = "black")
        eye1 = screen.create_oval(x-4,y-8,x-1,y-6,fill = "black")
        eye2 = screen.create_oval(x+4,y-8,x+1,y-6,fill = "black")
        top = screen.create_polygon(x-6,y+1,x-5,y+4,x-5,y+17,x,y+18,x+5,y+17,x+5,y+8,x+10,y+10,x+6,y+1,x,y,fill = "forest green",outline = "black")
        gun = screen.create_polygon(x-10,y+9,x-9,y+15,x+2,y+12,x+4,y+17,x+8,y+16,x+7,y+12,x+24,y+11,x+24,y+9,fill = "black")
        arm = screen.create_polygon(x-6,y+1,x-10,y+9,x-4,y+16,x-2,y+12,x-6,y+8,x-5,y+4,fill = "forest green",outline = "black")
        legs = screen.create_polygon(x-5,y+17,x-7,y+32,x-2,y+33,x,y+18,x+2,y+33,x+7,y+32,x+5,y+17,x,y+18,fill = "forest green",outline = "black")
        boot1 = screen.create_polygon(x-7,y+32,x-11,y+36,x-2,y+36,x-2,y+33,fill = "black")
        boot2 = screen.create_polygon(x+7,y+32,x+11,y+36,x+2,y+36,x+2,y+33, fill = "black")
    for s in range(1,6):
        skin = choice(skinColours)
        x = randint(140,280)
        m = (p3-p2)/140
        b = p2 - m * x
        eq = int(m * x + b)
        y = randint(eq,300)
        helmet = screen.create_polygon(x-7,y-9,x-6,y-15,x,y-17,x+6,y-15,x+7,y-9,fill = "forest green",outline = "black")
        face = screen.create_polygon(x-6,y-9,x-4,y-2,x,y,x+4,y-2,x+6,y-9,fill = skin,outline = "black")
        eye1 = screen.create_oval(x-4,y-8,x-1,y-6,fill = "black")
        eye2 = screen.create_oval(x+4,y-8,x+1,y-6,fill = "black")
        top = screen.create_polygon(x-6,y+1,x-5,y+4,x-5,y+17,x,y+18,x+5,y+17,x+5,y+8,x+10,y+10,x+6,y+1,x,y,fill = "forest green",outline = "black")
        gun = screen.create_polygon(x-10,y+9,x-9,y+15,x+2,y+12,x+4,y+17,x+8,y+16,x+7,y+12,x+24,y+11,x+24,y+9,fill = "black")
        arm = screen.create_polygon(x-6,y+1,x-10,y+9,x-4,y+16,x-2,y+12,x-6,y+8,x-5,y+4,fill = "forest green",outline = "black")
        legs = screen.create_polygon(x-5,y+17,x-7,y+32,x-2,y+33,x,y+18,x+2,y+33,x+7,y+32,x+5,y+17,x,y+18,fill = "forest green",outline = "black")
        boot1 = screen.create_polygon(x-7,y+32,x-11,y+36,x-2,y+36,x-2,y+33,fill = "black")
        boot2 = screen.create_polygon(x+7,y+32,x+11,y+36,x+2,y+36,x+2,y+33, fill = "black")
    for s in range(1,6):
        skin = choice(skinColours)
        x = randint(280,420)
        m = (p4-p3)/140
        b = p3 - m * x
        eq = int(m * x + b)
        y = randint(eq,300)
        helmet = screen.create_polygon(x-7,y-9,x-6,y-15,x,y-17,x+6,y-15,x+7,y-9,fill = "forest green",outline = "black")
        face = screen.create_polygon(x-6,y-9,x-4,y-2,x,y,x+4,y-2,x+6,y-9,fill = skin,outline = "black")
        eye1 = screen.create_oval(x-4,y-8,x-1,y-6,fill = "black")
        eye2 = screen.create_oval(x+4,y-8,x+1,y-6,fill = "black")
        top = screen.create_polygon(x-6,y+1,x-5,y+4,x-5,y+17,x,y+18,x+5,y+17,x+5,y+8,x+10,y+10,x+6,y+1,x,y,fill = "forest green",outline = "black")
        gun = screen.create_polygon(x-10,y+9,x-9,y+15,x+2,y+12,x+4,y+17,x+8,y+16,x+7,y+12,x+24,y+11,x+24,y+9,fill = "black")
        arm = screen.create_polygon(x-6,y+1,x-10,y+9,x-4,y+16,x-2,y+12,x-6,y+8,x-5,y+4,fill = "forest green",outline = "black")
        legs = screen.create_polygon(x-5,y+17,x-7,y+32,x-2,y+33,x,y+18,x+2,y+33,x+7,y+32,x+5,y+17,x,y+18,fill = "forest green",outline = "black")
        boot1 = screen.create_polygon(x-7,y+32,x-11,y+36,x-2,y+36,x-2,y+33,fill = "black")
        boot2 = screen.create_polygon(x+7,y+32,x+11,y+36,x+2,y+36,x+2,y+33, fill = "black")
    for s in range(1,6):
        skin = choice(skinColours)
        x = randint(420,560)
        m = (p5-p4)/140
        b = p4 - m * x
        eq = int(m * x + b)
        y = randint(eq,300)
        helmet = screen.create_polygon(x-7,y-9,x-6,y-15,x,y-17,x+6,y-15,x+7,y-9,fill = "forest green",outline = "black")
        face = screen.create_polygon(x-6,y-9,x-4,y-2,x,y,x+4,y-2,x+6,y-9,fill = skin,outline = "black")
        eye1 = screen.create_oval(x-4,y-8,x-1,y-6,fill = "black")
        eye2 = screen.create_oval(x+4,y-8,x+1,y-6,fill = "black")
        top = screen.create_polygon(x-6,y+1,x-5,y+4,x-5,y+17,x,y+18,x+5,y+17,x+5,y+8,x+10,y+10,x+6,y+1,x,y,fill = "forest green",outline = "black")
        gun = screen.create_polygon(x-10,y+9,x-9,y+15,x+2,y+12,x+4,y+17,x+8,y+16,x+7,y+12,x+24,y+11,x+24,y+9,fill = "black")
        arm = screen.create_polygon(x-6,y+1,x-10,y+9,x-4,y+16,x-2,y+12,x-6,y+8,x-5,y+4,fill = "forest green",outline = "black")
        legs = screen.create_polygon(x-5,y+17,x-7,y+32,x-2,y+33,x,y+18,x+2,y+33,x+7,y+32,x+5,y+17,x,y+18,fill = "forest green",outline = "black")
        boot1 = screen.create_polygon(x-7,y+32,x-11,y+36,x-2,y+36,x-2,y+33,fill = "black")
        boot2 = screen.create_polygon(x+7,y+32,x+11,y+36,x+2,y+36,x+2,y+33, fill = "black")
    for s in range(1,6):
        skin = choice(skinColours)
        x = randint(560,700)
        m = (p6-p5)/140
        b = p5 - m * x
        eq = int(m * x + b)
        y = randint(eq,300)
        helmet = screen.create_polygon(x-7,y-9,x-6,y-15,x,y-17,x+6,y-15,x+7,y-9,fill = "forest green",outline = "black")
        face = screen.create_polygon(x-6,y-9,x-4,y-2,x,y,x+4,y-2,x+6,y-9,fill = skin,outline = "black")
        eye1 = screen.create_oval(x-4,y-8,x-1,y-6,fill = "black")
        eye2 = screen.create_oval(x+4,y-8,x+1,y-6,fill = "black")
        top = screen.create_polygon(x-6,y+1,x-5,y+4,x-5,y+17,x,y+18,x+5,y+17,x+5,y+8,x+10,y+10,x+6,y+1,x,y,fill = "forest green",outline = "black")
        gun = screen.create_polygon(x-10,y+9,x-9,y+15,x+2,y+12,x+4,y+17,x+8,y+16,x+7,y+12,x+24,y+11,x+24,y+9,fill = "black")
        arm = screen.create_polygon(x-6,y+1,x-10,y+9,x-4,y+16,x-2,y+12,x-6,y+8,x-5,y+4,fill = "forest green",outline = "black")
        legs = screen.create_polygon(x-5,y+17,x-7,y+32,x-2,y+33,x,y+18,x+2,y+33,x+7,y+32,x+5,y+17,x,y+18,fill = "forest green",outline = "black")
        boot1 = screen.create_polygon(x-7,y+32,x-11,y+36,x-2,y+36,x-2,y+33,fill = "black")
        boot2 = screen.create_polygon(x+7,y+32,x+11,y+36,x+2,y+36,x+2,y+33, fill = "black")
    #GrassBack
    for g1 in range(1,100001):
        grass = choice(grassColours)
        x = randint(0,700)
        eq = int((-0.17 * x) + 660)
        y = randint(500,eq)
        x2 = randint(x-4,x+4)
        screen.create_line(x,y,x2,y - 12, fill = grass)
    #Road
    screen.create_polygon(0,772,710,648,710,526,0,650,fill = "saddle brown")
    for r in range(1,10001):
        road = choice(["saddle brown","peru","saddle brown","saddle brown"])
        x = randint(0,700)
        yeq2 = int((-0.17 * x) + 771)
        yeq1 = int((-0.17 * x) + 650)
        y = randint(yeq1,yeq2)
        sz = randint(5,30)
        screen.create_line(x,y,x+sz,y+3,fill = road)
        screen.create_oval(x,y,x+3,y+3,fill = road)
    #GrassFront
    for g2 in range(1,50001):
        grass = choice(grassColours)
        x = randint(0,700)
        eq = int((-0.17 * x) + 760)
        y = randint(eq,830)
        x2 = randint(x-6,x+6)
        screen.create_line(x,y,x2,y - 20, fill = grass)
    #BackTrack
    screen.create_polygon(15,550,15,571,21,588,151,650,295,636,250,550,fill = "#222B15",outline = "#362110",width = 10)
    #FrontTrack
    screen.create_polygon(683,556,683,571,652,615,331,668,197,606,186,588,187,554,693,507,fill = "#222B15",outline = "black")
    #Turret
    screen.create_polygon(166,468,204,412,303,383,382,383,523,397,565,466, fill = "DarkOliveGreen4", outline = "Black")
    screen.create_polygon(166,468,247,464,294,474,374,474,425,462,565,466,524,500,213,497,fill = "#2E3D1A",outline = "black")
    screen.create_polygon(247,464,294,474,374,474,425,462,375,436,290,436,fill = "#687D4D",outline = "black")
    screen.create_polygon(294,474,374,474,375,436,380,390,300,390,290,436,fill = "#4A5C32",outline = "black")
    #Gun
    screen.create_oval(340,443,321,414, fill = "#657A48",outline = "black")
    screen.create_polygon(156,323,334,416,328,443,151,368,fill = "#657A48")
    screen.create_oval(170,368,140,324,fill = "#657A48",outline = "#657A48")
    screen.create_oval(143,335,167,355,fill = "black")
    #BackTrackGuard
    screen.create_polygon(32,553,10,550,5,520,31,500,131,504,125,550,fill = "#4A5C32",outline = "black")
    #Glacius
    screen.create_polygon(21,520,41,580,132,595,120,518,fill = "#657A48", outline = "black")
    #Wheels
    screen.create_oval(180,545,240,625,fill = "#3A4D2B",outline = "black")
    wheelx1 = 366
    wheelx2 = 303
    wheely1 = 670
    wheely2 = 580
    for w in range(1,7):
        screen.create_oval(wheelx1,wheely1,wheelx2,wheely2,fill = "#3A4D2B",outline = "black")
        wheelx1 = wheelx1 +65 - w*2
        wheelx2 = wheelx1 -50 +w*2
        wheely1 = wheely1 -10
        wheely2 = wheely2 -5
    #FrontTrackDetail
    screen.create_polygon(132,595,148,613,289,681,323,681,187,616,173,591,173,536,120,517,fill = "#362110",outline = "black")
    screen.create_polygon(173,536,173,591,187,616,323,681,656,622,688,573,689,545,683,556,683,571,652,615,331,668,197,606,186,588,187,554,fill = "#5C4129",outline = "black")
    #FrontTrackGuard
    screen.create_polygon(110,551,107,527,139,496,343,493,166,513,158,556, fill = "DarkOliveGreen4", outline = "black")
    screen.create_polygon(217,596,676,568,697,532,693,507,343,493,166,513,158,556,fill = "dark olive green",outline = "black")
    #Symbol
    place = randint(1,3)
    if place == 1:
        screen.create_line(48,536,99,538,61,568,73,523,92,573,48,536, fill = "blanched almond")
    elif place == 2:
        screen.create_line(447,413,500,417,456,445,475,403,489,448,447,413, fill = "blanched almond")
    else:
        screen.create_line(590,524,637,526,601,554,612,510,627,556,590,524, fill = "blanched almond")
elif theme == 2:
    myInterface = Tk()
    screen = Canvas(myInterface, width=700, height=800, background="khaki2")
    screen.pack()
    #Hill and Sky
    p1 = randint(150,250)
    p2 = randint(150,250)
    p3 = randint(150,250)
    p4 = randint(150,250)
    p5 = randint(150,250)
    p6 = randint(150,250)
    for g3 in range(1,100001):
        grass = choice(desertColours)
        x = randint(0,700)
        y = randint(150,310)
        screen.create_oval(x,y,x-1,y - 1, fill = grass,outline = grass)
    for g4 in range(100000):
        grass = choice(desertColours)
        x = randint(0,700)
        y = randint(300,500)
        x2 = randint(x - 2,x - 1)
        y2 = randint(y - 2,y -1)
        screen.create_oval(x,y,x2,y2, fill = grass,outline = grass)
    screen.create_polygon(-100,300,0,p1,140,p2,280,p3,420,p4,560,p5,700,p6,800,300,1000,-100,-300,-100,smooth = True,fill = "sky blue")
    #Sun
    screen.create_oval(450,50,500,100,fill = "yellow")
    #Soldiers
    for s in range(1,6):
        skin = choice(skinColours)
        x = randint(0,140)
        m = (p2-p1)/140
        b = p1 - m * x
        eq = int(m * x + b)
        y = randint(eq,300)
        helmet = screen.create_polygon(x-7,y-9,x-6,y-15,x,y-17,x+6,y-15,x+7,y-9,fill = "khaki3",outline = "black")
        face = screen.create_polygon(x-6,y-9,x-4,y-2,x,y,x+4,y-2,x+6,y-9,fill = skin,outline = "black")
        eye1 = screen.create_oval(x-4,y-8,x-1,y-6,fill = "black")
        eye2 = screen.create_oval(x+4,y-8,x+1,y-6,fill = "black")
        top = screen.create_polygon(x-6,y+1,x-5,y+4,x-5,y+17,x,y+18,x+5,y+17,x+5,y+8,x+10,y+10,x+6,y+1,x,y,fill = "khaki3",outline = "black")
        gun = screen.create_polygon(x-10,y+9,x-9,y+15,x+2,y+12,x+4,y+17,x+8,y+16,x+7,y+12,x+24,y+11,x+24,y+9,fill = "black")
        arm = screen.create_polygon(x-6,y+1,x-10,y+9,x-4,y+16,x-2,y+12,x-6,y+8,x-5,y+4,fill = "khaki3",outline = "black")
        legs = screen.create_polygon(x-5,y+17,x-7,y+32,x-2,y+33,x,y+18,x+2,y+33,x+7,y+32,x+5,y+17,x,y+18,fill = "khaki3",outline = "black")
        boot1 = screen.create_polygon(x-7,y+32,x-11,y+36,x-2,y+36,x-2,y+33,fill = "black")
        boot2 = screen.create_polygon(x+7,y+32,x+11,y+36,x+2,y+36,x+2,y+33, fill = "black")
    for s in range(1,6):
        skin = choice(skinColours)
        x = randint(140,280)
        m = (p3-p2)/140
        b = p2 - m * x
        eq = int(m * x + b)
        y = randint(eq,300)
        helmet = screen.create_polygon(x-7,y-9,x-6,y-15,x,y-17,x+6,y-15,x+7,y-9,fill = "khaki3",outline = "black")
        face = screen.create_polygon(x-6,y-9,x-4,y-2,x,y,x+4,y-2,x+6,y-9,fill = skin,outline = "black")
        eye1 = screen.create_oval(x-4,y-8,x-1,y-6,fill = "black")
        eye2 = screen.create_oval(x+4,y-8,x+1,y-6,fill = "black")
        top = screen.create_polygon(x-6,y+1,x-5,y+4,x-5,y+17,x,y+18,x+5,y+17,x+5,y+8,x+10,y+10,x+6,y+1,x,y,fill = "khaki3",outline = "black")
        gun = screen.create_polygon(x-10,y+9,x-9,y+15,x+2,y+12,x+4,y+17,x+8,y+16,x+7,y+12,x+24,y+11,x+24,y+9,fill = "black")
        arm = screen.create_polygon(x-6,y+1,x-10,y+9,x-4,y+16,x-2,y+12,x-6,y+8,x-5,y+4,fill = "khaki3",outline = "black")
        legs = screen.create_polygon(x-5,y+17,x-7,y+32,x-2,y+33,x,y+18,x+2,y+33,x+7,y+32,x+5,y+17,x,y+18,fill = "khaki3",outline = "black")
        boot1 = screen.create_polygon(x-7,y+32,x-11,y+36,x-2,y+36,x-2,y+33,fill = "black")
        boot2 = screen.create_polygon(x+7,y+32,x+11,y+36,x+2,y+36,x+2,y+33, fill = "black")
    for s in range(1,6):
        skin = choice(skinColours)
        x = randint(280,420)
        m = (p4-p3)/140
        b = p3 - m * x
        eq = int(m * x + b)
        y = randint(eq,300)
        helmet = screen.create_polygon(x-7,y-9,x-6,y-15,x,y-17,x+6,y-15,x+7,y-9,fill = "khaki3",outline = "black")
        face = screen.create_polygon(x-6,y-9,x-4,y-2,x,y,x+4,y-2,x+6,y-9,fill = skin,outline = "black")
        eye1 = screen.create_oval(x-4,y-8,x-1,y-6,fill = "black")
        eye2 = screen.create_oval(x+4,y-8,x+1,y-6,fill = "black")
        top = screen.create_polygon(x-6,y+1,x-5,y+4,x-5,y+17,x,y+18,x+5,y+17,x+5,y+8,x+10,y+10,x+6,y+1,x,y,fill = "khaki3",outline = "black")
        gun = screen.create_polygon(x-10,y+9,x-9,y+15,x+2,y+12,x+4,y+17,x+8,y+16,x+7,y+12,x+24,y+11,x+24,y+9,fill = "black")
        arm = screen.create_polygon(x-6,y+1,x-10,y+9,x-4,y+16,x-2,y+12,x-6,y+8,x-5,y+4,fill = "khaki3",outline = "black")
        legs = screen.create_polygon(x-5,y+17,x-7,y+32,x-2,y+33,x,y+18,x+2,y+33,x+7,y+32,x+5,y+17,x,y+18,fill = "khaki3",outline = "black")
        boot1 = screen.create_polygon(x-7,y+32,x-11,y+36,x-2,y+36,x-2,y+33,fill = "black")
        boot2 = screen.create_polygon(x+7,y+32,x+11,y+36,x+2,y+36,x+2,y+33, fill = "black")
    for s in range(1,6):
        skin = choice(skinColours)
        x = randint(420,560)
        m = (p5-p4)/140
        b = p4 - m * x
        eq = int(m * x + b)
        y = randint(eq,300)
        helmet = screen.create_polygon(x-7,y-9,x-6,y-15,x,y-17,x+6,y-15,x+7,y-9,fill = "khaki3",outline = "black")
        face = screen.create_polygon(x-6,y-9,x-4,y-2,x,y,x+4,y-2,x+6,y-9,fill = skin,outline = "black")
        eye1 = screen.create_oval(x-4,y-8,x-1,y-6,fill = "black")
        eye2 = screen.create_oval(x+4,y-8,x+1,y-6,fill = "black")
        top = screen.create_polygon(x-6,y+1,x-5,y+4,x-5,y+17,x,y+18,x+5,y+17,x+5,y+8,x+10,y+10,x+6,y+1,x,y,fill = "khaki3",outline = "black")
        gun = screen.create_polygon(x-10,y+9,x-9,y+15,x+2,y+12,x+4,y+17,x+8,y+16,x+7,y+12,x+24,y+11,x+24,y+9,fill = "black")
        arm = screen.create_polygon(x-6,y+1,x-10,y+9,x-4,y+16,x-2,y+12,x-6,y+8,x-5,y+4,fill = "khaki3",outline = "black")
        legs = screen.create_polygon(x-5,y+17,x-7,y+32,x-2,y+33,x,y+18,x+2,y+33,x+7,y+32,x+5,y+17,x,y+18,fill = "khaki3",outline = "black")
        boot1 = screen.create_polygon(x-7,y+32,x-11,y+36,x-2,y+36,x-2,y+33,fill = "black")
        boot2 = screen.create_polygon(x+7,y+32,x+11,y+36,x+2,y+36,x+2,y+33, fill = "black")
    for s in range(1,6):
        skin = choice(skinColours)
        x = randint(560,700)
        m = (p6-p5)/140
        b = p5 - m * x
        eq = int(m * x + b)
        y = randint(eq,300)
        helmet = screen.create_polygon(x-7,y-9,x-6,y-15,x,y-17,x+6,y-15,x+7,y-9,fill = "khaki3",outline = "black")
        face = screen.create_polygon(x-6,y-9,x-4,y-2,x,y,x+4,y-2,x+6,y-9,fill = skin,outline = "black")
        eye1 = screen.create_oval(x-4,y-8,x-1,y-6,fill = "black")
        eye2 = screen.create_oval(x+4,y-8,x+1,y-6,fill = "black")
        top = screen.create_polygon(x-6,y+1,x-5,y+4,x-5,y+17,x,y+18,x+5,y+17,x+5,y+8,x+10,y+10,x+6,y+1,x,y,fill = "khaki3",outline = "black")
        gun = screen.create_polygon(x-10,y+9,x-9,y+15,x+2,y+12,x+4,y+17,x+8,y+16,x+7,y+12,x+24,y+11,x+24,y+9,fill = "black")
        arm = screen.create_polygon(x-6,y+1,x-10,y+9,x-4,y+16,x-2,y+12,x-6,y+8,x-5,y+4,fill = "khaki3",outline = "black")
        legs = screen.create_polygon(x-5,y+17,x-7,y+32,x-2,y+33,x,y+18,x+2,y+33,x+7,y+32,x+5,y+17,x,y+18,fill = "khaki3",outline = "black")
        boot1 = screen.create_polygon(x-7,y+32,x-11,y+36,x-2,y+36,x-2,y+33,fill = "black")
        boot2 = screen.create_polygon(x+7,y+32,x+11,y+36,x+2,y+36,x+2,y+33, fill = "black")
    #GrassBack
    for g1 in range(1,100001):
        grass = choice(desertColours)
        x = randint(0,700)
        eq = int((-0.17 * x) + 660)
        y = randint(500,eq)
        x2 = randint(x-3,x-1)
        y2 = randint(y-3,y-1)
        screen.create_oval(x,y,x2,y2, fill = grass,outline = grass)
    #Road
    screen.create_polygon(0,772,710,648,710,526,0,650,fill = "khaki2")
    for r in range(1,10001):
        road = choice(["khaki","peru","dark khaki","saddle brown"])
        x = randint(0,700)
        yeq2 = int((-0.17 * x) + 771)
        yeq1 = int((-0.17 * x) + 650)
        y = randint(yeq1,yeq2)
        sz = randint(5,30)
        screen.create_line(x,y,x+sz,y+3,fill = road)
        screen.create_oval(x,y,x+3,y+3,fill = road)
    #GrassFront
    for g2 in range(1,50001):
        grass = choice(desertColours)
        x = randint(0,771)
        eq = int((-0.17 * x) + 760)
        y = randint(eq,830)
        x2 = randint(x-3,x-1)
        y2 = randint(y-3,y-1)
        screen.create_oval(x,y,x2,y2, fill = grass,outline = grass)
    #BackTrack
    screen.create_polygon(15,550,15,571,21,588,151,650,295,636,250,550,fill = "#695B34",outline = "#362110",width = 10)
    #FrontTrack
    screen.create_polygon(683,556,683,571,652,615,331,668,197,606,186,588,187,554,693,507,fill = "#695B34",outline = "black")
    #Turret
    screen.create_polygon(166,468,204,412,303,383,382,383,523,397,565,466, fill = "#BFA55C", outline = "Black")
    screen.create_polygon(166,468,247,464,294,474,374,474,425,462,565,466,524,500,213,497,fill = "#917934",outline = "black")
    screen.create_polygon(247,464,294,474,374,474,425,462,375,436,290,436,fill = "#948048",outline = "black")
    screen.create_polygon(294,474,374,474,375,436,380,390,300,390,290,436,fill = "#CCB168",outline = "black")
    #Gun
    screen.create_oval(340,443,321,414, fill = "#BFA55C",outline = "black")
    screen.create_polygon(156,323,334,416,328,443,151,368,fill = "#BFA55C")
    screen.create_oval(170,368,140,324,fill = "#BFA55C",outline = "#BFA55C")
    screen.create_oval(143,335,167,355,fill = "black")
    #BackTrackGuard
    screen.create_polygon(32,553,10,550,5,520,31,500,131,504,125,550,fill = "#948048",outline = "black")
    #Glacius
    screen.create_polygon(21,520,41,580,132,595,120,518,fill = "#BFA55C", outline = "black")
    #Wheels
    screen.create_oval(180,545,240,625,fill = "#26200F",outline = "black")
    wheelx1 = 366
    wheelx2 = 303
    wheely1 = 670
    wheely2 = 580
    for w in range(1,7):
        screen.create_oval(wheelx1,wheely1,wheelx2,wheely2,fill = "#26200F",outline = "black")
        wheelx1 = wheelx1 +65 - w*2
        wheelx2 = wheelx1 -50 +w*2
        wheely1 = wheely1 -10
        wheely2 = wheely2 -5
    #FrontTrackDetail
    screen.create_polygon(132,595,148,613,289,681,323,681,187,616,173,591,173,536,120,517,fill = "#362110",outline = "black")
    screen.create_polygon(173,536,173,591,187,616,323,681,656,622,688,573,689,545,683,556,683,571,652,615,331,668,197,606,186,588,187,554,fill = "#5C4129",outline = "black")
    #FrontTrackGuard
    screen.create_polygon(110,551,107,527,139,496,343,493,166,513,158,556, fill = "#CCB168", outline = "black")
    screen.create_polygon(217,596,676,568,697,532,693,507,343,493,166,513,158,556,fill = "#BFA55C",outline = "black")
    #Symbol
    place = randint(1,3)
    if place == 1:
        screen.create_line(48,536,99,538,61,568,73,523,92,573,48,536, fill = "blanched almond")
    elif place == 2:
        screen.create_line(447,413,500,417,456,445,475,403,489,448,447,413, fill = "blanched almond")
    else:
        screen.create_line(590,524,637,526,601,554,612,510,627,556,590,524, fill = "blanched almond")
else:
    myInterface = Tk()
    screen = Canvas(myInterface, width=700, height=800, background="snow")
    screen.pack()
    #Hill and Sky
    p1 = randint(150,250)
    p2 = randint(150,250)
    p3 = randint(150,250)
    p4 = randint(150,250)
    p5 = randint(150,250)
    p6 = randint(150,250)
    for g3 in range(1,100001):
        grass = choice(snowColours)
        x = randint(0,700)
        y = randint(150,310)
        screen.create_oval(x,y,x-1,y - 1, fill = grass,outline = grass)
    for g4 in range(100000):
        grass = choice(snowColours)
        x = randint(0,700)
        y = randint(300,500)
        x2 = randint(x - 2,x - 1)
        y2 = randint(y - 2,y -1)
        screen.create_oval(x,y,x2,y2, fill = grass,outline = grass)
    screen.create_polygon(-100,300,0,p1,140,p2,280,p3,420,p4,560,p5,700,p6,800,300,1000,-100,-300,-100,smooth = True,fill = "sky blue")
    #Sun
    screen.create_oval(450,50,500,100,fill = "yellow")
    #Soldiers
    for s in range(1,6):
        skin = choice(skinColours)
        x = randint(0,140)
        m = (p2-p1)/140
        b = p1 - m * x
        eq = int(m * x + b)
        y = randint(eq,300)
        helmet = screen.create_polygon(x-7,y-9,x-6,y-15,x,y-17,x+6,y-15,x+7,y-9,fill = "gray88",outline = "black")
        face = screen.create_polygon(x-6,y-9,x-4,y-2,x,y,x+4,y-2,x+6,y-9,fill = skin,outline = "black")
        eye1 = screen.create_oval(x-4,y-8,x-1,y-6,fill = "black")
        eye2 = screen.create_oval(x+4,y-8,x+1,y-6,fill = "black")
        top = screen.create_polygon(x-6,y+1,x-5,y+4,x-5,y+17,x,y+18,x+5,y+17,x+5,y+8,x+10,y+10,x+6,y+1,x,y,fill = "gray88",outline = "black")
        gun = screen.create_polygon(x-10,y+9,x-9,y+15,x+2,y+12,x+4,y+17,x+8,y+16,x+7,y+12,x+24,y+11,x+24,y+9,fill = "black")
        arm = screen.create_polygon(x-6,y+1,x-10,y+9,x-4,y+16,x-2,y+12,x-6,y+8,x-5,y+4,fill = "gray88",outline = "black")
        legs = screen.create_polygon(x-5,y+17,x-7,y+32,x-2,y+33,x,y+18,x+2,y+33,x+7,y+32,x+5,y+17,x,y+18,fill = "gray88",outline = "black")
        boot1 = screen.create_polygon(x-7,y+32,x-11,y+36,x-2,y+36,x-2,y+33,fill = "black")
        boot2 = screen.create_polygon(x+7,y+32,x+11,y+36,x+2,y+36,x+2,y+33, fill = "black")
    for s in range(1,6):
        skin = choice(skinColours)
        x = randint(140,280)
        m = (p3-p2)/140
        b = p2 - m * x
        eq = int(m * x + b)
        y = randint(eq,300)
        helmet = screen.create_polygon(x-7,y-9,x-6,y-15,x,y-17,x+6,y-15,x+7,y-9,fill = "gray88",outline = "black")
        face = screen.create_polygon(x-6,y-9,x-4,y-2,x,y,x+4,y-2,x+6,y-9,fill = skin,outline = "black")
        eye1 = screen.create_oval(x-4,y-8,x-1,y-6,fill = "black")
        eye2 = screen.create_oval(x+4,y-8,x+1,y-6,fill = "black")
        top = screen.create_polygon(x-6,y+1,x-5,y+4,x-5,y+17,x,y+18,x+5,y+17,x+5,y+8,x+10,y+10,x+6,y+1,x,y,fill = "gray88",outline = "black")
        gun = screen.create_polygon(x-10,y+9,x-9,y+15,x+2,y+12,x+4,y+17,x+8,y+16,x+7,y+12,x+24,y+11,x+24,y+9,fill = "black")
        arm = screen.create_polygon(x-6,y+1,x-10,y+9,x-4,y+16,x-2,y+12,x-6,y+8,x-5,y+4,fill = "gray88",outline = "black")
        legs = screen.create_polygon(x-5,y+17,x-7,y+32,x-2,y+33,x,y+18,x+2,y+33,x+7,y+32,x+5,y+17,x,y+18,fill = "gray88",outline = "black")
        boot1 = screen.create_polygon(x-7,y+32,x-11,y+36,x-2,y+36,x-2,y+33,fill = "black")
        boot2 = screen.create_polygon(x+7,y+32,x+11,y+36,x+2,y+36,x+2,y+33, fill = "black")
    for s in range(1,6):
        skin = choice(skinColours)
        x = randint(280,420)
        m = (p4-p3)/140
        b = p3 - m * x
        eq = int(m * x + b)
        y = randint(eq,300)
        helmet = screen.create_polygon(x-7,y-9,x-6,y-15,x,y-17,x+6,y-15,x+7,y-9,fill = "gray88",outline = "black")
        face = screen.create_polygon(x-6,y-9,x-4,y-2,x,y,x+4,y-2,x+6,y-9,fill = skin,outline = "black")
        eye1 = screen.create_oval(x-4,y-8,x-1,y-6,fill = "black")
        eye2 = screen.create_oval(x+4,y-8,x+1,y-6,fill = "black")
        top = screen.create_polygon(x-6,y+1,x-5,y+4,x-5,y+17,x,y+18,x+5,y+17,x+5,y+8,x+10,y+10,x+6,y+1,x,y,fill = "gray88",outline = "black")
        gun = screen.create_polygon(x-10,y+9,x-9,y+15,x+2,y+12,x+4,y+17,x+8,y+16,x+7,y+12,x+24,y+11,x+24,y+9,fill = "black")
        arm = screen.create_polygon(x-6,y+1,x-10,y+9,x-4,y+16,x-2,y+12,x-6,y+8,x-5,y+4,fill = "gray88",outline = "black")
        legs = screen.create_polygon(x-5,y+17,x-7,y+32,x-2,y+33,x,y+18,x+2,y+33,x+7,y+32,x+5,y+17,x,y+18,fill = "gray88",outline = "black")
        boot1 = screen.create_polygon(x-7,y+32,x-11,y+36,x-2,y+36,x-2,y+33,fill = "black")
        boot2 = screen.create_polygon(x+7,y+32,x+11,y+36,x+2,y+36,x+2,y+33, fill = "black")
    for s in range(1,6):
        skin = choice(skinColours)
        x = randint(420,560)
        m = (p5-p4)/140
        b = p4 - m * x
        eq = int(m * x + b)
        y = randint(eq,300)
        helmet = screen.create_polygon(x-7,y-9,x-6,y-15,x,y-17,x+6,y-15,x+7,y-9,fill = "gray88",outline = "black")
        face = screen.create_polygon(x-6,y-9,x-4,y-2,x,y,x+4,y-2,x+6,y-9,fill = skin,outline = "black")
        eye1 = screen.create_oval(x-4,y-8,x-1,y-6,fill = "black")
        eye2 = screen.create_oval(x+4,y-8,x+1,y-6,fill = "black")
        top = screen.create_polygon(x-6,y+1,x-5,y+4,x-5,y+17,x,y+18,x+5,y+17,x+5,y+8,x+10,y+10,x+6,y+1,x,y,fill = "gray88",outline = "black")
        gun = screen.create_polygon(x-10,y+9,x-9,y+15,x+2,y+12,x+4,y+17,x+8,y+16,x+7,y+12,x+24,y+11,x+24,y+9,fill = "black")
        arm = screen.create_polygon(x-6,y+1,x-10,y+9,x-4,y+16,x-2,y+12,x-6,y+8,x-5,y+4,fill = "gray88",outline = "black")
        legs = screen.create_polygon(x-5,y+17,x-7,y+32,x-2,y+33,x,y+18,x+2,y+33,x+7,y+32,x+5,y+17,x,y+18,fill = "gray88",outline = "black")
        boot1 = screen.create_polygon(x-7,y+32,x-11,y+36,x-2,y+36,x-2,y+33,fill = "black")
        boot2 = screen.create_polygon(x+7,y+32,x+11,y+36,x+2,y+36,x+2,y+33, fill = "black")
    for s in range(1,6):
        skin = choice(skinColours)
        x = randint(560,700)
        m = (p6-p5)/140
        b = p5 - m * x
        eq = int(m * x + b)
        y = randint(eq,300)
        helmet = screen.create_polygon(x-7,y-9,x-6,y-15,x,y-17,x+6,y-15,x+7,y-9,fill = "gray88",outline = "black")
        face = screen.create_polygon(x-6,y-9,x-4,y-2,x,y,x+4,y-2,x+6,y-9,fill = skin,outline = "black")
        eye1 = screen.create_oval(x-4,y-8,x-1,y-6,fill = "black")
        eye2 = screen.create_oval(x+4,y-8,x+1,y-6,fill = "black")
        top = screen.create_polygon(x-6,y+1,x-5,y+4,x-5,y+17,x,y+18,x+5,y+17,x+5,y+8,x+10,y+10,x+6,y+1,x,y,fill = "gray88",outline = "black")
        gun = screen.create_polygon(x-10,y+9,x-9,y+15,x+2,y+12,x+4,y+17,x+8,y+16,x+7,y+12,x+24,y+11,x+24,y+9,fill = "black")
        arm = screen.create_polygon(x-6,y+1,x-10,y+9,x-4,y+16,x-2,y+12,x-6,y+8,x-5,y+4,fill = "gray88",outline = "black")
        legs = screen.create_polygon(x-5,y+17,x-7,y+32,x-2,y+33,x,y+18,x+2,y+33,x+7,y+32,x+5,y+17,x,y+18,fill = "gray88",outline = "black")
        boot1 = screen.create_polygon(x-7,y+32,x-11,y+36,x-2,y+36,x-2,y+33,fill = "black")
        boot2 = screen.create_polygon(x+7,y+32,x+11,y+36,x+2,y+36,x+2,y+33, fill = "black")
    #GrassBack
    for g1 in range(1,100001):
        grass = choice(snowColours)
        x = randint(0,700)
        eq = int((-0.17 * x) + 660)
        y = randint(500,eq)
        x2 = randint(x-3,x-1)
        y2 = randint(y-3,y-1)
        screen.create_oval(x,y,x2,y2, fill = grass,outline = grass)
    #Road
    screen.create_polygon(0,772,710,648,710,526,0,650,fill = "cornsilk")
    for r in range(1,10001):
        road = choice(["snow","cornsilk","saddle brown","snow"])
        x = randint(0,700)
        yeq2 = int((-0.17 * x) + 771)
        yeq1 = int((-0.17 * x) + 650)
        y = randint(yeq1,yeq2)
        sz = randint(5,30)
        screen.create_line(x,y,x+sz,y+3,fill = road)
        screen.create_oval(x,y,x+3,y+3,fill = road)
    #GrassFront
    for g2 in range(1,50001):
        grass = choice(snowColours)
        x = randint(0,700)
        eq = int((-0.17 * x) + 771)
        y = randint(eq,830)
        x2 = randint(x-3,x-1)
        y2 = randint(y-3,y-1)
        screen.create_oval(x,y,x2,y2, fill = grass,outline = grass)
    #BackTrack
    screen.create_polygon(15,550,15,571,21,588,151,650,295,636,250,550,fill = "gray8",outline = "gray3",width = 10)
    #FrontTrack
    screen.create_polygon(683,556,683,571,652,615,331,668,197,606,186,588,187,554,693,507,fill = "gray8",outline = "black")
    #Turret
    screen.create_polygon(166,468,204,412,303,383,382,383,523,397,565,466, fill = "white smoke", outline = "Black")
    screen.create_polygon(166,468,247,464,294,474,374,474,425,462,565,466,524,500,213,497,fill = "AntiqueWhite3",outline = "black")
    screen.create_polygon(247,464,294,474,374,474,425,462,375,436,290,436,fill = "snow2",outline = "black")
    screen.create_polygon(294,474,374,474,375,436,380,390,300,390,290,436,fill = "snow3",outline = "black")
    #Gun
    screen.create_oval(340,443,321,414, fill = "light gray",outline = "black")
    screen.create_polygon(156,323,334,416,328,443,151,368,fill = "light gray")
    screen.create_oval(170,368,140,324,fill = "light gray",outline = "light gray")
    screen.create_oval(143,335,167,355,fill = "black")
    #BackTrackGuard
    screen.create_polygon(32,553,10,550,5,520,31,500,131,504,125,550,fill = "snow3",outline = "black")
    #Glacius
    screen.create_polygon(21,520,41,580,132,595,120,518,fill = "white smoke", outline = "black")
    #Wheels
    screen.create_oval(180,545,240,625,fill = "AntiqueWhite3",outline = "black")
    wheelx1 = 366
    wheelx2 = 303
    wheely1 = 670
    wheely2 = 580
    for w in range(1,7):
        screen.create_oval(wheelx1,wheely1,wheelx2,wheely2,fill = "AntiqueWhite3",outline = "black")
        wheelx1 = wheelx1 +65 - w*2
        wheelx2 = wheelx1 -50 +w*2
        wheely1 = wheely1 -10
        wheely2 = wheely2 -5
    #FrontTrackDetail
    screen.create_polygon(132,595,148,613,289,681,323,681,187,616,173,591,173,536,120,517,fill = "gray3",outline = "black")
    screen.create_polygon(173,536,173,591,187,616,323,681,656,622,688,573,689,545,683,556,683,571,652,615,331,668,197,606,186,588,187,554,fill = "gray20",outline = "black")
    #FrontTrackGuard
    screen.create_polygon(110,551,107,527,139,496,343,493,166,513,158,556, fill = "cornsilk2", outline = "black")
    screen.create_polygon(217,596,676,568,697,532,693,507,343,493,166,513,158,556,fill = "white smoke",outline = "black")
    #Symbol
    place = randint(1,3)
    if place == 1:
        screen.create_line(48,536,99,538,61,568,73,523,92,573,48,536, fill = "black")
    elif place == 2:
        screen.create_line(447,413,500,417,456,445,475,403,489,448,447,413, fill = "black")
    else:
        screen.create_line(590,524,637,526,601,554,612,510,627,556,590,524, fill = "black")
    #Snow
    for s in range(1,1001):
        snow = choice(snowColours)
        x = randint(0,700)
        y = randint(0,800)
        z = randint(1,5)
        screen.create_oval(x,y,x+z,y+z,fill = snow)
#Creds
screen.create_rectangle(0,0,250,50,fill = "yellow")
screen.create_text(125,25,text = "By: Yijinmide Sodnam",font = "Impact 20",fill = "blue")
###GRID OVERLAY
##spacing = 50
##for x in range(0, 800, spacing): 
##    screen.create_line(x, 20, x, 800, fill="blue")
##    screen.create_text(x, 3, text=str(x), font="Times 10", anchor = N, fill="blue")
##
##for y in range(0, 800, spacing):
##    screen.create_line(20, y, 800, y, fill="blue")
##    screen.create_text(3, y, text=str(y), font="Times 10", anchor = W, fill="blue")
##
##screen.update()
##
