import turtle 
screen = turtle.Screen()
screen.setup(1200,1000)

square = turtle.Turtle()
square.shape("square")
square.speed("fastest")
square.up()

def trazar (col_1, poicion_y, cantidad):
    for i in range(cantidad):
        x = 25*i
square.forward(200)
square.right(90)
square.forward(200)
square.right(90)
square.forward(200)
square.right(90)
square.forward(200)
square.color("red")
square.stamp()
square.forward(50)
square.left(45)
square.stamp()
square.forward(50)
square.up()
square.stamp()
square.forward(50)
square.stamp()
square.goto(0,0)
square.color("green")
square.stamp()
square.goto(-400,300)
square.stamp()


turtle.exitonclick()