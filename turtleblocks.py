import turtle
from math import sin, cos
from random import randint, choice

#some random block drawing.
turtle.bgcolor("black")
turtle.color((.1, .5, .9))
turtle.hideturtle()
turtle.tracer(0, 0)

def square(x, y, height, heading=0):
    turtle.pu()
    turtle.goto(x, y)
    turtle.setheading(heading)
    turtle.pd()
    turtle.begin_fill()
    for x in range(4):
        turtle.fd(height)
        turtle.right(90)
    turtle.end_fill()


BLOCK_SIZE = 70
COLOR_SP = 3000 #divides the sin function parameter
R, G, B = 0, 0, 0
sizelist = []
head = 0

counter = 0
for x in range(1, 9):
    for i in range(10 - x):
        sizelist.append(x)
        
while True:

    bsize = BLOCK_SIZE #+ (12*sin(R/500))
    
    size = 2 #choice(sizelist)

    xpos = randint(-5, 5 - size)
    ypos = randint(-5 + size, 5)

    xpos *= bsize
    ypos *= bsize
    #head = (head+ .2)%360 rotate animation
    
    R += 7
    G += 11
    B += 3
    
    turtle.color(((sin(4*G/COLOR_SP)+ cos(1.7*G/COLOR_SP)+ 2)/4,
                 (sin(2*G/COLOR_SP)+ cos(3*G/COLOR_SP)+ 2)/4,
                 ((sin(1.9*G/COLOR_SP)+ cos(2.3*G/COLOR_SP)+ 2)/4)))

    square(xpos, ypos, size* bsize)
    counter += 1
    if counter % 1 == 0:
        turtle.update()




    
