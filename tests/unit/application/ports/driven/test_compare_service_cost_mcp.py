"""RED → GREEN — MCP tool: compare_service_cost."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.service_cost_port import (
    PodResourceSnapshotData,
    ServiceCostPort,
)
from hexawyn.domain.errors import ClusterUnreachableError


class TestCompareServiceCostTool:
    def test_delegates_and_returns_dict(self) -> None:
        mock_port = MagicMock(spec=ServiceCostPort)
        mock_port.fetch_pod_resources.return_value = [
            PodResourceSnapshotData(
                pod_name="payment-pod",
                namespace="production",
                month="2026-07",
                cpu_cores=2.0,
                memory_gb=4.0,
            ),
        ]

        with patch(
            "hexawyn.mcp.server.build_service_cost_adapter",
            return_value=mock_port,
        ):
            from hexawyn.mcp.tools.compare_service_cost import (
                compare_service_cost,
            )

            result = compare_service_cost(service_name="payment-service")

        assert result["service_name"] == "payment-service"
        assert result["current_month"]["total_cost"] > 0
        assert result["error"] is None

    def test_handles_exception_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_service_cost_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.compare_service_cost import (
                compare_service_cost,
            )

            result = compare_service_cost(service_name="svc")

        assert result["trend"] == "error"
        assert "down" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.compare_service_cost import register

        assert callable(register)
