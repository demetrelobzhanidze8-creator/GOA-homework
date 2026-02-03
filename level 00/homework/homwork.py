from turtle import *
#draw a house

#starter square

width(6)

speed(5)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#door

forward(75)
left(90)

forward(125)
right(90)

forward(50)
right(90)

forward(125)

#roof
penup()
goto(215,180)
pendown()

right(150)
forward(230)

left(120)
forward(230)

#left wall

penup()
goto(200, 0)
pendown()

left(130)
forward(210)

left(80)
forward(178)



#left roof

penup()
goto(215,180)
pendown()

right(80)
forward(210)

left(110)
forward(230)

left(70)
forward(211)

#lik my ass
penup()
goto(-15, 180)
pendown()

left(180)
forward(15)

#widow
penup()
goto(275, 75)
pendown()

forward(75)

left(80)
forward(75)

left(100)
forward(75)

left(80)
forward(75)

left(100)
forward(37.5)

left(80)
forward(75)

left(100)
forward(37.5)

left(80)
forward(37.5)

left(100)
forward(76)





exitonclick()