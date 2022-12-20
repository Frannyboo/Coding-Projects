# from turtle import Turtle, Screen
# chuka = Turtle()
# chuka.shape("turtle")
# chuka.color("red")
# chuka.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "fire"])
table.align = "l"
print(table)