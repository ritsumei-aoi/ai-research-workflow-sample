"""Tests for determinant computation."""

from ternary_det.det_compute import det_exact


def test_det_1x1():
    assert det_exact([[1]]) == 1
    assert det_exact([[0]]) == 0
    assert det_exact([[-1]]) == -1


def test_det_2x2():
    assert det_exact([[1, 0], [0, 1]]) == 1  # identity
    assert det_exact([[1, 1], [0, 1]]) == 1
    assert det_exact([[1, 1], [1, 1]]) == 0  # singular
    assert det_exact([[0, 1], [1, 0]]) == -1  # permutation


def test_det_3x3_identity():
    I3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert det_exact(I3) == 1


def test_det_3x3_known():
    # det([[1,1,1],[1,-1,0],[0,1,-1]]) = 1*(-1*-1 - 0*1) - 1*(1*-1 - 0*0) + 1*(1*1 - -1*0)
    # = 1 - (-1) + 1 = 3
    assert det_exact([[1, 1, 1], [1, -1, 0], [0, 1, -1]]) == 3


def test_det_zero_matrix():
    assert det_exact([[0, 0], [0, 0]]) == 0


def test_det_all_ones():
    # n×n all-ones matrix has det = 0 for n >= 2
    assert det_exact([[1, 1], [1, 1]]) == 0
    assert det_exact([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 0
