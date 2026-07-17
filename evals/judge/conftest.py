"""Fixtures for DeepEval judge tests."""

import json
import os
from pathlib import Path

import pytest

DATASETS_DIR = Path(__file__).parent / "datasets"


def pytest_configure(config: object) -> None:
    os.environ.setdefault("DEEPEVAL_TELEMETRY_OPT_OUT", "YES")


def _has_valid_openai_key() -> bool:
    key = os.environ.get("OPENAI_API_KEY", "")
    return bool(key) and len(key) > 30 and "xxxxx" not in key.lower()


def pytest_collection_modifyitems(config: object, items: list[pytest.Item]) -> None:
    if _has_valid_openai_key():
        return
    skip_msg = "No valid OPENAI_API_KEY. Set a real key to run DeepEval judge tests."
    for item in items:
        if item.get_closest_marker("judge"):
            item.add_marker(pytest.mark.skip(reason=skip_msg))


@pytest.fixture
def demo_mode() -> bool:
    return bool(os.environ.get("HEXAWYN_DEMO_MODE", "true"))


@pytest.fixture
def evaluator_model() -> str:
    return os.environ.get("EVALUATOR_MODEL", "qwen3:8b")


def load_cases(filename: str) -> list[dict[str, object]]:
    path = DATASETS_DIR / filename
    cases: list[dict[str, object]] = []
    for line in path.read_text(encoding="utf-8").strip().splitlines():
        if line.strip():
            cases.append(json.loads(line))
    return cases
