"""Practical: 1.7 Digit Extractor"""

number = int(input("Enter a 3-digit number: "))
number = abs(number)
if 100 <= number <= 999:
    hundreds = number // 100
    tens = (number // 10) % 10
    units = number % 10
    print("Hundreds digit:", hundreds)
    print("Tens digit:", tens)
    print("Units digit:", units)
    print("Sum of digits:", hundreds + tens + units)
    print("Product of digits:", hundreds * tens * units)
else:
    print("Please enter a 3-digit number.")
