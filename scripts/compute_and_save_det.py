#!/usr/bin/env python3
"""
Compute exhaustive determinant distributions for n=1..3 and save JSON results.
"""
from pathlib import Path
from ternary_det.distribution import compute_distribution
from ternary_det.schema_io import save_det_result

OUTPUT_DIR = Path("data/det_results")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for n in range(1, 4):
    print(f"Computing n={n}...")
    res = compute_distribution(n)
    # attach metadata
    res['metadata'] = {
        'computed_at': None,
        'computation_time_sec': None,
        'random_seed': None,
        'sample_size': None,
    }
    out = OUTPUT_DIR / f"det_{n}.json"
    save_det_result(res, out)
    print(f"Saved {out}")
