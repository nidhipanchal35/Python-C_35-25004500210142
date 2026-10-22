"""Practical: 3.8 2D Matrix (Nested List)"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print("Matrix:")
for row in matrix:
    print(" ".join(f"{value:4}" for value in row))
for index, row in enumerate(matrix, 1):
    print(f"Sum of row {index}: {sum(row)}")
diagonal_sum = sum(matrix[i][i] for i in range(3))
print("Main diagonal sum:", diagonal_sum)
