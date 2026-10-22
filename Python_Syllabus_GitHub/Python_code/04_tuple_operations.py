"""Practical: 3.4 Tuple Operations"""

marks = (78, 85, 92, 66, 88)
print("Tuple:", marks)
print("First mark:", marks[0])
print("First three marks:", marks[:3])
print("Length:", len(marks))
minimum, maximum, average = min(marks), max(marks), sum(marks) / len(marks)
print("Minimum:", minimum, "Maximum:", maximum, "Average:", average)
try:
    marks[0] = 100
except TypeError as error:
    print("Tuples cannot be modified:", error)
marks_list = list(marks)
marks_list[0] = 100
marks = tuple(marks_list)
print("Modified tuple after list conversion:", marks)
