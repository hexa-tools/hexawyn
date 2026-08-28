"""Dataset contract for the calico_felix_metrics intent examples."""

from __future__ import annotations

import importlib
from pathlib import Path

import yaml

_DATASET = Path(__file__).parents[3] / "datasets" / "intent_examples.yaml"


class TestCalicoFelixMetricsIntentExamples:
    def test_entry_maps_to_calico_felix_metrics_tool(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        entry = data["calico_felix_metrics"]
        assert entry["tool"] == "calico_felix_metrics"

    def test_has_description(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        assert str(data["calico_felix_metrics"]["description"]).strip()

    def test_has_at_least_five_questions(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["calico_felix_metrics"]["questions"]
        assert len(questions) >= 5  # noqa: PLR2004
        assert any("calico" in q.lower() for q in questions)

    def test_covers_deny_and_counters(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["calico_felix_metrics"]["questions"]
        assert any("deny" in q.lower() or "denied" in q.lower() for q in questions)
        assert any("packet" in q.lower() or "counter" in q.lower() for q in questions)

    def test_tool_is_auto_discovered_by_register_tools(self) -> None:
        mod = importlib.import_module("hexawyn.mcp.tools.calico_felix_metrics")
        assert callable(getattr(mod, "register"))
