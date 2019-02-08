#  File: Art.py

#  Description: Uses recursive code to draw fractal art

#  Student Name: Braeden Conrad

#  Student UT EID: bsc875

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 02/28/18

#  Date Last Modified: 02/28/18

import turtle
import math

# code for drawing a cross, includes a scale factor
def drawCross(ttl,scale):
    ttl.forward(10*scale)
    ttl.left(90)
    ttl.forward(40*scale)
    ttl.right(90)
    ttl.forward(20*scale)
    ttl.left(90)
    ttl.forward(10*scale)
    ttl.left(90)
    ttl.forward(20*scale)
    ttl.right(90)
    ttl.forward(20*scale)
    ttl.left(90)
    ttl.forward(10*scale)
    ttl.left(90)
    ttl.forward(20*scale)
    ttl.right(90)
    ttl.forward(20*scale)
    ttl.left(90)
    ttl.forward(10*scale)
    ttl.left(90)
    ttl.forward(20*scale)
    ttl.right(90)
    ttl.forward(40*scale)
    ttl.left(90)
# draws the main branch that goes straight up
def drawMainBranch(ttl,order,x=0,y=0,scale=1.0):
    # call function until order decreases to zero
    if (order > 0):
      ttl.penup()
      ttl.goto(x,y)
      ttl.pendown()
      drawCross(ttl,scale)
      ttl.penup()
      ttl.forward(10*scale)
      ttl.right(120)
      ttl.pendown()
      drawCross(ttl,scale)
      ttl.penup()
      ttl.forward(10*scale)
      ttl.right(120)
      ttl.pendown()
      drawCross(ttl,scale)
      ttl.setheading(0)
      #increment y value by the height of the cross
      y += 70*scale
      #recursively call with the scale and order decreasing
      drawMainBranch(ttl,order-1,x,y,scale-.1)
def drawbranch2(ttl,order,x=10,y=0,scale=1.0):
  if (order > 0):
    ttl.penup()
    ttl.right(120)
    # increment the x and y values using geometry plus slight adjustments
    x += 45*math.sqrt(2)*scale
    y -= 35*scale

    ttl.goto(x,y)
    ttl.pendown()
    drawCross(ttl,scale)
    ttl.penup()
    ttl.forward(10*scale)
    ttl.right(120)
    ttl.pendown()
    drawCross(ttl,scale)
    ttl.penup()
    ttl.forward(10*scale)
    ttl.right(120)
    ttl.pendown()
    drawCross(ttl,scale)
    ttl.setheading(0)
    drawbranch2(ttl,order-1,x,y,scale-.1)
def drawbranch3(ttl,order,x=5,y=-10*math.sqrt(2),scale=1.0):
  if (order>0):
    ttl.penup()
    ttl.left(120)
    # decrement x and y using geometry and adjustments
    x -= 45*math.sqrt(2)*scale
    y -= 35*scale
    ttl.goto(x,y)
    ttl.pendown()
    drawCross(ttl,scale)
    ttl.penup()
    ttl.forward(10*scale)
    ttl.right(120)
    ttl.pendown()
    drawCross(ttl,scale)
    ttl.penup()
    ttl.forward(10*scale)
    ttl.right(120)
    ttl.pendown()
    drawCross(ttl,scale)
    ttl.setheading(0)
    drawbranch3(ttl,order-1,x,y,scale-.1)

def main():
    order = int(input("Enter the order(1-6): "))
    while (order<1 and order>6):
        order = int(input("Enter the order (1-6): "))
    turtle.title("Triangular Crosses")
    turtle.setup(800,800,0,0)
    turtle.speed(0)
    ttl = turtle.Turtle()
    ttl.color('green')
    drawMainBranch(ttl,order)
    ttl.color('red')
    drawbranch2(ttl,order)
    ttl.color('blue')
    drawbranch3(ttl,order)

    turtle.done()
main()
