import numpy as np
from sympy import Matrix

# Define the matrix A as a NumPy array
A = np.array([[1, 5, 0],
              [2, 4, -1],
              [0, -2, 3]])

# Convert NumPy array to SymPy Matrix
sympy_matrix = Matrix(A)

# Compute the determinant using SymPy
determinant = sympy_matrix.det()

# Print the result
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)
print("Determinant of A:", determinant)
print("=" * 50)
