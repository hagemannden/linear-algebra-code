import numpy as np

# Define vectors as a list (can add as many as needed)
vectors = [
    np.array([[1],
              [2],
              [3]]),
    
    np.array([[2],
              [0],
              [1]]),
    
    np.array([[1],
              [1],
              [1]])
]

# Define coefficients (must match number of vectors)
coefficients = [2, -1, 3]

# Verify same number of vectors and coefficients
if len(vectors) != len(coefficients):
    print("ERROR: Number of vectors must match number of coefficients!")
    exit()

# Calculate linear combination
result = np.zeros_like(vectors[0], dtype=float)
for i, (coeff, vector) in enumerate(zip(coefficients, vectors)):
    result += coeff * vector

# Print the result
print("-" * 50)
print("Vectors:")
for i, v in enumerate(vectors):
    print(f"v{i+1} = {v.T[0]}")
print("-" * 50)
print("Coefficients:")
for i, c in enumerate(coefficients):
    print(f"c{i+1} = {c}")
print("-" * 50)
print("Linear Combination: ", end="")
terms = []
for i, c in enumerate(coefficients):
    if c >= 0 and i > 0:
        terms.append(f"+ {c}*v{i+1}")
    else:
        terms.append(f"{c}*v{i+1}")
print(" ".join(terms))
print("-" * 50)

# Show each scaled vector
print("Scaled vectors:")
for i, (coeff, vector) in enumerate(zip(coefficients, vectors)):
    scaled = coeff * vector
    print(f"{coeff}*v{i+1} = {scaled.T[0]}")
print("-" * 50)
print("Result:")
print(result)
print("=" * 50)
