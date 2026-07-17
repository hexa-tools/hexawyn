"""RED → GREEN — Layers 3-6: driven port, driving ports, app service, use case."""

import inspect
from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.weekly_reliability_report_port import (
    IncidentRawData,
    ServiceReliabilityRawData,
    WeeklyReliabilityReportPort,
)
from hexawyn.application.ports.driving.generate_weekly_reliability_report.generate_weekly_reliability_report_command import (
    GenerateWeeklyReliabilityReportCommand,
)
from hexawyn.application.ports.driving.generate_weekly_reliability_report.generate_weekly_reliability_report_response import (
    GenerateWeeklyReliabilityReportResponse,
)
from hexawyn.application.ports.driving.generate_weekly_reliability_report.generate_weekly_reliability_report_service_port import (
    GenerateWeeklyReliabilityReportServicePort,
)
from hexawyn.application.service.generate_weekly_reliability_report_service import (
    GenerateWeeklyReliabilityReportService,
)
from hexawyn.application.use_case.generate_weekly_reliability_report.generate_weekly_reliability_report_use_case import (
    GenerateWeeklyReliabilityReportUseCase,
)
from hexawyn.domain.models.weekly_reliability_report import WeeklyReliabilityReport


class TestWeeklyReliabilityReportPort:
    def test_is_abstract(self) -> None:
        assert inspect.isabstract(WeeklyReliabilityReportPort)

    def test_concrete_impl_must_implement_methods(self) -> None:
        class Bad(WeeklyReliabilityReportPort):
            pass

        with pytest.raises(TypeError):
            Bad()  # type: ignore[abstract]

    def test_concrete_impl_accepted(self) -> None:
        class Good(WeeklyReliabilityReportPort):
            def fetch_service_reliability(
                self, window_days: int
            ) -> list[ServiceReliabilityRawData]:
                return []

            def fetch_incidents(self, window_days: int) -> list[IncidentRawData]:
                return []

        adapter = Good()
        assert adapter.fetch_service_reliability(7) == []


class TestGenerateWeeklyReliabilityReportCommand:
    def test_default_window_is_7(self) -> None:
        cmd = GenerateWeeklyReliabilityReportCommand()
        assert cmd.window_days == 7

    def test_custom_window(self) -> None:
        cmd = GenerateWeeklyReliabilityReportCommand(window_days=14)
        assert cmd.window_days == 14

    def test_is_frozen(self) -> None:
        cmd = GenerateWeeklyReliabilityReportCommand()
        with pytest.raises(Exception):
            cmd.window_days = 30  # type: ignore[misc]


class TestGenerateWeeklyReliabilityReportResponse:
    def test_holds_result(self) -> None:
        inner = WeeklyReliabilityReport(
            health_score=100.0,
            total_services=5,
        )
        resp = GenerateWeeklyReliabilityReportResponse(result=inner)
        assert resp.result is inner


class TestGenerateWeeklyReliabilityReportService:
    def _mock_port(self) -> MagicMock:
        port = MagicMock(spec=WeeklyReliabilityReportPort)
        port.fetch_service_reliability.return_value = []
        port.fetch_incidents.return_value = []
        return port

    def test_calls_port_with_window(self) -> None:
        port = self._mock_port()
        service = GenerateWeeklyReliabilityReportService(reliability_port=port)

        service.generate_report(GenerateWeeklyReliabilityReportCommand(window_days=7))

        port.fetch_service_reliability.assert_called_once_with(7)
        port.fetch_incidents.assert_called_once_with(7)

    def test_returns_response_with_result(self) -> None:
        port = self._mock_port()
        service = GenerateWeeklyReliabilityReportService(reliability_port=port)

        response = service.generate_report(GenerateWeeklyReliabilityReportCommand())

        assert isinstance(response, GenerateWeeklyReliabilityReportResponse)
        assert isinstance(response.result, WeeklyReliabilityReport)

    def test_service_passes_slo_failures_to_engine(self) -> None:
        port = MagicMock(spec=WeeklyReliabilityReportPort)
        port.fetch_service_reliability.return_value = [
            ServiceReliabilityRawData(
                service_name="payment-service",
                uptime_pct=99.92,
                error_rate=0.08,
                p99_latency_ms=245.0,
                slo_target=99.9,
                downtime_minutes=0,
                data_gap_minutes=0,
                created_mid_week=False,
            ),
            ServiceReliabilityRawData(
                service_name="auth-service",
                uptime_pct=99.72,
                error_rate=0.28,
                p99_latency_ms=820.0,
                slo_target=99.9,
                downtime_minutes=18,
                data_gap_minutes=0,
                created_mid_week=False,
            ),
        ]
        port.fetch_incidents.return_value = []
        service = GenerateWeeklyReliabilityReportService(reliability_port=port)

        response = service.generate_report(GenerateWeeklyReliabilityReportCommand())

        assert response.result.total_services == 2
        assert response.result.slo_pass_count == 1
        assert response.result.slo_fail_count == 1
        assert response.result.health_score == 50.0


class TestGenerateWeeklyReliabilityReportUseCase:
    def test_delegates_to_service(self) -> None:
        service = MagicMock(spec=GenerateWeeklyReliabilityReportServicePort)
        inner = WeeklyReliabilityReport(total_services=5)
        service.generate_report.return_value = GenerateWeeklyReliabilityReportResponse(result=inner)
        use_case = GenerateWeeklyReliabilityReportUseCase(service=service)

        result = use_case.execute(GenerateWeeklyReliabilityReportCommand())

        service.generate_report.assert_called_once()
        assert result.result is inner
