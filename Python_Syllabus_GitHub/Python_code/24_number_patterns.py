"""Practical: 1.24 Number Pattern"""

rows = 5
print("Ascending pattern")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\nDescending pattern")
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
