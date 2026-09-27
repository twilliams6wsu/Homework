# ============================================================
# CS-135  Homework 2  —  Sessions 5 & 6
# Introduction to Python  |  Fall 2026
# Due: Sunday October 4, 2026  —  Submit via Blackboard
#
# Name:  Tyler Williams
# Date:  Sept 27 2026
#
# How to run:
#   python homework/homework2/homework2.py
#
# NOTE: Turtle exercises open a separate graphics window.
# Close the window to move on to the next exercise.
# ============================================================
import turtle


# ── PART 1: Turtle Graphics (45 points) ─────────────────────

# ── Exercise 1  —  initials(letter1, letter2)  [15 pts] ─────
# Draw your initials (two letters) using only:
#   forward(), backward(), left(), right(), penup(), pendown()
# Rules:
#   - Each letter must be at least 80px tall
#   - Use only straight lines — no curves
#   - The two letters must be side by side with a gap between them
#   - Use t.pensize(3) for a clear stroke width
#
# Steps:
#   1. Create a turtle:   t = turtle.Turtle()
#   2. Set speed:         t.speed(3)
#   3. Use penup() / goto(x, y) / pendown() to position
#   4. Build each letter from straight line segments
#
# Hint: plan each letter on paper first — mark the start
# point, direction, and length of each stroke.
#
# Example — drawing the vertical stroke of a letter:
#   t.penup()
#   t.goto(-80, 80)     # go to the top of the letter
#   t.pendown()
#   t.setheading(270)   # face downward
#   t.forward(160)      # draw a 160px vertical line

def initials(letter1, letter2):
    """Draw two initials side by side using straight lines."""
    t = turtle.Turtle()
    t.speed(20)
    t.pensize(3)
    # Draw letter1 on the left side (around x = -80)
    # YOUR CODE HERE
    t.goto(0,0)
    t.setheading(90)
    t.forward(80)
    t.setheading(0)
    t.forward(20)
    t.backward(40)
    t.penup()
    t.goto(40, 80)
    t.pendown()

    # Draw letter2 on the right side (around x = 40)
    # YOUR CODE HERE
    #40,80
    t.goto(60,0)
    t.goto(70,20)
    t.goto(80,0)
    t.goto(90,80)




# ── Exercise 2  —  checkerboard(squares, size)  [15 pts] ────
# Draw a checkerboard grid of filled squares alternating
# between black and white.
# squares = number of squares per row and column (e.g. 4 = 4×4)
# size    = side length of each small square in pixels
#
# Steps:
#   1. Create a turtle:   t = turtle.Turtle()
#   2. Set speed:         t.speed(0)
#   3. Calculate the top-left starting position so the whole
#      board is centered on screen:
#         start_x = -(squares * size) / 2
#         start_y =  (squares * size) / 2
#   4. Use two nested loops — outer for rows, inner for columns:
#         for row in range(squares):
#             for col in range(squares):
#   5. Inside the inner loop:
#      a. Calculate position:
#            x = start_x + col * size
#            y = start_y - row * size
#      b. Choose color: if (row + col) % 2 == 0 → "black"
#                       else → "white"
#      c. Move to (x, y) using penup() / goto() / pendown()
#      d. Set fill, draw a square (4 sides of length size,
#         turning left 90° each time), end fill

def checkerboard(squares, size):
    """Draw a checkerboard pattern of filled squares."""
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    # YOUR CODE HERE
    start_y = (squares * size) / 2
    t.goto(-(squares * size) / 2, (squares * size) / 2)


    t.shape("square")
    t.shapesize(size / 20, size / 20,2)
    for row in range(squares):
        for col in range(squares):
            t.color("white")
            if (row + col) % 2 == 0:
                t.color("black")
            t.stamp()
            t.penup()
            t.forward(size)
        t.goto(-(squares * size) / 2, start_y - ((row + 1) * size))
    t.pendown()


# ── Exercise 3  —  star(points, size, color)  [15 pts] ──────
# Draw a filled star with the given number of points.
# For any number of points p, the turn angle = 180 - (180 / p)
# A 5-pointed star turns right by 144° each step.
#
# Steps:
#   1. Create a turtle:   t = turtle.Turtle()
#   2. Set speed:         t.speed(6)
#   3. Calculate angle:   angle = 180 - (180 / points)
#   4. Set fill color and call begin_fill()
#   5. Loop `points` times:
#         t.forward(size)
#         t.right(angle)    ← turn RIGHT for a star shape
#   6. Call end_fill()
#
# Then draw TWO more stars at different positions, sizes,
# and colors using penup() / goto() to reposition.
#
# Hint: 5-point star angle = 144°, 6-point = 120°, 7-point ≈ 154°

def star(points, size, color="gold"):
    """Draw a filled star and two more at different positions."""
    t = turtle.Turtle()
    t.speed(6)
    # YOUR CODE HERE
    t.penup()
    t.goto(-100,100)
    t.pendown()
    t.color(color)
    angle = round(720 / points, 0)
    for x in range(points):
        t.forward(size)
        t.right(angle)

    pass

# ── Exercise 4  —  draw_snowflake(size)  ⭐ BONUS  [10 pts] ─
# Draw a 6-armed snowflake using forward(), backward(),
# left(), and right() only. No curves needed.
#
# One arm pattern:
#   forward(size)              → main arm out
#   backward(size / 3)         → back up 1/3
#   left(60)                   → branch left
#   forward(size / 3)          → draw branch
#   backward(size / 3)         → return
#   right(120)                 → branch right
#   forward(size / 3)          → draw branch
#   backward(size / 3)         → return
#   left(60)                   → straighten
#   backward(size * 2 / 3)    → return to center
#
# Repeat 6 times, turning right(60) between each arm.

def draw_snowflake(size):
    """Draw a 6-armed snowflake. BONUS exercise."""
    t = turtle.Turtle()
    t.speed(5)
    t.pencolor("steelblue")
    t.pensize(2)
    # YOUR CODE HERE
    for x in range(6):
            t.forward(size)         
            t.backward(size / 3)         
            t.left(60)                   
            t.forward(size / 3)         
            t.backward(size / 3)       
            t.right(120)               
            t.forward(size / 3)        
            t.backward(size / 3)       
            t.left(60)                
            t.backward(size * 2 / 3)   
            t.right(60)
    turtle.done()


# ── PART 2: Boolean Logic (55 points) ───────────────────────

# ── Exercise 5  —  Boolean Functions  [15 pts] ──────────────
# Write each function so it returns True or False.
# Do NOT use if statements — use comparison operators only.
#
# is_right_triangle(a, b, c) → True if the three sides form a
#   right triangle. A right triangle satisfies the Pythagorean
#   theorem: a² + b² = c² where c is the longest side.
#   Check all three combinations:
#     a**2 + b**2 == c**2  OR
#     a**2 + c**2 == b**2  OR
#     b**2 + c**2 == a**2
#
# is_leap_year(year) → True if the year is a leap year.
#   Rules in order:
#   1. Divisible by 400  → LEAP YEAR    (e.g. 2000 ✓)
#   2. Divisible by 100  → NOT a leap year (e.g. 1900 ✗)
#   3. Divisible by 4    → LEAP YEAR    (e.g. 2024 ✓)
#   4. Otherwise         → NOT a leap year
#   Hint: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#
# is_holiday(month, day) → True if the date matches any of
#   the 3 holidays YOU choose. Pick 3 that are meaningful to
#   you from any culture or tradition. Add a comment above
#   your function saying which holidays you chose and why.
#   Use: (month == M and day == D) or ...
#
# Expected output:
#   is_right_triangle(3, 4, 5)   → True
#   is_right_triangle(5, 12, 13) → True
#   is_right_triangle(3, 4, 6)   → False
#   is_leap_year(2000)           → True
#   is_leap_year(1900)           → False
#   is_leap_year(2024)           → True
#   is_holiday(...)              → depends on your choices

def is_right_triangle(a, b, c):
    return (a ** 2) + (b ** 2) == c



def is_leap_year(year):
    return year % 4 == 0


# Add a comment here explaining your 3 holiday choices:
# My holidays: ...
holidays = {
    "December" : 25,
    "December" : 31,
    "October" : 31
}
def is_holiday(month, day):
    try:
        return holidays[month] == day
    except:
        return False
    pass


# ── Exercise 6  —  if / elif / else  [20 pts] ───────────────
# Write fizzbuzz(n) — a classic programming challenge.
# Count from 1 to n. For each number PRINT (not return):
#   - Divisible by BOTH 3 and 5 → print "FizzBuzz"
#   - Divisible by 3 only       → print "Fizz"
#   - Divisible by 5 only       → print "Buzz"
#   - Otherwise                 → print the number
# Print all on ONE line separated by spaces.
#
# Why FizzBuzz? It's a word game where you replace multiples
# of 3 with "Fizz" and multiples of 5 with "Buzz". Check for
# divisibility by 15 (both 3 AND 5) FIRST or you'll miss it.
#
# Hint: use print(..., end=" ") to print on one line.
#
# Expected output for fizzbuzz(20):
#   1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz

def fizzbuzz(n):
    for x in range(n):
        if (x % 5 == 0) and (x % 3 == 0):
            print("FizzBuzz")
        elif (x % 5 == 0) and (x % 3 != 0):
            print("Buzz")
        elif (x % 5 != 0) and (x % 3 == 0):
            print("Fizz")
        else:
            print(n)



# ── Exercise 7  —  Nested if & Guard Clauses  [20 pts] ──────
# Write parking_cost(hours, is_weekend) that returns the
# parking cost as a formatted string (e.g. "$5.00").
#
# Put the guard clause FIRST, then work top to bottom:
#
# Condition                   Price     Notes
# ─────────────────────────────────────────────────────
# hours < 0                  "Invalid hours"  Guard clause
# hours == 0                 "$0.00"
# hours <= 1                 "$2.00"   First hour flat rate
# hours <= 3                 "$5.00"   Up to 3 hours
# is_weekend (hours > 3)     "$15.00"  Weekend flat rate
# hours <= 8                 "$10.00"  Weekday day rate
# Otherwise                  "$20.00"  Weekday overnight
#
# Expected output:
#   parking_cost(-1, False)  → Invalid hours
#   parking_cost(0,  False)  → $0.00
#   parking_cost(1,  False)  → $2.00
#   parking_cost(2,  False)  → $5.00
#   parking_cost(5,  False)  → $10.00
#   parking_cost(5,  True)   → $15.00
#   parking_cost(10, False)  → $20.00
#   parking_cost(10, True)   → $15.00

def parking_cost(hours, is_weekend):
    if hours < 0:
        print("Invalid hours")


# ── Run all exercises ────────────────────────────────────────
if __name__ == "__main__":

    # ── Part 1: Turtle ────────────────────────────────────────
    # DO NOT MODIFY THIS SECTION — it is used for grading.
    # Each exercise runs automatically one after another.
    # Change the initials on Exercise 1 to YOUR initials.
    # Uncomment Exercise 4 only when you attempt the bonus.

    screen = turtle.Screen()
    screen.tracer(0)

    print("Exercise 1 — initials()")
    initials("T", "W")          # ← change to YOUR initials
    screen.update()
    screen.clear()

    print("Exercise 2 — checkerboard(4, 60)")
    checkerboard(4, 60)
    screen.update()
    screen.clear()

    print("Exercise 3 — star()")
    star(5, 120, "gold")
    screen.update()
    screen.clear()

    # Uncomment when you attempt the bonus:
    print("Exercise 4 — draw_snowflake() BONUS")
    draw_snowflake(100)
    screen.update()
    screen.clear()


    # ── Part 2: Boolean ───────────────────────────────────────
    print()
    print("=" * 50)
    print("Exercise 5 — Boolean Functions")
    print("=" * 50)
    print("is_right_triangle(3,4,5)   →", is_right_triangle(3, 4, 5))
    print("is_right_triangle(5,12,13) →", is_right_triangle(5, 12, 13))
    print("is_right_triangle(3,4,6)   →", is_right_triangle(3, 4, 6))
    print("is_leap_year(2000)         →", is_leap_year(2000))
    print("is_leap_year(1900)         →", is_leap_year(1900))
    print("is_leap_year(2024)         →", is_leap_year(2024))
    print("is_holiday — your test cases here")

    print()
    print("=" * 50)
    print("Exercise 6 — fizzbuzz(20)")
    print("=" * 50)
    fizzbuzz(20)

    print()
    print("=" * 50)
    print("Exercise 7 — parking_cost()")
    print("=" * 50)
    print("parking_cost(-1, False)  →", parking_cost(-1, False))
    print("parking_cost(0,  False)  →", parking_cost(0,  False))
    print("parking_cost(1,  False)  →", parking_cost(1,  False))
    print("parking_cost(2,  False)  →", parking_cost(2,  False))
    print("parking_cost(5,  False)  →", parking_cost(5,  False))
    print("parking_cost(5,  True)   →", parking_cost(5,  True))
    print("parking_cost(10, False)  →", parking_cost(10, False))
    print("parking_cost(10, True)   →", parking_cost(10, True))


