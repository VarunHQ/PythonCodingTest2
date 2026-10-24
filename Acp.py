def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print("Calculator")

try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    operation = input("Add, Subtract, Multiply or Divide: ")
    if operation == "Add":
        print(add(first_number, second_number))
    elif operation == "Subtract":
        print(subtract(first_number, second_number))
    elif operation == "Multiply":
        print(multiply(first_number, second_number))
    elif operation == "Divide":
        print(divide(first_number, second_number))
    else:
        print("Unknown operation")
          
except ValueError:
    print("Enter only numbers, no letters")
except ZeroDivisionError:
    print("Division with zero is not possible")
finally:
    print("Thank you for using my calculator")
