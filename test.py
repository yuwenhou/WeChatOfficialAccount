from turtle import *
reset()
bgcolor('black')
speed(0)
colors = ['red','orange','green','cyan','blue','purple']
for i in range(360):
    pencolor(colors[i%6])
    fd(i*3/6+i)
    left(61)
    pensize(i*6/200)