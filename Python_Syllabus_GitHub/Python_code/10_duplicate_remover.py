"""Practical: 3.10 Duplicate Remover"""

numbers = [int(x) for x in input("Enter list 1 numbers separated by spaces: ").split()]
second = [int(x) for x in input("Enter list 2 numbers separated by spaces: ").split()]
unique_numbers = list(set(numbers))
print("List without duplicates (order may change):", unique_numbers)
print("Elements in list 1 but not list 2:", sorted(set(numbers) - set(second)))
frequency = {}
for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1
print("Frequency in list 1:", frequency)
