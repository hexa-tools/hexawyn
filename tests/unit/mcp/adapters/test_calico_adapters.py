"""Tests for mcp/adapters/calico_adapters.py builder functions."""

from __future__ import annotations

from unittest.mock import patch

from hexawyn.application.ports.driven.calico_port import CalicoPort


class TestCalicoAdapterBuilders:
    def test_build_calico_adapter_returns_calico_port(self) -> None:
        from hexawyn.mcp.adapters.calico_adapters import build_calico_adapter

        with patch(
            "hexawyn.mcp.adapters.calico_adapters.build_calico_metrics_adapter",
            return_value=None,
        ):
            result = build_calico_adapter()

        assert isinstance(result, CalicoPort)

    def test_build_calico_metrics_adapter(self) -> None:
        from hexawyn.adapters.secondary.calico.calico_prometheus_adapter import (
            CalicoPrometheusAdapter,
        )
        from hexawyn.mcp.adapters.calico_adapters import build_calico_metrics_adapter

        with patch(
            "hexawyn.mcp.adapters.observability_adapters.build_metrics_query_adapter",
            return_value=None,
        ):
            result = build_calico_metrics_adapter()

        assert isinstance(result, CalicoPrometheusAdapter)

    def test_server_module_reexports_builders(self) -> None:
        import hexawyn.mcp.server

        assert "build_calico_adapter" in hexawyn.mcp.server.__all__
        assert "build_calico_metrics_adapter" in hexawyn.mcp.server.__all__
        assert callable(hexawyn.mcp.server.build_calico_adapter)
        assert callable(hexawyn.mcp.server.build_calico_metrics_adapter)
