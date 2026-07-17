"""Unit tests for SpanBottleneckAnalysisUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.span_bottleneck_analysis.span_bottleneck_analysis_service_port import (
    SpanBottleneckAnalysisServicePort,
)
from hexawyn.application.use_case.span_bottleneck_analysis.span_bottleneck_analysis_use_case import (
    SpanBottleneckAnalysisUseCase,
)


class TestSpanBottleneckAnalysisUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=SpanBottleneckAnalysisServicePort)
        use_case = SpanBottleneckAnalysisUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.analyze.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=SpanBottleneckAnalysisServicePort)
        mock_service.analyze.side_effect = RuntimeError("test error")
        use_case = SpanBottleneckAnalysisUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
