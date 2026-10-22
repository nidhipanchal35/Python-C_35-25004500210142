"""Practical: 1.17 Prime Number Checker & List"""

n = int(input("Check whether a number is prime: "))
is_prime = n >= 2
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
print(f"{n} is prime." if is_prime else f"{n} is not prime.")

limit = int(input("Print prime numbers from 2 to: "))
print("Prime numbers:")
for number in range(2, limit + 1):
    prime = True
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            prime = False
            break
    if prime:
        print(number, end=" ")
print()
