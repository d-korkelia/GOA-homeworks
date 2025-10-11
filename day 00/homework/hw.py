from turtle import *

#we want to paint a house


#step 1: draw a square
speed(30)
width(8)
color("grey")
forward (190)
left(90)

forward(190)
left(90)

forward(190)
left(90)

forward(190)
left(90)
# end of square

#drawing a door


forward(80)
color("black")
begin_fill()
left(90)
forward(100)     #height of the door
right(90)
forward(30)
right(90)
forward(100)
end_fill()

penup()
goto(190,190)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(123)
forward(200)
end_fill()

#drawing a window

penup()
goto(60,60)
pendown()

color("brown")
begin_fill()
right(150)
forward(60)
left(90)
forward(40)
right(40)
left(120)
forward(60)
left(100)
forward(50)

#drawing second window

penup()
goto(120,120)
pendown()

color("brown")
begin_fill()
forward(60)
left(90)
right(180)
forward(60)
left(90)
right(180)
forward(60)
right(90)
forward(60)








exitonclick()