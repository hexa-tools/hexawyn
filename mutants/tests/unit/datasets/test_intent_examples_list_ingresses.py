"""Dataset contract for the list_ingresses intent examples.

The intent corpus (datasets/intent_examples.yaml) feeds the BM25 tool
ranking: each entry contributes its description plus its question variants
as the document for a tool. This test locks the list_ingresses entry to
generic intent coverage and keeps the OpenShift routes capability distinct.
"""

from __future__ import annotations

import importlib
from pathlib import Path

import yaml

_DATASET = Path(__file__).parents[3] / "datasets" / "intent_examples.yaml"


class TestListIngressesIntentExamples:
    def test_entry_maps_to_list_ingresses_tool(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        entry = data["list_ingresses"]
        assert entry["tool"] == "list_ingresses"

    def test_has_at_least_five_generic_questions(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        questions = data["list_ingresses"]["questions"]
        assert len(questions) >= 5  # noqa: PLR2004
        assert any("hosts" in q for q in questions)
        assert any("TLS" in q for q in questions)
        assert any("service" in q for q in questions)

    def test_openshift_routes_entry_remains_distinct(self) -> None:
        data = yaml.safe_load(_DATASET.read_text(encoding="utf-8"))
        assert "list_openshift_routes" in data
        assert "list_ingresses" in data

    def test_tool_is_auto_discovered_by_register_tools(self) -> None:
        mod = importlib.import_module("hexawyn.mcp.tools.list_ingresses")
        assert callable(getattr(mod, "register"))
