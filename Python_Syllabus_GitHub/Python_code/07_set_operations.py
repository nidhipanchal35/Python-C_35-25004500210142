"""Practical: 3.7 Set Operations Lab"""

set1 = {n for n in range(1, 16) if n % 2 == 1}
set2 = {n for n in range(1, 16) if n % 3 == 0}
print("Set 1 (odd numbers):", set1)
print("Set 2 (multiples of 3):", set2)
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Set 1 - Set 2:", set1 - set2)
print("Set 2 - Set 1:", set2 - set1)
print("Symmetric difference:", set1 ^ set2)
