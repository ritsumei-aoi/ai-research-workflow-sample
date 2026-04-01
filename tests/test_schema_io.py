import json
from pathlib import Path
from ternary_det.schema_io import save_det_result, load_det_result


def test_save_and_load_metadata(tmp_path):
    data = {
        'matrix_size': 2,
        'computation_type': 'exhaustive',
        'total_matrices': 81,
        'distribution': {'0': 50},
        'det_max': 2,
        'det_min': -2,
        'extremal_matrices': {'max': [], 'min': []}
    }
    out = tmp_path / 'det_test.json'
    save_det_result(data, out)
    loaded = load_det_result(out)
    assert loaded['schema_version'] == '1.0'
    assert 'metadata' in loaded
    assert 'computed_at' in loaded['metadata']
    assert loaded['metadata']['sample_size'] == 81
