"""RED → GREEN — MCP tool: compute_slo_error_budget."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.error_budget_port import (
    ErrorBudgetPort,
    ServiceSuccessRateRawData,
)
from hexawyn.domain.errors import PrometheusUnavailableError


class TestComputeSLOErrorBudgetTool:
    def test_delegates_and_returns_dict(self) -> None:
        mock_port = MagicMock(spec=ErrorBudgetPort)
        mock_port.fetch_success_rate.return_value = ServiceSuccessRateRawData(
            service_name="payment-service",
            total_requests=100000,
            successful_requests=99500,
            failed_requests=500,
            success_rate=0.995,
            error_rate=0.005,
            has_data=True,
            observation_days=30,
        )

        with patch(
            "hexawyn.mcp.server.build_error_budget_adapter",
            return_value=mock_port,
        ):
            from hexawyn.mcp.tools.compute_slo_error_budget import (
                compute_slo_error_budget,
            )

            result = compute_slo_error_budget(
                service_name="payment-service",
                slo_target=0.999,
            )

        assert result["burn_rate"] == 5.0
        assert result["verdict"] == "budget_exhausted"
        assert result["service_name"] == "payment-service"
        assert result["error"] is None

    def test_handles_exception_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_error_budget_adapter",
            side_effect=PrometheusUnavailableError("down"),
        ):
            from hexawyn.mcp.tools.compute_slo_error_budget import (
                compute_slo_error_budget,
            )

            result = compute_slo_error_budget(service_name="test-svc")

        assert result["burn_rate"] == 0.0
        assert "Prometheus" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.compute_slo_error_budget import register

        assert callable(register)
