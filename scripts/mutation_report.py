#!/usr/bin/env python3
"""Aggregate mutation-testing results (Python mutmut) into a machine report.

Reads ``mutants/mutmut-cicd-stats.json`` (produced by ``mutmut export-cicd-stats``)
and writes ``docs/mutation/report.json``, the single source of truth used by CI
and the README mutation badge.

Usage:
    python scripts/mutation_report.py            # print summary table
    python scripts/mutation_report.py --badge    # also update the README badge
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MUTMUT_STATS = ROOT / "mutants" / "mutmut-cicd-stats.json"
DEFAULT_REPORT = ROOT / "docs" / "mutation" / "report.json"
README_PATH = ROOT / "README.md"

# Overridable for tests; None means "derive the color from the score".
BADGE_COLOR: str | None = None

# Single badge (python). The shields ``--`` keeps a literal dash inside the
# label so the rendered text reads "mutation-python".
BADGES = (
    ("python", "mutation--python", r"https://img\.shields\.io/badge/mutation--python-[^)\s]+"),
)


def _badge_url(label: str, score: float) -> str:
    color = BADGE_COLOR if BADGE_COLOR is not None else _color(score)
    return f"https://img.shields.io/badge/{label}-{score:.1f}%25-{color}.svg"


def _load(path: Path) -> dict[str, object] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _score(killed: int, total: int) -> float:
    return round(100.0 * killed / total, 1) if total else 0.0


def _color(score: float) -> str:
    if score >= 90:  # noqa: PLR2004
        return "brightgreen"
    if score >= 75:  # noqa: PLR2004
        return "yellowgreen"
    if score >= 60:  # noqa: PLR2004
        return "yellow"
    if score >= 40:  # noqa: PLR2004
        return "orange"
    return "red"


def summarize(mutmut: dict[str, object] | None) -> dict[str, object]:
    """Fold the mutmut stats into the python + overall report shape."""
    py: dict[str, object] = {"enabled": mutmut is not None}
    if mutmut:
        # Structural equivalents marked 'skipped' (tool/mark_equivalent_mutants.py)
        # are accepted, not failures — count them as killed like the project does.
        killed = int(mutmut["killed"]) + int(mutmut.get("skipped", 0))
        total = int(mutmut["total"])
        py.update(
            killed=killed,
            survived=int(mutmut["survived"]),
            no_tests=int(mutmut.get("no_tests", 0)),
            timeout=int(mutmut.get("timeout", 0)),
            total=total,
            score=_score(killed, total),
        )

    overall_total = int(mutmut["total"]) if mutmut else 0
    overall_killed = int(mutmut["killed"]) if mutmut else 0
    if mutmut:
        overall_killed += int(mutmut.get("skipped", 0))

    return {
        "python": py,
        "overall": {
            "total": overall_total,
            "killed": overall_killed,
            "score": _score(overall_killed, overall_total),
        },
    }


def print_table(summary: dict[str, object]) -> None:
    python = summary["python"]
    assert isinstance(python, dict)
    if not python.get("enabled"):
        print("python: no report found (run `make mutation-python` first)")
        return
    print(
        f"python: {python['killed']}/{python['total']} killed "
        f"({python['score']}%) survived={python.get('survived', 0)} "
        f"timeout={python.get('timeout', 0)}"
    )
    overall = summary["overall"]
    assert isinstance(overall, dict)
    print(f"overall: {overall['killed']}/{overall['total']} ({overall['score']}%)")


def write_report(summary: dict[str, object], path: Path = DEFAULT_REPORT) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"✅ Report written to {path}")


def update_badge(summary: dict[str, object], readme: Path = README_PATH) -> bool:
    """Update the mutation-python badge in the README.

    Returns True when the badge line changed; False when the README is already
    up to date, or when it contains no mutation badge at all.
    """
    content = readme.read_text(encoding="utf-8")
    found_any = any(re.search(pattern, content) for _, _, pattern in BADGES)
    new_content = content

    for name, label, pattern in BADGES:
        data = summary[name]
        assert isinstance(data, dict)
        score = float(data["score"]) if data.get("enabled") else 0.0
        new_content = re.sub(pattern, _badge_url(label, score), new_content)

    if new_content == content:
        if not found_any:
            print("⚠️  Mutation badge not found in README.md — add it first")
        else:
            print("✅ Mutation badge already up to date")
        return False

    python = summary["python"]
    assert isinstance(python, dict)
    readme.write_text(new_content, encoding="utf-8")
    print(f"✅ Updated mutation badge (python {python['score']}%)")
    return True


if __name__ == "__main__":
    summary = summarize(_load(MUTMUT_STATS))
    print_table(summary)
    write_report(summary)
    if "--badge" in sys.argv:
        update_badge(summary)
