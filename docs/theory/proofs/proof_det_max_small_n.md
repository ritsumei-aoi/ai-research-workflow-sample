# Proofs: det_max for small n

This document collects verification notes and proof sketches showing det_max(n) for small n computed by exhaustive search.

- n=1: trivial, det_max=1
- n=2: exhaustive search confirms det_max=2
- n=3: exhaustive search confirms det_max=4
- n=4: to be computed/exhaustively verified

Method:
- Exhaustive enumeration using scripts/compute_and_save_det.py to generate distributions and confirm det_max.
- Record extremal matrices in data/det_results for formal verification.
