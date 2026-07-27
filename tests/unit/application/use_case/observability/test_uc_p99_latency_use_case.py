from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.p99_latency.command import (
    P99LatencyCommand,
)
from hexawyn.application.use_case.observability.p99_latency.p99_latency_use_case import (  # noqa: E501
    P99LatencyUseCase,
)
from hexawyn.application.use_case.observability.p99_latency.response import (
    P99LatencyResponse,
)
from hexawyn.domain.models.p99_latency import LatencyPercentiles


class TestP99LatencyUseCase:
    def test_execute_returns_response(self) -> None:
        lp = LatencyPercentiles(
            p50_ms=10.0,
            p95_ms=25.0,
            p99_ms=150.0,
            sample_count=1000,
        )
        port = MagicMock()
        port.fetch_percentiles.return_value = lp

        use_case = P99LatencyUseCase(port=port)
        result = use_case.execute(P99LatencyCommand(slo_threshold_ms=200))

        assert isinstance(result, P99LatencyResponse)

    def test_execute_empty_data(self) -> None:
        lp = LatencyPercentiles(
            p50_ms=0.0,
            p95_ms=0.0,
            p99_ms=0.0,
            sample_count=0,
        )
        port = MagicMock()
        port.fetch_percentiles.return_value = lp

        use_case = P99LatencyUseCase(port=port)
        result = use_case.execute(P99LatencyCommand(slo_threshold_ms=200))

        assert isinstance(result, P99LatencyResponse)
