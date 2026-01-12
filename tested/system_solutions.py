import numpy as np
from sympy import Matrix
from fractions import Fraction

# Define coefficient matrix A and constant vector b
A = np.array([[1, 3, 1, 1],
              [2, -2, 1, 2],
              [3, 1, 2, -1]])
b = np.array([[3],
              [8],
              [-1]])

# Create augmented matrix
A_augmented = np.hstack([A, b])
sympy_coeff = Matrix(A)
sympy_augmented = Matrix(A_augmented)

# Helper function to convert float to fraction
def to_fraction(val, max_denom=1000):
    """Convert a number to fraction form"""
    try:
        frac = Fraction(str(val)).limit_denominator(max_denom)
        return str(frac)
    except:
        return str(val)

# Compute RREF
rref_augmented, pivot_cols_augmented = sympy_augmented.rref()
rref_array = np.array(rref_augmented, dtype=float)

# Basic info
num_vars = A.shape[1]
rank_coeff = sympy_coeff.rank()
rank_aug = sympy_augmented.rank()
num_free = num_vars - rank_coeff
free_vars = [i for i in range(num_vars) if i not in pivot_cols_augmented]

print("-" * 50)
print("Coefficient Matrix A:")
print(A)
print("-" * 50)
print("Augmented Matrix [A | b]:")
print(A_augmented)
print("-" * 50)
print("RREF of Augmented Matrix (Decimal):")
print(np.round(rref_array, 4))
print("-" * 50)
print("RREF of Augmented Matrix (Fraction):")
for i in range(len(rref_array)):
    row = []
    for j in range(len(rref_array[i])):
        row.append(to_fraction(rref_array[i, j]))
    print("  [ " + ", ".join(f"{f:>6}" for f in row) + " ]")
print("-" * 50)
print(f"Rank of A: {rank_coeff}, Rank of [A|b]: {rank_aug}")
print(f"Number of leading variables: {rank_coeff}")
print(f"Number of free variables: {num_free}")
print(f"Pivot columns (leading vars): {pivot_cols_augmented}")
print(f"Free variable columns: {free_vars}")
print("-" * 50)

# Check consistency
if rank_coeff != rank_aug:
    print("STATUS: ✗ INCONSISTENT (No Solution)")
elif rank_coeff == rank_aug == num_vars:
    print("STATUS: ✓ CONSISTENT (Unique Solution)")
    solution = rref_array[:num_vars, -1]
    print("Solution (Decimal):")
    for i in range(num_vars):
        print(f"  x{i+1} = {solution[i]:.4f}")
    print("\nSolution (Fraction):")
    for i in range(num_vars):
        print(f"  x{i+1} = {to_fraction(solution[i])}")
else:
    print("STATUS: ✓ CONSISTENT (Infinite Solutions)")
    print("System Type: HOMOGENEOUS" if np.allclose(b, 0) else "System Type: NON-HOMOGENEOUS")
    print(f"Number of free variables: {num_free}")
    
    # Part for homogeneous system - create basis vectors
    if np.allclose(b, 0):
        print("\n" + "=" * 50)
        print("TRIVIAL SOLUTION:")
        print("  x = 0 (always a solution for homogeneous systems)")
        
        # Create basis vectors for each free variable
        basic_solutions = []
        for fv in free_vars:
            vec = np.zeros(num_vars)
            vec[fv] = 1
            for i, pivot in enumerate(pivot_cols_augmented):
                vec[pivot] = -rref_array[i, fv]
            basic_solutions.append(vec)
        
        # BASIC SOLUTION (all parameters = 0)
        print("\n" + "=" * 50)
        print("BASIC SOLUTION (c₁ = c₂ = ... = 0):")
        basic_sol = np.zeros(num_vars)
        for i in range(num_vars):
            print(f"  x{i+1} = 0")
        
        # GENERAL SOLUTION
        print("\n" + "=" * 50)
        print("GENERAL SOLUTION (NONTRIVIAL SOLUTIONS):")
        print("x = c₁*v₁ + c₂*v₂ + ... where c₁, c₂, ... ∈ ℝ")
        print()
        
        # Print basis vectors clearly
        print("BASIS VECTORS (Decimal):")
        for j, vec in enumerate(basic_solutions):
            vec_str = ", ".join([f"{v:.4f}" for v in vec])
            print(f"  v{j+1} = [{vec_str}]ᵀ")
        
        print("\nBASIS VECTORS (Fraction):")
        for j, vec in enumerate(basic_solutions):
            vec_str = ", ".join([to_fraction(v) for v in vec])
            print(f"  v{j+1} = [{vec_str}]ᵀ")
        
        print("\nParametric Form:")
        # Print parametric solution
        exprs = []
        for i in range(num_vars):
            terms = []
            for j, fv in enumerate(free_vars):
                if not np.isclose(basic_solutions[j][i], 0):
                    coeff = basic_solutions[j][i]
                    if np.isclose(coeff, 1):
                        terms.append(f"c{j+1}")
                    elif np.isclose(coeff, -1):
                        terms.append(f"-c{j+1}")
                    else:
                        terms.append(f"{coeff:.4f}*c{j+1}")
            expr = " + ".join(terms).replace("+ -", "- ") if terms else "0"
            exprs.append(expr)
        
        for i, e in enumerate(exprs):
            print(f"  x{i+1} = {e}")
    else:
        # Non-homogeneous case
        # BASIC SOLUTION (all free variables = 0)
        print("\n" + "=" * 50)
        print("BASIC SOLUTION (free variables = 0):")
        print("Decimal:")
        particular = np.zeros(num_vars)
        for i, pivot in enumerate(pivot_cols_augmented):
            if i < len(rref_array):
                particular[pivot] = rref_array[i, -1]
        for i in range(num_vars):
            print(f"  x{i+1} = {particular[i]:.4f}")
        print("Fraction:")
        for i in range(num_vars):
            print(f"  x{i+1} = {to_fraction(particular[i])}")
        
        # Homogeneous part basis vectors
        print("\n" + "=" * 50)
        print("GENERAL SOLUTION:")
        print("x = x_p + c₁*v₁ + c₂*v₂ + ... where c₁, c₂, ... ∈ ℝ")
        print()
        print("Particular Solution x_p (Decimal):")
        for i in range(num_vars):
            print(f"  x_p[{i+1}] = {particular[i]:.4f}")
        print("Particular Solution x_p (Fraction):")
        for i in range(num_vars):
            print(f"  x_p[{i+1}] = {to_fraction(particular[i])}")
        
        # Create homogeneous basis vectors
        basic_solutions = []
        for fv in free_vars:
            vec = np.zeros(num_vars)
            vec[fv] = 1
            for i, pivot in enumerate(pivot_cols_augmented):
                if i < len(rref_array):
                    vec[pivot] = -rref_array[i, fv]
            basic_solutions.append(vec)
        
        print("\nBasis vectors for homogeneous solution (Decimal):")
        for j, vec in enumerate(basic_solutions):
            vec_str = ", ".join([f"{v:.4f}" for v in vec])
            print(f"  v{j+1} = [{vec_str}]ᵀ")
        
        print("\nBasis vectors for homogeneous solution (Fraction):")
        for j, vec in enumerate(basic_solutions):
            vec_str = ", ".join([to_fraction(v) for v in vec])
            print(f"  v{j+1} = [{vec_str}]ᵀ")
        
        print("\nGeneral Solution (Parametric Form):")
        for i in range(num_vars):
            terms = [f"{particular[i]:.4f}"]
            for j, fv in enumerate(free_vars):
                if not np.isclose(basic_solutions[j][i], 0):
                    coeff = basic_solutions[j][i]
                    if np.isclose(coeff, 1):
                        terms.append(f"c{j+1}")
                    elif np.isclose(coeff, -1):
                        terms.append(f"-c{j+1}")
                    else:
                        sign = "+" if coeff > 0 else ""
                        terms.append(f"{sign}{coeff:.4f}*c{j+1}".replace("+-", "-"))
            expr = " + ".join(terms).replace("+ -", "- ")
            print(f"  x{i+1} = {expr}")

print("=" * 50)