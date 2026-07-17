from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.redundant_call_detection_port import (
    RedundantCallDetectionPort,
)
from hexawyn.domain.models.redundant_calls import RedundancyType, SpanInfo


class TestRedundantCallsTool:
    def test_returns_n_plus_one(self) -> None:
        from hexawyn.mcp.tools.redundant_calls import redundant_calls

        with patch("hexawyn.mcp.server.build_redundant_call_detection_adapter") as m:
            a = MagicMock(spec=RedundantCallDetectionPort)
            a.fetch_spans.return_value = [
                SpanInfo(
                    span_name="SELECT * FROM products WHERE id = ?",
                    service_name="db-service",
                    duration_ms=15.0,
                )
                for _ in range(47)
            ]
            m.return_value = a
            r = redundant_calls(flow="web -> api -> db")
        assert r["error"] is None
        assert len(r["patterns"]) >= 1
        assert r["patterns"][0]["type"] == RedundancyType.N_PLUS_ONE
        assert r["patterns"][0]["occurrences"] == 47

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.redundant_calls import redundant_calls

        with patch(
            "hexawyn.mcp.server.build_redundant_call_detection_adapter",
            side_effect=RuntimeError("boom"),
        ):
            r = redundant_calls(flow="web -> api")
        assert r["error"] == "boom"


class TestBuildRedundantCallDetectionAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.redundant_call_detection_port import (
            RedundantCallDetectionPort,
        )
        from hexawyn.mcp.server import build_redundant_call_detection_adapter

        assert isinstance(build_redundant_call_detection_adapter(), RedundantCallDetectionPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.redundant_calls")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
