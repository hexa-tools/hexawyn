"""Dataset contract for the calico_bgp_audit intent examples."""

from __future__ import annotations

import importlib
from pathlib import Path

import yaml

_DATASET = Path(__file__).parents[3] / "datasets" / "intent_examples.yaml"


class TestCalicoBgpAuditIntentExamples:
    def test_entry_maps_to_calico_bgp_audit_tool(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        entry = data["calico_bgp_audit"]
        assert entry["tool"] == "calico_bgp_audit"

    def test_content(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        entry = data["calico_bgp_audit"]
        assert str(entry["description"]).strip()
        assert entry["tool"] == "calico_bgp_audit"

    def test_has_at_least_five_questions(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["calico_bgp_audit"]["questions"]
        assert len(questions) >= 5  # noqa: PLR2004
        assert any("bgp" in q.lower() for q in questions)

    def test_covers_peers_and_mesh(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["calico_bgp_audit"]["questions"]
        assert any("peer" in q.lower() for q in questions)
        assert any("mesh" in q.lower() or "asn" in q.lower() for q in questions)

    def test_tool_is_auto_discovered_by_register_tools(self) -> None:
        mod = importlib.import_module("hexawyn.mcp.tools.calico_bgp_audit")
        assert callable(getattr(mod, "register"))
