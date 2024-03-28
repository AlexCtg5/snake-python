from turtle import Turtle
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270
POSITIONS = [(0,0), (-20,0), (-40,0)]
directions = [UP, RIGHT, LEFT, DOWN]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for positions in range(len(POSITIONS)):
            tim = Turtle("square")
            tim.color('chartreuse')
            tim.penup()
            tim.goto(POSITIONS[positions])
            self.segments.append(tim)

    def add_snake(self):
        last_x = self.segments[len(self.segments) - 1].xcor()
        last_y = self.segments[len(self.segments) - 1].ycor()
        tim = Turtle("square")
        tim.color('chartreuse')
        tim.penup()
        for dic in directions:
            if self.segments[len(self.segments)-1].heading() == dic:
                tim.goto(last_x, last_y)
                self.segments.append(tim)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,100)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def move(self):
        for seg_numb in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_numb - 1].xcor()
            new_y = self.segments[seg_numb - 1].ycor()
            self.segments[seg_numb].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)


