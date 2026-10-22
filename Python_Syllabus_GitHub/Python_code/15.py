A = []

for i in range(5):
    num = int(input("Enter Number: "))
    A.append(num)

print("List:", A)

# Find average
total = 0
for num in A:
    total += num

average = total / len(A)
print("Average:", average)