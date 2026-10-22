"""Practical: 1.10 BMI Calculator"""

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in metres: "))
if height <= 0 or weight <= 0:
    print("Weight and height must be positive.")
else:
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.2f}")
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    print("Category:", category)
