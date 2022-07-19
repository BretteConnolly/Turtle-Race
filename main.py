from random import randint
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make Your Bet", "Which turtle will win the race? Pick a color: ")

colors = ["yellow", "orange", "red", "purple", "green", "blue"]
y_coordinates = [165, 99, 33, -33, -99, -165]
all_turtles = []
is_race_on = False

for turtle in range(0, 6):
  new_turtle = Turtle("turtle")
  new_turtle.color(colors[turtle])
  new_turtle.penup()
  new_turtle.goto(-230, y_coordinates[turtle])
  all_turtles.append(new_turtle)

if user_bet:
  is_race_on = True
  
while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor() > 230:
      is_race_on = False
      print(f"The {turtle.pencolor()} turtle won!")
      if user_bet == turtle.pencolor():
        print("You won!")
      else:
        print("You lost.")
    else:
      rand_distance = randint(0, 10)
      turtle.forward(rand_distance)
    


screen.exitonclick()