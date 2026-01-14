import sympy as sp

# Unknown matrix A
a11, a12, a21, a22 = sp.symbols('a11 a12 a21 a22')
A = sp.Matrix([[a11, a12],
               [a21, a22]])

# Known matrices
M1 = sp.Matrix([[1, -1],
               [1, 2]])

M2 = sp.Matrix([[2, 1],
                 [0, 5]])

# Write equation, for example: (3*A.T + 2*M).T = RHS
expr = (A+(3*M1)).T - (M2)
# Solve
solution = sp.solve(expr, [a11, a12, a21, a22], dict=True)

# Build result
if solution:
    sol = solution[0]
    A_result = sp.Matrix([[sol[a11], sol[a12]],
                          [sol[a21], sol[a22]]])
    print("A =")
    print(A_result)
else:
    print("No solution found")
