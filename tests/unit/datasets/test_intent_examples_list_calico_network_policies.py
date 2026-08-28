"""Dataset contract for the list_calico_network_policies intent examples."""

from __future__ import annotations

import importlib
from pathlib import Path

import yaml

_DATASET = Path(__file__).parents[3] / "datasets" / "intent_examples.yaml"


class TestListCalicoNetworkPoliciesIntentExamples:
    def test_entry_maps_to_list_calico_network_policies_tool(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        entry = data["list_calico_network_policies"]
        assert entry["tool"] == "list_calico_network_policies"

    def test_has_description(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        assert str(data["list_calico_network_policies"]["description"]).strip()

    def test_has_at_least_five_questions(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["list_calico_network_policies"]["questions"]
        assert len(questions) >= 5  # noqa: PLR2004
        assert any("calico" in q.lower() for q in questions)

    def test_covers_namespaced_and_global(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["list_calico_network_policies"]["questions"]
        assert any("namespaced" in q.lower() or "namespace" in q.lower() for q in questions)
        assert any("global" in q.lower() for q in questions)

    def test_tool_is_auto_discovered_by_register_tools(self) -> None:
        mod = importlib.import_module("hexawyn.mcp.tools.list_calico_network_policies")
        assert callable(getattr(mod, "register"))
