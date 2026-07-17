"""Unit tests for CLI command_router."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.cli.command_router import route_command


class TestRouteCommand:
    def test_route_command_returns_response(self) -> None:
        with patch("hexawyn.cli.command_router.get_runtime", return_value=MagicMock()):
            result = route_command("test query", adapter=MagicMock())
            assert result is not None

    def test_empty_query_returns_response(self) -> None:
        with patch("hexawyn.cli.command_router.get_runtime", return_value=MagicMock()):
            result = route_command("", adapter=MagicMock())
            assert result is not None
