import turtle

def draw_square(color, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

def draw_chessboard():
    size = 50  # Size of each square
    colors = ["white", "black"]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            x = col * size - 200  # Shifting the board to the left
            y = row * size - 200  # Shifting the board downwards
            draw_square(color, x, y, size)

def main():
    turtle.speed(0)  # Set the turtle's speed to maximum
    turtle.hideturtle()  # Hide the turtle icon
    draw_chessboard()
    turtle.done()

if __name__ == "__main__":
    main()