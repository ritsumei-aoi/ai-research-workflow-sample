#!/usr/bin/env python3
"""
Run sampling for n=4 ternary matrices and save a summary JSON.
"""
import json
from pathlib import Path
from time import perf_counter
from ternary_det.distribution import compute_distribution
from ternary_det.schema_io import save_det_result

OUTPUT_DIR = Path("data/det_results")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SAMPLE_SIZE = 100000
SEED = 42

print(f"Sampling n=4 with {SAMPLE_SIZE} samples (seed={SEED})")
start = perf_counter()
res = compute_distribution(4, sample_size=SAMPLE_SIZE, random_seed=SEED)
end = perf_counter()
res['metadata'] = {
    'computed_at': None,
    'computation_time_sec': end - start,
    'random_seed': SEED,
    'sample_size': SAMPLE_SIZE,
}
out = OUTPUT_DIR / "det_4_sample_100k.json"
save_det_result(res, out)
print(f"Saved {out} (time={res['metadata']['computation_time_sec']:.2f}s)")
