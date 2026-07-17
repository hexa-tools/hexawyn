"""RED tests — use case + MCP server integration"""

import asyncio
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driving.estimate_rightsizing_savings.estimate_rightsizing_savings_command import (
    EstimateRightsizingSavingsCommand,
)
from hexawyn.application.ports.driving.estimate_rightsizing_savings.estimate_rightsizing_savings_response import (
    EstimateRightsizingSavingsResponse,
)
from hexawyn.application.ports.driving.estimate_rightsizing_savings.estimate_rightsizing_savings_service_port import (
    EstimateRightsizingSavingsServicePort,
)
from hexawyn.application.use_case.estimate_rightsizing_savings.estimate_rightsizing_savings_use_case import (
    EstimateRightsizingSavingsUseCase,
)
from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.domain.models.rightsizing import (
    RightsizingRecommendation,
    RightsizingReport,
    RightsizingType,
)


def _make_response(
    recommendations: list[RightsizingRecommendation] | None = None,
    metrics_available: bool = True,
) -> EstimateRightsizingSavingsResponse:
    return EstimateRightsizingSavingsResponse(
        report=RightsizingReport(
            recommendations=recommendations or [],
            skipped_count=0,
            total_monthly_savings_usd=sum(
                r.monthly_savings_usd for r in (recommendations or []) if r.monthly_savings_usd > 0
            ),
        ),
        metrics_server_available=metrics_available,
    )


def _rec(name: str = "ml-worker", savings: float = 71.0) -> RightsizingRecommendation:
    return RightsizingRecommendation(
        resource_name=name,
        namespace="production",
        kind="Deployment",
        rightsizing_type=RightsizingType.OVER_PROVISIONED,
        current_cpu_cores=4.0,
        recommended_cpu_cores=1.04,
        current_memory_mi=8192.0,
        recommended_memory_mi=2730.0,
        monthly_savings_usd=savings,
        waste_percentage=80.0,
        reason="CPU usage 20% of requests",
        priority="high",
    )


class TestEstimateRightsizingSavingsUseCase:
    def test_delegates_to_service(self) -> None:
        service = MagicMock(spec=EstimateRightsizingSavingsServicePort)
        service.estimate_rightsizing_savings.return_value = _make_response([_rec()])
        use_case = EstimateRightsizingSavingsUseCase(service=service)

        result = use_case.execute(EstimateRightsizingSavingsCommand())

        service.estimate_rightsizing_savings.assert_called_once()
        assert len(result.report.recommendations) == 1

    def test_passes_command_through(self) -> None:
        service = MagicMock(spec=EstimateRightsizingSavingsServicePort)
        service.estimate_rightsizing_savings.return_value = _make_response()
        use_case = EstimateRightsizingSavingsUseCase(service=service)
        cmd = EstimateRightsizingSavingsCommand(top_n=3)

        use_case.execute(cmd)

        service.estimate_rightsizing_savings.assert_called_once_with(cmd)

    def test_cluster_error_propagates(self) -> None:
        service = MagicMock(spec=EstimateRightsizingSavingsServicePort)
        service.estimate_rightsizing_savings.side_effect = ClusterUnreachableError("down")
        use_case = EstimateRightsizingSavingsUseCase(service=service)

        with pytest.raises(ClusterUnreachableError):
            use_case.execute(EstimateRightsizingSavingsCommand())


class TestMCPEstimateRightsizingSavingsTool:
    def test_tool_is_registered(self) -> None:
        from hexawyn.mcp.server import mcp

        tools = asyncio.run(mcp.list_tools())
        tool_names = {t.name for t in tools}
        assert "estimate_rightsizing_savings" in tool_names

    def test_returns_recommendations_for_over_provisioned(self) -> None:
        from hexawyn.application.ports.driven.rightsizing_port import RightsizingPort

        mock_port = MagicMock(spec=RightsizingPort)
        mock_port.get_workload_rightsizing_data.return_value = [
            {
                "resource_name": "ml-worker",
                "namespace": "production",
                "kind": "Deployment",
                "cpu_requested_cores": 4.0,
                "memory_requested_mi": 8192.0,
                "cpu_actual_cores": 0.8,
                "memory_actual_mi": 2100.0,
            }
        ]

        with patch("hexawyn.mcp.server.build_rightsizing_adapter", return_value=mock_port):
            from hexawyn.mcp.tools.estimate_rightsizing_savings import (
                estimate_rightsizing_savings,
            )

            result = estimate_rightsizing_savings()

        assert result["error"] is None
        assert len(result["recommendations"]) == 1
        assert result["recommendations"][0]["resource_name"] == "ml-worker"
        assert result["metrics_server_available"] is True

    def test_cluster_error_captured_in_error_field(self) -> None:
        from hexawyn.application.ports.driven.rightsizing_port import RightsizingPort
        from hexawyn.domain.errors import ClusterUnreachableError

        mock_port = MagicMock(spec=RightsizingPort)
        mock_port.get_workload_rightsizing_data.side_effect = ClusterUnreachableError("down")

        with patch("hexawyn.mcp.server.build_rightsizing_adapter", return_value=mock_port):
            from hexawyn.mcp.tools.estimate_rightsizing_savings import (
                estimate_rightsizing_savings,
            )

            result = estimate_rightsizing_savings()

        assert result["error"] is not None
        assert result["recommendations"] == []

    def test_metrics_server_unavailable_reflected_in_response(self) -> None:
        from hexawyn.application.ports.driven.rightsizing_port import RightsizingPort

        mock_port = MagicMock(spec=RightsizingPort)
        mock_port.get_workload_rightsizing_data.return_value = [
            {
                "resource_name": "svc",
                "namespace": "ns",
                "kind": "Deployment",
                "cpu_requested_cores": 2.0,
                "memory_requested_mi": 4096.0,
                "cpu_actual_cores": None,
                "memory_actual_mi": None,
            }
        ]

        with patch("hexawyn.mcp.server.build_rightsizing_adapter", return_value=mock_port):
            from hexawyn.mcp.tools.estimate_rightsizing_savings import (
                estimate_rightsizing_savings,
            )

            result = estimate_rightsizing_savings()

        assert result["metrics_server_available"] is False
