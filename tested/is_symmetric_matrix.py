import numpy as np
import sympy as sp

# Define the matrix A as a NumPy array
A = np.array([[2, 3],
              [4, 5]])

# Check if the matrix is symmetric
is_symmetric = np.allclose(A, A.T)

#Calculate the matrix as the sum of a symmetric matrix
S = (A + A.T) / 2

#Calculate the matrix as the sum of a skew-symmetric matrix
K = (A - A.T) / 2

# Print the result
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)
print("Transpose of A:")
print(A.T)
print("-" * 50)
print("Is matrix symmetric?", is_symmetric)
print("=" * 50)
print("Symmetric part S:")
print(S)
print("-" * 50)
print("Skew-symmetric part K:")
print(K)
print("=" * 50)
