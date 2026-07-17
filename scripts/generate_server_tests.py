"""Generate tests for all build_*_adapter() functions in mcp/server.py."""

import re
from pathlib import Path

SERVER_PATH = Path("src/hexawyn/mcp/server.py")
TEST_PATH = Path("tests/unit/mcp")


def extract_builders(source: str) -> list[tuple[str, str]]:
    """Extract (function_name, return_type) for each build_*_adapter."""
    builders = []
    for m in re.finditer(r"def (build_\w+)\(\) -> (\w+):", source):
        builders.append((m.group(1), m.group(2)))
    return builders


def extract_port_module(source: str, return_type: str) -> str:
    """Find the import module for a given return type. Handles multi-line imports."""
    # Try single-line first
    for m in re.finditer(rf"from (hexawyn\.application\.ports\.driven\.\w+) import.*\b{return_type}\b", source):
        return m.group(1)

    # Try multi-line — find the return type, then backtrack to the from line
    lines = source.split("\n")
    for i, line in enumerate(lines):
        if return_type in line and "import" not in line and i > 0:
            # Backtrack to find "from ... import ("
            for j in range(i - 1, max(i - 10, 0), -1):
                prev = lines[j].strip()
                if prev.startswith("from hexawyn.application.ports.driven"):
                    m = re.match(r"from (hexawyn\.application\.ports\.driven\.\w+) import", prev)
                    if m:
                        return m.group(1)
    return ""


def main() -> None:
    source = SERVER_PATH.read_text()
    builders = extract_builders(source)

    tests = []
    skipped = []
    for func_name, return_type in builders:
        port_mod = extract_port_module(source, return_type)
        if not port_mod:
            skipped.append(f"{func_name} -> {return_type}")
            continue

        tests.append(f'''
    def test_{func_name}_returns_{return_type.lower()}(self) -> None:
        from {port_mod} import {return_type}

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import {func_name}

            result = {func_name}()

            assert isinstance(result, {return_type})
''')

    test_file = f'''"""Unit tests for all build_*_adapter() factories in mcp/server.py.

Per AGENTS.md: every build_*_adapter() MUST have a corresponding test.
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestMCPServerAdapterFactories:
{''.join(tests)}
'''

    (TEST_PATH / "test_server_adapters.py").write_text(test_file)
    print(f"Generated {len(builders) - len(skipped)} adapter tests in test_server_adapters.py")
    if skipped:
        print(f"\nSkipped {len(skipped)} (port module not found):")
        for s in skipped:
            print(f"  - {s}")


if __name__ == "__main__":
    main()
