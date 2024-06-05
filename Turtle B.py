#Luke Hurley
#June 5th
#Turtle B
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
c = 100
#ask for square size
shape = str(input("Do you want the square to move up or down? "))
if shape == "up" or shape == "Up":
    #move up
    turtle.left(90)
    turtle.forward(c)
    turtle.backward(0)
elif shape == "down" or shape == "Down":
    #move down
    turtle.right(90)
    turtle.forward(c)
else:
    print("That's a move turtle can do.")
shape = str(input("Do you want the square to the left up or to the right? "))
if shape == "left" or shape == "Left":
    #move left
    turtle.right(90)
    turtle.forward(c)
elif shape == "right" or shape == "Right":
    #move right
    turtle.left(90)
    turtle.forward(c)
else:
    print("That's a move turtle can do.")
    
    
