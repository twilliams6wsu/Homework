#CS-135 Homework 1
#Name: Tyler Williams
#Date: September 16 2026
#Run this file to test all exercises

def greet(name):
    print(f"Hello, {name}")
def greet_class():
    greet("Tyler")
    greet("Jacob")
    greet("Professor Perez")


def about_me():
    eye_color = "Brown"
    age = 18
    height = 6.0
    pet_amount = 2
    sibling_amount = 2
    print(eye_color, type(eye_color))
    print(age, type(age))
    print(height , type(height))
    print(pet_amount, type(pet_amount))
    print(sibling_amount, type(sibling_amount))


def build_sentence():
    first_name = "Tyler"
    last_name = "Williams"
    age = 18
    city = "Leicester"
    print(first_name, last_name)
    print(first_name, "lives in ", city)
    print(first_name, "is ", str(age), "years old")

def build_fstring():
    first_name = "Tyler"
    last_name = "Williams"
    age = 18
    city = "Leicester"
    print(f"{first_name} {last_name}")
    print(f"{first_name}lives in {city}")
    print(f"{first_name} is {age} years old.")

a = 100
b = 50
def arithmetic_explorer(a,b):
    print(f"a = {a}, b = {b}")
    try:
        print(f"{a} + {b} = {a+b}")
        print(f"{a} - {b} = {a-b}")
        print(f"{a} * {b} = {a*b}")
        print(f"{a} / {b} = {a/b}")
        print(f"{a} ** {b} = {a**b}")
        print(f"{a} % {b} = {a%b}")
        print(f"{a} // {b} = {a//b}")
    except:
        print("Only numbers please!")

seconds = 3661
def seconds_analysis(seconds):
    hours = seconds // 3600
    minutes = seconds // 60
    remaining = seconds % 60
    print(f"{hours} hour(s), {minutes} minute(s), and {remaining} second(s)")

def userProfileInit():

    try:
        age = int(input("Input age>"))
    except:
        print("Integers only")
        userProfileInit()
    name = input("Input name>")
    try:
        int(name)
        print("Interesting name!")
    except:
        pass
    try:
        gpa = int(input("Input GPA>"))
    except:
        print("Floats only")
    print("--Profile--")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"GPA: {gpa}")
    print(f"Age in five years (because you can't do math): {age + 5}")

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
