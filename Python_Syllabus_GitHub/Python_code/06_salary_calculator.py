"""Practical: 1.6 Salary Calculator"""

basic = float(input("Enter basic salary: "))
hra = basic * 0.20
da = basic * 0.10
pf = basic * 0.12
gross = basic + hra + da
net = gross - pf
print(f"HRA: {hra:.2f}")
print(f"DA: {da:.2f}")
print(f"PF: {pf:.2f}")
print(f"Gross salary: {gross:.2f}")
print(f"Net salary: {net:.2f}")
