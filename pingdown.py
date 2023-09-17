# import turtle module
import turtle
wind = turtle.Screen()
wind.title("Hitting ball from bottom")
wind.bgcolor("black")
wind.setup(width=600, height=300)
wind.tracer(0)

# set lives
lives = 5

# racket
racket = turtle.Turtle()
racket.speed(0)
racket.shape("square")
racket.shapesize(stretch_len=5, stretch_wid=1)
racket.color("blue")
racket.penup()
racket.goto(0, -125)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 130)
ball.dx = 0.2
ball.dy = 0.2

# add score
score_num = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(-300, 120)
score.write("Score: 0", font=("Courier", 16, "normal"))

# show lives number
life = turtle.Turtle()
life.speed(0)
life.color("white")
life.penup()
life.hideturtle()
life.goto(180, 120)
life.write("lives: 5", font=("Courier", 16, "normal"))


# move racket
def racket_right():
    x = racket.xcor()
    x += 20
    racket.setx(x)

def racket_left():
    x = racket.xcor()
    x -= 20
    racket.setx(x)

# waiting for keyboard input
wind.listen()
wind.onkeypress(racket_right, "Right")
wind.onkeypress(racket_left, "Left")

# game loop
while True:
    wind.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # handle border touching
    if ball.ycor() > 130:
        ball.sety(130)
        ball.dy *= -1
    if ball.xcor() > 280:
        ball.setx(280)
        ball.dx *= -1
    if ball.xcor() < -280:
        ball.setx(-280)
        ball.dx *= -1
    if ball.ycor() < -130:
        if lives == 0:
            ball.setx(0)
            ball.sety(0)
            ball.dx = 0
            ball.dy = 0
            score.clear()
            life.clear()
            score.goto(0, 120)
            score.write("Game Over, Final Score: {}".format(score_num), align="center", font=("Courier", 16, "normal"))
        else:
            ball.goto(0, 130)
            ball.dy *= -1
            lives -= 1
            life.clear()
            life.write("lives: {}".format(lives), font=("Courier", 16, "normal"))
    # hit the racket
    if ball.ycor() < -120  and ball.xcor() < racket.xcor() + 40 and ball.xcor() > racket.xcor() - 40:
        ball.sety(-120)
        ball.dy *= -1
        score_num += 1
        score.clear()
        score.write("Score: {}".format(score_num), font=("Courier", 16, "normal"))
