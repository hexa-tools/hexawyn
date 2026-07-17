"""Generate minimal tests for all untested MCP tool modules."""

import re
from pathlib import Path

TOOLS_DIR = Path("src/hexawyn/mcp/tools")
TEST_DIR = Path("tests/unit/mcp/tools")


def extract_func_info(source: str) -> tuple[str, str]:
    """Extract main tool function name and call args. Returns (name, call_args_str)."""
    params_str = ""

    # Priority 1: public function returning dict
    for m in re.finditer(r"def (\w+)\((.*?)\)(?:\s*->\s*dict)", source, re.DOTALL):
        name = m.group(1)
        if name.startswith("_") or name == "register":
            continue
        params_str = m.group(2).strip()
        return name, build_call_args(params_str)

    # Priority 2: first public function (any return type)
    for m in re.finditer(r"def (\w+)\((.*?)\)", source):
        name = m.group(1)
        if name.startswith("_") or name == "register":
            continue
        params_str = m.group(2).strip()
        return name, build_call_args(params_str)

    return "", ""


def build_call_args(params_str: str) -> str:
    args = []
    for param in params_str.split(","):
        param = param.strip()
        if not param or param == "self":
            continue
        name_part = param.split(":")[0].strip() if ":" in param else param
        name_part = name_part.split("=")[0].strip() if "=" in name_part else name_part
        if "=" in param:
            continue  # has default
        if name_part == "namespaces":
            continue
        if name_part == "namespace":
            args.append('namespace="test-ns"')
        elif any(k in name_part for k in ("service", "deployment", "pipeline", "pod", "name", "node")):
            args.append(f'{name_part}="test-{name_part}"')
        else:
            args.append(f'{name_part}="test"')
    return ", ".join(args)


def extract_adapters(source: str) -> str:
    adapters = set()
    for m in re.finditer(r"build_(\w+)", source):
        adapters.add(m.group(0))
    return ", ".join(sorted(adapters))


def main() -> None:
    existing = set()
    for tf in TEST_DIR.glob("test_*.py"):
        if tf.name != "__init__.py":
            existing.add(tf.stem.replace("test_", ""))

    count = 0
    for tool_file in sorted(TOOLS_DIR.glob("*.py")):
        if tool_file.name == "__init__.py":
            continue
        base_name = tool_file.stem
        if base_name in existing:
            continue

        source = tool_file.read_text()
        func_name, call_args = extract_func_info(source)
        if not func_name:
            continue

        module = f"hexawyn.mcp.tools.{base_name}"
        adapters = extract_adapters(source)
        class_name = "".join(w.capitalize() for w in base_name.split("_"))

        # Build patch blocks
        adapter_list = adapters.split(", ") if adapters else []
        patches_happy_lines = []
        patches_error_lines = []
        patches_happy_lines.append(
            '        patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),'
        )
        for ad in adapter_list:
            patches_happy_lines.append(
                f'        patch("hexawyn.mcp.server.{ad}", return_value=MagicMock()),'
            )
            patches_error_lines.append(
                f'        patch("hexawyn.mcp.server.{ad}", side_effect=RuntimeError("test error")),'
            )
        patches_error_lines.append(
            '        patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),'
        )

        patch_happy = "\n".join(patches_happy_lines) if patches_happy_lines else ""
        patch_error = "\n".join(patches_error_lines) if patches_error_lines else ""

        call_str = f"{func_name}({call_args})" if call_args else f"{func_name}()"

        test_content = f'''"""Unit tests for MCP tool: {base_name}."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class Test{class_name}Tool:
    def test_{func_name}_returns_dict(self) -> None:
        from {module} import {func_name}

        with (
{patch_happy}
        ):
            result = {call_str}

        assert isinstance(result, dict)

    def test_{func_name}_handles_error(self) -> None:
        from {module} import {func_name}

        with ({patch_error}
        ):
            result = {call_str}

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("{module}")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
'''

        (TEST_DIR / f"test_{base_name}.py").write_text(test_content)
        count += 1

    print(f"Generated {count} MCP tool test files.")


if __name__ == "__main__":
    main()
