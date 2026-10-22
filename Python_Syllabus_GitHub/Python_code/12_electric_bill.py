"""Practical: 1.12 Electric Bill Calculator"""

previous = int(input("Enter previous meter reading: "))
current = int(input("Enter current meter reading: "))
if current < previous:
    print("Current reading cannot be less than previous reading.")
else:
    units = current - previous
    bill = units * 5.50 + 100
    print("Units consumed:", units)
    print(f"Total bill: Rs. {bill:.2f}")
