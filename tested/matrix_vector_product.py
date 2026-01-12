import numpy as np

# Define the matrix A
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Define the vector x
x = np.array([[1],
              [2],
              [3]])

# Perform matrix-vector multiplication
result = A @ x

# Print the result
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)
print("Vector x:")
print(x)
print("-" * 50)
print("Result of A @ x:")
print(result)
print("=" * 50)
