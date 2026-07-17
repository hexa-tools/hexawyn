"""Generate use case unit tests by reading actual class names from source ports."""

import ast
from pathlib import Path

USE_CASE_DIR = Path("src/hexawyn/application/use_case")
TEST_DIR = Path("tests/unit/application/use_case")
PORTS_DIR = Path("src/hexawyn/application/ports/driving")


def find_class_names(source: str) -> list[str]:
    try:
        tree = ast.parse(source)
        return [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    except SyntaxError:
        return []


def find_service_call_method(source: str) -> str:
    """Find the service method name called in execute()."""
    try:
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "execute":
                for subnode in ast.walk(node):
                    if isinstance(subnode, ast.Call):
                        if hasattr(subnode.func, "attr"):
                            return subnode.func.attr
        return "execute"
    except SyntaxError:
        return "execute"


def get_use_case_class(source: str) -> str:
    classes = find_class_names(source)
    for cls in classes:
        if "UseCase" in cls and "ABC" not in cls:
            return cls
    return ""


def get_service_class(use_case_name: str) -> str:
    sp_file = PORTS_DIR / use_case_name / f"{use_case_name}_service_port.py"
    if not sp_file.exists():
        return ""
    classes = find_class_names(sp_file.read_text())
    for cls in classes:
        if "Port" in cls:
            return cls
    return ""


def main() -> None:
    for f in TEST_DIR.glob("test_uc_*.py"):
        f.unlink()

    count = 0
    errors = []
    for uc_dir in sorted(USE_CASE_DIR.iterdir()):
        if not uc_dir.is_dir():
            continue
        name = uc_dir.name
        py_files = list(uc_dir.glob("*_use_case.py"))
        if not py_files:
            continue

        source = py_files[0].read_text()
        uc_class = get_use_case_class(source)
        svc_class = get_service_class(name)
        method = find_service_call_method(source)

        if not uc_class or not svc_class:
            errors.append(f"{name}: uc={uc_class}, svc={svc_class}")
            continue

        test_content = f'''"""Unit tests for {uc_class}."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.{name}.{name}_service_port import {svc_class}
from hexawyn.application.use_case.{name}.{name}_use_case import {uc_class}


class Test{uc_class}:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec={svc_class})
        use_case = {uc_class}(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.{method}.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec={svc_class})
        mock_service.{method}.side_effect = RuntimeError("test error")
        use_case = {uc_class}(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
'''
        (TEST_DIR / f"test_uc_{name}_use_case.py").write_text(test_content)
        count += 1

    print(f"Generated {count} use case test files.")
    if errors:
        print(f"Skipped {len(errors)}:")
        for e in errors[:10]:
            print(f"  - {e}")


if __name__ == "__main__":
    main()
