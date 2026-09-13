#Create a square matrix of 4×4 order. Find out the:
#(i) Eigenvalues and Eigenvectors of this matrix using SciPy.
#(ii) Find out P, L, U (Permutation Matrix, Lower Triangular Matrix, Upper Triangular Matrix).

import numpy as np
from scipy import linalg

A = np.array([[4, 1, 1, 0],
              [1, 4, 0, 1],
              [1, 0, 4, 1],
              [0, 1, 1, 4]])

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

# LU decomposition
P, L, U = linalg.lu(A)

print("\nPermutation Matrix P:")
print(P)

print("\nLower Triangular Matrix L:")
print(L)

print("\nUpper Triangular Matrix U:")
print(U)