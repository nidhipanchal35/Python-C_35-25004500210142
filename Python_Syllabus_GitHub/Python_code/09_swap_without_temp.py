"""Practical: 1.9 Swap Without Temporary Variable"""

a = float(input("Enter a: "))
b = float(input("Enter b: "))
print("Before swap:", a, b)
a, b = b, a
print("After tuple swap:", a, b)

# Arithmetic swap demonstration
a = a + b
b = a - b
a = a - b
print("After arithmetic swap (swapped back):", a, b)
