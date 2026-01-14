def check_solution(equations, variables, *values):
    """
    equations: list of lambda functions, each representing an equation
    variables: list of variable names as strings, e.g. ['x1', 'x2', 'x3']
    *values: values to substitute, e.g. 1, 2, 0
    Returns True if all equations are satisfied, else False.
    Usage: check_solution(equations, variables, 1, 2, 0)
    """
    subs = dict(zip(variables, values))
    results = []
    for eq in equations:
        results.append(eq(**subs))
    return all(results)

if __name__ == "__main__":
    # Example system:
    # x1 + x2 == 3
    # x2 - x3 == 2
    # 2*x1 + x2 + x3 == 4
    equations = [
        lambda x1, x2, x3: (x1 + x2) == 3,
        lambda x1, x2, x3: (x2 - x3) == 2,
        lambda x1, x2, x3: (2*x1 + x2 + x3) == 4
    ]
    variables = ['x1', 'x2', 'x3']

    # Only check one set of values at a time:
    print(check_solution(equations, variables, 1, 2, 0))  # Change these numbers to test other values