import sympy as sp

# Definer lambda som symbol
lambda_ = sp.symbols('lambda')

# Karakteristisk polynomium ÆNDRER HER
char_poly = (2-lambda_)**3 * (-3-lambda_)**10 * (5-lambda_)

# Expand before finding roots
char_poly = sp.expand(char_poly)

# Find rødder med multiplicitet
eigenvalues = sp.roots(char_poly, lambda_)

# Print resultat
print(eigenvalues)