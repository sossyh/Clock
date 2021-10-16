import turtle
#module used to get local time 
import time
import datetime
# to change the screen color and area 
back_screen=turtle.Screen()
back_screen.bgcolor("ivory2")
back_screen.setup(width=1000, height=800)
mack=turtle.Turtle()

#to draw the clock
def clock(radius,hours,minutes,length,color):
    
    mack.pensize(10)
    mack.penup()
    mack.goto(0,radius)
   
    mack.pendown()
    mack.fillcolor(color)
    mack.pencolor("maroon")
    mack.begin_fill()
    
    for x in range(0,360,360//minutes):
        mack.circle(-radius,360//minutes)
        mack.right(90)
        mack.forward(length/3)
        mack.back(length/3)
        mack.left(90)
    mack.end_fill()
    mack.pencolor("black")
   
   
    for x in range(0,360,360//hours):
        mack.circle(-radius,360//hours)
        mack.right(90)
        mack.forward(length)
        mack.back(length)
        mack.left(90)
    mack.penup()
    mack.forward(2*radius)
    mack.pendown()
    
   
        
#to draw the hands

def hands(angle, radius, width, color, edge_color):
   
        
    mack.pensize(5)
    mack.penup()
    mack.home()
    mack.fillcolor(color)
    mack.begin_fill()
    mack.left(90)
    mack.right(angle)
    mack.forward(radius)
    mack.pendown()
    mack.left(150)
    mack.forward(width)
    mack.home()
    mack.left(90)
    mack.right(angle)
    mack.penup()
    mack.forward(radius)
    mack.pendown()
    mack.right(150)
    mack.forward(width)
    mack.home()
    mack.end_fill()


radius=300
mack.speed(0)
mack.hideturtle()

#calling the clock function to draw the clock
clock(radius,12,60,radius*.1,"peachpuff1")
#getting the current time
now=datetime.datetime.now().time()
#calling the hand function to draw the hands
hands(now.minute * 6, radius * .6, radius // 10, "salmon2","black")
hands(((now.hour + now.minute / 60) % 12) * 30, radius * .3, radius // 15, "salmon3","black")
hands(now.second*6, radius * .9, radius // 20, "salmon4","black")
turtle.tracer(0)
#since the time is always changing we need the loop which changes always then calling the fuctions again
while True:
    new_time=datetime.datetime.now().time()
    if now != new_time:
        clock(radius,12,60,radius*.1,"peachpuff1")
        
        hands(now.second*6, radius * .9, radius // 20, "salmon4","black")
        hands(now.minute * 6, radius * .6, radius // 10, "salmon2","black")
        
        hands(((now.hour + now.minute / 60) % 12) * 30, radius * .3, radius // 10, "salmon3","black")
        
        
    now=new_time
    turtle.update()
    
    mack.clear()





    
    
