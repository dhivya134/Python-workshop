import turtle
from random import randint
bob = turtle.Turtle()

def draw_polygon(bob,sides, length, breadth):
    angle = 360 / sides   
    for i in range(sides):
        if i%2!=0:
            bob.forward(breadth)
            bob.left(angle)
        else:
            bob.forward(length)
            bob.left(angle)
def draw(bob,sides,length):
    angle = 360 / sides
    for i in range(sides): 
        bob.forward(length)
        bob.left(angle)
    
def move(bob, x, y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()


def rectangle():
    bob.color("brown")
    sides = 4
    length = 30
    breadth = 60
    bob.begin_fill()
    draw_polygon(bob, sides, length, breadth)
    bob.end_fill()

def triangle1() :
    bob.color("green")
    sides = 3
    length = 120
    bob.begin_fill()
    draw(bob, sides, length)
    bob.end_fill()

def triangle2() :
    bob.color("light green")
    sides = 3
    length = 90
    bob.begin_fill()
    draw(bob, sides, length)
    bob.end_fill()

def triangle3() :
    bob.color("yellow")
    sides = 3
    length = 60
    bob.begin_fill()
    draw(bob, sides, length)
    bob.end_fill()

  
 
move(bob, 0, 0)
rectangle()

move(bob, -45, 60)
triangle1()

move(bob, -30 , 120)
triangle2()

move(bob, -15 , 170)
triangle3()

move(bob, 12,220)
for i in range(20):  
    draw(bob, 3, 10)
    bob.color("red")
    bob.left(18)



turtle.done()
