"""Unit tests for MCP tool description injection from intent_examples.yaml."""

from __future__ import annotations

import asyncio
from pathlib import Path
from unittest.mock import patch

import yaml
from hexawyn.mcp.server import (
    EXAMPLES_LIMIT,
    build_enriched_tool_descriptions,
    build_tool_descriptions,
)


class TestToolDescriptionInjection:
    def test_loads_descriptions_from_intent_yaml(self) -> None:
        descriptions = build_tool_descriptions()

        min_descriptions = 100
        assert isinstance(descriptions, dict)
        assert len(descriptions) >= min_descriptions
        assert descriptions["adaptive_namespace_investigation"]

    def test_every_registered_tool_has_a_description(self) -> None:
        from hexawyn.mcp.server import mcp

        descriptions = build_tool_descriptions()

        async def _names() -> set[str]:
            tools = await mcp.list_tools()
            return {t.name for t in tools}

        registered = asyncio.run(_names())
        missing = {name for name in registered if not descriptions.get(name)}
        assert not missing, f"tools without description: {missing}"

    def test_descriptions_match_control_plane_yaml(self) -> None:
        with open("datasets/intent_examples.yaml") as f:
            intents = yaml.safe_load(f)

        descriptions = build_tool_descriptions()
        for use_case, entry in intents.items():
            if not isinstance(entry, dict) or not entry.get("tool"):
                continue
            tool = entry["tool"]
            # Canonical use case (key == tool name) defines the tool description.
            if use_case != tool:
                continue
            assert descriptions.get(tool) == entry.get(
                "description"
            ), f"description mismatch for tool '{tool}'"

    def test_returns_empty_when_yaml_missing(self) -> None:
        with patch.object(Path, "read_text", side_effect=FileNotFoundError):
            assert build_tool_descriptions() == {}

    def test_returns_empty_when_yaml_not_a_dict(self) -> None:
        with patch("hexawyn.mcp.server.yaml.safe_load", return_value=["just", "a", "list"]):
            assert build_tool_descriptions() == {}

    def test_skips_entries_without_description(self) -> None:
        data = {
            "good": {"tool": "good", "description": "has desc"},
            "no_desc": {"tool": "no_desc"},
            "bad_entry": "not a dict",
        }
        with patch("hexawyn.mcp.server.yaml.safe_load", return_value=data):
            descriptions = build_tool_descriptions()

        assert descriptions == {"good": "has desc"}

    def test_register_tools_skips_broken_modules(self) -> None:
        from fastmcp import FastMCP
        from hexawyn.mcp.server import register_tools

        server = FastMCP("test")

        with patch(
            "importlib.import_module",
            side_effect=ImportError("broken module"),
        ):
            register_tools(server)

        assert callable(getattr(server, "list_tools"))


class TestEnrichedToolDescriptions:
    def test_build_enriched_adds_examples(self) -> None:
        questions = [
            "Analyze the logs of checkout.",
            "Any errors in checkout logs?",
            "Why is api-gateway failing?",
        ]
        data = {
            "analyze_pod_logs": {
                "tool": "analyze_pod_logs",
                "description": "Analyze pod logs for errors.",
                "questions": questions,
            }
        }
        with patch("hexawyn.mcp.server.yaml.safe_load", return_value=data):
            enriched = build_enriched_tool_descriptions()

        desc = enriched["analyze_pod_logs"]
        assert "Analyze pod logs for errors." in desc
        assert "Examples:" in desc
        assert "- Analyze the logs of checkout." in desc
        assert "- Any errors in checkout logs?" in desc
        assert "- Why is api-gateway failing?" in desc
        assert desc.count("- ") == len(questions)

    def test_build_enriched_caps_at_limit(self) -> None:
        many = [f"Question number {i}" for i in range(12)]
        data = {
            "cap_tool": {"tool": "cap_tool", "description": "A capped tool.", "questions": many}
        }
        with patch("hexawyn.mcp.server.yaml.safe_load", return_value=data):
            enriched = build_enriched_tool_descriptions()

        desc = enriched["cap_tool"]
        assert desc.count("- Question") == EXAMPLES_LIMIT
        assert f"- Question number {EXAMPLES_LIMIT - 1}" in desc
        assert f"- Question number {EXAMPLES_LIMIT}" not in desc

    def test_build_enriched_keeps_description_without_questions(self) -> None:
        data = {"bare": {"tool": "bare", "description": "No examples here."}}
        with patch("hexawyn.mcp.server.yaml.safe_load", return_value=data):
            enriched = build_enriched_tool_descriptions()

        assert enriched["bare"] == "No examples here."

    def test_build_enriched_returns_empty_when_no_data(self) -> None:
        with patch("hexawyn.mcp.server.yaml.safe_load", return_value={}):
            assert build_enriched_tool_descriptions() == {}

    def test_register_tools_sets_enriched_description(self) -> None:
        from fastmcp import FastMCP
        from hexawyn.mcp.server import register_tools

        def analyze_pod_logs() -> dict[str, str]:
            """Analyze pod logs for errors."""
            return {}

        data = {
            "analyze_pod_logs": {
                "tool": "analyze_pod_logs",
                "description": "Analyze pod logs for errors.",
                "questions": ["Analyze the logs of checkout.", "Why is api-gateway failing?"],
            }
        }

        server = FastMCP("test")
        server.tool()(analyze_pod_logs)

        with patch("hexawyn.mcp.server.yaml.safe_load", return_value=data):
            with patch("importlib.import_module", side_effect=ImportError("skip discovery")):
                register_tools(server)

        tool = next(t for t in asyncio.run(server.list_tools()) if t.name == "analyze_pod_logs")
        assert "Examples:" in tool.description
        assert "- Analyze the logs of checkout." in tool.description
        assert "- Why is api-gateway failing?" in tool.description
