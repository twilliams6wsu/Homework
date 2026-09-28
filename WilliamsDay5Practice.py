# ============================================================
# Session 5 Practice — Turtle Graphics: Drawing with Functions
# Introduction to Python  |  Fall 2026  |  Mon Sep 21
# ============================================================
# Instructions:
#   1. Write your code where it says TODO.
#   2. Run the file — a turtle window will open.
#   3. Close the window to move to the next exercise.
#
#   python activities5/practice.py
#
# TIP: set turtle.speed(0) for instant drawing while testing,
#      then slow it down (speed(3)) once it looks right.
# ============================================================
import turtle
turtle.speed(20)

# ── Helper used throughout ────────────────────────────────────────────────
def jump_to(x, y):
    """Move to (x, y) without drawing."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


# ── Reset between exercises ───────────────────────────────────────────────
def reset():
    turtle.clearscreen()
    turtle.speed(0)
    turtle.hideturtle()


# ------------------------------------------------------------
# EXERCISE 1 — draw_square(size)
# ------------------------------------------------------------
# Write a function draw_square(size) that draws a square
# with sides of length `size`.
# Then call it three times with sizes 50, 100, 150.
# Each square should start at a different position so they
# don't overlap — use jump_to() between calls.
#
# Expected result: three separate squares on screen.

# reset()
print("Exercise 1: three squares")

# TODO: define draw_square(size)
def draw_square(size : int):
    for x in range(4):
        turtle.forward(size)
        turtle.left(90)

# TODO: jump to (-150, -75), draw square size 50
# TODO: jump to (-50,  -50), draw square size 100
# TODO: jump to ( 80,  -75), draw square size 150
jump_to(-150,-75)
draw_square(50)
jump_to(-50,-50)
draw_square(100)
jump_to(80,-75)
draw_square(150)
# turtle.done()
# reset()


# ------------------------------------------------------------
# EXERCISE 2 — draw_triangle(size)
# ------------------------------------------------------------
# Write draw_triangle(size) that draws an equilateral triangle.
# Hint: all three angles are 120 degrees (exterior angle).
# Call it with sizes 60, 100, 140 at different positions.
#
# Expected result: three separate triangles.

print("Exercise 2: three triangles")

# TODO: define draw_triangle(size)
def draw_triangle(size: int):
    for x in range(3):
        turtle.forward(size)
        turtle.left(120)

# TODO: three calls at different positions
jump_to(1,1)
draw_triangle(50)
jump_to(2,2)
draw_triangle(100)
jump_to(3,3)
draw_triangle(75)
# turtle.done()
# reset()


# ------------------------------------------------------------
# EXERCISE 3 — draw_polygon(sides, size)
# ------------------------------------------------------------
# Write draw_polygon(sides, size) that draws any regular
# polygon. The exterior angle = 360 / sides.
# Draw these 5 shapes in a row:
#   triangle (3), square (4), pentagon (5), hexagon (6),
#   octagon (8)
# All at size 60, spaced 120 pixels apart horizontally.
#
# Expected result: 5 shapes in a horizontal row.

print("Exercise 3: polygon row")

# TODO: define draw_polygon(sides, size)
def draw_polygon(sides: int, size: int):
    if sides == 1 or sides == 2:
        return
    angle = 360 / sides
    jump_to(100,100)
    for x in range(sides):
        turtle.forward(size)
        turtle.left(angle)


# TODO: draw the 5 shapes in a row
draw_polygon(10,50)
draw_polygon(5,50)
draw_polygon(7,50)


# turtle.done()
# reset()


# ------------------------------------------------------------
# EXERCISE 4 — Colored squares
# ------------------------------------------------------------
# Write draw_colored_square(size, color) that:
#   1. Sets the turtle color
#   2. Calls begin_fill()
#   3. Draws a square
#   4. Calls end_fill()
# Then draw 6 filled squares in a row using these colors:
#   "red", "orange", "yellow", "green", "blue", "purple"
# Each size 70, spaced 80 pixels apart.
#
# Expected result: a rainbow row of filled squares.

print("Exercise 4: rainbow squares")

# TODO: define draw_colored_square(size, color)
def draw_colored_square(size: int, color: str):
    turtle.color(color)
    for x in range(4):
        turtle.forward(size)
        turtle.left(90)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# TODO: loop over colors, jump to position, draw each square
iter = 50
for color in colors:
    
    turtle.color(color)
    jump_to(iter, 100)
    draw_square(50)
    iter += 50
# turtle.done()
# reset()


# ------------------------------------------------------------
# EXERCISE 5 — Nested squares (target pattern)
# ------------------------------------------------------------
# Draw 5 squares, all centered at (0, 0), with sizes
# 40, 80, 120, 160, 200. Each should be a different color.
# Use jump_to() to position the pen at the bottom-left corner
# of each square before drawing.
#
# HINT: the bottom-left corner of a square centered at (0,0)
# with side `s` is at (-s/2, -s/2).
#
# Expected result: concentric squares like a target.

print("Exercise 5: target pattern")

colors = ["red", "orange", "gold", "green", "blue"]
sizes  = [40, 80, 120, 160, 200]

# TODO: loop over sizes and colors, jump to bottom-left, draw
jump_to(-200,200)
for color in colors:
    index = colors.index(color)
    turtle.color(color)
    jump_to(-1 * sizes[index] / 2, -1 *  sizes[index] / 2)
    draw_square(sizes[index])

# turtle.done()
# reset()


# ------------------------------------------------------------
# EXERCISE 6 — Pentagon spiral
# ------------------------------------------------------------
# Draw 20 pentagons (5 sides), each rotated 18 degrees more
# than the previous one, all starting from (0, 0).
# Use size 80 for all pentagons.
# Each pentagon can be a different color — use this list:
#   colors = ["red","orange","gold","lime","cyan",
#             "blue","purple","magenta"] * 3   (repeats)
#
# HINT: after drawing each pentagon, turn left 18 degrees
#       (don't move — just rotate before the next one).
#
# Expected result: a rotated star-like pattern.

print("Exercise 6: pentagon spiral")

colors = ["red","orange","gold","lime","cyan",
          "blue","purple","magenta"] * 3

# TODO: loop 20 times: set color, draw pentagon, turn left 18
for x in range(20):
    color_index = colors[x % 8]
    for side in range(5):
        turtle.forward(30)
        turtle.left(72)
    turtle.left(18)


# turtle.done()
# reset()


# ------------------------------------------------------------
# EXERCISE 7 — Grid of shapes
# ------------------------------------------------------------
# Write draw_grid(shape_fn, size, rows, cols, spacing) that
# draws a grid of any shape (passed as a function argument).
# - shape_fn is a function like draw_square or draw_triangle
# - size is the size argument to pass it
# - rows and cols define the grid dimensions
# - spacing is the distance between shape origins
#
# Call it twice:
#   draw_grid(draw_square,   50, 4, 5, 80)
#   draw_grid(draw_triangle, 50, 3, 6, 80)
#
# HINT: use nested loops for rows and columns.
#
# Expected result: a neat grid of squares, then a grid of
# triangles.
turtle.speed(5)
print("Exercise 7: grid of shapes")
def new_draw_squares(size : int):
    turtle.setheading(0)
    for x in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.setheading(0)

    turtle.up()
    turtle.forward(size)
    turtle.down()

# TODO: define draw_grid(shape_fn, size, rows, cols, spacing)
def draw_grid(shape: function, size : int, rows : int, cols : int, spacing : int):
    jump_to(-450,400)

    for row in range(rows):
        jump_to(-450,(400 - (row * spacing)))

        for column in range(cols):
            shape(size)
            turtle.up()
            turtle.forward(spacing)
            turtle.down()
        turtle.up()
        turtle.setheading(270)
        turtle.forward(spacing)
        turtle.down()
    



# TODO: call draw_grid with squares then triangles
draw_grid(new_draw_squares, 20, 3,3,20)

# turtle.done()
# reset()


# ------------------------------------------------------------
# EXERCISE 8 — CHALLENGE: draw a house
# ------------------------------------------------------------
# Using only draw_square() and draw_triangle() (from earlier),
# draw a simple house:
#   - A square base (size 120) at the bottom
#   - A triangle roof sitting on top of the square
#
# The trick: after drawing the square, you need to move the
# turtle to the bottom-left corner of where the roof goes
# (i.e., the top-left of the square), then face the right
# direction before drawing the triangle.
#
# Add a door: a small rectangle (draw_square(30)) centered
# at the bottom of the house.
#
# BONUS: give the house a different color for walls and roof.
#
# Expected result: a recognizable house shape.

print("Exercise 8 (Challenge): draw a house")

# TODO: draw_house() function using draw_square and draw_triangle


# TODO: call draw_house()


turtle.done()