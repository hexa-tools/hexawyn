"""RED → GREEN — Layers 3-6: driven port, driving ports, app service, use case."""

import inspect
from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.error_budget_port import (
    ErrorBudgetPort,
    ServiceSuccessRateRawData,
)
from hexawyn.application.ports.driving.compute_slo_error_budget.compute_slo_error_budget_command import (
    ComputeSLOErrorBudgetCommand,
)
from hexawyn.application.ports.driving.compute_slo_error_budget.compute_slo_error_budget_response import (
    ComputeSLOErrorBudgetResponse,
)
from hexawyn.application.ports.driving.compute_slo_error_budget.compute_slo_error_budget_service_port import (
    ComputeSLOErrorBudgetServicePort,
)
from hexawyn.application.service.compute_slo_error_budget_service import (
    ComputeSLOErrorBudgetService,
)
from hexawyn.application.use_case.compute_slo_error_budget.compute_slo_error_budget_use_case import (
    ComputeSLOErrorBudgetUseCase,
)
from hexawyn.domain.models.error_budget import SLOErrorBudgetResult


class TestErrorBudgetPort:
    def test_is_abstract(self) -> None:
        assert inspect.isabstract(ErrorBudgetPort)

    def test_concrete_impl_must_implement_fetch_success_rate(self) -> None:
        class BadAdapter(ErrorBudgetPort):
            pass

        with pytest.raises(TypeError):
            BadAdapter()  # type: ignore[abstract]

    def test_concrete_impl_accepted(self) -> None:
        class GoodAdapter(ErrorBudgetPort):
            def fetch_success_rate(
                self, service_name: str, window_days: int
            ) -> ServiceSuccessRateRawData:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=1.0,
                    error_rate=0.0,
                    has_data=True,
                    observation_days=window_days,
                )

        adapter = GoodAdapter()
        result = adapter.fetch_success_rate("test", 30)
        assert result["service_name"] == "test"


class TestComputeSLOErrorBudgetCommand:
    def test_default_values(self) -> None:
        cmd = ComputeSLOErrorBudgetCommand(service_name="payments")
        assert cmd.service_name == "payments"
        assert cmd.slo_target == 0.999
        assert cmd.rolling_window_days == 30

    def test_custom_values(self) -> None:
        cmd = ComputeSLOErrorBudgetCommand(
            service_name="auth", slo_target=0.995, rolling_window_days=7
        )
        assert cmd.slo_target == 0.995
        assert cmd.rolling_window_days == 7

    def test_is_frozen(self) -> None:
        cmd = ComputeSLOErrorBudgetCommand(service_name="svc")
        with pytest.raises(Exception):
            cmd.slo_target = 0.99  # type: ignore[misc]


class TestComputeSLOErrorBudgetResponse:
    def test_holds_result(self) -> None:
        inner = SLOErrorBudgetResult(
            service_name="test",
            slo_target=0.999,
        )
        resp = ComputeSLOErrorBudgetResponse(result=inner)
        assert resp.result is inner


class TestComputeSLOErrorBudgetService:
    def _mock_port(self) -> MagicMock:
        port = MagicMock(spec=ErrorBudgetPort)
        port.fetch_success_rate.return_value = ServiceSuccessRateRawData(
            service_name="payment-service",
            total_requests=100000,
            successful_requests=99500,
            failed_requests=500,
            success_rate=0.995,
            error_rate=0.005,
            has_data=True,
            observation_days=30,
        )
        return port

    def test_calls_port_with_correct_args(self) -> None:
        port = self._mock_port()
        service = ComputeSLOErrorBudgetService(error_budget_port=port)

        service.compute_slo_error_budget(
            ComputeSLOErrorBudgetCommand(
                service_name="payment-service",
                slo_target=0.999,
                rolling_window_days=30,
            )
        )

        port.fetch_success_rate.assert_called_once_with("payment-service", 30)

    def test_returns_response_with_result(self) -> None:
        port = self._mock_port()
        service = ComputeSLOErrorBudgetService(error_budget_port=port)

        response = service.compute_slo_error_budget(
            ComputeSLOErrorBudgetCommand(
                service_name="payment-service",
                slo_target=0.999,
            )
        )

        assert isinstance(response, ComputeSLOErrorBudgetResponse)
        assert isinstance(response.result, SLOErrorBudgetResult)
        assert response.result.service_name == "payment-service"
        assert response.result.burn_rate == 5.0

    def test_burn_rate_5x_returns_exhausted_verdict(self) -> None:
        port = MagicMock(spec=ErrorBudgetPort)
        port.fetch_success_rate.return_value = ServiceSuccessRateRawData(
            service_name="payment-service",
            total_requests=100000,
            successful_requests=99500,
            failed_requests=500,
            success_rate=0.995,
            error_rate=0.005,
            has_data=True,
            observation_days=30,
        )
        service = ComputeSLOErrorBudgetService(error_budget_port=port)

        response = service.compute_slo_error_budget(
            ComputeSLOErrorBudgetCommand(
                service_name="payment-service",
                slo_target=0.999,
                rolling_window_days=30,
            )
        )

        assert response.result.verdict == "budget_exhausted"

    def test_uses_default_slo_when_not_configured(self) -> None:
        port = MagicMock(spec=ErrorBudgetPort)
        port.fetch_success_rate.return_value = ServiceSuccessRateRawData(
            service_name="svc",
            total_requests=100000,
            successful_requests=100000,
            failed_requests=0,
            success_rate=1.0,
            error_rate=0.0,
            has_data=True,
            observation_days=30,
        )
        service = ComputeSLOErrorBudgetService(error_budget_port=port)

        response = service.compute_slo_error_budget(
            ComputeSLOErrorBudgetCommand(
                service_name="svc",
                slo_target=0.0,
            )
        )

        assert response.result.slo_target == 0.995


class TestComputeSLOErrorBudgetUseCase:
    def test_delegates_to_service(self) -> None:
        service = MagicMock(spec=ComputeSLOErrorBudgetServicePort)
        inner = SLOErrorBudgetResult(service_name="test")
        service.compute_slo_error_budget.return_value = ComputeSLOErrorBudgetResponse(result=inner)
        use_case = ComputeSLOErrorBudgetUseCase(service=service)

        result = use_case.execute(ComputeSLOErrorBudgetCommand(service_name="test"))

        service.compute_slo_error_budget.assert_called_once()
        assert result.result is inner

    def test_passes_command_through(self) -> None:
        service = MagicMock(spec=ComputeSLOErrorBudgetServicePort)
        service.compute_slo_error_budget.return_value = ComputeSLOErrorBudgetResponse(
            result=SLOErrorBudgetResult()
        )
        use_case = ComputeSLOErrorBudgetUseCase(service=service)
        cmd = ComputeSLOErrorBudgetCommand(
            service_name="auth", slo_target=0.995, rolling_window_days=7
        )

        use_case.execute(cmd)

        service.compute_slo_error_budget.assert_called_once_with(cmd)
