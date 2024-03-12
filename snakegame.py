import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turns off screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Score
score = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

# Functions
def start_game():
    global score
    start_text.clear()
    game_over_text.clear()
    score_display.clear()
    score = 0
    score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
    head.direction = "stop"
    head.goto(0, 0)
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    move_food()
    move_snake()

def move_food():
    x = random.randint(-14, 14) * 20
    y = random.randint(-14, 14) * 20
    food.goto(x, y)

def move_snake():
    global score
    if head.direction != "stop":
        x = head.xcor()
        y = head.ycor()
        if head.direction == "up":
            head.sety(y + 20)
        elif head.direction == "down":
            head.sety(y - 20)
        elif head.direction == "left":
            head.setx(x - 20)
        elif head.direction == "right":
            head.setx(x + 20)
        # Check collision with food
        if head.distance(food) < 20:
            move_food()
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)
            score += 10
            score_display.clear()
            score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        # Check collision with wall or self
        if (head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290
            or any(segment.distance(head) < 20 for segment in segments)):
            game_over()

def game_over():
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    game_over_text.write("Game Over", align="center", font=("Courier", 36, "normal"))
    game_over_text.goto(0, -50)
    game_over_text.write("Your Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
    start_text.write("Press 'Space' to Start", align="center", font=("Courier", 24, "normal"))

# Start text
start_text = turtle.Turtle()
start_text.speed(0)
start_text.color("white")
start_text.penup()
start_text.hideturtle()
start_text.goto(0, 0)
start_text.write("Press 'Space' to Start", align="center", font=("Courier", 24, "normal"))

# Game over text
game_over_text = turtle.Turtle()
game_over_text.speed(0)
game_over_text.color("white")
game_over_text.penup()
game_over_text.hideturtle()
game_over_text.goto(0, 0)

# Keyboard bindings
screen.listen()
screen.onkeypress(start_game, "space")

# Main loop
while True:
    screen.update()
    move_snake()
    time.sleep(0.1)

screen.mainloop()