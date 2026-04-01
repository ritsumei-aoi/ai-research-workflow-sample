"""Tests for matrix generation."""

from ternary_det.matrix_gen import generate_all_ternary_matrices, count_ternary_matrices


def test_count_1x1():
    assert count_ternary_matrices(1) == 3


def test_count_2x2():
    assert count_ternary_matrices(2) == 81


def test_generate_1x1():
    matrices = list(generate_all_ternary_matrices(1))
    assert len(matrices) == 3
    assert [[-1]] in matrices
    assert [[0]] in matrices
    assert [[1]] in matrices


def test_generate_2x2_count():
    matrices = list(generate_all_ternary_matrices(2))
    assert len(matrices) == 81


def test_all_entries_valid():
    for matrix in generate_all_ternary_matrices(2):
        for row in matrix:
            for entry in row:
                assert entry in {-1, 0, 1}
