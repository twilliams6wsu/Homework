# ============================================================
# CS-135  Homework 3  —  Sessions 6 & 7
# Introduction to Python  |  Fall 2026
# Due: Monday October 12, 2026  —  Submit via Blackboard
#
# Name:  Tyler Williams
# Date:  Oct 5 2026
#
# How to run:
#   python homework/homework3/homework3.py
#
# When you run this file you will see:
#   - Your output for each exercise
#   - A self-check section at the bottom showing ✅ or ❌
#     for each expected result — aim for all green!
# ============================================================


# ── Exercise 1  —  describe_number(n)  [20 pts] ────────────────
# Return a descriptive string using NESTED if statements.
#
# Steps:
#   1. Outer if:  check if n > 0
#      Inner if:    check if n is even (n % 2 == 0)
#                   → return "positive even"
#      Inner else:  → return "positive odd"
#   2. Outer elif: check if n < 0
#      Inner if:    check if abs(n) >= 10
#                   → return "large negative"
#      Inner else:  → return "small negative"
#   3. Outer else: (n must be 0)
#      → return "zero"
#
# ⚠  Remember: the INNER if/else must be indented 8 spaces
#    (inside the outer if block).
#
# Expected output:
#   describe_number(4)   → positive even
#   describe_number(7)   → positive odd
#   describe_number(-3)  → small negative
#   describe_number(-15) → large negative
#   describe_number(0)   → zero

def describe_number(n):
    # Step 1: check outer condition (sign of n)
    # Step 2: inside each outer branch, add the inner check
    # Step 3: don't forget the n == 0 case
    if n > 0:
        if n % 2 == 0:
            return "positive even"
        else:
            return "positive odd"
    elif n < 0:
        if abs(n) > 10:
            return "large negative"
        else:
            return "small negative"
    elif n == 0:
        return "zero"
    return None


# ── Exercise 2  —  season(month)  [10 pts] ─────────────────────
# Given a month number (1–12), return the season using a
# flat if/elif/elif/elif/else chain — NO nesting required.
#
# Month ranges:
#   December, January, February  (12, 1, 2)   → "Winter"
#   March, April, May            (3, 4, 5)    → "Spring"
#   June, July, August           (6, 7, 8)    → "Summer"
#   September, October, November (9, 10, 11)  → "Fall"
#
# Guard clause: if month < 1 or month > 12 → return "Invalid month"
#
# Steps:
#   1. Guard clause FIRST: check if month is out of range
#   2. elif month in (12, 1, 2): → return "Winter"
#   3. elif month <= 5:          → return "Spring"
#   4. elif month <= 8:          → return "Summer"
#   5. else:                     → return "Fall"
#
# ⚠  This exercise uses a FLAT if/elif chain — no nested ifs needed.
# ⚠  Note that December (12) is Winter, not Fall.
#
# Expected output:
#   season(1)  → Winter
#   season(3)  → Spring
#   season(7)  → Summer
#   season(10) → Fall
#   season(12) → Winter
#   season(0)  → Invalid month
#   season(13) → Invalid month
months = {
    1 : "Winter",
    2 : "Winter",
    3: "Spring",
    4: "Spring",
    5 : "Spring",
    6: "Summer",
    7: "Summer",
    8: "Summer",
    9: "Fall",
    10 : "Fall",
    11 : "Fall",
    12 : "Winter",
}
def season(month):
    # Step 1: guard clause — is month valid?
    # Step 2: which season is it?
    if month in months:
        return months[month]
    else:
        return "Invalid month"


# ── Exercise 3  —  safe_divide(a, b)  [10 pts] ─────────────────
# Use a guard clause to protect against bad input BEFORE
# doing the division.
#
# Steps:
#   1. Guard clause FIRST: if b == 0, return "Error: division by zero"
#   2. Otherwise: return a / b
#
# ⚠  The guard clause must come BEFORE the calculation.
#    If b is 0 and you divide anyway, Python raises a ZeroDivisionError.
#
# Expected output:
#   safe_divide(10, 2)  → 5.0
#   safe_divide(7,  3)  → 2.3333333333333335
#   safe_divide(10, 0)  → Error: division by zero
#   safe_divide(-6, 2)  → -3.0

def safe_divide(a, b):
    # Step 1: guard clause — check for bad input first
    # Step 2: safe to divide now
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: division by zero"


# ── Exercise 4  —  shipping_cost(weight_kg, destination)  [25 pts]
# Return the shipping cost as a formatted string (e.g. "$6.00")
# using NESTED if statements.
#
# Steps:
#   1. Guard clause FIRST: if destination is not "local" or
#      "national" → return "Unknown destination"
#   2. Outer if/else: check destination
#   3. Inside each destination branch, check weight_kg:
#      Inner if:   weight_kg <= 5  → low rate
#      Inner else: weight_kg > 5   → high rate
#   4. Return the cost as a formatted string e.g. "$6.00"
#
# ⚠  Use f"{cost:.2f}" or just return the string "$6.00" directly.
# ⚠  The inner condition is simple: <= 5 kg or > 5 kg.
#
# Destination    <= 5 kg    > 5 kg
# ──────────────────────────────────
# "local"         $6.00     $10.00
# "national"      $12.00    $20.00
#
# Expected output:
#   shipping_cost(3,  "local")     → $6.00
#   shipping_cost(8,  "local")     → $10.00
#   shipping_cost(3,  "national")  → $12.00
#   shipping_cost(8,  "national")  → $20.00
#   shipping_cost(3,  "overseas")  → Unknown destination

def shipping_cost(weight_kg, destination):
    # Step 1: guard clause — check destination is valid
    # Step 2: outer if/else checks destination
    # Step 3: inner if/else checks weight inside each branch
    if destination == "national":
        if weight_kg <= 5:
            return "$12.00"
        else:
            return "$20.00"
    elif destination == "local":
        if weight_kg <= 5:
            return "$6.00"
        else:
            return "$10.00"
    else:
        return "Unknown destination"





# ── Exercise 5  —  my_max(a, b, c)  [15 pts] ───────────────────
# Recreate Python's built-in max() from scratch using only
# if/elif/else and comparisons.
#
# Steps:
#   1. if a >= b and a >= c:   → return a   (a is biggest)
#   2. elif b >= a and b >= c: → return b   (b is biggest)
#   3. else:                   → return c   (c must be biggest)
#
# ⚠  Do NOT use max() or min() anywhere inside this function.
# ⚠  Test with equal values too — my_max(5, 5, 3) should return 5.
#
# Expected output:
#   my_max(3, 7, 2)  → 7
#   my_max(5, 5, 3)  → 5
#   my_max(-1,-5,-2) → -1
#   my_max(4, 4, 4)  → 4

def my_max(a, b, c):
    # Step 1: is a the largest?
    # Step 2: is b the largest?
    # Step 3: c must be the largest
    if a > b:
        c = a
    else:
        c = b
    return c


# ── Exercise 6  —  letter_to_grade(letter, passing_only)  [20 pts]
# Given a letter grade and a boolean, return a description.
#
# Steps:
#   1. Guard clause FIRST: if letter is not in
#      ["A", "B", "C", "D", "F"] → return "Invalid grade"
#   2. Outer if: passing_only is True
#      Inner if/else: "F" → "Fail", anything else → "Pass"
#   3. Outer else: passing_only is False
#      Inner if/elif/elif/elif/else: map each letter to its description
#        "A" → "Excellent"
#        "B" → "Good"
#        "C" → "Satisfactory"
#        "D" → "Passing"
#        "F" → "Failing"
#
# ⚠  Guard clause must come BEFORE the nested if.
# ⚠  passing_only is a boolean (True/False), not a string.
#
# Expected output:
#   letter_to_grade("A", True)   → Pass
#   letter_to_grade("F", True)   → Fail
#   letter_to_grade("A", False)  → Excellent
#   letter_to_grade("B", False)  → Good
#   letter_to_grade("C", False)  → Satisfactory
#   letter_to_grade("D", False)  → Passing
#   letter_to_grade("F", False)  → Failing
#   letter_to_grade("X", False)  → Invalid grade

letter_desc = {
    "A" : "Excellent",
    "B" : "Good",
    "C" : "Satisfactory",
    "D" : "Passing",
    "F" : "Failing"
}
def letter_to_grade(letter, passing_only):
    # Step 1: guard clause — check letter is valid
    # Step 2: outer if — check passing_only
    # Step 3: inner if/elif — map letter to description
    try:
        if passing_only:
            if letter != "F":
                return "Pass"
            else:
                return "Fail"
        else:
            return letter_desc[letter]
    except KeyError:
        return "Invalid grade"



# ── Run all exercises ─────────────────────────────────────────
if __name__ == "__main__":

    print("=" * 50)
    print("Exercise 1 — describe_number()")
    print("=" * 50)
    print("describe_number(4)   →", describe_number(4))
    print("describe_number(7)   →", describe_number(7))
    print("describe_number(-3)  →", describe_number(-3))
    print("describe_number(-15) →", describe_number(-15))
    print("describe_number(0)   →", describe_number(0))

    print()
    print("=" * 50)
    print("Exercise 2 — season()")
    print("=" * 50)
    print("season(1)  →", season(1))
    print("season(3)  →", season(3))
    print("season(7)  →", season(7))
    print("season(10) →", season(10))
    print("season(12) →", season(12))
    print("season(0)  →", season(0))
    print("season(13) →", season(13))

    print()
    print("=" * 50)
    print("Exercise 3 — safe_divide()")
    print("=" * 50)
    print("safe_divide(10, 2)  →", safe_divide(10, 2))
    print("safe_divide(7,  3)  →", safe_divide(7,  3))
    print("safe_divide(10, 0)  →", safe_divide(10, 0))
    print("safe_divide(-6, 2)  →", safe_divide(-6, 2))

    print()
    print("=" * 50)
    print("Exercise 4 — shipping_cost()")
    print("=" * 50)
    print('shipping_cost(3,  "local")     →', shipping_cost(3,  "local"))
    print('shipping_cost(8,  "local")     →', shipping_cost(8,  "local"))
    print('shipping_cost(3,  "national")  →', shipping_cost(3,  "national"))
    print('shipping_cost(8,  "national")  →', shipping_cost(8,  "national"))
    print('shipping_cost(3,  "overseas")  →', shipping_cost(3,  "overseas"))

    print()
    print("=" * 50)
    print("Exercise 5 — my_max()")
    print("=" * 50)
    print("my_max(3, 7, 2)  →", my_max(3, 7, 2))
    print("my_max(5, 5, 3)  →", my_max(5, 5, 3))
    print("my_max(-1,-5,-2) →", my_max(-1,-5,-2))
    print("my_max(4, 4, 4)  →", my_max(4, 4, 4))

    print()
    print("=" * 50)
    print("Exercise 6 — letter_to_grade()")
    print("=" * 50)
    print('letter_to_grade("A", True)   →', letter_to_grade("A", True))
    print('letter_to_grade("F", True)   →', letter_to_grade("F", True))
    print('letter_to_grade("A", False)  →', letter_to_grade("A", False))
    print('letter_to_grade("B", False)  →', letter_to_grade("B", False))
    print('letter_to_grade("C", False)  →', letter_to_grade("C", False))
    print('letter_to_grade("D", False)  →', letter_to_grade("D", False))
    print('letter_to_grade("F", False)  →', letter_to_grade("F", False))
    print('letter_to_grade("X", False)  →', letter_to_grade("X", False))

    # ── Self-Check ────────────────────────────────────────────
    print()
    print("=" * 50)
    print("Self-Check")
    print("=" * 50)

    def check(label, got, expected):
        if got == expected:
            print(f"  ✅  {label}")
        else:
            print(f"  ❌  {label}")
            print(f"       got:      {repr(got)}")
            print(f"       expected: {repr(expected)}")

    # Exercise 1
    check("describe_number(4)   → 'positive even'",  describe_number(4),   "positive even")
    check("describe_number(7)   → 'positive odd'",   describe_number(7),   "positive odd")
    check("describe_number(-3)  → 'small negative'", describe_number(-3),  "small negative")
    check("describe_number(-15) → 'large negative'", describe_number(-15), "large negative")
    check("describe_number(0)   → 'zero'",           describe_number(0),   "zero")

    # Exercise 2
    check("season(1)  → 'Winter'",        season(1),  "Winter")
    check("season(3)  → 'Spring'",        season(3),  "Spring")
    check("season(7)  → 'Summer'",        season(7),  "Summer")
    check("season(10) → 'Fall'",          season(10), "Fall")
    check("season(12) → 'Winter'",        season(12), "Winter")
    check("season(0)  → 'Invalid month'", season(0),  "Invalid month")
    check("season(13) → 'Invalid month'", season(13), "Invalid month")

    # Exercise 3
    check("safe_divide(10, 2)  → 5.0",                       safe_divide(10, 2),  5.0)
    check("safe_divide(10, 0)  → 'Error: division by zero'",  safe_divide(10, 0),  "Error: division by zero")
    check("safe_divide(-6, 2)  → -3.0",                      safe_divide(-6, 2),  -3.0)

    # Exercise 4
    check('shipping_cost(3,  "local")    → "$6.00"',            shipping_cost(3,  "local"),    "$6.00")
    check('shipping_cost(8,  "local")    → "$10.00"',           shipping_cost(8,  "local"),    "$10.00")
    check('shipping_cost(3,  "national") → "$12.00"',           shipping_cost(3,  "national"), "$12.00")
    check('shipping_cost(8,  "national") → "$20.00"',           shipping_cost(8,  "national"), "$20.00")
    check('shipping_cost(3,  "overseas") → "Unknown destination"', shipping_cost(3, "overseas"), "Unknown destination")

    # Exercise 5
    check("my_max(3, 7, 2)  → 7",  my_max(3, 7, 2),   7)
    check("my_max(5, 5, 3)  → 5",  my_max(5, 5, 3),   5)
    check("my_max(-1,-5,-2) → -1", my_max(-1,-5,-2),  -1)
    check("my_max(4, 4, 4)  → 4",  my_max(4, 4, 4),   4)

    # Exercise 6
    check('letter_to_grade("A", True)  → "Pass"',         letter_to_grade("A", True),  "Pass")
    check('letter_to_grade("F", True)  → "Fail"',         letter_to_grade("F", True),  "Fail")
    check('letter_to_grade("A", False) → "Excellent"',    letter_to_grade("A", False), "Excellent")
    check('letter_to_grade("B", False) → "Good"',         letter_to_grade("B", False), "Good")
    check('letter_to_grade("C", False) → "Satisfactory"', letter_to_grade("C", False), "Satisfactory")
    check('letter_to_grade("D", False) → "Passing"',      letter_to_grade("D", False), "Passing")
    check('letter_to_grade("F", False) → "Failing"',      letter_to_grade("F", False), "Failing")
    check('letter_to_grade("X", False) → "Invalid grade"',letter_to_grade("X", False), "Invalid grade")
