
    # Author : Y.marrakchi
    # GitHub : https://github.com/youness-marrakchi

import turtle
import winsound

win = turtle.Screen() # creating a window
win.title("Python Pong Game | by Y.marrakchi") # giving the window a title
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0) # stops the window from updating to speed up the game

# the score
playerA_Score = 0
playerB_Score = 0

# paddle A
pdl_a = turtle.Turtle()
pdl_a.speed(0) # animation speed
pdl_a.shape("square")
pdl_a.shapesize(stretch_wid=5, stretch_len=1)
pdl_a.color("white")
pdl_a.penup()
pdl_a.goto(-350, 0)

# paddle B
pdl_b = turtle.Turtle()
pdl_b.speed(0)
pdl_b.shape("square")
pdl_b.shapesize(stretch_wid=5, stretch_len=1)
pdl_b.color("white")
pdl_b.penup()
pdl_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed("slow")
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# scoreBoard
sb = turtle.Turtle()
sb.speed(0)
sb.color("white")
sb.penup()
sb.hideturtle()
sb.goto(0, 260)
sb.write("Player A : {} | Player B : {}".format(playerA_Score, playerB_Score), align="center", font=("Ariel", 15, "normal"))

# functionalities
def pdla_Up():
    y = pdl_a.ycor()
    y += 20
    pdl_a.sety(y)

def pdla_Down():
    y = pdl_a.ycor()
    y -= 20
    pdl_a.sety(y)

def pdlb_Up():
    y = pdl_b.ycor()
    y += 20
    pdl_b.sety(y)

def pdlb_Down():
    y = pdl_b.ycor()
    y -= 20
    pdl_b.sety(y)

# keyboard binding
win.listen()
win.onkeypress(pdla_Up, "z")
win.onkeypress(pdla_Down, "s")
win.onkeypress(pdlb_Up, "Up")
win.onkeypress(pdlb_Down, "Down")

# Main Game Loop
while True:
    win.update() # updates the screen everytime the loop runs
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # marking the limits
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        playerA_Score += 1
        sb.clear()
        sb.write("Player A : {} | Player B : {}".format(playerA_Score, playerB_Score), align="center", font=("Ariel", 15, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        playerB_Score += 1
        sb.clear()
        sb.write("Player A : {} | Player B : {}".format(playerA_Score, playerB_Score), align="center", font=("Ariel", 15, "normal"))

    # ball paddle collision
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < pdl_b.ycor() + 50 and ball.ycor() > pdl_b.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < pdl_a.ycor() + 50 and ball.ycor() > pdl_a.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1

    # HighScore animation
    if playerA_Score >= 5 or playerB_Score >= 5:
        sb.color("orange")

    if playerA_Score >= 10 or playerB_Score >= 10:
        sb.color("yellow")

    if playerA_Score >= 25 or playerB_Score >= 25:
        sb.color("green")
        ball.color("green")

    if playerA_Score >= 50:
        sb.color("red")
        pdl_a.color("red")
        ball.color("white")

    if playerB_Score >= 50:
        sb.color("red")
        pdl_b.color("red")
        ball.color("white")

        