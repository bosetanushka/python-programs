#Create/consider a square matrix and use the following methods. After printing the result, verify with explanation.

#(i) qr()
#(ii) svd()
#(iii) lstsq()

import numpy as np
from scipy import linalg

A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

b = np.array([3, 7, 11])

# 1. QR decomposition
Q, R = linalg.qr(A)

print("Q matrix:")
print(Q)

print("\nR matrix:")
print(R)

# 2. Singular Value Decomposition
U, S, Vt = linalg.svd(A)

print("\nU matrix:")
print(U)

print("\nSingular values:")
print(S)

print("\nV transpose:")
print(Vt)

# 3. Least Squares
x, residuals, rank, singular_values = linalg.lstsq(A, b)

print("\nLeast Squares Solution:")
print(x)