A = []
for i in range(3):
    num = int(input("Enter Number: "))
    A.append(num)

B = []
for i in range(3):
    num = int(input("Enter Number: "))
    B.append(num)

print("First List:", A)
print("Second List:", B)

# Merge manually
merged = []
for num in A + B:
    merged.append(num)
#for num in B:
 #   merged.append(num)

print("Merged List:", merged)