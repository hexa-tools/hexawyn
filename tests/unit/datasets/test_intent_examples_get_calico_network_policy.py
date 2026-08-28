"""Dataset contract for the get_calico_network_policy intent examples."""

from __future__ import annotations

import importlib
from pathlib import Path

import yaml

_DATASET = Path(__file__).parents[3] / "datasets" / "intent_examples.yaml"


class TestGetCalicoNetworkPolicyIntentExamples:
    def test_entry_maps_to_get_calico_network_policy_tool(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        entry = data["get_calico_network_policy"]
        assert entry["tool"] == "get_calico_network_policy"

    def test_has_description(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        assert str(data["get_calico_network_policy"]["description"]).strip()

    def test_has_at_least_five_questions(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["get_calico_network_policy"]["questions"]
        assert len(questions) >= 5  # noqa: PLR2004
        assert any("calico" in q.lower() for q in questions)

    def test_covers_selector_and_action(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["get_calico_network_policy"]["questions"]
        assert any("selector" in q.lower() for q in questions)
        assert any("allow" in q.lower() or "deny" in q.lower() for q in questions)

    def test_tool_is_auto_discovered_by_register_tools(self) -> None:
        mod = importlib.import_module("hexawyn.mcp.tools.get_calico_network_policy")
        assert callable(getattr(mod, "register"))
