"""Practical: 1.11 Percentage Calculator"""

marks = []
for i in range(1, 6):
    marks.append(float(input(f"Enter marks for subject {i} (out of 100): ")))
total = sum(marks)
percentage = total / 500 * 100
average = total / 5
print(f"Total: {total:g}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Average: {average:.2f}")
