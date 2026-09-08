"""Unit tests for scripts/run_mutmut.py — the mutmut CLI wrapper that neutralizes
beartype.claw (activated by the py-key-value dependency at import time), which
otherwise segfaults mutmut's multiprocessing.Pool mutant generation."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

WRAPPER = Path(__file__).resolve().parents[2] / "scripts" / "run_mutmut.py"


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(WRAPPER), *args],
        capture_output=True,
        text=True,
        check=False,
    )


class TestRunMutmutWrapper:
    def test_help_exits_zero_and_lists_commands(self) -> None:
        result = _run("--help")
        assert result.returncode == 0
        assert "Usage:" in result.stdout
        assert "run" in result.stdout

    def test_unknown_command_fails(self) -> None:
        result = _run("definitely-not-a-command")
        assert result.returncode != 0
