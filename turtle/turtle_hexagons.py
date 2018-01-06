from turtle import *
 
speed(0)
bgcolor("Black")
color("White")
 
def hex(side):
    for count in range(6):
        forward(side)
        left(60)
 
def rotation():
 
    n = 0
    colormode(255)
    c = 0
    pencolor(c,c,c)
 
    for count in range(120):
        c += 255.0/120
        pencolor(c,c,c)
        hex(n)
        n += 1
        left(3)
 
 
penup()
goto(0,0)
pendown()
 
rotation()
 
hideturtle()
done()