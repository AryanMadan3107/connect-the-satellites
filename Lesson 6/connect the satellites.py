import pgzrun
import random

HEIGHT=600
WIDTH=800

nrs=10
sat=[]

for i in range(nrs):
    s=Actor("satellite")
    s.x=random.randint(50,750)
    s.y=random.randint(50,550)
    sat.append(s)

def draw():
    screen.blit("background",(0,0))
    for satellite in sat:
        satellite.draw()

pgzrun.go()