import turtle
import random


my_screen = turtle.Screen()
my_screen.setup(width=500, height=400)
bet = my_screen.textinput(
    title="Make your bet!", prompt="Which turtle is going to win? Enter a color: "
).lower()

color = ["red", "orange", "yellow", "green", "blue", "purple"]

y = 0

turtles = []

for i in range(len(color)):
    item = turtle.Turtle(shape="turtle")
    item.color(color[i])
    item.penup()
    item.goto(x=-230, y=-100 + y)
    y += 50
    turtles.append(item)

print(turtles)

game = True
while game:
    for objects in turtles:
        objects.forward(random.randint(1, 10))
        if objects.xcor() > 230:
            game = False
            winning_color = objects.pencolor()
            if winning_color == bet:
                print(f"You've won. {winning_color} turtle is the winner")
            else:
                print(f"You've lost. {winning_color} turtle is the winner")


my_screen.exitonclick()
