"""Practical: 3.1 List Statistics"""

n = int(input("How many numbers? "))
numbers = []
for i in range(n):
    numbers.append(float(input(f"Enter number {i + 1}: ")))
if numbers:
    print("List:", numbers)
    print("Sorted list:", sorted(numbers))
    print("Reversed list:", numbers[::-1])
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
    print("Sum:", sum(numbers))
    print("Average:", sum(numbers) / len(numbers))
else:
    print("No numbers were entered.")
