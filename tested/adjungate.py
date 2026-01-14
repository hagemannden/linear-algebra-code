import sympy as sp

A = sp.Matrix([
    [1, 0, -1],
    [-1, 1, 0],
    [0, -1, 1]
])
print("The adjugate of the matrix is:")
sp.pprint(A.adjugate())