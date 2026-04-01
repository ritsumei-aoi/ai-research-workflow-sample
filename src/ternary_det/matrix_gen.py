"""
Ternary matrix generation.

Generate n×n matrices with entries from {-1, 0, 1}.
"""

import itertools
from typing import Iterator


def generate_all_ternary_matrices(n: int) -> Iterator[list[list[int]]]:
    """Generate all n×n matrices with entries in {-1, 0, 1}.

    Yields row-major list-of-lists representation.
    Total count: 3^(n²).

    Args:
        n: Matrix size (positive integer).

    Yields:
        Each n×n ternary matrix as a list of lists.
    """
    entries = [-1, 0, 1]
    for flat in itertools.product(entries, repeat=n * n):
        yield [list(flat[i * n:(i + 1) * n]) for i in range(n)]


def count_ternary_matrices(n: int) -> int:
    """Return the total number of n×n ternary matrices: 3^(n²)."""
    return 3 ** (n * n)
