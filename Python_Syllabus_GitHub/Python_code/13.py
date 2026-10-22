A = []

for i in range(5):
    num = int(input("Enter Number: "))
    A.append(num)

print("Original List:", A)

# Remove duplicates manually
unique_list = []
for num in A:
    if num not in unique_list:
        unique_list.append(num)

print("List without duplicates:", unique_list)