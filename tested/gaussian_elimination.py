import numpy as np
from sympy import Matrix

def row_echelon_form(matrix):
    """Convert matrix to row echelon form (REF) using Gaussian elimination."""
    M = matrix.copy()
    rows, cols = M.shape
    current_row = 0
    
    for col in range(cols):
        # Find pivot
        pivot_row = None
        for row in range(current_row, rows):
            if M[row, col] != 0:
                pivot_row = row
                break
        
        if pivot_row is None:
            continue
        
        # Swap rows if needed
        if pivot_row != current_row:
            M[[current_row, pivot_row]] = M[[pivot_row, current_row]]
        
        # Scale pivot row so leading entry is 1
        pivot_value = M[current_row, col]
        M[current_row] = M[current_row] / pivot_value
        
        # Eliminate below
        for row in range(current_row + 1, rows):
            if M[row, col] != 0:
                factor = M[row, col]
                M[row] = M[row] - factor * M[current_row]
        
        current_row += 1
        if current_row >= rows:
            break
    
    return M

# Define the augmented matrix [A | b]
# System: 2x + 3y + z = 11
#         x - y + 2z = 8
#         3x + y - z = 6
A = np.array([[10, 20, 5060],
              [50, 30, 14310],
              [30, 30, 10470]], dtype=np.float64)

# Compute Row Echelon Form (REF)
ref_matrix = row_echelon_form(A)

# Convert to SymPy Matrix for RREF
sympy_matrix = Matrix(A)

# Perform Gaussian elimination to reduced row echelon form
row_echelon = sympy_matrix.rref()

# Extract the RREF matrix
rref_matrix = row_echelon[0]
numpy_rref = np.array(rref_matrix, dtype=np.float64)

# Print the results
print("-" * 50)
print("Original matrix:")
print(A)
print("-" * 50)
print("Row Echelon Form (REF):")
print(ref_matrix)
print("-" * 50)
print("Reduced Row Echelon Form (RREF):")
print(numpy_rref)
print("=" * 50)
