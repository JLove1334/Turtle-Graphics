# Justin Love
# Project 2
# Turtle Tv 
# 9/2/2022
import turtle
# open screen for turtle
my_window = turtle.Screen()
# set turtle to a variable 
t = turtle.Turtle()

#First rectangle
t.fillcolor('black')              #Fill the color of the First Screen 
t.begin_fill()
t.forward(300)                    #Start Point 
t.left(90)
t.forward(200)
t.left(90)
t.forward(300)
t.left(90)
t.forward(200)
t.left(90)
t.forward(25)
t.end_fill()

#Second rectangle
t.fillcolor('white')              #Fill the color of the screen 
t.begin_fill()
t.penup()
t.left(90)
t.forward(20)
t.right(90)
t.pendown()
t.forward(250)                    #Start Point of the screen
t.left(90)
t.forward(150)
t.left(90)
t.forward(250)
t.left(90)
t.forward(150)
t.end_fill()


#Tv Stand
t.forward(20)
t.left(90)
t.forward(130)
t.right(90)
t.pensize(5)
t.pendown()
t.pencolor('grey')
t.fillcolor('grey')              #Fill the color of the Tv Stand 
t.begin_fill()
t.forward(25)                     #Start Point of the Tv Stand
t.right(90)                  
t.forward(30)
t.left(90)
t.forward(100)
t.left(90)
t.forward(70)
t.left(90)
t.forward(100)
t.left(90)
t.forward(30)
t.right(90)
t.forward(25)
t.end_fill()

#Tv Stand Speakers
t.penup()
t.right(208)
t.forward(50)
t.pendown()
t.pencolor('black')
t.pensize(3)
r = 20
t.circle(r)
t.penup()
t.left(60)                        #Start of the little circle 
t.forward(18)
t.pendown()
t.fillcolor('black')
t.begin_fill()
r = 10
t.circle(r)
t.end_fill()

#Second Tv Stand Speakers
t.penup()
t.right(47)
t.forward(37)
#t.right(90)
#t.forward(20)
t.pendown()
r = 20
t.circle(r)
t.penup()
t.left(60)                        #Start of the little circle
t.forward(18)
t.pendown()
t.fillcolor('black')
t.begin_fill()
r = 10
t.circle(r)
t.end_fill()
turtle.exitonclick()





