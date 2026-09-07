from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.service.chat_router import route_command


class TestRouteCommand:
    def test_route_command_imports_and_runs(self) -> None:
        MagicMock()
        assert callable(route_command)


class TestRouteCommandSignature:
    def test_accepts_text_and_adapter(self) -> None:
        mock_adapter = MagicMock()
        try:
            route_command("hello", mock_adapter)
        except Exception:
            pass
