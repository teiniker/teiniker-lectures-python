import numpy as np

# Define matrix A (coefficients) and vector B (constants)


A = np.array([[3, 2, 1],
              [2, -2, 4],
              [-1, 0.5, -1]])

B = np.array([1, -2, 0])

# Solve the system AX = B
solution = np.linalg.solve(A, B)

print("Solution:", solution)
