#Functions
#A function is a reusable block of code.

def greet():
    print("Hello, Ajay")

greet()

# def defines a function.
# greet is the function name.
# greet() calls the function and runs its code.

# 1. Parameters and arguments

def greet(name):
    print("Hello", name)

greet("Ajay")
greet("Rahul")


def multiply(a,b):
    output = a * b
    print(output)
multiply(4, 5)
multiply(3, 7)