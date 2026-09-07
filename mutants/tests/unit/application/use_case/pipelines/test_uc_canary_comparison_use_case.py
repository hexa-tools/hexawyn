from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.pipelines.canary_comparison.canary_comparison_use_case import (  # noqa: E501
    CanaryComparisonUseCase,
)
from hexawyn.application.use_case.pipelines.canary_comparison.command import (
    CanaryComparisonCommand,
)
from hexawyn.application.use_case.pipelines.canary_comparison.response import (
    CanaryComparisonResponse,
)
from hexawyn.domain.models.canary_comparison import VersionMetrics


class TestCanaryComparisonUseCase:
    def test_execute_returns_response(self) -> None:
        metrics = VersionMetrics(
            version="v2.0",
            request_count=1000,
            p50_ms=10.0,
            p95_ms=25.0,
            p99_ms=50.0,
            error_rate_pct=0.1,
        )
        port = MagicMock()
        port.fetch_stable_metrics.return_value = metrics
        port.fetch_canary_metrics.return_value = metrics

        use_case = CanaryComparisonUseCase(port=port)
        result = use_case.execute(CanaryComparisonCommand(service_name="api"))

        assert isinstance(result, CanaryComparisonResponse)

    def test_execute_empty_metrics(self) -> None:
        metrics = VersionMetrics(
            version="v2.0",
            request_count=0,
            p50_ms=0.0,
            p95_ms=0.0,
            p99_ms=0.0,
            error_rate_pct=0.0,
        )
        port = MagicMock()
        port.fetch_stable_metrics.return_value = metrics
        port.fetch_canary_metrics.return_value = metrics

        use_case = CanaryComparisonUseCase(port=port)
        result = use_case.execute(CanaryComparisonCommand(service_name="api"))

        assert isinstance(result, CanaryComparisonResponse)
