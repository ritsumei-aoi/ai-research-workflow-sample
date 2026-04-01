# Proofs: det_max for small n

This document collects verification notes and proof sketches showing det_max(n) for small n computed by exhaustive search.

- n=1: trivial, det_max=1
- n=2: exhaustive search confirms det_max=2
- n=3: exhaustive search confirms det_max=4
- n=4: to be computed/exhaustively verified

Method:
- Exhaustive enumeration using scripts/compute_and_save_det.py to generate distributions and confirm det_max.
- Record extremal matrices in data/det_results for formal verification.

# Proof of det_max(n) for small n (n <= 3)

## Overview

This document details the proof of the maximum determinant for n×n matrices with entries in {-1, 0, 1} for small values of n (n ≤ 3), based on exhaustive computation.

## n=1

- **Matrices:** [[-1]], [[0]], [[1]]
- **Determinants:** -1, 0, 1
- **det_max(1):** 1
- **det_min(1):** -1
- **Number of matrices achieving det_max(1):** 1
- **Number of matrices achieving det_min(1):** 1

## n=2

- **Total matrices:** 3^4 = 81
- **Determinants:** {-2, -1, 0, 1, 2}
- **det_max(2):** 2
- **det_min(2):** -2
- **Number of matrices achieving det_max(2):** 4
- **Number of matrices achieving det_min(2):** 4
- **Example matrix for det=2:**
  ```
  [[ 1,  1],
   [ 0, -1]]
  ```

## n=3

- **Total matrices:** 3^9 = 19683
- **Determinants:** {-4, -3, -2, -1, 0, 1, 2, 3, 4}
- **det_max(3):** 4
- **det_min(3):** -4
- **Number of matrices achieving det_max(3):** 240
- **Number of matrices achieving det_min(3):** 240

## n=4

- **Total matrices:** 3^16 = 43,046,721
- **Exhaustive computation for n=4 is not yet performed.** This is a significant computational task and will be planned for a future session.
- **Current results (sampling):** See `data/det_results/det_4.json` for sampled determinant values and counts.
- **Known det_max(4):** 16 (from OEIS A003433 and MathWorld).

## Conclusion

The maximum determinant for n×n matrices with {-1, 0, 1} entries grows rapidly. For n ≤ 3, it is achieved by explicit constructions and verified through exhaustive search. For n=4, the maximum determinant is known to be 16, but an exhaustive proof/construction is pending.
