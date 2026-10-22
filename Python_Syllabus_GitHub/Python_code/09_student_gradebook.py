"""Practical: 3.9 Student Gradebook"""

students = {
    "Nidhi": [88, 92, 95],
    "Aarav": [78, 82, 80],
    "Riya": [91, 89, 94],
    "Dev": [65, 70, 68],
}
averages = {name: sum(marks) / len(marks) for name, marks in students.items()}
print("Students sorted by average (highest first):")
for name, average in sorted(averages.items(), key=lambda item: item[1], reverse=True):
    print(f"{name}: {average:.2f}")
top_student = max(averages, key=averages.get)
print("Top student:", top_student, f"({averages[top_student]:.2f})")
