import numpy as np
from sympy import Matrix

# Define the matrix A as a NumPy array
A = np.array([[1],  
              [1]])

# Define the matrix B as a NumPy array
B = np.array([[1, 0]])    

# Convert to SymPy matrices 
symA = Matrix(A)
symB = Matrix(B)

# Multiply with SymPy
symC = symA * symB                                       # Matrix multiplication in SymPy
symC = np.array(symC).astype(np.float64)                 # Convert back to NumPy array and print

# Print the resulting
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)
print("Matrix B:")
print(B)
print("=" * 50)
print("Result of A * B:")
print(symC)
print("=" * 50)