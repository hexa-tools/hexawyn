"""Dataset contract for the get_calico_host_endpoints intent examples."""

from __future__ import annotations

import importlib
from pathlib import Path

import yaml

_DATASET = Path(__file__).parents[3] / "datasets" / "intent_examples.yaml"


class TestGetCalicoHostEndpointsIntentExamples:
    def test_entry_maps_to_get_calico_host_endpoints_tool(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        entry = data["get_calico_host_endpoints"]
        assert entry["tool"] == "get_calico_host_endpoints"

    def test_has_description(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        assert str(data["get_calico_host_endpoints"]["description"]).strip()

    def test_has_at_least_five_questions(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["get_calico_host_endpoints"]["questions"]
        assert len(questions) >= 5  # noqa: PLR2004
        assert any("calico" in q.lower() for q in questions)

    def test_covers_interfaces_and_policies(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["get_calico_host_endpoints"]["questions"]
        assert any("node" in q.lower() or "interface" in q.lower() for q in questions)
        assert any("policy" in q.lower() for q in questions)

    def test_tool_is_auto_discovered_by_register_tools(self) -> None:
        mod = importlib.import_module("hexawyn.mcp.tools.get_calico_host_endpoints")
        assert callable(getattr(mod, "register"))
