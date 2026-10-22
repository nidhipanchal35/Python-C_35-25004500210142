A = []

for i in range(5):
    num = int(input("Enter Number: "))
    A.append(num)

print("Original List:", A)

# Reverse using slicing
A.reverse()
print(A)              
