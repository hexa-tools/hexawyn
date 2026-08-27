#!/usr/bin/env python3
"""Update the tests badge in README.md with the current test count.

Runs pytest in collect-only mode (fast, no execution) to count tests,
then rewrites the badge URL in README.md.

Usage:
    python scripts/update_test_badge.py
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
README = ROOT / "README.md"
# Matches both `tests-123_passed` and the URL-encoded `tests-8500%2B_passed`
# (`%2B` == `+`) forms previously hardcoded in README.md.
BADGE_PATTERN = re.compile(
    r"https://img\.shields\.io/badge/tests-\d+(?:%2B)?_passed-brightgreen\.svg"
)


def render_badge_url(count: int) -> str:
    """Shields.io URL for the test-count badge."""
    return f"https://img.shields.io/badge/tests-{count}_passed-brightgreen.svg"


def count_tests() -> int:
    result = subprocess.run(
        ["poetry", "run", "pytest", "tests/", "--collect-only", "-q", "--no-header"],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    # Output ends with a line like "1552 tests collected in 4.23s"
    for line in reversed(result.stdout.splitlines()):
        match = re.search(r"(\d+) tests? collected", line)
        if match:
            return int(match.group(1))
    return 0


def update_badge(count: int) -> bool:
    content = README.read_text()
    new_url = render_badge_url(count)
    new_content, n = BADGE_PATTERN.subn(new_url, content)
    if n == 0:
        print("⚠️  Badge pattern not found in README.md — skipping update")
        return False
    if new_content == content:
        print(f"✅ Badge already up to date ({count} tests)")
        return False
    README.write_text(new_content)
    print(f"✅ Updated README.md badge → {count} tests")
    return True


if __name__ == "__main__":
    count = count_tests()
    if count == 0:
        print("❌ Could not collect test count — aborting badge update")
        sys.exit(1)
    update_badge(count)
