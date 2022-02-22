import turtle
import random
import time

DELAY = 0.075
COLLISION = 1

yourScore = 0
highScore = 0

win = turtle.Screen()
win.title('Classic Snake Game!')
win.bgcolor("green")
win.setup(width = 450, height = 450)
win.tracer(0)

snakeBody = turtle.Turtle()
snakeBody.speed(0)
snakeBody.shape("square")
snakeBody.color("purple")
snakeBody.penup()
snakeBody.goto(0,0)
snakeBody.direction = "stop"

snakeApple = turtle.Turtle()
snakeApple.speed(0)
snakeApple.shape("circle")
snakeApple.color("red")
snakeApple.penup()
snakeApple.goto(0, 100)

scoreSys = turtle.Turtle()
scoreSys.speed(0)
scoreSys.color("black")
scoreSys.penup()
scoreSys.hideturtle()
scoreSys.goto(0, 185)
scoreSys.write("Your Score: {}  High Score {}".format(yourScore, highScore), align = "center", font = ("Calibri", 22, "normal"))

sysBorder = turtle.Turtle()
sysBorder.speed(0)
sysBorder.color("black")
sysBorder.penup()
sysBorder.hideturtle()
sysBorder.goto(0, 160)
sysBorder.write("----------------------------------------".format(), align = "center", font = ("Calibri", 24, "normal"))

snakeSegments = []

def snakeBody_up():
    if snakeBody.direction != "down":
        snakeBody.direction = "up"

def snakeBody_down():
    if snakeBody.direction != "up":
        snakeBody.direction = "down"

def snakeBody_right():
    if snakeBody.direction != "left":
        snakeBody.direction = "right"

def snakeBody_left():
    if snakeBody.direction != "right":
        snakeBody.direction = "left"

def motion():
    if snakeBody.direction == "up":
        y = snakeBody.ycor()
        snakeBody.sety(y + 20)

    if snakeBody.direction == "down":
        y = snakeBody.ycor()
        snakeBody.sety(y - 20)

    if snakeBody.direction == "right":
        x = snakeBody.xcor()
        snakeBody.setx(x + 20)

    if snakeBody.direction == "left":
        x = snakeBody.xcor()
        snakeBody.setx(x - 20)

def bg_teal():
    win.bgcolor("teal")

def bg_coral():
    win.bgcolor("coral")
    
def bg_reset():
    win.bgcolor("green")

win.listen()
win.onkeypress(snakeBody_up, "w")
win.onkeypress(snakeBody_up, "Up")
win.onkeypress(snakeBody_down, "s")
win.onkeypress(snakeBody_down, "Down")
win.onkeypress(snakeBody_right, "d")
win.onkeypress(snakeBody_right, "Right")
win.onkeypress(snakeBody_left, "a")
win.onkeypress(snakeBody_left, "Left")
win.onkeypress(bg_teal, "1")
win.onkeypress(bg_coral, "2")
win.onkeypress(bg_reset, "Tab")

while True:

    win.update()

    if snakeBody.xcor() > 200 or snakeBody.xcor() < -200 or snakeBody.ycor() > 155 or snakeBody.ycor() < -200:
        time.sleep(COLLISION)
        snakeBody.goto(0, 0)
        snakeApple.goto(0, 100)
        snakeBody.direction = "stop"

        for snakeSegment in snakeSegments:
            snakeSegment.goto(1000, 1000)
        snakeSegments.clear()

        yourScore = 0
        scoreSys.clear()
        scoreSys.write("Your Score: {}  High Score: {}".format(yourScore, highScore), align = "center", font = ("Calibri", 22, "normal"))

    if snakeBody.distance(snakeApple) < 20:
        yourScore = yourScore + 1
        scoreSys.clear()
        scoreSys.write("Your Score: {}  High Score: {}".format(yourScore, highScore), align = "center", font = ("Calibri", 22, "normal"))

        if yourScore > highScore:
            highScore = yourScore
        scoreSys.clear()
        scoreSys.write("Your Score: {}  High Score: {}".format(yourScore, highScore), align = "center", font = ("Calibri", 22, "normal"))

    if snakeBody.distance(snakeApple) < 20:
        snakeApple.goto(random.randint(-155, 155), random.randint(-155, 155))

        addSegment = turtle.Turtle()
        addSegment.speed(0)
        addSegment.color("blue")
        addSegment.shape("square")
        addSegment.penup()
        snakeSegments.append(addSegment)
    
    for move in range(len(snakeSegments) - 1, 0, - 1):
        x = snakeSegments[move - 1].xcor()
        y = snakeSegments[move -1].ycor()
        snakeSegments[move].goto(x, y)

    if len(snakeSegments) > 0:
        snakeSegments[0].goto(snakeBody.xcor(), snakeBody.ycor())

    motion()

    for snakeSegment in snakeSegments:
        if snakeSegment.distance(snakeBody) < 20:
            time.sleep(COLLISION)
            snakeBody.goto(0, 0)
            snakeApple.goto(0, 100)
            snakeBody.direction = "stop"

            yourScore = 0
            scoreSys.clear()
            scoreSys.write("Your Score: {}  High Score: {}".format(yourScore, highScore), align = "center", font = ("Calibri", 22, "normal"))
            
            for snakeSegment in snakeSegments:
                snakeSegment.goto(1000, 1000)
            snakeSegments.clear()

    time.sleep(DELAY)