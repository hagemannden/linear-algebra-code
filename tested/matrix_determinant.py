import numpy as np


def determinant_2x2(matrix):
    """
    Calculate the determinant of a 2x2 matrix.
    For a 2x2 matrix: [[a, b], [c, d]]
    det = ad - bc
    """
    if matrix.shape != (2, 2):
        raise ValueError("Matrix must be 2x2")
    
    a, b = matrix[0, 0], matrix[0, 1]
    c, d = matrix[1, 0], matrix[1, 1]
    
    det = a * d - b * c
    return det


def determinant_3x3(matrix):
    """
    Calculate the determinant of a 3x3 matrix using the rule of Sarrus.
    For a 3x3 matrix: [[a, b, c], [d, e, f], [g, h, i]]
    det = aei + bfg + cdh - ceg - afh - bdi
    """
    if matrix.shape != (3, 3):
        raise ValueError("Matrix must be 3x3")
    
    a, b, c = matrix[0, 0], matrix[0, 1], matrix[0, 2]
    d, e, f = matrix[1, 0], matrix[1, 1], matrix[1, 2]
    g, h, i = matrix[2, 0], matrix[2, 1], matrix[2, 2]
    
    det = (a*e*i + b*f*g + c*d*h) - (c*e*g + a*f*h + b*d*i)
    return det


def determinant_recursive(matrix):
    """
    Calculate the determinant of any n x n matrix using cofactor expansion.
    Works for matrices of any size (1x1, 2x2, 3x3, 4x4, etc.)
    
    Method: Cofactor expansion along the first row
    """
    matrix = np.array(matrix, dtype=float)
    n = matrix.shape[0]
    
    if matrix.shape != (n, n):
        raise ValueError("Matrix must be square")
    
    # Base case: 1x1 matrix
    if n == 1:
        return matrix[0, 0]
    
    # Base case: 2x2 matrix
    if n == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    
    # Recursive case: cofactor expansion along first row
    det = 0
    for j in range(n):
        # Create minor matrix by removing row 0 and column j
        minor = np.delete(np.delete(matrix, 0, axis=0), j, axis=1)
        # Cofactor = (-1)^(0+j) * element * det(minor)
        cofactor = ((-1) ** j) * matrix[0, j] * determinant_recursive(minor)
        det += cofactor
    
    return det


def determinant_nxn(matrix):
    """
    Calculate the determinant of any n x n matrix using NumPy.
    This is the most efficient method for large matrices.
    """
    matrix = np.array(matrix, dtype=float)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square")
    return np.linalg.det(matrix)


def determinant(matrix):
    """
    Automatically calculate the determinant of any square matrix.
    Chooses the best method based on matrix size.
    """
    matrix = np.array(matrix, dtype=float)
    n = matrix.shape[0]
    
    if matrix.shape != (n, n):
        raise ValueError("Matrix must be square")
    
    # Use specialized methods for small matrices
    if n == 2:
        return determinant_2x2(matrix)
    elif n == 3:
        return determinant_3x3(matrix)
    else:
        # Use recursive method for larger matrices
        return determinant_recursive(matrix)




# Define the matrix A as a NumPy array
A = np.array([[-3, 0, 0, 0],
              [4, 1, 0, 0],
              [-1, 4, -4, 0],
              [0, 3, 2, 3]])

# Compute the determinant (automatically chooses the right method)
det_result = determinant(A)
det_numpy = np.linalg.det(A)

# Print the result
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)
print(f"Determinant: {det_result}")
print(f"NumPy verification: {det_numpy}")
print("=" * 50)

