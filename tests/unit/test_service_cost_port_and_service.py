"""RED → GREEN — Layers 3-6: driven port, driving ports, app service, use case."""

import inspect
from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.service_cost_port import (
    PodResourceSnapshotData,
    ServiceCostPort,
)
from hexawyn.application.ports.driving.compare_service_cost.compare_service_cost_command import (
    CompareServiceCostCommand,
)
from hexawyn.application.ports.driving.compare_service_cost.compare_service_cost_response import (
    CompareServiceCostResponse,
)
from hexawyn.application.ports.driving.compare_service_cost.compare_service_cost_service_port import (
    CompareServiceCostServicePort,
)
from hexawyn.application.service.compare_service_cost_service import (
    CompareServiceCostService,
)
from hexawyn.application.use_case.compare_service_cost.compare_service_cost_use_case import (
    CompareServiceCostUseCase,
)
from hexawyn.domain.models.service_cost_comparison import ServiceCostComparison


class TestServiceCostPort:
    def test_is_abstract(self) -> None:
        assert inspect.isabstract(ServiceCostPort)

    def test_concrete_impl_must_implement(self) -> None:
        class Bad(ServiceCostPort):
            pass

        with pytest.raises(TypeError):
            Bad()  # type: ignore[abstract]


class TestCompareServiceCostCommand:
    def test_defaults(self) -> None:
        cmd = CompareServiceCostCommand(service_name="payment-service")
        assert cmd.cpu_price_per_core_hour == 0.03
        assert cmd.memory_price_per_gb_hour == 0.01

    def test_custom_pricing(self) -> None:
        cmd = CompareServiceCostCommand(
            service_name="svc",
            cpu_price_per_core_hour=0.04,
            memory_price_per_gb_hour=0.02,
        )
        assert cmd.cpu_price_per_core_hour == 0.04

    def test_is_frozen(self) -> None:
        cmd = CompareServiceCostCommand(service_name="svc")
        with pytest.raises(Exception):
            cmd.service_name = "other"  # type: ignore[misc]


class TestCompareServiceCostResponse:
    def test_holds_result(self) -> None:
        inner = ServiceCostComparison(service_name="test")
        resp = CompareServiceCostResponse(result=inner)
        assert resp.result is inner


class TestCompareServiceCostService:
    def _mock_port(self) -> MagicMock:
        port = MagicMock(spec=ServiceCostPort)
        port.fetch_pod_resources.return_value = []
        return port

    def test_calls_port_for_current_and_previous_month(self) -> None:
        port = self._mock_port()
        service = CompareServiceCostService(cost_port=port)

        service.compare(CompareServiceCostCommand(service_name="svc"))

        assert port.fetch_pod_resources.call_count == 2

    def test_returns_response_with_result(self) -> None:
        port = MagicMock(spec=ServiceCostPort)
        port.fetch_pod_resources.return_value = [
            PodResourceSnapshotData(
                pod_name="pod-1",
                namespace="production",
                month="2026-07",
                cpu_cores=2.0,
                memory_gb=4.0,
            ),
        ]
        service = CompareServiceCostService(cost_port=port)

        response = service.compare(CompareServiceCostCommand(service_name="svc"))

        assert isinstance(response, CompareServiceCostResponse)
        assert isinstance(response.result, ServiceCostComparison)


class TestCompareServiceCostUseCase:
    def test_delegates_to_service(self) -> None:
        service = MagicMock(spec=CompareServiceCostServicePort)
        inner = ServiceCostComparison(service_name="test")
        service.compare.return_value = CompareServiceCostResponse(result=inner)
        use_case = CompareServiceCostUseCase(service=service)

        result = use_case.execute(CompareServiceCostCommand(service_name="test"))

        service.compare.assert_called_once()
        assert result.result is inner
