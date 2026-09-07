from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

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

    def test_execute_handles_january_edge_case(self) -> None:
        port = MagicMock()
        port.fetch_pod_resources.return_value = []

        use_case = CompareUseCaseCostUseCase(cost_port=port)

        january = datetime(2024, 1, 15, tzinfo=UTC)
        with patch(
            "hexawyn.application.use_case.finops.compare_service_cost.compare_service_cost_use_case.datetime"
        ) as mock_datetime:
            mock_datetime.now.return_value = january
            mock_datetime.UTC = UTC
            mock_datetime.datetime = datetime

            result = use_case.execute(CompareServiceCostCommand(service_name="api-gateway"))

        assert isinstance(result, CompareServiceCostResponse)
