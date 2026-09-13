#Create a matrix of 4×4 order and find out the transpose of the matrix and the rank of the matrix using SciPy.

import numpy as np
from scipy import linalg

A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [2, 4, 6, 8],
              [1, 3, 5, 7]])

print("Matrix A:")
print(A)

# Transpose
transpose = A.T

print("\nTranspose of A:")
print(transpose)

# Rank
rank = np.linalg.matrix_rank(A)

print("\nRank of A:")
print(rank)