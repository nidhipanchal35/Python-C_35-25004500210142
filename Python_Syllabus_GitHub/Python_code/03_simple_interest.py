"""Practical: 1.3 Simple Interest Calculator"""

principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual rate (%): "))
time = float(input("Enter time in years: "))
si = principal * rate * time / 100
total_amount = principal + si
print(f"Simple Interest: {si:.2f}")
print(f"Total Amount: {total_amount:.2f}")
