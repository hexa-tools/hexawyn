from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.finops.estimate_cost_saving.command import (
    EstimateCostSavingCommand,
)
from hexawyn.application.use_case.finops.estimate_cost_saving.estimate_cost_saving_use_case import (  # noqa: E501
    EstimateCostSavingUseCase,
)
from hexawyn.application.use_case.finops.estimate_cost_saving.response import (
    EstimateCostSavingResponse,
)


class TestEstimateCostSavingUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_pod_resource_data.return_value = []

        use_case = EstimateCostSavingUseCase(
            cost_saving_port=port,
        )
        result = use_case.estimate_cost_saving(EstimateCostSavingCommand())

        assert isinstance(result, EstimateCostSavingResponse)
