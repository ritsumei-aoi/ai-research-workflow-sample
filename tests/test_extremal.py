from ternary_det.extremal import find_extremal_matrices
from ternary_det.distribution import compute_distribution


def test_extremal_n1():
    max_list, min_list = find_extremal_matrices(1)
    # For 1x1 matrices with entries -1,0,1, max det is 1, min is -1
    assert any(item['det'] == 1 for item in max_list)
    assert any(item['det'] == -1 for item in min_list)


def test_extremal_matches_distribution_n2():
    # Verify extremal matrices agree with compute_distribution results for n=2
    dist = compute_distribution(2)
    expected_max = dist['det_max']
    expected_min = dist['det_min']
    max_list, min_list = find_extremal_matrices(2)
    assert all(item['det'] == expected_max for item in max_list)
    assert all(item['det'] == expected_min for item in min_list)
