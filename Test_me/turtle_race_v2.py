from turtle import Turtle, Screen
import random

# Create a screen object
screen = Screen()
screen.setup(width=500, height=400)

# Ask the user to make a bet on the winning turtle's color
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# List of colors for the turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70,-40,-10,20,50,80]

# create an object container
all_turtle = []

# Creating 6 turtles with different colors

for turtle_index in range(0,6):
    tim = Turtle(shape= "turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230 , y=y_positions [turtle_index])
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won ! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        else:
            turtle.forward(random.randint(0,10))
screen.exitonclick()