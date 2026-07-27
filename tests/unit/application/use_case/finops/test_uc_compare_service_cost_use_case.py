from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.finops.compare_service_cost.command import (
    CompareServiceCostCommand,
)
from hexawyn.application.use_case.finops.compare_service_cost.compare_service_cost_use_case import (  # noqa: E501
    CompareUseCaseCostUseCase,
)
from hexawyn.application.use_case.finops.compare_service_cost.response import (
    CompareServiceCostResponse,
)


class TestCompareServiceCostUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_pod_resources.return_value = []

        use_case = CompareUseCaseCostUseCase(cost_port=port)
        result = use_case.execute(CompareServiceCostCommand(service_name="api-gateway"))

        assert isinstance(result, CompareServiceCostResponse)

    def test_execute_with_no_pods(self) -> None:
        port = MagicMock()
        port.fetch_pod_resources.return_value = []

        use_case = CompareUseCaseCostUseCase(cost_port=port)
        result = use_case.execute(CompareServiceCostCommand(service_name="empty-service"))

        assert isinstance(result, CompareServiceCostResponse)
