"""Practical: 2.12 Lambda Sort"""

students = [
    ("Aarav", 72),
    ("Nidhi", 91),
    ("Riya", 58),
    ("Dev", 84),
    ("Mira", 65),
]
students.sort(key=lambda student: student[1], reverse=True)
print("Students sorted by marks (highest first):")
for name, marks in students:
    print(name, marks)
print("\nStudents with marks >= 60:")
qualified = list(filter(lambda student: student[1] >= 60, students))
for student in qualified:
    print(student)
