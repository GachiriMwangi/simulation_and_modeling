import turtle
import random

def drawflowers():
    # Set initial position
    turtle.penup()
    turtle.left (180) # Turns pen counterclockwise
    
    turtle.fd(110) 
    turtle.pendown ()
    turtle.right (180)

    # flower base
    turtle.fillcolor (gencolors())
    turtle.begin_fill ()
    turtle.circle (1,180)
    turtle.circle (2.5,110)
    turtle.left (50)
    turtle.circle (6,45)
    turtle.circle (2,170)
    turtle.right (24)
    turtle.fd (3)
    turtle.left (10)
    turtle.circle (3,110)
    turtle.fd (2)
    turtle.left (40)
    turtle.circle (9,70)
    turtle.circle (3,150)
    turtle.right (30)
    turtle.fd (1.5)
    turtle.circle (8,90)
    turtle.left (15)
    turtle.fd (4.5)
    turtle.right (165)
    turtle.fd (2)
    turtle.left (155)
    turtle.circle (15,80)
    turtle.left (50)
    turtle.circle (15,90)
    turtle.end_fill ()

    # Petal 1
    turtle.left (150)
    turtle.circle (-9,70)
    turtle.left (20)
    turtle.circle (7.5,105)
    turtle.setheading (60)
    turtle.circle (8,98)
    turtle.circle (-9,40)

    # Petal 2
    turtle.left (180)
    turtle.circle (9,40)
    turtle.circle (-8,98)
    turtle.setheading (-83)

    # Leaves 1
    turtle.fd (3)
    turtle.left (90)
    turtle.fd (2.5)
    turtle.left (45)
    turtle.fillcolor (gencolors())
    turtle.begin_fill ()
    turtle.circle (-8,90)
    turtle.right (90)
    turtle.circle (-8,90)
    turtle.end_fill ()
    turtle.right (135)
    turtle.fd (6)
    turtle.left (180)
    turtle.fd (8.5)
    turtle.left (90)
    turtle.fd (8)

    # Leaves 2
    turtle.right (90)
    turtle.right (45)
    turtle.fillcolor (gencolors())
    turtle.begin_fill ()
    turtle.circle (8,90)
    turtle.left (90)
    turtle.circle (8,90)
    turtle.end_fill ()
    turtle.left (135)
    turtle.fd (6)
    turtle.left (180)
    turtle.fd (6)
    turtle.right (90)
    turtle.circle (20,60)


# Function used to generate colors randomly
def gencolors():
    return ((random.random(),random.random(),random.random()))


def main():
    turtle.hideturtle() # Hide the turtle icon while drawing
    turtle.speed(0) # Speed up drawing
    turtle.tracer(1,0) # Skip animation of drawing

    # Set initial position before drawing flowers
    turtle.penup()
    turtle.goto(700,-100)

    # Draw environment with the flowers
    for i in range(8):
        drawflowers() # Draw flowers

# Draw the environment first before cars
main()