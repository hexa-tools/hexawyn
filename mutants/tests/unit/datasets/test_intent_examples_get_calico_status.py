"""Dataset contract for the get_calico_status intent examples."""

from __future__ import annotations

import importlib
from pathlib import Path

import yaml

_DATASET = Path(__file__).parents[3] / "datasets" / "intent_examples.yaml"


class TestGetCalicoStatusIntentExamples:
    def test_entry_maps_to_get_calico_status_tool(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        entry = data["get_calico_status"]
        assert entry["tool"] == "get_calico_status"

    def test_has_description(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        assert str(data["get_calico_status"]["description"]).strip()

    def test_has_at_least_five_questions(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["get_calico_status"]["questions"]
        assert len(questions) >= 5  # noqa: PLR2004
        assert any("calico" in q.lower() for q in questions)

    def test_covers_health_and_connectivity(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["get_calico_status"]["questions"]
        assert any("health" in q.lower() or "ready" in q.lower() for q in questions)
        assert any("datapath" in q.lower() or "healthz" in q.lower() for q in questions)

    def test_tool_is_auto_discovered_by_register_tools(self) -> None:
        mod = importlib.import_module("hexawyn.mcp.tools.get_calico_status")
        assert callable(getattr(mod, "register"))
