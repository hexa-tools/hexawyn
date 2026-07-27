from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.span_bottleneck_analysis.command import (
    SpanBottleneckAnalysisCommand,
)
from hexawyn.application.use_case.observability.span_bottleneck_analysis.response import (
    SpanBottleneckAnalysisResponse,
)
from hexawyn.application.use_case.observability.span_bottleneck_analysis.span_bottleneck_analysis_use_case import (  # noqa: E501
    SpanBottleneckAnalysisUseCase,
)
from hexawyn.domain.models.span_bottleneck import SpanBreakdown


class TestSpanBottleneckAnalysisUseCase:
    def test_execute_returns_response(self) -> None:
        db = SpanBreakdown(
            category="database",
            avg_ms=50.0,
            p95_ms=200.0,
            max_ms=500.0,
            slowest_operation="SELECT * FROM users",
        )
        port = MagicMock()
        port.fetch_db_spans.return_value = db
        port.fetch_redis_spans.return_value = None

        use_case = SpanBottleneckAnalysisUseCase(port=port)
        result = use_case.execute(SpanBottleneckAnalysisCommand(service_name="api"))

        assert isinstance(result, SpanBottleneckAnalysisResponse)

    def test_execute_empty_spans(self) -> None:
        db = SpanBreakdown(
            category="database",
            avg_ms=0.0,
            p95_ms=0.0,
            max_ms=0.0,
            slowest_operation=None,
        )
        port = MagicMock()
        port.fetch_db_spans.return_value = db
        port.fetch_redis_spans.return_value = None

        use_case = SpanBottleneckAnalysisUseCase(port=port)
        result = use_case.execute(SpanBottleneckAnalysisCommand(service_name="api"))

        assert isinstance(result, SpanBottleneckAnalysisResponse)
