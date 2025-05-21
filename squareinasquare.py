#Drawing a square inside a square
import turtle
turtle.Screen().setup
turtle.Screen().bgcolor('light blue')
#Initializing
start=turtle.Turtle()
#Pen colour inti
turtle.pencolor('red')
#Outer Square
val=0
while True:
 start.forward(val+1)
 start.left(90)
 val=val-5
 val+=1
turtle.done()