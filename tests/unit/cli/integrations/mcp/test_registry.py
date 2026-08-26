from __future__ import annotations

import pytest
from hexawyn.cli.integrations.mcp.base import MCPClientIntegration
from hexawyn.cli.integrations.mcp.claude import ClaudeCodeIntegration
from hexawyn.cli.integrations.mcp.codex import CodexIntegration
from hexawyn.cli.integrations.mcp.cursor import CursorIntegration
from hexawyn.cli.integrations.mcp.deepseek import DeepSeekHarnessIntegration
from hexawyn.cli.integrations.mcp.gemini import GeminiIntegration
from hexawyn.cli.integrations.mcp.opencode import OpenCodeIntegration
from hexawyn.cli.integrations.mcp.registry import get_integration, list_clients


class TestRegistry:
    def test_clients_are_registered(self) -> None:
        assert set(list_clients()) == {
            "claude",
            "codex",
            "opencode",
            "cursor",
            "gemini",
            "deepseek",
        }

    def test_get_claude_returns_claude_integration(self) -> None:
        integration = get_integration("claude")
        assert isinstance(integration, ClaudeCodeIntegration)

    def test_get_codex_returns_codex_integration(self) -> None:
        integration = get_integration("codex")
        assert isinstance(integration, CodexIntegration)

    def test_get_opencode_returns_opencode_integration(self) -> None:
        integration = get_integration("opencode")
        assert isinstance(integration, OpenCodeIntegration)

    def test_get_cursor_returns_cursor_integration(self) -> None:
        integration = get_integration("cursor")
        assert isinstance(integration, CursorIntegration)

    def test_get_gemini_returns_gemini_integration(self) -> None:
        integration = get_integration("gemini")
        assert isinstance(integration, GeminiIntegration)

    def test_get_deepseek_returns_deepseek_integration(self) -> None:
        integration = get_integration("deepseek")
        assert isinstance(integration, DeepSeekHarnessIntegration)

    def test_get_unknown_client_raises_key_error(self) -> None:
        with pytest.raises(KeyError):
            get_integration("copilot")

    def test_every_registered_client_is_an_integration(self) -> None:
        for client in list_clients():
            integration = get_integration(client)
            assert isinstance(integration, MCPClientIntegration)
