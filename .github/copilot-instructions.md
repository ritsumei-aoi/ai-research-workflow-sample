# Purpose

Short, actionable instructions for Copilot/GitHub AI sessions in this repository: build/test/lint commands, high-level architecture, and repository-specific conventions to make automated sessions effective.

# Quick commands

- Setup (editable install):
  - pip install -e .
  - pip install -r requirements.txt
- Run regression tests:
  - pytest tests/ -v
- Run a single test:
  - pytest tests/<file>.py::test_function_name -q
- Generate determinant data for n×n:
  - python experiments/generate_det_data.py --n 3
- Validate JSON schema:
  - python experiments/validate_schema.py data/det_results/det_3.json

# Linter / formatting

- No repository-wide linter config detected (e.g. .flake8, pyproject.toml for black) — use your preferred tools (flake8/ruff/black) scoped to src/ and tests/ if desired.

# High-level architecture (big picture)

- Data-driven pipeline: determinant computation results are stored as JSON under data/ and analyzed by scripts.
  - Schema 1 (data/det_results/): determinant computation results for each n (distribution, extremal matrices)
  - Schema 2 (data/analysis/): aggregate analysis across multiple n values (trends, conjectures)
- Core library (src/ternary_det):
  - matrix_gen.py — ternary matrix generation (exhaustive for small n, sampling for large n)
  - det_compute.py — determinant computation with caching and optimization
  - distribution.py — determinant distribution analysis (histogram, statistics)
  - extremal.py — maximal/minimal determinant search algorithms
  - schema_io.py — JSON schema I/O utilities
- Experiment scripts (experiments/):
  - generate_det_data.py — generate determinant data for given n
  - validate_schema.py — validate JSON data against schema
  - analyze_trends.py — analyze det_max(n) trends across n values

# Key repository-specific conventions

- JSON schema naming:
  - det_results: det_{n}.json (e.g., det_3.json, det_4.json)
  - analysis: analysis_{n_range}.json (e.g., analysis_1_to_6.json)
- Matrix representation: row-major list of lists, e.g., [[1,0,-1],[0,1,1],[-1,0,1]]
- Determinant values are always stored as integers (exact computation, no floating point)
- For large n (n ≥ 5), use random sampling instead of exhaustive enumeration
  - Sampling results include sample_size and confidence metadata

# AI agent rules & integration notes

- Read these files at session start (in this order):
  1) handover/README.md
  2) handover/workflow_common.md
  3) handover/workflow_method_b.md
  4) handover/handover_memo_latest.md
- Method selection:
  - AI agents with direct execution (Copilot Chat / Gemini CLI): use Method B (handover/workflow_method_b.md)
  - Interactive dialog without direct execution: use Method A (handover/workflow_method_a.md)
- Keep changes surgical and run tests after edits.

# Where to look next

- docs/json_schema_det_results.md (Schema 1: per-n determinant data)
- docs/json_schema_analysis.md (Schema 2: cross-n analysis)
- handover/* for session-specific notes and workflows
- experiments/ for scripts that generate and validate data

# If there are existing AI assistant configs

- This repository uses handover/workflow_method_b.md as the unified AI agent workflow (Method B).
  No CLAUDE.md, AGENTS.md, or .cursorrules files are used.
