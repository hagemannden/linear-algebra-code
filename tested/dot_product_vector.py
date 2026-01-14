import numpy as np

# Define two vectors
u = np.array( [5, 7, 1])
v = np.array([2, -1, 3])

# Compute the dot product
dot_product = np.dot(u, v)

# Helper functions
def angle_degrees(a: np.ndarray, b: np.ndarray) -> float | None:
	"""Return the angle between vectors a and b in degrees.
	If either vector has zero norm, return None.
	"""
	na = np.linalg.norm(a)
	nb = np.linalg.norm(b)
	if na == 0 or nb == 0:
		return None
	cos_theta = np.dot(a, b) / (na * nb)
	# Numerical safety
	cos_theta = np.clip(cos_theta, -1.0, 1.0)
	return float(np.degrees(np.arccos(cos_theta)))

def classify_by_dot(d: float, tol: float = 1e-12) -> str:
	"""Classify angle via dot-product sign with tolerance."""
	if d > tol:
		return "acute (< 90°)"
	if d < -tol:
		return "obtuse (> 90°)"
	return "right (90°)"

def is_orthogonal(d: float, tol: float = 1e-12) -> bool:
	return abs(d) <= tol

# Print the result
print("-" * 50)
print("Vector u:")
print(u)
print("\nVector v:")
print(v)
print("-" * 50)
print("Dot product u · v:", dot_product)
print("=" * 50)
# Angle and classification
theta = angle_degrees(u, v)
if theta is not None:
	print(f"Angle between u and v: {theta:.3f}°")
else:
	print("Angle between u and v: undefined (zero vector involved)")
print("Classification:", classify_by_dot(dot_product))
print("Orthogonal (perpendicular)?:", is_orthogonal(dot_product))

# Projections (using standard dot-product formulas)
u_dot_u = np.dot(u, u)
v_dot_v = np.dot(v, v)

# projection of v onto u: (v·u / ||u||^2) u  (same as (u·v / ||u||^2) u)
proj_v_on_u = (dot_product / u_dot_u) * u
# projection of u onto v: (u·v / ||v||^2) v
proj_u_on_v = (dot_product / v_dot_v) * v

print("\nProjection of v onto u ( (v·u / ||u||^2) u ):", proj_v_on_u)
print("Projection of u onto v ( (u·v / ||v||^2) v ):", proj_u_on_v)

# Key properties demonstration
print("-" * 50)
print("Properties check")
dot_uv = np.dot(u, v)
dot_vu = np.dot(v, u)
print("Commutative a·b = b·a:", dot_uv == dot_vu, f"({dot_uv} vs {dot_vu})")

w = np.array([2, -1, 3])
left = np.dot(u, v + w)
right = np.dot(u, v) + np.dot(u, w)
print("Distributive a·(b+c) = a·b + a·c:", left == right, f"({left} vs {right})")
print("=" * 50)
