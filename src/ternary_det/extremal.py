"""Extremal matrix search utilities.

Provides simple brute-force search for n<=4 and a sampled search for larger n.
"""
from typing import Optional
from .matrix_gen import generate_all_ternary_matrices
from .det_compute import det_exact


def find_extremal_matrices(n: int, sample_size: Optional[int] = None, random_seed: Optional[int] = None):
    """Return (max_list, min_list) of matrices achieving extremal determinants.

    For exhaustive search (sample_size is None), enumerates all matrices.
    For sampling, returns extremal matrices found within the sample.
    """
    max_list = []
    min_list = []

    if sample_size is None:
        for matrix in generate_all_ternary_matrices(n):
            d = det_exact(matrix)
            if not max_list or d > max_list[0]["det"]:
                max_list = [{"matrix": matrix, "det": d}]
            elif d == max_list[0]["det"]:
                max_list.append({"matrix": matrix, "det": d})

            if not min_list or d < min_list[0]["det"]:
                min_list = [{"matrix": matrix, "det": d}]
            elif d == min_list[0]["det"]:
                min_list.append({"matrix": matrix, "det": d})
    else:
        import random
        if random_seed is not None:
            random.seed(random_seed)
        entries = [-1, 0, 1]
        for _ in range(sample_size):
            matrix = [[random.choice(entries) for _ in range(n)] for _ in range(n)]
            d = det_exact(matrix)
            if not max_list or d > max_list[0]["det"]:
                max_list = [{"matrix": matrix, "det": d}]
            elif d == max_list[0]["det"]:
                max_list.append({"matrix": matrix, "det": d})

            if not min_list or d < min_list[0]["det"]:
                min_list = [{"matrix": matrix, "det": d}]
            elif d == min_list[0]["det"]:
                min_list.append({"matrix": matrix, "det": d})

    return max_list, min_list
