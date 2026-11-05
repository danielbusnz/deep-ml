def matrix_dot_vector(a, b):

	
    if any(len(row) != len(b) for row in a):
        return -1

    return [
        sum(x * y for x, y in zip(row, b))
        for row in a
    ]

												