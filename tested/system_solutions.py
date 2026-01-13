from sympy import Matrix, symbols
from fractions import Fraction
import numpy as np


def to_fraction(val, max_denom=1000):
    """Convert a number to fraction form"""
    try:
        frac = Fraction(str(float(val))).limit_denominator(max_denom)
        return str(frac)
    except:
        return str(val)


def format_matrix(matrix, as_fractions=True, col_width=8):
    """
    Format a SymPy matrix for nice printing.
    
    Args:
        matrix: SymPy Matrix object
        as_fractions: If True, convert values to fractions
        col_width: Width of each column
    
    Returns:
        str: Formatted matrix string
    """
    rows = matrix.rows
    cols = matrix.cols
    
    # Convert matrix to list of lists with formatted strings
    formatted_rows = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = matrix[i, j]
            if as_fractions:
                cell_str = to_fraction(val)
            else:
                try:
                    cell_str = f"{float(val):.6g}"
                except:
                    cell_str = str(val)
            row.append(cell_str)
        formatted_rows.append(row)
    
    # Calculate column widths
    col_widths = []
    for j in range(cols):
        max_width = max(len(formatted_rows[i][j]) for i in range(rows))
        col_widths.append(max(max_width, col_width))
    
    # Build matrix string
    lines = []
    for i, row in enumerate(formatted_rows):
        # Left bracket
        left = "⎡ " if i == 0 else "⎢ " if i < rows - 1 else "⎣ "
        
        # Cells
        cells = []
        for j, val in enumerate(row):
            cells.append(val.rjust(col_widths[j]))
        
        # Right bracket
        right = " ⎤" if i == 0 else " ⎥" if i < rows - 1 else " ⎦"
        
        lines.append(left + "  ".join(cells) + right)
    
    return "\n".join(lines)


def solve_linear_system(A, b):
    """
    Solve linear system Ax = b comprehensively.
    
    Args:
        A (list[list]): Coefficient matrix
        b (list): Right-hand side vector
    
    Returns:
        dict: Complete solution information
    """
    # Convert to SymPy
    A_coeff = Matrix(A)
    b_vec = Matrix(b)
    augmented = A_coeff.row_join(b_vec)
    
    # Basic info
    num_vars = A_coeff.cols
    num_eqs = A_coeff.rows
    rank_A = A_coeff.rank()
    rank_aug = augmented.rank()
    
    # RREF
    rref_matrix, pivot_cols = augmented.rref()
    free_var_indices = [i for i in range(num_vars) if i not in pivot_cols]
    
    # Classification
    if rank_A < rank_aug:
        status = "No solution (Inconsistent)"
        solution_type = "INCONSISTENT"
    elif rank_A == rank_aug == num_vars:
        status = "Unique solution"
        solution_type = "UNIQUE"
    else:
        status = "Infinitely many solutions"
        solution_type = "INFINITE"
    
    return {
        "A": A_coeff,
        "b": b_vec,
        "augmented": augmented,
        "rref": rref_matrix,
        "pivot_cols": pivot_cols,
        "free_var_indices": free_var_indices,
        "rank_A": rank_A,
        "rank_aug": rank_aug,
        "num_vars": num_vars,
        "num_eqs": num_eqs,
        "status": status,
        "solution_type": solution_type,
        "is_homogeneous": all(val == 0 for val in b),
    }


def print_system_analysis(result):
    """Print detailed system analysis"""
    print("-" * 60)
    print("COEFFICIENT MATRIX A:")
    print(format_matrix(result["A"], as_fractions=True))
    print("-" * 60)
    print("CONSTANT VECTOR b:")
    print(format_matrix(result["b"], as_fractions=True))
    print("-" * 60)
    print("AUGMENTED MATRIX [A | b]:")
    print(format_matrix(result["augmented"], as_fractions=True))
    print("-" * 60)
    print("RREF OF AUGMENTED MATRIX:")
    print(format_matrix(result["rref"], as_fractions=True))
    print("-" * 60)
    print(f"Rank(A) = {result['rank_A']}, Rank([A|b]) = {result['rank_aug']}")
    print(f"Number of variables: {result['num_vars']}")
    print(f"Pivot columns (leading variables): {result['pivot_cols']}")
    print(f"Free variables: {result['free_var_indices']}")
    print(f"Number of free variables: {len(result['free_var_indices'])}")
    print("-" * 60)
    print(f"STATUS: {result['status']}")
    print("-" * 60)


def get_unique_solution(result):
    """Extract unique solution if it exists"""
    if result["solution_type"] != "UNIQUE":
        return None
    
    num_vars = result["num_vars"]
    rref = result["rref"]
    pivot_cols = result["pivot_cols"]
    
    solution = {}
    for i, pivot_col in enumerate(pivot_cols):
        solution[f"x{pivot_col + 1}"] = {
            "decimal": float(rref[i, -1]),
            "fraction": to_fraction(rref[i, -1])
        }
    return solution


def get_parametric_solution(result):
    """
    Extract parametric solution for infinite or homogeneous case.
    
    Returns:
        dict with:
        - 'particular': particular solution (non-homogeneous case)
        - 'basis_vectors': basis vectors for solution space
        - 'free_vars': free variable indices
    """
    rref = result["rref"]
    pivot_cols = result["pivot_cols"]
    free_var_indices = result["free_var_indices"]
    num_vars = result["num_vars"]
    
    # Particular solution (set free vars = 0)
    particular = {}
    for i, pivot_col in enumerate(pivot_cols):
        val = rref[i, -1]
        particular[f"x{pivot_col + 1}"] = {
            "decimal": float(val),
            "fraction": to_fraction(val)
        }
    
    # Basis vectors for homogeneous solution
    basis_vectors = []
    for free_var_idx in free_var_indices:
        vec = {}
        # Free variable is 1, others are 0
        for j in range(num_vars):
            if j == free_var_idx:
                vec[f"x{j + 1}"] = 1.0
            elif j in pivot_cols:
                pivot_row = list(pivot_cols).index(j)
                val = -rref[pivot_row, free_var_idx]
                vec[f"x{j + 1}"] = float(val)
            else:
                vec[f"x{j + 1}"] = 0.0
        basis_vectors.append(vec)
    
    return {
        "particular": particular,
        "basis_vectors": basis_vectors,
        "free_vars": free_var_indices
    }


def print_solution(result):
    """Print solution based on system type"""
    if result["solution_type"] == "INCONSISTENT":
        print("✗ No solution exists for this system.")
        return
    
    if result["solution_type"] == "UNIQUE":
        print("✓ UNIQUE SOLUTION:")
        solution = get_unique_solution(result)
        print("\nDecimal:")
        for var, vals in solution.items():
            print(f"  {var} = {vals['decimal']:.6f}")
        print("\nFraction:")
        for var, vals in solution.items():
            print(f"  {var} = {vals['fraction']}")
        return
    
    # INFINITE solutions
    parametric = get_parametric_solution(result)
    is_homogeneous = result["is_homogeneous"]
    
    if is_homogeneous:
        print("✓ HOMOGENEOUS SYSTEM (Infinitely many solutions)")
        print("\nTRIVIAL SOLUTION:")
        for i in range(result["num_vars"]):
            print(f"  x{i + 1} = 0")
        
        print("\nGENERAL SOLUTION:")
        print("x = c₁*v₁ + c₂*v₂ + ... (c₁, c₂, ... ∈ ℝ)")
        print("\nBASIS VECTORS (Decimal):")
        for j, vec in enumerate(parametric["basis_vectors"]):
            vals = [f"{vec[f'x{k+1}']:.6f}" for k in range(result["num_vars"])]
            print(f"  v{j + 1} = [{', '.join(vals)}]ᵀ")
        
        print("\nBASIS VECTORS (Fraction):")
        for j, vec in enumerate(parametric["basis_vectors"]):
            vals = [to_fraction(vec[f'x{k+1}']) for k in range(result["num_vars"])]
            print(f"  v{j + 1} = [{', '.join(vals)}]ᵀ")
    
    else:
        print("✓ NON-HOMOGENEOUS SYSTEM (Infinitely many solutions)")
        particular = parametric["particular"]
        
        print("\nPARTICULAR SOLUTION (free variables = 0):")
        print("Decimal:")
        for i in range(result["num_vars"]):
            var_name = f"x{i + 1}"
            if var_name in particular:
                print(f"  {var_name} = {particular[var_name]['decimal']:.6f}")
            else:
                print(f"  {var_name} = 0")
        
        print("Fraction:")
        for i in range(result["num_vars"]):
            var_name = f"x{i + 1}"
            if var_name in particular:
                print(f"  {var_name} = {particular[var_name]['fraction']}")
            else:
                print(f"  {var_name} = 0")
        
        print("\nGENERAL SOLUTION:")
        print("x = x_p + c₁*v₁ + c₂*v₂ + ... (c₁, c₂, ... ∈ ℝ)")
        
        print("\nBASIS VECTORS FOR HOMOGENEOUS PART (Decimal):")
        for j, vec in enumerate(parametric["basis_vectors"]):
            vals = [f"{vec[f'x{k+1}']:.6f}" for k in range(result["num_vars"])]
            print(f"  v{j + 1} = [{', '.join(vals)}]ᵀ")
        
        print("\nBASIS VECTORS FOR HOMOGENEOUS PART (Fraction):")
        for j, vec in enumerate(parametric["basis_vectors"]):
            vals = [to_fraction(vec[f'x{k+1}']) for k in range(result["num_vars"])]
            print(f"  v{j + 1} = [{', '.join(vals)}]ᵀ")
        
        print("\nPARAMETRIC FORM:")
        for i in range(result["num_vars"]):
            var_name = f"x{i + 1}"
            
            # Particular part
            if var_name in particular:
                base = f"{particular[var_name]['decimal']:.6f}"
            else:
                base = "0"
            
            terms = [base]
            
            # Add basis vector contributions
            for j, vec in enumerate(parametric["basis_vectors"]):
                coeff = vec[var_name]
                if not np.isclose(coeff, 0):
                    if np.isclose(coeff, 1):
                        terms.append(f"c{j + 1}")
                    elif np.isclose(coeff, -1):
                        terms.append(f"-c{j + 1}")
                    else:
                        terms.append(f"{coeff:.6f}*c{j + 1}")
            
            expr = " + ".join(terms).replace("+ -", "- ")
            print(f"  {var_name} = {expr}")


# ============================================================
# EXAMPLE USAGE
# ============================================================
if __name__ == "__main__":
    # Example: Non-homogeneous with infinite solutions
    A = [
        [1, -2],
        [2, -1]
    ]
    b = [3, 0]
    
    print("\n" + "=" * 60)
    print("SOLVING LINEAR SYSTEM")
    print("=" * 60 + "\n")
    
    result = solve_linear_system(A, b)
    print_system_analysis(result)
    print()
    print_solution(result)
    print("\n" + "=" * 60)