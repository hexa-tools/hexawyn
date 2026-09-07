"""Dataset contract for the calico_segmentation_audit intent examples."""

from __future__ import annotations

import importlib
from pathlib import Path

import yaml

_DATASET = Path(__file__).parents[3] / "datasets" / "intent_examples.yaml"


class TestCalicoSegmentationAuditIntentExamples:
    def test_entry_maps_to_calico_segmentation_audit_tool(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        entry = data["calico_segmentation_audit"]
        assert entry["tool"] == "calico_segmentation_audit"

    def test_has_description(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        assert str(data["calico_segmentation_audit"]["description"]).strip()

    def test_has_at_least_five_questions(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["calico_segmentation_audit"]["questions"]
        assert len(questions) >= 5  # noqa: PLR2004
        assert any("calico" in q.lower() for q in questions)

    def test_covers_reachability_and_matrix(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["calico_segmentation_audit"]["questions"]
        assert any("reach" in q.lower() for q in questions)
        assert any("segmentation" in q.lower() or "matrix" in q.lower() for q in questions)

    def test_tool_is_auto_discovered_by_register_tools(self) -> None:
        mod = importlib.import_module("hexawyn.mcp.tools.calico_segmentation_audit")
        assert callable(getattr(mod, "register"))
