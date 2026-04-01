"""
Determinant distribution analysis.
"""

from collections import Counter
from typing import Optional

from .matrix_gen import generate_all_ternary_matrices
from .det_compute import det_exact


def compute_distribution(n: int, sample_size: Optional[int] = None,
                         random_seed: Optional[int] = None) -> dict:
    """Compute the determinant distribution for n×n ternary matrices.

    Args:
        n: Matrix size.
        sample_size: If None, exhaustive enumeration. Otherwise, random sampling.
        random_seed: Random seed for reproducibility (required if sample_size is set).

    Returns:
        Dictionary with distribution data.
    """
    counter: Counter[int] = Counter()

    if sample_size is None:
        # Exhaustive enumeration
        for matrix in generate_all_ternary_matrices(n):
            d = det_exact(matrix)
            counter[d] += 1
        total = sum(counter.values())
        computation_type = "exhaustive"
    else:
        import random
        if random_seed is not None:
            random.seed(random_seed)
        entries = [-1, 0, 1]
        for _ in range(sample_size):
            matrix = [[random.choice(entries) for _ in range(n)] for _ in range(n)]
            d = det_exact(matrix)
            counter[d] += 1
        total = sample_size
        computation_type = "sampling"

    distribution = {str(k): v for k, v in sorted(counter.items())}
    det_max = max(counter.keys())
    det_min = min(counter.keys())

    return {
        "matrix_size": n,
        "computation_type": computation_type,
        "total_matrices": total,
        "distribution": distribution,
        "det_max": det_max,
        "det_min": det_min,
    }
