"""Practical: 1.14 Grade Calculator"""

marks = float(input("Enter marks out of 100: "))
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 35:
    grade = "D"
else:
    grade = "Fail"
print("Grade:", grade)
if marks >= 90:
    print("Distinction")
