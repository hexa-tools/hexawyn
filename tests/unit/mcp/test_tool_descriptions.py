"""Unit tests for MCP tool description injection from intent_examples.yaml."""

from __future__ import annotations

import asyncio
from pathlib import Path
from unittest.mock import patch

import yaml
from hexawyn.mcp.server import build_tool_descriptions


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
