"""Unit tests for HotNodeAnalysisUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.hot_node_analysis.hot_node_analysis_service_port import (
    HotNodeAnalysisServicePort,
)
from hexawyn.application.use_case.hot_node_analysis.hot_node_analysis_use_case import (
    HotNodeAnalysisUseCase,
)


class TestHotNodeAnalysisUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=HotNodeAnalysisServicePort)
        use_case = HotNodeAnalysisUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.analyze.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=HotNodeAnalysisServicePort)
        mock_service.analyze.side_effect = RuntimeError("test error")
        use_case = HotNodeAnalysisUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
