from turtle import Turtle, Screen

ella = Turtle()
screen = Screen()

def forward():
    ella.forward(10)
def backward():
    ella.back(10)

def clockwise():
    ella.right(90)
def counter_clockwise():
    ella.left(90)
def clear():
    ella.clear()

screen.listen()
screen.onkey(key="w", fun= forward)
screen.onkey(key= "s", fun = backward)
screen.onkey(key= "a", fun = counter_clockwise)
screen.onkey(key= "d", fun = clockwise)
screen.onkey(key= "c", fun = clear)

screen.exitonclick()