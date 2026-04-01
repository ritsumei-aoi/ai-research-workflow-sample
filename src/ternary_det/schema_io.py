"""
JSON schema I/O utilities for determinant data.
"""

import json
from pathlib import Path
from datetime import datetime, timezone


SCHEMA_VERSION = "1.0"


def save_det_result(data: dict, filepath: str | Path) -> None:
    """Save determinant computation result to JSON.

    Args:
        data: Result dictionary from compute_distribution or similar.
        filepath: Output JSON file path.
    """
    result = {
        "schema_version": SCHEMA_VERSION,
        **data,
        "metadata": data.get("metadata", {
            "computed_at": datetime.now(timezone.utc).isoformat(),
            "computation_time_sec": None,
            "random_seed": None,
            "sample_size": None,
        }),
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
