"""Dataset contract for the list_calico_ip_pools intent examples."""

from __future__ import annotations

import importlib
from pathlib import Path

import yaml

_DATASET = Path(__file__).parents[3] / "datasets" / "intent_examples.yaml"


class TestListCalicoIpPoolsIntentExamples:
    def test_entry_maps_to_list_calico_ip_pools_tool(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        entry = data["list_calico_ip_pools"]
        assert entry["tool"] == "list_calico_ip_pools"

    def test_has_description(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        assert str(data["list_calico_ip_pools"]["description"]).strip()

    def test_has_at_least_five_questions(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["list_calico_ip_pools"]["questions"]
        assert len(questions) >= 5  # noqa: PLR2004
        assert any("calico" in q.lower() for q in questions)

    def test_covers_cidr_and_disabled(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["list_calico_ip_pools"]["questions"]
        assert any("cidr" in q.lower() for q in questions)
        assert any("disabled" in q.lower() or "nat" in q.lower() for q in questions)

    def test_tool_is_auto_discovered_by_register_tools(self) -> None:
        mod = importlib.import_module("hexawyn.mcp.tools.list_calico_ip_pools")
        assert callable(getattr(mod, "register"))
