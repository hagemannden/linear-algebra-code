import numpy as np

# Define the scalar
c = 2

# Define the matrix A as a NumPy array
A = np.array([[1, 1],
              [-2, 1]])

# Perform scalar multiplication
result = c * A

# Print the result
print("-" * 50)
print(f"Scalar: c = {c}")
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)
print(f"Result of {c}A:")
print(result)
print("=" * 50)
