from turtle import Turtle, Screen 
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snack Game")
screen.bgcolor("black")
screen.tracer(20)

starting_pos = [(0,0), (-20,0), (-40, 0)]
segments = []


# init snack
for pos in starting_pos:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(pos)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.25)
    
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
screen.exitonclick()