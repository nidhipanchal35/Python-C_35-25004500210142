"""Practical: 1.4 Temperature Converter"""

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15
print(f"Fahrenheit: {fahrenheit:.2f} F")
print(f"Kelvin: {kelvin:.2f} K")
