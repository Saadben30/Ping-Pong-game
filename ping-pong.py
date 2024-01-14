import turtle

# add screen
wind = turtle.Screen() # inutialize screen
wind.title("ping pong by saad")
wind.bgcolor("black")
wind.setup(height=600, width=800) # size of screen
wind.tracer(0)

#madrab1
madrab1 = turtle.Turtle() # initialize turtle object(shape)
madrab1.speed(0) #set the speed of the aniamtion
madrab1.shape("square") #set the shape of the object
madrab1.color("blue") # color
madrab1.shapesize(stretch_wid=5, stretch_len=1) # size of madrab
madrab1.penup() # don't write 
madrab1.goto(-350, 0) # postion
#madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# score 
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player1: 0  player2: 0", align="center", font=("courier", 24, "normal"))
# functions
def madrab1_up(): 
    y = madrab1.ycor()#set the y of the madrab1
    y+=20# set the y increase be 20
    madrab1.sety(y) # set the of the madrab 1 to the new y cordinate
def madrab1_down():
    y = madrab1.ycor()
    y-=20
    madrab1.sety(y)
def madrab2_up():
    y = madrab2.ycor()
    y+=20
    madrab2.sety(y)
def madrab2_down():
    y = madrab2.ycor()
    y-=20
    madrab2.sety(y)
#keyboard bindings
wind.listen() # tell the window to except keyboard input
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up,  "Up")
wind.onkeypress(madrab2_down, "Down")
#game loop 
while True:
    wind.update()

    # move the ball 
    ball.setx(ball.xcor() + ball.dx) # ball start at 0 and everytime lopps --->+0.5 xaxis
    ball.sety(ball.ycor() + ball.dy)
    
    #boarder check
    if ball.ycor() > 290: # if ball is top border
        ball.sety(290) # set y cordinate +290
        ball.dy *= -1 # reverse direction,  making +2.5 -->0.5
    if ball.ycor() < -290: # if ball is bottom border
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0) #return ball to direction 
        ball.dx *= -1 # reverse the x direction
        score1 += 1
        score.clear()
        score.write("player1: {} player2: {}".format(score1, score2), align="center", font=("courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score.clear()
        score2 += 1
        score.write("player1: {} player2: {}".format(score1, score2), align="center", font=("courier", 24, "normal")) 
    # tasdom madrab and ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1