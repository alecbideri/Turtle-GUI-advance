from turtle import Turtle, Screen
import random

# Create a screen object
screen = Screen()
screen.setup(width=500, height=400)

# Ask the user to make a bet on the winning turtle's color
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# List of colors for the turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# List to store turtle objects
turtles = []

# Create turtles with random colors and add them to the list
for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    turtles.append(tim)

# Starting positions for the turtles on the y-axis
y_positions = [-100, -60, -20, 20, 60]

# Ensure that there are enough starting positions for all turtles
while len(turtles) > len(y_positions):
    y_positions.append(y_positions[-1] + 40)

# Position each turtle at its starting position
for index, turtle in enumerate(turtles):
    turtle.goto(x=-230, y=y_positions[index])

# Flag to control the race
is_race_on = False

# If the user made a bet, start the race
if user_bet:
    is_race_on = True

# Main loop to control the race
while is_race_on:
    for turtle in turtles:
        # Check if a turtle has reached the finish line
        if turtle.xcor() > 230:  # Adjust this value based on the screen width
            is_race_on = False
            winning_color = turtle.pencolor()
            # Determine the winner and print the result
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break
        else:
            # Move each turtle forward by a random distance
            turtle.forward(random.randint(1, 10))

# Keep the screen open until the user closes it
screen.mainloop()
