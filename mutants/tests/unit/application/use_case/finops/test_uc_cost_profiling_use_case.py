from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.finops.cost_profiling.command import (
    CostProfilingCommand,
)
from hexawyn.application.use_case.finops.cost_profiling.cost_profiling_use_case import (  # noqa: E501
    CostProfilingUseCase,
)
from hexawyn.application.use_case.finops.cost_profiling.response import (
    CostProfilingResponse,
)


class TestCostProfilingUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_endpoint_cpu_metrics.return_value = []

        use_case = CostProfilingUseCase(port=port)
        result = use_case.execute(CostProfilingCommand())

        assert isinstance(result, CostProfilingResponse)
