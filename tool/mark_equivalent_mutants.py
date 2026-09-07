"""Mark structurally-equivalent mutants as skipped (exit code 34) in mutmut caches.

Usage:
    python tool/mark_equivalent_mutants.py --list docs/mutation/equivalent_mutants.txt

Each line of the list file is a full mutant key, e.g.:
    hexawyn.domain.services.cost_forecast.cost_forecast_engine.x__compute_trend__mutmut_1

The tool rewrites the source .meta JSON (mutants/src/<path>.py.meta) so the
referenced mutant gets exit code 34 ("skipped"), removing it from `survived`
in `mutmut results` without touching source code or tests.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_MUTANTS_ROOT = Path("mutants/src")


def module_to_meta_path(root: Path, mutant_key: str) -> Path:
    module_path = mutant_key.split(".x")[0].replace(".", "/")
    return root / f"{module_path}.py.meta"


def mark_mutants(root: Path, mutant_keys: list[str]) -> tuple[int, list[str]]:
    marked: list[str] = []
    errors: list[str] = []
    for key in mutant_keys:
        meta = module_to_meta_path(root, key)
        if not meta.exists():
            errors.append(f"missing meta for {key} ({meta})")
            continue
        data = json.loads(meta.read_text(encoding="utf-8"))
        if key not in data["exit_code_by_key"]:
            errors.append(f"key not in cache for {key}")
            continue
        data["exit_code_by_key"][key] = 34
        meta.write_text(json.dumps(data, indent=4) + "\n", encoding="utf-8")
        marked.append(key)
    return len(marked), errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--list", required=True, help="Path to a text file with one mutant key per line"
    )
    args = parser.parse_args()

    keys = [
        line.strip()
        for line in Path(args.list).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    count, errors = mark_mutants(_MUTANTS_ROOT, keys)
    print(f"Marked {count}/{len(keys)} mutants as skipped.")
    for error in errors:
        print(f"  ERROR: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
