"""Practical: 1.13 Number Classifier"""

n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
print("Even" if n % 2 == 0 else "Odd")
print("Divisible by 5" if n % 5 == 0 else "Not divisible by 5")
