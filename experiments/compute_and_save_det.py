#!/usr/bin/env python3
"""
Compute exhaustive determinant distributions for n=1..4 and save JSON results.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))


from pathlib import Path
from time import perf_counter
from pathlib import Path
from ternary_det.distribution import compute_distribution
from ternary_det.schema_io import save_det_result

OUTPUT_DIR = Path("data/det_results")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for n in range(1, 5):
    print(f"Computing n={n}...")
    t0 = perf_counter()
    res = compute_distribution(n)
    t1 = perf_counter()
    res['metadata'] = {
        'computed_at': None,
        'computation_time_sec': t1 - t0,
        'random_seed': None,
        'sample_size': res.get('total_matrices'),
    }
    out = OUTPUT_DIR / f"det_{n}.json"
    save_det_result(res, out)
    print(f"Saved {out} (time={res['metadata']['computation_time_sec']:.4f}s)")
