from time import *
from tkinter import *
from math import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="sky blue")
screen.pack()
x1 = 0
y1 = 800 
x2 = x1 + 131 
y2 = 737
for w in range(1,701):
    screen.create_rectangle(0,300,800,800,fill = "forest green")
    if x1 > 800:
        x1 = 0
        y1 = 800
    speed = 0.03*w**2
    #Colours
    base1 = "red"
    base2 = "#C21D1D"
    highlight1 = "#FF4D4D"
    highlight2 = "#FF7575"
    shade1 = "#AD1818"
    windowBase = "grey10"
    #Road
    screen.create_polygon(0,612,800,385,800,520,593,800,0,800,fill = "grey50")
    slope = 0.048
    x1 = (x1 + 0.1 *w) 
    y1 = (y1 - slope*w) 
    x2 = x1 + 131 - 1
    y2 = y1 - 63 + slope *10
    
    mark = screen.create_line(x1,y1,x2,y2,fill = "yellow",width = 5)
    #Cabin
    screen.create_polygon(396,366,323,376,100,479,631,466,686,409,593,363,577,360,fill = base1,smooth = True)
    screen.create_polygon(390,366,164,456,631,466,686,409,593,363,577,360,fill = base1)
    #Windscreen
    screen.create_polygon(207,440,586,434,572,366,396,366,326,380,fill = windowBase,smooth = True)
    screen.create_polygon(195,440,586,434,572,363,396,370,326,383,fill = windowBase)
    #Window
    screen.create_polygon(586,364,608,471,679,410,fill = windowBase,smooth = True)
    screen.create_polygon(593,398,614,378,586,364,fill = windowBase,smooth = True)
    screen.create_polygon(590,383,600,433,640,391,601,372,fill = windowBase)
    #Back Wheel
    screen.create_oval(709,438,730,542,fill = "black")
    screen.create_oval(705,448,733,561,fill = "grey13")
    screen.create_polygon(719,563,650,563,700,500,fill = "grey13")

    theta = radians(90 - speed)
    
    x = 718 + 8*cos(theta)
    y = 505 + 48*sin(theta)
    spoke1 = screen.create_line(718,505,x,y,fill = "black",width = 5)
    screen.create_line(718,505,x,y,fill = "#B50000",width = 0.1)

    x = 718 + 8*cos(theta + pi/2)
    y = 505 + 48*sin(theta + pi/2)
    spoke2 = screen.create_line(718,505,x,y,fill = "black",width = 5)
    screen.create_line(718,505,x,y,fill = "#B50000",width = 0.1)

    x = 718 + 8*cos(theta + pi)
    y = 505 + 48*sin(theta + pi)
    spoke2 = screen.create_line(718,505,x,y,fill = "black",width = 5)
    screen.create_line(718,505,x,y,fill = "#B50000",width = 0.1)

    x = 718 + 8*cos(theta + 3*pi/2)
    y = 505 + 48*sin(theta + 3*pi/2)
    spoke2 = screen.create_line(718,505,x,y,fill = "black",width = 5)
    screen.create_line(718,505,x,y,fill = "#B50000",width = 0.1)
    screen.create_oval(710,456,726,553,outline = "black",width = 3)
    #Body
    screen.create_polygon(597,459,680,406,705,415,717,425,723,439,720,438,716,441,714,446,707,550,626,611,fill = base2)
    #Sculpting
    screen.create_polygon(597,459,680,406,705,415,607,510,fill = "#FF2E2E")
    screen.create_polygon(616,558,672,515,684,529,621,585,fill = "#FF2E2E")
    screen.create_polygon(607,510,687,433,689,436,672,515,616,558,fill = shade1)
    #Vent
    screen.create_polygon(676,449,689,436,704,445,700,511,684,529,672,515,fill = "black")
    #Wipers
    #screen.create_polygon(195,440,586,434,586,450,195,470,fill = "grey5")
    #Left Bumper
    screen.create_polygon(60,546,66,641,94,660,158,654,170,590,fill = base2)
    screen.create_polygon(67,639,95,658,136,611,90,616,fill = highlight1)
    screen.create_polygon(75,631,100,647,135,610,90,616,fill = "#FF6969")
    #Left Grille
    screen.create_polygon(59,564,63,608,87,619,107,631,132,599,116,578,98,578,65,558,fill = "grey20")
    screen.create_polygon(91,583,94,609,115,621,132,599,116,578,98,578,fill = "grey10")
    #Center Grille
    screen.create_polygon(164,620,118,650,118,657,199,676,352,677,362,631,fill = "grey10")
    screen.create_line(118,654,199,673,fill = "grey30",width = 5)
    screen.create_line(199,673,352,674,fill = "grey20",width = 5)
    screen.create_line(161,622,221,634,220,647,148,631,fill = "grey35",width = 3)
    screen.create_line(342,634,221,634,220,647,352,646,fill = "grey20",width = 3)
    #Front Wheel
    screen.create_oval(614,450,646,580,fill = "black")
    screen.create_rectangle(623,656,500,500,fill = "grey15")
    screen.create_line(613,489,628,448,637,448,643,461,647,475,643,563,fill = base2, width = 6,smooth = True)
    screen.create_oval(604,467,646,655,fill = "grey15",outline = "grey15")

    speed = -0.03*w**2

    theta = radians(90 + speed)
    
    x = 623 + 13*cos(theta)
    y = 568 + 78*sin(theta)
    spoke1 = screen.create_line(623,568,x,y,fill = "black",width = 6)
    screen.create_line(623,568,x,y,fill = "#B50000",width = 0.2)

    x = 623 + 13*cos(theta + pi/2)
    y = 568 + 78*sin(theta + pi/2)
    spoke2 = screen.create_line(623,568,x,y,fill = "black",width = 6)
    screen.create_line(623,568,x,y,fill = "#B50000",width = 0.1)

    x = 623 + 13*cos(theta + pi)
    y = 568 + 78*sin(theta + pi)
    spoke2 = screen.create_line(623,568,x,y,fill = "black",width = 6)
    screen.create_line(623,568,x,y,fill = "#B50000",width = 0.1)

    x = 623 + 13*cos(theta + 3*pi/2)
    y = 568 + 78*sin(theta + 3*pi/2)
    spoke2 = screen.create_line(623,568,x,y,fill = "black",width = 6)
    screen.create_line(623,568,x,y,fill = "#B50000",width = 0.1)
    
    screen.create_oval(637,642,610,486,outline = "black",width = 4)
    #Hood Part 1(Left to Right)
    screen.create_polygon(120,571,83,568,66,558,57,547,64,526,77,507,93,489,108,475,119,467,131,459,142,453,165,444,190,439,203,439,265,445,fill = "#FF6969",smooth = True)
    screen.create_polygon(203,439,290,445,114,571,83,565,fill = "#FF6969")
    #Hood Part 2(Left to Right)
    screen.create_polygon(101,566,104,554,129,525,162,500,197,476,225,462,265,445,346,443,323,451,298,463,275,478,239,508,211,537,193,571,190,585,133,573,fill = highlight1,smooth = True)
    screen.create_polygon(101,563,140,616,212,629,190,575,fill = "#FF4545")
    #Hood Part 3(Left to Right)
    screen.create_polygon(346,442,323,450,298,462,275,477,239,507,211,536,193,570,190,579,272,577,346,569,360,520,389,467,410,440,fill = "#FF1717")
    screen.create_polygon(190,576,212,629,345,631,346,569,fill = "#C22929")
    #Hood Part 4(Left to Right)
    screen.create_polygon(332,582,346,569,360,520,389,467,410,440,474,430,516,425,541,423,562,423,611,428,625,435,618,439,590,474,576,503,563,531,487,553,fill = base1)
    screen.create_polygon(576,503,590,474,618,439,622,437,631,447,617,486,fill = base2)
    screen.create_polygon(611,428,618,434,631,447,637,447,633,441,618,430,fill = base2)
    screen.create_line(628,453,637,453,fill = base2,width = 6)
    #Right Bumper
    screen.create_polygon(332,582,332,626,351,684,506,672,598,646,605,600,617,486,576,503,562,531,487,553,fill = base2)
    #Right Grille
    screen.create_polygon(354,590,349,617,380,654,501,646,533,630,488,567,fill = "grey20")
    screen.create_polygon(366,600,400,642,507,634,476,579,fill = "grey10")
    #Hood Lines
    screen.create_line(173,443,137,461,112,499,fill = "grey5",smooth = True)
    screen.create_line(111,510,138,519,205,525,fill = "grey5")
    screen.create_line(205,525,231,515,248,525,fill = "grey5",smooth = True)
    screen.create_line(248,525,360,520,410,510,421,510,fill = "grey5")
    screen.create_line(447,497,513,446,579,425,fill = "grey5", smooth = True)
    #Lights
    screen.create_polygon(108,476,118,499,112,511,74,531,65,526,77,509,93,490,fill = "grey15")
    screen.create_polygon(417,510,447,534,500,529,551,467,548,466,428,498,fill = "grey15")
    print(w)
    screen.update()
    sleep(0.03)
    if w < 700:
        screen.delete(ALL)
    if w > 700:
        screen.delete(mark)
y3 = 900
for p in range(1,300):
    x3 = 400
    y3 = y3 - p ** 2
    if y3 < 200:
        y3 = 199
    creds = screen.create_text(x3,y3,text = "By: Yijinmide Sodnam",font = "Impact 30", fill = "black")
    screen.update()
    sleep(0.03)
    screen.delete(creds,mark)
