import numpy as np

# Define Matrix A
A = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
])

# Define Matrix B
B = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 10]
])

# Find inverse of Matrix A
A_inverse = np.linalg.inv(A)

# Find determinant of Matrix B
B_determinant = np.linalg.det(B)

# Calculate A × A^-1
result = np.dot(A, A_inverse)

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nInverse of Matrix A:")
print(A_inverse)

print("\nDeterminant of Matrix B:")
print(B_determinant)

print("\nResult of A × A^-1:")
print(result)