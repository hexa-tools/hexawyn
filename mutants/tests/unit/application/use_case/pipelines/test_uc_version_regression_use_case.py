from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.pipelines.version_regression.command import (
    VersionRegressionCommand,
)
from hexawyn.application.use_case.pipelines.version_regression.response import (
    VersionRegressionResponse,
)
from hexawyn.application.use_case.pipelines.version_regression.version_regression_use_case import (  # noqa: E501
    VersionRegressionUseCase,
)
from hexawyn.domain.models.version_regression import VersionMetrics


class TestVersionRegressionUseCase:
    def test_execute_returns_response(self) -> None:
        metrics = VersionMetrics(
            version="v2.0",
            p50_ms=10.0,
            p95_ms=25.0,
            p99_ms=50.0,
            error_rate_pct=0.1,
            request_count=1000,
        )
        port = MagicMock()
        port.fetch_baseline_metrics.return_value = metrics
        port.fetch_current_metrics.return_value = metrics

        use_case = VersionRegressionUseCase(port=port)
        result = use_case.execute(VersionRegressionCommand(service_name="api"))

        assert isinstance(result, VersionRegressionResponse)

    def test_execute_no_regression(self) -> None:
        baseline = VersionMetrics(
            version="v1.0",
            p50_ms=10.0,
            p95_ms=20.0,
            p99_ms=30.0,
            error_rate_pct=0.1,
            request_count=1000,
        )
        current = VersionMetrics(
            version="v2.0",
            p50_ms=8.0,
            p95_ms=18.0,
            p99_ms=28.0,
            error_rate_pct=0.05,
            request_count=1000,
        )
        port = MagicMock()
        port.fetch_baseline_metrics.return_value = baseline
        port.fetch_current_metrics.return_value = current

        use_case = VersionRegressionUseCase(port=port)
        result = use_case.execute(VersionRegressionCommand(service_name="api"))

        assert isinstance(result, VersionRegressionResponse)
