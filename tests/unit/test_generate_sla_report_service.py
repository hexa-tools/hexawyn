from unittest.mock import MagicMock

from hexawyn.application.ports.driven.sla_report_port import (
    QuarterSlaData,
    ServiceSlaRaw,
    SlaReportPort,
)
from hexawyn.application.ports.driving.generate_sla_report.generate_sla_report_command import (
    GenerateSlaReportCommand,
)


def _svc(name: str, uptime: float) -> ServiceSlaRaw:
    return ServiceSlaRaw(
        service_name=name,
        sla_target_pct=99.9,
        uptime_pct=uptime,
        coverage_days=90,
        quarter_days=90,
        maintenance_minutes=0,
    )


def _data(services: list[ServiceSlaRaw], has_data: bool = True) -> QuarterSlaData:
    return QuarterSlaData(has_data=has_data, services=services, breaches=[])


def _port(data: QuarterSlaData, previous: float | None = None) -> MagicMock:
    port = MagicMock(spec=SlaReportPort)
    port.get_quarter_sla_data.return_value = data
    port.get_previous_quarter_avg_uptime.return_value = previous
    return port


class TestGenerateSlaReportService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.generate_sla_report.generate_sla_report_service_port import (  # noqa: E501
            GenerateSlaReportServicePort,
        )
        from hexawyn.application.service.generate_sla_report_service import (
            GenerateSlaReportService,
        )

        service = GenerateSlaReportService(sla_port=MagicMock(spec=SlaReportPort))

        assert isinstance(service, GenerateSlaReportServicePort)

    def test_generate_returns_report(self) -> None:
        from hexawyn.application.service.generate_sla_report_service import (
            GenerateSlaReportService,
        )

        service = GenerateSlaReportService(sla_port=_port(_data([_svc("payment", 99.95)])))

        response = service.generate(GenerateSlaReportCommand(quarter="2026-Q1"))

        service.sla_port_calls = None  # noqa: E501
        assert response.result.overall_met_count == 1

    def test_generate_requests_quarter_and_previous(self) -> None:
        from hexawyn.application.service.generate_sla_report_service import (
            GenerateSlaReportService,
        )

        port = _port(_data([_svc("payment", 99.9), _svc("checkout", 99.9)]), previous=99.5)
        service = GenerateSlaReportService(sla_port=port)

        response = service.generate(GenerateSlaReportCommand(quarter="2026-Q1"))

        port.get_quarter_sla_data.assert_called_once_with("2026-Q1")
        port.get_previous_quarter_avg_uptime.assert_called_once_with("2026-Q1")
        assert response.result.trend == "improving"

    def test_lets_error_propagate(self) -> None:
        import pytest
        from hexawyn.application.service.generate_sla_report_service import (
            GenerateSlaReportService,
        )
        from hexawyn.domain.errors import ClusterUnreachableError

        port = MagicMock(spec=SlaReportPort)
        port.get_quarter_sla_data.side_effect = ClusterUnreachableError("down")
        service = GenerateSlaReportService(sla_port=port)

        with pytest.raises(ClusterUnreachableError):
            service.generate(GenerateSlaReportCommand(quarter="2026-Q1"))
