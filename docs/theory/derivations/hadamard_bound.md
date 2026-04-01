# Hadamard bound (ternary matrices)

This note outlines the relationship between Hadamard matrices and upper bounds on determinants for matrices with entries in {-1,0,1}.

Summary:

- Hadamard matrices (±1) achieve maximal determinants for their order when they exist, giving Hadamard's bound det(A) <= n^{n/2} for ±1 matrices.
- For ternary matrices, entries of 0 reduce achievable determinant magnitude; converting a ternary matrix to ±1 may increase determinant magnitude but is not always possible while preserving structure.

Planned content:

- Formal statement of upper bounds adapted to ternary matrices.
- Examples contrasting ternary optimal matrices with Hadamard matrices where applicable.
- References to OEIS and Hadamard conjecture.

# Hadamard Bound and Ternary Matrices

## Overview

This document explores the Hadamard bound on matrix determinants and its application to ternary matrices (matrices with entries from {-1, 0, 1}).

## The Hadamard Bound

For an $n \times n$ real matrix $A$, the determinant satisfies the inequality:
$|\det(A)| \le \prod_{i=1}^n \|v_i\|$, where $v_i$ are the column vectors of $A$.

The tightest bound, the Hadamard bound, applies to matrices with entries of magnitude 1 (e.g., $\{-1, 1\}$ matrices). For such matrices, $\|v_i\| = \sqrt{n}$, leading to:
$|\det(A)| \le (\sqrt{n})^n = n^{n/2}$.

Matrices achieving this bound are called Hadamard matrices. They exist only for $n=1, 2$ or $n$ being a multiple of 4.

## Application to Ternary Matrices

Ternary matrices, with entries from $\{-1, 0, 1\}$, are a generalization of $\{-1, 1\}$ matrices. The presence of 0s can potentially reduce the determinant value compared to $\{-1, 1\}$ matrices.

### Upper Bound for Ternary Matrices

While the strict Hadamard bound ($n^{n/2}$) is for $\{-1, 1\}$ matrices, we can derive bounds for ternary matrices. A simple upper bound can be obtained by considering the maximum possible column norms.

For a ternary matrix, the maximum $L_2$ norm of a column vector $v_i$ occurs when all entries are 1 or -1, i.e., $\|v_i\| \le \sqrt{n \cdot 1^2} = \sqrt{n}$.
Thus, a loose upper bound is still $|\det(A)| \le n^{n/2}$.

However, specific constructions and computational results show that for ternary matrices, the maximum determinant might differ from the Hadamard bound for certain values of n. For example:
- det_max(1) = 1 ($1^{1/2} = 1$)
- det_max(2) = 2 ($2^{2/2} = 2$)
- det_max(3) = 4 (Hadamard bound: $3^{3/2} \approx 5.196$)
- det_max(4) = 16 ($4^{4/2} = 16$)

The equality $|\det(A)| = n^{n/2}$ is achieved for n=1, 2, 4 with ternary matrices. For n=3, the maximum determinant (4) is less than the Hadamard bound (approx. 5.196).

### Further Research

- Investigating specific constructions of ternary matrices that achieve or approach the Hadamard bound.
- Analyzing the determinant distribution for ternary matrices and how it deviates from the bound.
- Exploring the existence of "generalized Hadamard matrices" within the ternary set.
