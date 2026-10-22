"""Practical: 2.7 Modular Calculator"""

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
def power(a, b): return a ** b

while True:
    print("\n1.Add  2.Subtract  3.Multiply  4.Divide  5.Power  6.Exit")
    choice = input("Choose an option: ")
    if choice == "6":
        print("Goodbye!")
        break
    if choice not in {"1", "2", "3", "4", "5"}:
        print("Invalid choice.")
        continue
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    try:
        operations = {"1": add, "2": subtract, "3": multiply, "4": divide, "5": power}
        print("Result:", operations[choice](a, b))
    except ZeroDivisionError as error:
        print(error)
