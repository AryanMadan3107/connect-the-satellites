import pgzrun
import random

HEIGHT=600
WIDTH=800

nrs=10
sat=[]
line=[]
satnrs=1
next=0

for i in range(nrs):
    s=Actor("satellite")
    s.x=random.randint(50,750)
    s.y=random.randint(50,550)
    sat.append(s)

def draw(): 
    global satnrs
    screen.blit("background",(0,0))
    for satellite in sat:
        satellite.draw()
        screen.draw.text(str(satnrs),(satellite.x,satellite.y+20))
        satnrs+=1
    
#def update():
#    pass

def on_mouse_down(pos):
    global next, line, sat
    if sat[next].collidepoint(pos):
        if next>0:
            line.append((sat[next-1].pos,sat[next].pos))
            print(line)
        next+=1
        print(satnrs)

pgzrun.go()