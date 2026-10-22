# Write a program to Access the first, last, and middle elements.
A = []

for i in range(5):
    num = int(input("Enter Number: "))
    A.append(num)

print("Length Of List : ",len(A))
print(A[0],A[2],A[4])