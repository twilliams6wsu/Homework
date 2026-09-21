# ============================================================
# Session 4 Practice — Variables, Strings & Numbers
# Introduction to Python  |  Fall 2026  |  Wed Sep 16
# ============================================================
# Instructions: Write your code where it says TODO, then run:
#   python activities4/practice.py
# ============================================================

print("=" * 52)
print("Session 4 Practice — Variables, Strings & Numbers")
print("=" * 52)
print()


# ------------------------------------------------------------
# EXERCISE 1 — Create and print variables
# ------------------------------------------------------------
# Create three variables:
#   first_name — your first name (str)
#   birth_year — the year you were born (int)
#   height_m   — your height in metres, e.g. 1.75 (float)
# Print each value, then print the type() of each.
#
# Expected output (your values will differ):
#   Jordan
#   2005
#   1.75
#   <class 'str'>
#   <class 'int'>
#   <class 'float'>

print("--- Exercise 1 ---")

# TODO: create the three variables
first_name = "Tyler"
birth_year = 2007
height_m = round(6 * 0.3048,2)



# TODO: print each variable
print(first_name, birth_year, height_m)

# TODO: print type() of each
print(type(first_name), type(birth_year), type(height_m))

print()


# ------------------------------------------------------------
# EXERCISE 2 — String concatenation (no f-strings)
# ------------------------------------------------------------
# Using ONLY the + operator (no f-strings), build and print
# both sentences from these variables. Do NOT retype values.
#
first = "Ada"
last  = "Lovelace"
title = "mathematician"
year  = 1815           # hint: you'll need str(year)
#
# Expected output:
#   Ada Lovelace was a mathematician.
#   Ada Lovelace was born in 1815.

print("--- Exercise 2 ---")

# TODO: sentence 1 using +
print(first + last)

# TODO: sentence 2 using + and str()
print("The year was " + str(year))

print()


# ------------------------------------------------------------
# EXERCISE 3 — f-strings
# ------------------------------------------------------------
# Rewrite both sentences from Exercise 2 using f-strings.
# Same variables, same expected output.

print("--- Exercise 3 ---")

# TODO: f-string version of sentence 1
print(f"{first} {last}")

# TODO: f-string version of sentence 2
print(f"The year was {year}")

print()


# ------------------------------------------------------------
# EXERCISE 4 — Arithmetic explorer
# ------------------------------------------------------------
# Given a = 29, b = 4, print all 7 operators in this format:
#   29 + 4  = 33
# Use f-strings. Do NOT type 29 or 4 directly in the strings.
#
# Expected output:
#   29 + 4  = 33
#   29 - 4  = 25
#   29 * 4  = 116
#   29 / 4  = 7.25
#   29 // 4 = 7
#   29 % 4  = 1
#   29 ** 4 = 707281

print("--- Exercise 4 ---")

a = 29
b = 4

# TODO: seven print statements, one per operator
print(a + b)

print(a - b)

print(a * b)

print(a / b)

print(a // b)

print(a % b)

print(a ** b)


print()


# ------------------------------------------------------------
# EXERCISE 5 — Type detective
# ------------------------------------------------------------
# Before running, predict the TYPE of each expression.
# Write your prediction as a comment, then run to verify.

print("--- Exercise 5 ---")

# A)  5 + 3           Prediction:  Int
print(type(5 + 3))

# B)  5 / 2           Prediction: Float
print(type(5 / 2))

# C)  5 // 2          Prediction: Int
print(type(5 // 2))

# D)  "hello" + "!"   Prediction: String
print(type("hello" + "!"))

# E)  str(99)         Prediction: string
print(type(str(99)))

# F)  int("42")       Prediction: int
print(type(int("42")))

# G)  float(7)        Prediction: float
print(type(float(7)))

print()


# ------------------------------------------------------------
# EXERCISE 6 — Fix the broken code
# ------------------------------------------------------------
# Each block has ONE bug. Find and fix it.
# Expected output after all fixes:
#   The answer is 42
#   3.14
#   Total: 15

print("--- Exercise 6 ---")

# Bug A: can't concatenate str and int
# TODO: fix the line below (hint: convert 42 to a string)
print("The answer is " + str(42))   # ← BUG: fix this line above, then uncomment


# Bug B: wrong variable name
pi_value = 3.14
# TODO: fix the line below (the variable is pi_value, not pi)

print(pi_value)  # DELETE this placeholder

# Bug C: arithmetic on a string
count = "5"
# TODO: fix the line below (count is a str, convert it first)
total = int(count) + 10 
print(f"Total: {total}")

print()


# ------------------------------------------------------------
# EXERCISE 7 — Function with f-string formatting
# ------------------------------------------------------------
# Write describe_book(title, author, pages, price) that prints:
#   "Dune" by Frank Herbert — 688 pages — $12.99
# Use :.2f to format the price to 2 decimal places.
# Call it with three different books.
#
# Expected output:
#   "Dune" by Frank Herbert — 688 pages — $12.99
#   "1984" by George Orwell — 328 pages — $9.50
#   "Python Crash Course" by Eric Matthes — 544 pages — $29.95

print("--- Exercise 7 ---")

# TODO: define describe_book(title, author, pages, price)
def describe_book(title, author, pages, price):
    print("'{title}' by {author} - {pages} pages - ${price}")

# TODO: three calls
describe_book("Dune", "Frank Herbert", 688, 12.99)
describe_book("1984", "George Orwell", 328, 9.50)
describe_book("Python Crash Course", "Eric Matthes", 544, 29.95)

print()


# ------------------------------------------------------------
# EXERCISE 8 — Lab: sum_and_product
# ------------------------------------------------------------
# Write sum_and_product(a, b) that:
#   1. Stores a + b in variable  total
#   2. Stores a * b in variable  product
#   3. Prints:   {a} + {b} = {total}
#                {a} * {b} = {product}
# Call with: (4,5)  (7,3)  (10,10)  (0,99)
#
# Expected output:
#   4 + 5 = 9
#   4 * 5 = 20
#   7 + 3 = 10
#   7 * 3 = 21
#   10 + 10 = 20
#   10 * 10 = 100
#   0 + 99 = 99
#   0 * 99 = 0

print("--- Exercise 8 (Lab) ---")

# TODO: define sum_and_product(a, b)
def sum_and_product(a,b):
    print(f"SUM: {a+b}")
    print(f"PRODUCT: {a*b}")

# TODO: four calls
sum_and_product(3,5)
sum_and_product(9,2)
sum_and_product(10,10)
sum_and_product(9,90)


print()


# ------------------------------------------------------------
# EXERCISE 9 — CHALLENGE: Temperature converter
# ------------------------------------------------------------
# celsius_to_fahrenheit(c):  f = (c * 9/5) + 32
#   prints:  {c}°C = {f:.1f}°F
#
# fahrenheit_to_celsius(f):  c = (f - 32) * 5/9
#   prints:  {f}°F = {c:.1f}°C
#
# Expected output:
#   0°C = 32.0°F
#   100°C = 212.0°F
#   37°C = 98.6°F
#   32°F = 0.0°C
#   212°F = 100.0°C
#   98.6°F = 37.0°C

print("--- Exercise 9 (Challenge) ---")

# TODO: define celsius_to_fahrenheit(c)


# TODO: define fahrenheit_to_celsius(f)


# TODO: calls

def tempConvert():
    temp_value = input("Insert temp to convert:")
    try:
        temp_value = float(temp_value)
    except:
        print("Float/Ints only!")
    temp_name = input("[F/C/K]>>").upper()
    if temp_name == "F":
        print(f"""
            Temp: {temp_value} {temp_name}
            Temp -> Celsius: {round((temp_value - 32) * 5/9,2)}
            Temp -> Kelvin: {round(((temp_value -32) * 5/9) + 273,2)}
        """)
    elif temp_name == "K":
        print(f"""
            Temp: {temp_value} {temp_name}
            Temp -> Celsius: {temp_value - 273}
            Temp -> Fareinheit: {round((temp_value +273)*9/5 + 32,2)}
        """)
    elif temp_name == "C":
        print(f"""
            Temp: {temp_value} {temp_name}
            Temp -> Kelvin: {temp_value + 273}
            Temp -> Fareinheit: {round((temp_value*9/5) + 32,2)}
        """)
    else:
        print("Invalid temp type")

tempConvert()
print()
print("=" * 52)
print("Done! Check your outputs carefully.")
print("=" * 52)

