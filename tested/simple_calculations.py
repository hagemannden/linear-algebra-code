"""
Linear Combination of Vectors

This script calculates a linear combination of three vectors:
3*[3, -1, 1] - 5*[6, 2, 5] + 7*[1, -1, -3]

This is equivalent to:
3v₁ - 5v₂ + 7v₃

where v₁ = [3, -1, 1], v₂ = [6, 2, 5], v₃ = [1, -1, -3]

examples:
result = (3*np.array([3, -1, 1]))-(5*np.array([6, 2, 5]))+(7*np.array([1, -1, -3]))'

result = (np.array([3, 2, 1], [5, 1, 1])-(5*np.array([3, 0, -2], [1, -1, 1]))

example with transpose:
result = (np.array([[3, -1], [2, 1]]).T-(2*np.array([[1, -2], [1, 1]]).T))
"""

import numpy as np

result = (np.array([[3, -1], [2, 1]]).T-(2*np.array([[1, -2], [1, 1]]).T))
print(result)