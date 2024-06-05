#Luke Hurley
#June 3rd
#Turtle C
import turtle
#customize the turtle
turtle.speed("fast")
turtle.pensize("15")
turtle.shape("circle")
turtle.pencolor("#58D68D")
turtle.fillcolor("#9366C4")
turtle.bgcolor("#083D5D")
#set length variable
w = 300
i = 100
h = 40
r = 80
t = 260
f = 135
#transition to the right
turtle.penup()
turtle.right(180)
turtle.forward(w)
turtle.left(180)
#create an L
turtle.begin_fill()
turtle.pendown()
turtle.right(90)
turtle.forward(w)
turtle.left(90)
turtle.forward(2*i)
turtle.left(90)
turtle.forward(h)
turtle.left(90)
turtle.forward(2*r)
turtle.right(90)
turtle.forward(t)
turtle.left(90)
turtle.forward(h)
turtle.end_fill()
#transition to H
turtle.penup()
turtle.right(180)
turtle.forward(w)
turtle.pendown()
#create an H
turtle.begin_fill()
turtle.pendown()
turtle.right(90)
turtle.forward(w)
turtle.left(90)
turtle.forward(h)
turtle.left(90)
turtle.forward(f)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(f)
turtle.left(90)
turtle.forward(h)
turtle.left(90)
turtle.forward(w)
turtle.left(90)
turtle.forward(h)
turtle.left(90)
turtle.forward(f)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(f)
turtle.left(90)
turtle.forward(h)
turtle.end_fill()

