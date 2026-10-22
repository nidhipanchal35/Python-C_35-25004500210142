"""Practical: 1.19 Number Reversal & Palindrome"""

original = int(input("Enter a non-negative integer: "))
if original < 0:
    print("Please enter a non-negative integer.")
else:
    n = original
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10
    print("Reversed number:", reverse)
    print("Palindrome" if original == reverse else "Not a palindrome")
