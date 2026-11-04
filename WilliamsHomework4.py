"""Homework 4: Lists, Strings, and Tuples (CS-135)

Name: Tyler Williams
"""


# Exercise 1
def copy_and_add(lst, item):
    """Return a new list with item added at the end. lst is not changed."""
    new_lst = lst.copy()
    new_lst.append(item)
    return new_lst
    pass


# Exercise 2
def move_to_front(lst, item):
    """Move the first copy of item to the front of lst, in place."""
    lst.insert(0, lst.pop(lst.index(item)))
    return lst
    pass


# Exercise 3
def top_three(scores):
    """Return the three highest scores, highest first. scores is not changed."""
    scores_list = sorted(scores.copy(),reverse=True)
    return scores_list[:3]
    pass


# Exercise 4
def min_max_avg(numbers):
    """Return (smallest, largest, average), or (None, None, None) if empty."""
    if len(numbers) == 0: return (None, None, None)
    return (min(numbers), max(numbers), sum(numbers) / len(numbers))
    pass


# Exercise 5: Fix the Tuple Bugs
# Each function below has a mistake. Fix it, and add a short comment above
# each fix saying what was wrong.
def swap_pair(pair):
    """Return a new tuple with the two items swapped."""
    #Tuples are immutable.

    return (pair[1], pair[0])


def make_single(x):
    """Return a tuple holding just the one item x."""
    #(x) is of type int, (x,) is of type tuple
    return (x,)


if __name__ == "__main__":
    # Test your functions here with assert statements.
    copy_and_add([1, 2, 3, 4], 5)
    move_to_front([1, 2, 3, 4], 3)
    top_three([1, 2, 3, 4])
    min_max_avg([1, 2, 3, 4])
    swap_pair([1, 2])
    make_single("Hi")
    pass
