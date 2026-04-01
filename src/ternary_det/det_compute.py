"""
Determinant computation for integer matrices.

Uses exact integer arithmetic (no floating point).
"""


def det_exact(matrix: list[list[int]]) -> int:
    """Compute the determinant of an integer matrix exactly.

    Uses Bareiss algorithm for exact integer determinant.

    Args:
        matrix: n×n integer matrix as list of lists.

    Returns:
        Determinant as an integer.
    """
    n = len(matrix)
    if n == 0:
        return 1
    if n == 1:
        return matrix[0][0]

    # Bareiss algorithm for exact integer determinant
    M = [row[:] for row in matrix]  # deep copy
    sign = 1

    for col in range(n):
        # Find pivot
        pivot_row = None
        for row in range(col, n):
            if M[row][col] != 0:
                pivot_row = row
                break

        if pivot_row is None:
            return 0

        if pivot_row != col:
            M[col], M[pivot_row] = M[pivot_row], M[col]
            sign *= -1

        for row in range(col + 1, n):
            for j in range(col + 1, n):
                M[row][j] = M[col][col] * M[row][j] - M[row][col] * M[col][j]
                if col > 0:
                    M[row][j] //= M[col - 1][col - 1]
            M[row][col] = 0

    return sign * M[n - 1][n - 1]
