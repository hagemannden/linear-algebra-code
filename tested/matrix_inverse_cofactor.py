import sympy as sp
from fractions import Fraction

# Define the matrix A directly as SymPy Matrix
A = sp.Matrix([
    [1, 2, -1],
    [3, 1, 1],
    [0, 4, 7]
])

print("=" * 50)
print("Using Theorem 3.2.4 - Cofactor Method")
print("=" * 50)
print("\nMatrix A:")
print(A)

# Compute determinant
det_A = A.det()
print(f"\ndet(A) = {det_A}")

# Get cofactor matrix (adjugate is transpose of cofactor matrix)
cofactor_matrix = A.adjugate()
print("\nCofactor Matrix (Adjugate):")
print(cofactor_matrix)

# Entry (1,1) of A^-1: cofactor[1,1] / det(A)
entry_11 = cofactor_matrix[0, 0] / det_A
print(f"\nA^(-1)[1,1] = C[1,1] / det(A) = {cofactor_matrix[0, 0]} / {det_A} = {entry_11}")

# Entry (2,3) of A^-1: cofactor[3,2] / det(A)
entry_23 = cofactor_matrix[2, 1] / det_A
print(f"A^(-1)[2,3] = C[3,2] / det(A) = {cofactor_matrix[2, 1]} / {det_A} = {entry_23}")

print("\n" + "=" * 50)
print("Full Inverse Matrix A^(-1):")
print("=" * 50)
A_inv = A.inv()
sp.pprint(A_inv)
