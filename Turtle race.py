from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make a bet", prompt="Who will win the race? pick a color ")

anna = Turtle(shape="turtle")
anna.color("red")
anna.penup()
anna.goto(x=-230, y=-100)

bill = Turtle(shape="turtle")
bill.color("blue")
bill.penup()
bill.goto(x=-230, y=-60)

clay = Turtle(shape="turtle")
clay.color("yellow")
clay.penup()
clay.goto(x=-230, y=-20)

dell = Turtle(shape="turtle")
dell.color("green")
dell.penup()
dell.goto(x=-230, y=20)

wall = Turtle(shape="turtle")
wall.color("orange")
wall.penup()
wall.goto(x=-230, y=60)

tom = Turtle(shape="turtle")
tom.color("purple")
tom.penup()
tom.goto(x=-230, y=100)

screen.exitonclick()