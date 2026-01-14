import numpy as np

def euclidean_distance(vec1, vec2):
    """
    Beregn Euclidean distance mellem to vektorer vec1 og vec2.
    """
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.linalg.norm(vec1 - vec2)

# Eksempel på brug
v1 = [1, 2, 3]
v2 = [4, 0, 3]

dist = euclidean_distance(v1, v2)
print("Euclidean distance:", dist)