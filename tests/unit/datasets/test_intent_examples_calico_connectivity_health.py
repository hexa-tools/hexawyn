"""Dataset contract for the calico_connectivity_health intent examples."""

from __future__ import annotations

import importlib
from pathlib import Path

import yaml

_DATASET = Path(__file__).parents[3] / "datasets" / "intent_examples.yaml"


class TestCalicoConnectivityHealthIntentExamples:
    def test_entry_maps_to_calico_connectivity_health_tool(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        entry = data["calico_connectivity_health"]
        assert entry["tool"] == "calico_connectivity_health"

    def test_has_description(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        assert str(data["calico_connectivity_health"]["description"]).strip()

    def test_has_at_least_five_questions(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["calico_connectivity_health"]["questions"]
        assert len(questions) >= 5  # noqa: PLR2004
        assert any("calico" in q.lower() for q in questions)

    def test_covers_dataplane_and_verdict(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["calico_connectivity_health"]["questions"]
        assert any("dataplane" in q.lower() for q in questions)
        assert any("healthy" in q.lower() or "degraded" in q.lower() for q in questions)

    def test_tool_is_auto_discovered_by_register_tools(self) -> None:
        mod = importlib.import_module("hexawyn.mcp.tools.calico_connectivity_health")
        assert callable(getattr(mod, "register"))
