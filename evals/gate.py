"""Eval gate orchestrator — runs deterministic + judge evaluations."""

import subprocess
import sys


def _run(cmd: list[str], label: str) -> bool:
    print(f"\n{'=' * 60}")
    print(f"  GATE: {label}")
    print(f"{'=' * 60}")
    result = subprocess.run(cmd)
    return result.returncode == 0


def main() -> None:
    deterministic_ok = _run(
        ["pytest", "tests/unit/", "-q", "--tb=short"],
        "Phase 1 — Deterministic (must be 100%)",
    )
    if not deterministic_ok:
        print("\nGATE FAILED: deterministic tests failed")
        sys.exit(1)

    judge_ok = _run(
        [
            "pytest",
            "evals/judge/",
            "-q",
            "-m",
            "judge",
            "--tb=short",
        ],
        "Phase 2 — Judge (must be >= 80%)",
    )
    if not judge_ok:
        print("\nGATE FAILED: judge score < 80%")
        sys.exit(1)

    print("\nGATE PASSED")


if __name__ == "__main__":
    main()
