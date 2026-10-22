"""Practical: 1.20 Star Pattern Collection"""

rows = 5
print("Right-angled triangle")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

print("\nInverted triangle")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print("\nDiamond pattern")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)
