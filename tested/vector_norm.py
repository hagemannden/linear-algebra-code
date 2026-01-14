import numpy as np

# Vektorer
u = np.array([3, -1, -5])
v = np.array([6, -2, 3])

# Norm (længde) af hver vektor
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)

print("||u|| =", norm_u)
print("||v|| =", norm_v)
