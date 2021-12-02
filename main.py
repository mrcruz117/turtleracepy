import turtle
from turtle import Turtle, Screen
import random

race_start = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Choose a color: ")
colors = ['red', 'orange', 'black', 'green', 'blue', 'purple']
all_turtles = []
starting_y = -80

for turtle_idx in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_idx])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=starting_y)
    starting_y += 30
    all_turtles.append(new_turtle)

if user_bet:
    race_start = True
winner = ''
while race_start:
    for turtle in all_turtles:
        if turtle.xcor() >= 220:
            winner = turtle.pencolor()
            race_start = False
        distance = random.randint(10, 20)
        turtle.forward(distance)
if user_bet.lower() == winner.lower():
    print('Your turtle won!!!!')
else:
    print(f"You lost... The winner was {winner}.")

screen.exitonclick()
