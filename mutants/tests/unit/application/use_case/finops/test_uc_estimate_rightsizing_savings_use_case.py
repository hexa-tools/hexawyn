from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.finops.estimate_rightsizing_savings.command import (
    EstimateRightsizingSavingsCommand,
)
from hexawyn.application.use_case.finops.estimate_rightsizing_savings.estimate_rightsizing_savings_use_case import (  # noqa: E501
    EstimateRightsizingSavingsUseCase,
)
from hexawyn.application.use_case.finops.estimate_rightsizing_savings.response import (  # noqa: E501
    EstimateRightsizingSavingsResponse,
)


class TestEstimateRightsizingSavingsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_workload_rightsizing_data.return_value = []

        use_case = EstimateRightsizingSavingsUseCase(
            rightsizing_port=port,
        )
        result = use_case.estimate_rightsizing_savings(EstimateRightsizingSavingsCommand())

        assert isinstance(result, EstimateRightsizingSavingsResponse)
