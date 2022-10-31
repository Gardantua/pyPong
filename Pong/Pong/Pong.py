
import turtle
import winsound

wn = turtle.Screen()
wn.title("PING PONG MOTHERFUCKER !!!")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font=("Courier", 24, "bold"))



# Function
def paddle_a_up():
    axis_y = paddle_a.ycor()
    axis_y += 20
    paddle_a.sety(axis_y)

def paddle_a_down():
    axis_y = paddle_a.ycor()
    axis_y -= 20
    paddle_a.sety(axis_y)

def paddle_b_up():
    axis_y = paddle_b.ycor()
    axis_y += 20
    paddle_b.sety(axis_y)

def paddle_b_down():
    axis_y = paddle_b.ycor()
    axis_y -= 20
    paddle_b.sety(axis_y)

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# MAİN GAME LOOP

while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("soundBounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("soundBounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.setx(0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -390:
        ball.setx(0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font=("Courier", 24, "bold"))
        
    # Ball collision
    if 340 <= ball.xcor() <= 350 and paddle_b.ycor() - 40 <= ball.ycor() <= paddle_b.ycor() + 40:
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("soundBounce.wav", winsound.SND_ASYNC)

    if -350 <= ball.xcor() <= -340 and paddle_a.ycor() - 40 <= ball.ycor() <= paddle_a.ycor() + 40:
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("soundBounce.wav", winsound.SND_ASYNC)



