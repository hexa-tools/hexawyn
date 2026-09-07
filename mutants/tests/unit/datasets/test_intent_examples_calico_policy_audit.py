"""Dataset contract for the calico_policy_audit intent examples."""

from __future__ import annotations

import importlib
from pathlib import Path

import yaml

_DATASET = Path(__file__).parents[3] / "datasets" / "intent_examples.yaml"


class TestCalicoPolicyAuditIntentExamples:
    def test_entry_maps_to_calico_policy_audit_tool(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        entry = data["calico_policy_audit"]
        assert entry["tool"] == "calico_policy_audit"

    def test_has_description(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        assert str(data["calico_policy_audit"]["description"]).strip()

    def test_has_at_least_five_questions(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["calico_policy_audit"]["questions"]
        assert len(questions) >= 5  # noqa: PLR2004
        assert any("calico" in q.lower() for q in questions)

    def test_covers_gaps_and_default_deny(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["calico_policy_audit"]["questions"]
        assert any("gap" in q.lower() or "unrestricted" in q.lower() for q in questions)
        assert any("default-deny" in q.lower() for q in questions)

    def test_tool_is_auto_discovered_by_register_tools(self) -> None:
        mod = importlib.import_module("hexawyn.mcp.tools.calico_policy_audit")
        assert callable(getattr(mod, "register"))
