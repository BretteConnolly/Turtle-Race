from random import randint
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make Your Bet", "Which turtle will win the race? Pick a color: ") #creates a graphical user interface in which to type one's bet

colors = ["yellow", "orange", "red", "purple", "green", "blue"]
y_coordinates = [165, 99, 33, -33, -99, -165] #turtles placed equidistant from one another in a vertical line
all_turtles = [] #turtles in a list to iterate on
is_race_on = False

for turtle in range(0, 6):
  new_turtle = Turtle("turtle") #create 6 turtles
  new_turtle.color(colors[turtle])
  new_turtle.penup()
  new_turtle.goto(-230, y_coordinates[turtle]) #starting line
  all_turtles.append(new_turtle)

if user_bet:
  is_race_on = True
  
while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor() > 230: #finish line
      is_race_on = False
      print(f"The {turtle.pencolor()} turtle won!")
      if user_bet == turtle.pencolor():
        print("You won!")
      else:
        print("You lost.")
    else:
      rand_distance = randint(0, 10)
      turtle.forward(rand_distance) #every turtle moves forward a different randomly generated distance 
    


screen.exitonclick()