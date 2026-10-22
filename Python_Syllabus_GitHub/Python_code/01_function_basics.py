def greet(name):
    print(f"Hello, {name}!")

def square(n):
    return n ** 2

def cube(n):
    return n ** 3

for name in ["Nidhi", "Aarav", "Riya"]:
    greet(name)
for number in [2, 4, 6]:
    print(f"Square of {number}: {square(number)}")
for number in [2, 3, 5]:
    print(f"Cube of {number}: {cube(number)}")
