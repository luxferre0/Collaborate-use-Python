import turtle


my_turtle = turtle.Turtle()

def drawGraph(len, line):
	for i in range(line):
		my_turtle.forward(len)
		my_turtle.left(360 / line)
		#my_turtle.forward(len)

drawGraph(100, 6)

turtle.exitonclick()