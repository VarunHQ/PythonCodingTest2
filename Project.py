def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)
try:
    a = float(input("Enter first number(in decimal): "))
    b = float(input("Enter second number(in decimal): "))
except ValueError:
    print("Only numbers in decimal.")
except ZeroDivisionError:
    print("Division with 0 is not possible")

    