#  File: Train.py

#  Description: File that uses turtle library to draw a train

#  Student Name: Braeden Conrad

#  Student UT EID: bsc875

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 02/11/18

#  Date Last Modified: 02/11/18

import turtle

def draw_spokes(x,y,R,r,ttl):
    ttl.penup()
    ttl.goto(x,y) #go to center
    ttl.setheading(10)
    ttl.forward(r)
    ttl.pendown()
    ttl.forward(R-r)
    ttl.penup()
    ttl.goto(x,y)
    for i in range(7):
        ttl.left(45)
        ttl.penup()
        ttl.forward(r)
        ttl.pendown()
        ttl.forward(R-r)
        ttl.penup()
        ttl.goto(x,y)
    ttl.right(10)
    ttl.penup()
    ttl.forward(r)
    ttl.pendown()
    ttl.forward(R-r)
    ttl.penup()
    ttl.goto(x,y)
    for i in range(7):
        ttl.right(45)
        ttl.penup()
        ttl.forward(r)
        ttl.pendown()
        ttl.forward(R-r)
        ttl.penup()
        ttl.goto(x,y)
    ttl.penup()

def main():
    # put the label
    turtle.title("Braeden's Train")

    # setup screen size
    turtle.setup(800, 800, 0, 0)
    ttl = turtle.Turtle()

    # draw the track
    # draw the top line
    ttl.penup()
    ttl.goto(-200,-200)
    ttl.pendown()
    ttl.goto(200,-200)
    # draw bottom part
    ttl.penup()
    ttl.goto(-200,-210)
    ttl.pendown()
    ttl.goto(200,-210)
    ttl.penup()
    ttl.goto(-200,-210)
    ttl.setheading(0)
    turtle.forward(10)
    for i in range (13):
        ttl.pendown()
        ttl.setheading(270)
        ttl.forward(5)
        ttl.setheading(0)
        ttl.forward(10)
        ttl.setheading(90)
        ttl.forward(5)
        ttl.penup()
        ttl.setheading(0)
        ttl.forward(22)

    #draw bottom frame of train
    ttl.penup()
    ttl.color('blue')
    ttl.goto(-175,-160)
    ttl.setheading(0)
    ttl.pendown()
    ttl.forward(10)
    ttl.left(90)
    ttl.circle(-40,180)
    ttl.setheading(0)
    ttl.forward(40)
    ttl.left(90)
    ttl.circle(-40,180)
    ttl.setheading(0)
    ttl.forward(30)
    ttl.left(90)
    ttl.circle(-40,180)
    ttl.setheading(0)
    ttl.forward(15)
    # draw the wheels
    ttl.color('red')
    # wheel 1
    ttl.penup()
    ttl.goto(-160,-165)
    ttl.setheading(90)
    ttl.pendown()
    ttl.circle(-35,360)
    ttl.setheading(0) #inner circle
    ttl.penup()
    ttl.forward(5)
    ttl.pendown()
    ttl.setheading(90)
    ttl.circle(-30,360)
    ttl.setheading(0)
    ttl.penup()
    ttl.forward(25)
    ttl.pendown()
    ttl.setheading(90)
    ttl.circle(-5,360) #small 2nd inner circle
    draw_spokes(-125,-165,30,5,ttl)
    # wheel 2
    ttl.penup()
    ttl.goto(-35,-170)
    ttl.setheading(90)
    ttl.pendown()
    ttl.circle(-30,360)
    ttl.penup()
    ttl.setheading(0)
    ttl.forward(5)
    ttl.pendown()
    ttl.setheading(90)
    ttl.circle(-25,360)
    ttl.setheading(0)
    ttl.penup()
    ttl.forward(20)
    ttl.pendown()
    ttl.setheading(90)
    ttl.circle(-5,360) #small 2nd inner circle
    draw_spokes(-5,-170,25,5,ttl)
    #wheel3
    ttl.penup()
    ttl.goto(75,-170)
    ttl.setheading(90)
    ttl.pendown()
    ttl.circle(-30,360)
    ttl.penup()
    ttl.setheading(0)
    ttl.forward(5)
    ttl.pendown()
    ttl.setheading(90)
    ttl.circle(-25,360)
    ttl.setheading(0)
    ttl.penup()
    ttl.forward(20)
    ttl.pendown()
    ttl.setheading(90)
    ttl.circle(-5,360) #small 2nd inner circle
    draw_spokes(105,-170,25,5,ttl)
    #outer frame
    ttl.color('blue')
    ttl.penup()
    ttl.goto(-175,-160)
    ttl.setheading(90)
    ttl.pendown()
    ttl.goto(-175,30)
    ttl.penup()
    ttl.goto(-70,-160)
    ttl.pendown()
    ttl.goto(-70,30)
    #rectangle on top
    ttl.setheading(0)
    ttl.forward(10)
    ttl.left(90)
    ttl.forward(5)
    ttl.goto(-185,35)
    ttl.goto(-185,30)
    ttl.goto(-65,30)
    #continue outer part
    ttl.penup()
    ttl.goto(-70,-20)
    ttl.pendown()
    ttl.goto(160,-20)
    ttl.goto(160,-175)
    #front of train
    ttl.goto(190,-175) #bottom line on the train
    ttl.setheading(105)
    ttl.forward(40)
    ttl.setheading(180)
    ttl.setx(160)  #or forward 22
    ttl.penup()
    #rectangles
    ttl.goto(160,-20)
    ttl.goto(160,-30)
    ttl.pendown()
    #big recangle
    ttl.goto(170,-30)
    ttl.goto(170,-120)
    ttl.goto(160,-120)
    #small rectangle
    ttl.penup()
    ttl.goto(170,-60)
    ttl.pendown()
    ttl.goto(175,-60)
    ttl.goto(175,-90)
    ttl.goto(170,-90)

    #windows
    ttl.penup()
    ttl.goto(-155,20)
    #left
    ttl.pendown()
    ttl.begin_fill()
    ttl.color('gray')
    ttl.goto(-130,20)
    ttl.goto(-130,-20)
    ttl.goto(-155,-20)
    ttl.goto(-155,20)
    ttl.end_fill()
    ttl.color('blue')
    ttl.goto(-130,20)
    ttl.goto(-130,-20)
    ttl.goto(-155,-20)
    ttl.goto(-155,20)
    #right
    ttl.penup()
    ttl.goto(-70,30) #right corner
    ttl.goto(-90,20)
    ttl.pendown()
    ttl.begin_fill()
    ttl.color('gray')
    ttl.goto(-115,20)
    ttl.goto(-115,-20)
    ttl.goto(-90,-20)
    ttl.goto(-90,20)
    ttl.end_fill()
    ttl.color('blue')
    ttl.goto(-115,20)
    ttl.goto(-115,-20)
    ttl.goto(-90,-20)
    ttl.goto(-90,20)

    #top rectangles
    ttl.penup()
    ttl.goto(25,-20)
    ttl.pendown()
    ttl.goto(25,-10)
    ttl.goto(45,-10)
    ttl.goto(45,-20)
    ttl.penup()
    ttl.goto(30,-10)
    ttl.pendown()
    ttl.goto(30,-5)
    ttl.goto(40,-5)
    ttl.goto(40,-10)

    #smoke thing
    ttl.penup()
    ttl.goto(100,-20)
    ttl.pendown()
    ttl.goto(90,40)
    ttl.penup()
    ttl.goto(115,-20)
    ttl.pendown()
    ttl.goto(125,40)
    ttl.goto(90,40)
    ttl.goto(95,45)
    ttl.penup()
    ttl.goto(125,40)
    ttl.pendown()
    ttl.goto(120,45)
    ttl.goto(95,45)

    # add in the dot part
    ttl.penup()
    ttl.goto(20,-20)
    ttl.pendown()
    ttl.goto(20,-100)
    ttl.goto(15,-100)
    ttl.goto(15,-20)
    ttl.penup()
    ttl.goto(17.5,-20)
    y = -20
    for i in range (16):
        y-=5
        ttl.pendown()
        ttl.dot(3,'black')
        ttl.penup()
        ttl.goto(17.5,y)

    ttl.penup()
    ttl.goto(-70,-100)
    ttl.pendown()
    ttl.goto(160,-100)
    ttl.goto(160,-105)
    ttl.goto(-70,-105)
    ttl.penup()
    ttl.goto(-70,-102.5)
    x = -70
    for i in range (48):
        x+=5
        ttl.pendown()
        ttl.dot(3,'black')
        ttl.penup()
        ttl.goto(x,-102.5)


    ttl.goto(105,-20)
    ttl.pendown()
    ttl.goto(105,-100)
    ttl.goto(110,-100)
    ttl.goto(110,-20)
    ttl.penup()
    ttl.goto(107.5,-20)
    y = -20
    for i in range (16):
        y-=5
        ttl.pendown()
        ttl.dot(3,'black')
        ttl.penup()
        ttl.goto(107.5,y)



    turtle.done()

main()
