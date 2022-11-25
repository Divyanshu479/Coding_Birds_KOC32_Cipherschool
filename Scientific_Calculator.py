import math


# simple functions
# This function to add two numbers
def add(x, y):
    return x + y


# This function to subtract two numbers
def subtract(x, y):
    return x - y


# This function to divide two numbers
def divide(x, y):
    return x / y


# This function to multiply two numbers
def multiply(x, y):
    return x * y


# This function is to square root
def square_root(x):
    return (x ** (1 / 2))


# This function is to exponent
def power(x, y):
    return x ** y


# This function is to find Sine of given angle in degrees
def sin(x):
    return math.sin(math.radians(x))


# This function is to find cosine of given angle in degrees
def cosine(x):
    return math.cos(math.radians(x))


# This function is to find tangent of given angle in degrees
def tangent(x):
    return math.tan(math.radians(x))


# This function is to find Sine of given angle in radians
def sine(x):
    return math.sin(math.radians(x))


# This function is to find cosine of given angle in radians
def cosin(x):
    return math.cos(math.radians(x))


# This function is to find tangent of given angle in radians
def tan(x):
    return math.tan(math.radians(x))


# This function is to convert angle from radians to degrees
def Radians_To_Degrees(x):
    return math.degrees(x)


# This function is to convert angle from degrees to radians
def Degrees_To_Radians(x):
    return math.radians(x)


print("Select operation.")
print("1) Add")
print("2) Subtract")
print("3) Divide")
print("4) Multiply")
print("5) Sqaure Root")
print("6) Power")
print("7) Sin(angle in degrees)")
print("8) Cosine(angle in degrees)")
print("9) Tangent(angle in degrees)")
print("10) Sine(angle in radians)")
print("11) Cosin(angle in radians)")
print("12) Tan(angle in radians)")
print("13) convert angle from radians to degrees")
print("14) convert angle from degrees to radians")

while True:
    # take input from the user
    choice = int(input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14: "))

    if choice in (1, 2, 3, 4,6):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 2:
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 3:
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == 4:
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == 6:
            print(num1, "**", num2, "=", power(num1, num2))


    elif choice == 5:
        num = int(input("Enter the number: "))
        print("sqrt", num, "=", square_root(num))

    elif choice == 7:
        angle = int(input("Enter the angle in degrees: "))
        print("sin(", angle, ")", sin(angle))

    elif choice == 8:
        angle = int(input("Enter the angle in degrees: "))
        print("cos(", angle, ")", cosine(angle))

    elif choice == 9:
        angle = int(input("Enter the angle in degrees: "))
        print("tan(", angle, ")", tangent(angle))

    elif choice == 10:
        angle = int(input("Enter the angle in radians: "))
        print("Sin(", angle, ")", sine(angle))

    elif choice == 11:
        angle = int(input("Enter the angle in radians: "))
        print("cos(", angle, ")", cosin(angle))

    elif choice == 12:
        angle = int(input("Enter the angle in radians: "))
        print("tan(", angle, ")", tan(angle))

    elif choice == 13:
        angle = int(input("Enter the angle: "))
        print(Radians_To_Degrees(angle), "degrees")

    elif choice == 14:
        angle = int(input("Enter the angle: "))
        print(Degrees_To_Radians(angle), "radians")
    else:
        print("Invalid Number")

        # check if the user wants another calculation
        # break the while loop if answer is no
    next_calculation = input("Let's do next calculation?(yes/no)")
    if next_calculation == "no":
        break
    else:
        continue