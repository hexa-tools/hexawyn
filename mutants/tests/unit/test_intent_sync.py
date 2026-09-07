"""Unit tests for datasets/intent_examples.yaml — synchronized with control-plane."""

from __future__ import annotations

from pathlib import Path

import yaml

_INTENT_PATH = Path(__file__).parent.parent.parent / "datasets" / "intent_examples.yaml"
_CONTROL_PLANE_PATH = Path("/home/djepeno/sites/hexa-control-plane/datasets/intent_examples.yaml")


def _load_intents(path: Path) -> dict[str, dict[str, object]]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return {k: v for k, v in data.items() if isinstance(v, dict)}


class TestIntentSynchronization:
    def test_every_use_case_has_description(self) -> None:
        intents = _load_intents(_INTENT_PATH)

        for use_case, entry in intents.items():
            description = str(entry.get("description", "")).strip()
            assert description, f"use case '{use_case}' is missing a description"

    def test_every_use_case_has_at_least_five_questions(self) -> None:
        intents = _load_intents(_INTENT_PATH)
        min_questions = 5

        for use_case, entry in intents.items():
            questions = entry.get("questions", [])
            assert (
                isinstance(questions, list) and len(questions) >= min_questions
            ), f"use case '{use_case}' has fewer than {min_questions} questions"

    def test_shared_use_cases_match_control_plane_descriptions(self) -> None:
        if not _CONTROL_PLANE_PATH.exists():
            return
        local = _load_intents(_INTENT_PATH)
        control = _load_intents(_CONTROL_PLANE_PATH)

        for use_case, local_entry in local.items():
            control_entry = control.get(use_case)
            if not control_entry:
                continue
            assert local_entry.get("description") == control_entry.get(
                "description"
            ), f"description drift for '{use_case}'"

    def test_tools_match_registered_mcp_tools(self) -> None:
        import asyncio

        from hexawyn.mcp.server import mcp

        async def _tool_names() -> set[str]:
            tools = await mcp.list_tools()
            return {t.name for t in tools}

        registered = asyncio.run(_tool_names())
        intents = _load_intents(_INTENT_PATH)

        for use_case, entry in intents.items():
            tool = str(entry.get("tool", ""))
            assert tool, f"use case '{use_case}' has no tool"
            assert (
                tool in registered
            ), f"tool '{tool}' (for {use_case}) is not a registered MCP tool"
