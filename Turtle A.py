#Luke Hurley
#June 5th
#Turtle A
import turtle
import random
#random pen size
p = random.randint(3,15)
#customize the turtle
turtle.colormode(255)
turtle.begin_fill()
turtle.speed(1)
turtle.pensize(p)
turtle.shape("circle")
turtle.pencolor("#58D68D")
turtle.bgcolor("#083D5D")
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
turtle.fillcolor(r,g,b)
c = random.randint(50,400)
#ask for square size
shape = str(input("Do you want a circle or a square drawn? "))
if shape == "square" or shape == "Square":
    #create a square
    turtle.right(90)
    turtle.forward(c)
    #
    turtle.right(90)
    turtle.forward(c)
    #
    turtle.right(90)
    turtle.forward(c)
    #
    turtle.right(90)
    turtle.forward(c)
    #
    turtle.end_fill()
elif shape == "circle" or shape == "Circle":
    turtle.circle(c)
else:
    print("That's not a shape we can draw.")
    
