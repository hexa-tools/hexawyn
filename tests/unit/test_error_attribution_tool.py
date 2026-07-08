from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.error_attribution_port import ErrorAttributionPort


class TestErrorAttributionTool:
    def test_returns_culprit(self) -> None:
        from hexawyn.mcp.tools.error_attribution import error_attribution

        with patch("hexawyn.mcp.server.build_error_attribution_adapter") as m:
            a = MagicMock(spec=ErrorAttributionPort)
            a.fetch_error_attribution.return_value = [
                {"service": "auth-service", "count": 1012},
                {"service": "payment-service", "count": 180},
                {"service": "checkout-service", "count": 48},
            ]
            m.return_value = a
            r = error_attribution(gateway="api-gateway")
        assert r["error"] is None
        assert r["total_errors"] == 1240
        assert r["pareto_culprit"] == "auth-service"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.error_attribution import error_attribution

        with patch(
            "hexawyn.mcp.server.build_error_attribution_adapter",
            side_effect=RuntimeError("boom"),
        ):
            r = error_attribution(gateway="x")
        assert r["error"] == "boom"


class TestBuildErrorAttributionAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.error_attribution_port import (
            ErrorAttributionPort,
        )
        from hexawyn.mcp.server import build_error_attribution_adapter

        assert isinstance(build_error_attribution_adapter(), ErrorAttributionPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.error_attribution")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
