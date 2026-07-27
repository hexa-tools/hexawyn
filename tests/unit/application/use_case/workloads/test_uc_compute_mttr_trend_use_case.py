from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.workloads.compute_mttr_trend.command import (
    ComputeMTTRTrendCommand,
)
from hexawyn.application.use_case.workloads.compute_mttr_trend.compute_mttr_trend_use_case import (
    ComputeMTTRTrendUseCase,
)
from hexawyn.application.use_case.workloads.compute_mttr_trend.response import (
    ComputeMTTRTrendResponse,
)


class TestComputeMTTRTrendUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_incidents_by_month.return_value = []
        use_case = ComputeMTTRTrendUseCase(mttr_port=port)
        result = use_case.execute(ComputeMTTRTrendCommand())
        assert isinstance(result, ComputeMTTRTrendResponse)

    def test_execute_empty_data(self) -> None:
        port = MagicMock()
        port.fetch_incidents_by_month.return_value = []
        use_case = ComputeMTTRTrendUseCase(mttr_port=port)
        result = use_case.execute(ComputeMTTRTrendCommand())
        assert isinstance(result, ComputeMTTRTrendResponse)
