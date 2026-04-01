"""Tests for distribution computation."""

from ternary_det.distribution import compute_distribution


def test_distribution_1x1():
    result = compute_distribution(1)
    assert result["matrix_size"] == 1
    assert result["computation_type"] == "exhaustive"
    assert result["total_matrices"] == 3
    dist = result["distribution"]
    assert dist["-1"] == 1
    assert dist["0"] == 1
    assert dist["1"] == 1
    assert result["det_max"] == 1
    assert result["det_min"] == -1


def test_distribution_2x2():
    result = compute_distribution(2)
    assert result["matrix_size"] == 2
    assert result["total_matrices"] == 81
    assert result["det_max"] == 2
    assert result["det_min"] == -2
