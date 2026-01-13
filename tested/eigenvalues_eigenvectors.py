
# *** defin a matrix at the bottom and run the analysis ***

import numpy as np
from sympy import Matrix

def eigen_analysis(A):
    M = Matrix(A)
    n = M.shape[0]

    print("=" * 60)
    print("Matrix A:")
    print(M)
    print("=" * 60)

    # Eigenvalues (unikke + multiplicitet)
    eigenvals = M.eigenvals()
    eigenvects = M.eigenvects()

    # Fuld liste med gentagelser
    lambda_list = []
    for val, mult in eigenvals.items():
        lambda_list.extend([val] * mult)

    lambda_list = sorted(lambda_list)

    print("Egenværdier:")
    for i, val in enumerate(lambda_list, start=1):
        print(f"  λ{i} = {val}")

    print("-" * 60)
    print("Egenvektorer og multiplicitet:")

    diagonaliserbar = True

    for val, alg_mult, vecs in eigenvects:
        geo_mult = len(vecs)

        print(f"\nλ = {val}")
        print(f"  Algebraisk multiplicitet: {alg_mult}")
        print(f"  Geometrisk multiplicitet: {geo_mult}")

        if geo_mult < alg_mult:
            diagonaliserbar = False

        for i, v in enumerate(vecs, start=1):
            print(f"  v{i} = {v.T}")

    print("-" * 60)

    if diagonaliserbar:
        print("Matrixen er diagonaliserbar")
    else:
        print("Matrixen er IKKE diagonaliserbar")
        print("\nJordansk normalform:")
        J, P = M.jordan_form()
        print("J =")
        print(J)
        print("\n(P er basis-skiftematricen)")

    print("=" * 60)


# ====== INDSÆT KUN MATRIXEN HER ======
A = np.array([[2, 2, 2],
              [2, 2, 2],
              [2, 2, 2]])

eigen_analysis(A)
