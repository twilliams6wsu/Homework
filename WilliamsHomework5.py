# ============================================================
# CS-135  Homework 5  —  Session 11
# Introduction to Python  |  Fall 2026
# Due: Sunday October 26, 2026  —  Submit via Blackboard
#
# Name:  Tyler Williams
# Date:  10/21/26
#
# How to run:
#   python homework/homework5/homework5.py
#
# When you run this file you will see:
#   - Your output for each exercise
#   - A self-check section at the bottom showing ✅ or ❌
#     for each expected result — aim for all green!
# ============================================================

# ── About this assignment ─────────────────────────────────────
# You are building a simple grade book program using a dictionary.
# Each exercise adds one piece of functionality.
# All four functions work together — the gradebook you build in
# Exercise 1 is used by Exercises 2, 3, and 4.


# ── Exercise 1  —  build_gradebook(names, grades) ────────────
# Given a list of student names and a list of their grades
# (in the same order), return a dictionary {name: grade}.

def build_gradebook(names, grades):
    empty_dict  = {}
    for i, single_name in enumerate(names):
        empty_dict[single_name] = grades[i]
    return empty_dict


# ── Exercise 2  —  lookup_grade(gradebook, name) ─────────────
# Return the grade for the given student.
# If the student is not in the gradebook, return "Not found".

def lookup_grade(gradebook, name):
    # Step 1: check if name is a key in the gradebook
    # Step 2: return the grade if found, "Not found" if not
    if gradebook.get(name):
        return gradebook.get(name)
    else:
        return "Not found"



# ── Exercise 3  —  update_grade(gradebook, name, new_grade) ──
# Update the grade for an existing student.
# If the student is not in the gradebook, do nothing.
# This function does not return anything.

def update_grade(gradebook, name, new_grade):
    # Step 1: check if the student is in the gradebook
    # Step 2: if yes, update their grade
    if gradebook.get(name):
        gradebook[name] = new_grade



# ── Exercise 4  —  class_average(gradebook) ──────────────────
# Return the average of all grades in the gradebook.
# If the gradebook is empty, return 0.0.

def class_average(gradebook):
    # Step 1: handle the empty gradebook case
    # Step 2: loop through the values and add them up
    # Step 3: divide by the number of students and return
    if gradebook:
        return sum(gradebook.values()) / len(gradebook)
    else:
        return 0.0


# ── Run all exercises ─────────────────────────────────────────
if __name__ == "__main__":

    names  = ["Alice", "Bob", "Carmen", "David"]
    grades = [92, 85, 78, 90]

    print("=" * 50)
    print("Exercise 1 — build_gradebook()")
    print("=" * 50)
    gb = build_gradebook(names, grades)
    print(gb)
    # Expected: {'Alice': 92, 'Bob': 85, 'Carmen': 78, 'David': 90}

    print()
    print("=" * 50)
    print("Exercise 2 — lookup_grade()")
    print("=" * 50)
    print(lookup_grade(gb, "Bob"))      # 85
    print(lookup_grade(gb, "Zara"))     # Not found

    print()
    print("=" * 50)
    print("Exercise 3 — update_grade()")
    print("=" * 50)
    update_grade(gb, "Bob", 91)
    print(lookup_grade(gb, "Bob"))      # 91  (updated)
    update_grade(gb, "Zara", 99)        # does nothing — Zara not in gradebook
    print("Zara" in gb)                 # False

    print()
    print("=" * 50)
    print("Exercise 4 — class_average()")
    print("=" * 50)
    print(class_average(gb))            # 87.75
    print(class_average({}))            # 0.0

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

    names  = ["Alice", "Bob", "Carmen", "David"]
    grades = [92, 85, 78, 90]
    gb = build_gradebook(names, grades)

    check('build_gradebook — Alice → 92',  gb.get("Alice"),  92)
    check('build_gradebook — David → 90',  gb.get("David"),  90)
    check('build_gradebook — 4 entries',   len(gb),          4)

    check('lookup_grade("Bob")  → 85',          lookup_grade(gb, "Bob"),  85)
    check('lookup_grade("Zara") → "Not found"', lookup_grade(gb, "Zara"), "Not found")

    update_grade(gb, "Bob", 91)
    check('update_grade("Bob", 91) → 91',         lookup_grade(gb, "Bob"),  91)
    update_grade(gb, "Zara", 99)
    check('update_grade("Zara", 99) — not added', "Zara" in gb, False)

    check('class_average → 87.75',   class_average(gb), 87.75)
    check('class_average({}) → 0.0', class_average({}), 0.0)
