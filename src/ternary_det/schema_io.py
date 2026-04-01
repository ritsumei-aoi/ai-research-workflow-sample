"""
JSON schema I/O utilities for determinant data.
"""

import json
from pathlib import Path
from datetime import datetime, timezone


SCHEMA_VERSION = "1.0"


def save_det_result(data: dict, filepath: str | Path) -> None:
    """Save determinant computation result to JSON.

    Ensures metadata fields are present and populated where possible.

    Args:
        data: Result dictionary from compute_distribution or similar.
        filepath: Output JSON file path.
    """
    meta = data.get("metadata") or {}

    # populate metadata defaults
    computed_at = meta.get("computed_at") or datetime.now(timezone.utc).isoformat()
    computation_time_sec = meta.get("computation_time_sec")
    random_seed = meta.get("random_seed")
    sample_size = meta.get("sample_size") if meta.get("sample_size") is not None else data.get("total_matrices")

    result = {
        "schema_version": SCHEMA_VERSION,
        **{k: v for k, v in data.items() if k != "metadata"},
        "metadata": {
            "computed_at": computed_at,
            "computation_time_sec": computation_time_sec,
            "random_seed": random_seed,
            "sample_size": sample_size,
        },
    }

    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)


def load_det_result(filepath: str | Path) -> dict:
    """Load determinant computation result from JSON.

    Args:
        filepath: Input JSON file path.

    Returns:
        Parsed result dictionary.

    Raises:
        ValueError: If schema_version is incompatible.
    """
    with open(filepath) as f:
        data = json.load(f)

    if data.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(
            f"Incompatible schema_version: {data.get('schema_version')} "
            f"(expected {SCHEMA_VERSION})"
        )

    return data
