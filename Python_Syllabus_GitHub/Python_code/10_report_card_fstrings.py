"""Practical: 2.10 Report Card with f-strings"""

student_name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
marks = [float(input(f"Enter marks for subject {i} (out of 100): ")) for i in range(1, 6)]
total = sum(marks)
percentage = total / 500 * 100
if percentage >= 90: grade = "A+"
elif percentage >= 80: grade = "A"
elif percentage >= 70: grade = "B"
elif percentage >= 60: grade = "C"
elif percentage >= 35: grade = "D"
else: grade = "Fail"

print("\n" + "=" * 35)
print(f"{'STUDENT REPORT CARD':^35}")
print("=" * 35)
print(f"{'Name:':<15}{student_name}")
print(f"{'Roll No:':<15}{roll_no}")
for i, mark in enumerate(marks, 1):
    print(f"{('Subject ' + str(i) + ':'):<15}{mark:>6.2f}")
print("-" * 35)
print(f"{'Total:':<15}{total:>6.2f}/500")
print(f"{'Percentage:':<15}{percentage:>6.2f}%")
print(f"{'Grade:':<15}{grade}")
print("=" * 35)
