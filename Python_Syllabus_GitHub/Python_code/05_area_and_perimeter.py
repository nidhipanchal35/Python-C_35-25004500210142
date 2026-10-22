"""Practical: 1.5 Area & Perimeter"""

length = float(input("Enter rectangle length: "))
breadth = float(input("Enter rectangle breadth: "))
rectangle_area = length * breadth
perimeter = 2 * (length + breadth)
circle_area = 3.14159 * length ** 2
print(f"Rectangle area: {rectangle_area:.2f}")
print(f"Rectangle perimeter: {perimeter:.2f}")
print(f"Circle area (radius = length): {circle_area:.2f}")
