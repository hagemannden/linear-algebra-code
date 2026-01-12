import numpy as np

# Define the matrix A as a NumPy array
A = np.array([[ 3,  2],
              [-1,  1]])

# Define the matrix B as a NumPy array
B = np.array([[ 2,  2],
              [-4,  2]])

# Perform matrix subtraction
result = A - B

# Print the result
print("-" * 50)
print("Matrix A:")
print(A)
print("-")
print("Matrix B:")
print(B)
print("-" * 50)
print("Result of A - B:")
print(result)
print("=" * 50)
