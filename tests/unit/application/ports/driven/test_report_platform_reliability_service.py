from unittest.mock import MagicMock

from hexawyn.application.ports.driven.platform_reliability_port import (
    PlatformReliabilityPort,
    ReliabilityData,
)
from hexawyn.application.ports.driving.report_platform_reliability.report_platform_reliability_command import (  # noqa: E501
    ReportPlatformReliabilityCommand,
)


def _data(cost_per_minute: float | None = None) -> ReliabilityData:
    return ReliabilityData(
        period_minutes=43200,
        incidents=[
            {
                "date": "2026-06-14",
                "severity": "minor",
                "downtime_minutes": 12,
                "resolution_minutes": 12,
                "root_cause": "",
                "resolved": True,
                "planned_maintenance": False,
            }
        ],
        previous_avg_resolution_minutes=14,
        cost_per_downtime_minute_eur=cost_per_minute,
    )


class TestReportPlatformReliabilityService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.report_platform_reliability.report_platform_reliability_service_port import (  # noqa: E501
            ReportPlatformReliabilityServicePort,
        )
        from hexawyn.application.service.report_platform_reliability_service import (
            ReportPlatformReliabilityService,
        )

        service = ReportPlatformReliabilityService(
            reliability_port=MagicMock(spec=PlatformReliabilityPort)
        )

        assert isinstance(service, ReportPlatformReliabilityServicePort)

    def test_report_returns_result(self) -> None:
        from hexawyn.application.service.report_platform_reliability_service import (
            ReportPlatformReliabilityService,
        )

        port = MagicMock(spec=PlatformReliabilityPort)
        port.get_reliability_data.return_value = _data()
        service = ReportPlatformReliabilityService(reliability_port=port)

        response = service.report(ReportPlatformReliabilityCommand(period="2026-06"))

        port.get_reliability_data.assert_called_once_with("2026-06")
        assert response.result.total_incidents == 1
        assert response.result.executive_summary != ""

    def test_report_lets_error_propagate(self) -> None:
        import pytest
        from hexawyn.application.service.report_platform_reliability_service import (
            ReportPlatformReliabilityService,
        )
        from hexawyn.domain.errors import ClusterUnreachableError

        port = MagicMock(spec=PlatformReliabilityPort)
        port.get_reliability_data.side_effect = ClusterUnreachableError("down")
        service = ReportPlatformReliabilityService(reliability_port=port)

        with pytest.raises(ClusterUnreachableError):
            service.report(ReportPlatformReliabilityCommand(period="2026-06"))
