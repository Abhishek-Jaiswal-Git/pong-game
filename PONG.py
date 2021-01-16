# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:10:50 2021

@author: abhis
"""

import turtle
screen = turtle.Screen()
screen.title("my first game")
screen.bgcolor("white")
screen.setup(width= 800,height= 600)
screen.tracer(0)
block_1=turtle.Turtle()
block_1.speed(0)
block_1.shape("square")
block_1.shapesize(stretch_wid=5,stretch_len=1)
block_1.color("black")
block_1.penup()
block_1.goto(-350,0)

block_2=turtle.Turtle()
block_2.speed(0)
block_2.shape("square")
block_2.shapesize(stretch_wid=5,stretch_len=1)
block_2.color("black")
block_2.penup()
block_2.goto(350,0)

ball=turtle.Turtle()
ball.speed()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx= 0.1
ball.dy =0.1


def block_1_up():
    y=block_1.ycor()
    y=y+20
    block_1.sety(y)
def block_1_down():
    y=block_1.ycor()
    y=y-20
    block_1.sety(y)
def block_2_up():
    y=block_2.ycor()
    y=y+20
    block_2.sety(y)
def block_2_down():
    y=block_2.ycor()
    y=y-20
    block_2.sety(y)    
screen.listen()
screen.onkeypress(block_1_down,"s")
screen.onkeypress(block_1_up,"w") 
screen.onkeypress(block_2_up,"Up")
screen.onkeypress(block_2_down,"Down")  
while True:
    screen.update()
    
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)
    
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy= ball.dy*-1
    elif ball.ycor()<-290:
        ball.sety(290)
        ball.dy=ball.dy*-1
    elif ball.xcor()>390 or ball.xcor()< -390:
        ball.goto(0,0)
        ball.dx=ball.dx*-1
    elif (ball.xcor()> 340 and ball.xcor()<350) and (ball.ycor()< block_2.ycor()+40 and ball.ycor()> block_2.ycor() -40):
        ball.setx(340)
        ball.dx*= -1
    elif (ball.xcor()< -340 and ball.xcor()<-350) and (ball.ycor()< block_1.ycor()+40 and ball.ycor()> block_1.ycor() +40):
        ball.setx(0)
        ball.dx*= -1
    
   