"""RED → GREEN — Layers 3-6: driven port, driving ports, app service, use case."""

import inspect
from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.mttr_trend_port import (
    IncidentResolutionData,
    MTTRTrendPort,
)
from hexawyn.application.ports.driving.compute_mttr_trend.compute_mttr_trend_command import (
    ComputeMTTRTrendCommand,
)
from hexawyn.application.ports.driving.compute_mttr_trend.compute_mttr_trend_response import (
    ComputeMTTRTrendResponse,
)
from hexawyn.application.ports.driving.compute_mttr_trend.compute_mttr_trend_service_port import (
    ComputeMTTRTrendServicePort,
)
from hexawyn.application.service.compute_mttr_trend_service import (
    ComputeMTTRTrendService,
    _last_3_months,
)
from hexawyn.application.use_case.compute_mttr_trend.compute_mttr_trend_use_case import (
    ComputeMTTRTrendUseCase,
)
from hexawyn.domain.models.mttr_trend import MTTRTrendReport


class TestMTTRTrendPort:
    def test_is_abstract(self) -> None:
        assert inspect.isabstract(MTTRTrendPort)


class TestComputeMTTRTrendCommand:
    def test_default_months_empty(self) -> None:
        cmd = ComputeMTTRTrendCommand()
        assert cmd.months == []

    def test_is_frozen(self) -> None:
        cmd = ComputeMTTRTrendCommand()
        with pytest.raises(Exception):
            cmd.months = []  # type: ignore[misc]


class TestComputeMTTRTrendResponse:
    def test_holds_result(self) -> None:
        inner = MTTRTrendReport(trend="improving")
        resp = ComputeMTTRTrendResponse(result=inner)
        assert resp.result is inner


class TestComputeMTTRTrendService:
    def _mock_port(self) -> MagicMock:
        port = MagicMock(spec=MTTRTrendPort)
        port.fetch_incidents_by_month.return_value = []
        return port

    def test_calls_port_for_each_month(self) -> None:
        port = self._mock_port()
        service = ComputeMTTRTrendService(mttr_port=port)

        service.compute(ComputeMTTRTrendCommand(months=["2026-05", "2026-06", "2026-07"]))

        assert port.fetch_incidents_by_month.call_count == 3

    def test_returns_response_with_result(self) -> None:
        port = MagicMock(spec=MTTRTrendPort)
        port.fetch_incidents_by_month.return_value = [
            IncidentResolutionData(
                incident_id="INC-001",
                service_name="payment",
                severity="P1",
                resolution_minutes=45,
                resolved=True,
                root_cause="OOM",
            ),
        ]
        service = ComputeMTTRTrendService(mttr_port=port)

        response = service.compute(ComputeMTTRTrendCommand(months=["2026-07"]))

        assert isinstance(response, ComputeMTTRTrendResponse)
        assert isinstance(response.result, MTTRTrendReport)

    def test_default_months_uses_last_3(self) -> None:
        port = self._mock_port()
        service = ComputeMTTRTrendService(mttr_port=port)

        response = service.compute(ComputeMTTRTrendCommand())

        assert isinstance(response, ComputeMTTRTrendResponse)


class TestComputeMTTRTrendUseCase:
    def test_delegates_to_service(self) -> None:
        service = MagicMock(spec=ComputeMTTRTrendServicePort)
        inner = MTTRTrendReport(trend="improving")
        service.compute.return_value = ComputeMTTRTrendResponse(result=inner)
        use_case = ComputeMTTRTrendUseCase(service=service)

        result = use_case.execute(ComputeMTTRTrendCommand())

        service.compute.assert_called_once()
        assert result.result is inner


class TestLast3Months:
    def test_july_2026_returns_may_june_july(self) -> None:
        assert _last_3_months(2026, 7) == ["2026-05", "2026-06", "2026-07"]

    def test_january_2026_wraps_to_previous_year(self) -> None:
        assert _last_3_months(2026, 1) == ["2025-11", "2025-12", "2026-01"]
