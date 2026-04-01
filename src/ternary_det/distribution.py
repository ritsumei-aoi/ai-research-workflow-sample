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
    extremal_max: list[dict] = []
    extremal_min: list[dict] = []

    if sample_size is None:
        # Exhaustive enumeration
        for matrix in generate_all_ternary_matrices(n):
            d = det_exact(matrix)
            counter[d] += 1
            # track extremal matrices
            if not extremal_max or d > extremal_max[0]["det"]:
                extremal_max = [{"matrix": matrix, "det": d}]
            elif d == extremal_max[0]["det"]:
                extremal_max.append({"matrix": matrix, "det": d})

            if not extremal_min or d < extremal_min[0]["det"]:
                extremal_min = [{"matrix": matrix, "det": d}]
            elif d == extremal_min[0]["det"]:
                extremal_min.append({"matrix": matrix, "det": d})

        total = sum(counter.values())
        computation_type = "exhaustive"
    else:
        import random
        if random_seed is not None:
            random.seed(random_seed)
        entries = [-1, 0, 1]
        # For sampling, we only record extremal examples seen in the sample
        for _ in range(sample_size):
            matrix = [[random.choice(entries) for _ in range(n)] for _ in range(n)]
            d = det_exact(matrix)
            counter[d] += 1
            if not extremal_max or d > extremal_max[0]["det"]:
                extremal_max = [{"matrix": matrix, "det": d}]
            elif d == extremal_max[0]["det"]:
                extremal_max.append({"matrix": matrix, "det": d})

            if not extremal_min or d < extremal_min[0]["det"]:
                extremal_min = [{"matrix": matrix, "det": d}]
            elif d == extremal_min[0]["det"]:
                extremal_min.append({"matrix": matrix, "det": d})

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
        "extremal_matrices": {"max": extremal_max, "min": extremal_min},
    }
