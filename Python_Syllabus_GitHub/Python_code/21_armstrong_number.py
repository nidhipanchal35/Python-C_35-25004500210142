"""Practical: 1.21 Armstrong Number Finder"""

n = int(input("Enter a non-negative integer: "))
digits = str(n)
total = sum(int(digit) ** len(digits) for digit in digits)
print("Armstrong number" if n >= 0 and total == n else "Not an Armstrong number")

print("Armstrong numbers from 1 to 999:")
for number in range(1, 1000):
    digits = str(number)
    if sum(int(digit) ** len(digits) for digit in digits) == number:
        print(number, end=" ")
print()
