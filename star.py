#Drawing a star using turtle
import turtle
turtle.Screen()
turtle.Screen().setup(500,500)

start=turtle.Turtle()
start.pencolor('red')
#First Triangle for Star
start.forward(100)

start.left(120)
start.forward(100)

start.left(120)
start.forward(100)
#Going upwards
start.penup()
start.right(150)
start.forward(50)
#Drawing 2nd Triangle
start.pendown()
start.right(90)
start.forward(100)

start.right(120)
start.forward(100)

start.right(120)
start.forward(100)

turtle.done()