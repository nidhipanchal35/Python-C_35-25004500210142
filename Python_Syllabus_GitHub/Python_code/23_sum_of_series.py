"""Practical: 1.23 Sum of Series"""

n = int(input("Enter a positive integer N: "))
if n < 1:
    print("Please enter N >= 1.")
else:
    natural_sum = 0
    square_sum = 0
    cube_sum = 0
    for i in range(1, n + 1):
        natural_sum += i
        square_sum += i ** 2
        cube_sum += i ** 3
    print("Sum of natural numbers:", natural_sum)
    print("Sum of squares:", square_sum)
    print("Sum of cubes:", cube_sum)
