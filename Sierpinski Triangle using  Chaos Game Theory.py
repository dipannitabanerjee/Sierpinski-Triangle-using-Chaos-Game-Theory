import turtle                                                       # import the turtle package
import random                                                       # import the random package

screen = turtle.Screen()                                            # define graphics windows as a playground for the drawing turtles
screen.title('Sierpinski Triangle with Python Turtle')              # provide title for screen
screen.tracer(0,0)                                                  # turn animation on and off
turtle.hideturtle()                                                 # hide the turtle
turtle.speed(0)                                                     # make the turtle go as fast as possible
turtle.up()                                                         # pick up turtle pen

A = (0,300)                                                         # position of vertices
B = (-350,-250)
C = (350,-250)
P = (A,B,C)                                                         # three initial vertices of triangle 
for v in P:
    turtle.goto(v)                                                  # move the turtle to position of the vertices
    turtle.dot('midnight blue')

n = 50000                                                           # number of times the process of point allocation needs to be carried out
p = (random.uniform(-100,100),random.uniform(-100,100))             # random starting point
t = turtle.Turtle()
t.up()
t.hideturtle()

for i in range(n):
    t.goto(p)
    t.dot(2,'blue violet')
    r = random.randrange(len(P))                                    # random vertex to start
    p = ((P[r][0]+p[0])/2,(P[r][1]+p[1])/2)                         # mid point of the random vertex and previous point   
    if i % 1000 == 0:                                               
        t = turtle.Turtle()                                         # use new turtle after every 1000 moves
        t.up()
        t.hideturtle()
        screen.update()
