"""Unit tests for MCP tool: calico_felix_metrics."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCalicoFelixMetricsTool:
    def test_returns_dict(self) -> None:
        from hexawyn.mcp.tools.calico_felix_metrics import calico_felix_metrics

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.not_installed_marker = None
        mock_response.metrics_available = True
        mock_response.metrics_message = None
        mock_response.total_denies = 10
        mock_response.total_allows = 5
        mock_response.deny_policy_count = 1
        mock_response.policies = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_calico_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.calico_felix_metrics.CalicoFelixMetricsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = calico_felix_metrics()

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["total_denies"] == 10  # noqa: PLR2004
        assert result["error"] is None

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.calico_felix_metrics import calico_felix_metrics

        with patch(
            "hexawyn.mcp.server.build_calico_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = calico_felix_metrics()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"
        assert result.get("installed") is False

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.calico_felix_metrics")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))

    def test_policy_dict(self) -> None:
        from hexawyn.domain.models.calico import CalicoFelixPolicyCounter
        from hexawyn.mcp.tools.calico_felix_metrics import _policy_dict

        counter = CalicoFelixPolicyCounter(
            policy="default.deny",
            allow_packets=0,
            deny_packets=12,
            allow_bytes=0,
            deny_bytes=4096,
        )
        result = _policy_dict(counter)

        assert result["policy"] == "default.deny"
        assert result["deny_packets"] == 12  # noqa: PLR2004
        assert result["deny_bytes"] == 4096  # noqa: PLR2004
