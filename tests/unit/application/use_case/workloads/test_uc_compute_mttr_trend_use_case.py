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

    def test_execute_with_explicit_months(self) -> None:
        port = MagicMock()
        port.fetch_incidents_by_month.return_value = []

        use_case = ComputeMTTRTrendUseCase(mttr_port=port)
        result = use_case.execute(ComputeMTTRTrendCommand(months=["2024-01", "2024-02"]))

        assert isinstance(result, ComputeMTTRTrendResponse)

    def test_last_3_months_january_wrap(self) -> None:
        from hexawyn.application.use_case.workloads.compute_mttr_trend.compute_mttr_trend_use_case import (  # noqa: E501
            _last_3_months,
        )

        result = _last_3_months(2024, 1)

        assert result == ["2023-11", "2023-12", "2024-01"]

    def test_last_3_months_mid_year(self) -> None:
        from hexawyn.application.use_case.workloads.compute_mttr_trend.compute_mttr_trend_use_case import (  # noqa: E501
            _last_3_months,
        )

        result = _last_3_months(2024, 6)

        assert result == ["2024-04", "2024-05", "2024-06"]
