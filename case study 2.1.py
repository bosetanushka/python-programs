#  Consider the following linear equations and solve using SciPy.
#(i) 2x + 3y = 8
#(ii) 4x + 5y = 14

import numpy as np
from scipy import linalg

A = np.array([[2, 3],
             [4, 5]])

B = np.array([8, 14])

solution = linalg.solve(A, B)

print("Solution of equations:")
print("x =", solution[0])
print("y =", solution[1])