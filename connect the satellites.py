import pgzrun
import random
from time import time

HEIGHT = 600
WIDTH = 800

nrs = 10
sat = []
line = []
next = 0
start = time()
gameover = False
yw=False
#go = 


for i in range(nrs):
    s = Actor("satellite")
    s.x = random.randint(50, 750)
    s.y = random.randint(50, 550)
    sat.append(s)

def draw(): 
    global start,total
    satnrs = 1
    screen.blit("background", (0, 0))
    if next<nrs:
        total=time()-start
        screen.draw.text(str(round(total,1)),(15,15))
    else:
       screen.draw.text(str(round(total,1)),(15,15)) 
    
    for l in line:
        screen.draw.line(l[0], l[1], "white")
    
    for satellite in sat:
        satellite.draw()
        screen.draw.text(str(satnrs), (satellite.x, satellite.y + 20))
        satnrs += 1
    if gameover:
        screen.fill("red")
        screen.draw.text("Time's up!",center=(400,300),fontsize=50,color="white")
    if yw:
        screen.fill("green")
        screen.draw.text("You win!",center=(400,300),fontsize=50,color="white")

def update():
    pass

def on_mouse_down(pos):
    global next, line, sat
    if sat[next].collidepoint(pos):
        if next > 0:
            line.append((sat[next-1].pos, sat[next].pos))
            if next==9:
                yw()
        next +=1
            
    else:
        line = []
        next=0

def yw():
    global yw
    yw=True

def timeup():
    global gameover
    gameover=True

clock.schedule(timeup,15.0)

pgzrun.go()
