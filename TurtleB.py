#Luke Hurley
#June 3rd
#Turtle B
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
#create an equilateral triangle
turtle.forward(w)
turtle.right(120)
turtle.forward(w)
turtle.right(120)
turtle.forward(w)
#pen up
turtle.penup()
# move 300 to left
turtle.left(60)
turtle.forward(w)
#pen down
turtle.pendown()
#create a hexigon
turtle.forward(i)
turtle.right(60)
turtle.forward(i)
turtle.right(60)
turtle.forward(i)
turtle.right(60)
turtle.forward(i)
turtle.right(60)
turtle.forward(i)
turtle.right(60)
turtle.forward(i)




