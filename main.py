from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Choose a color: ")
colors = ['red', 'orange', 'black', 'green', 'blue', 'purple']

starting_y = -80

for turtle_idx in range(len(colors)):
    tim = Turtle(shape='turtle')
    tim.color(colors[turtle_idx])
    tim.penup()
    tim.goto(x=-240, y=starting_y)
    starting_y += 30

screen.exitonclick()
