from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.hot_node_analysis.hot_node_analysis_command import (
    HotNodeAnalysisCommand,
)
from hexawyn.application.ports.driving.hot_node_analysis.hot_node_analysis_response import (
    HotNodeAnalysisResponse,
)
from hexawyn.application.ports.driving.hot_node_analysis.hot_node_analysis_service_port import (
    HotNodeAnalysisServicePort,
)
from hexawyn.application.use_case.hot_node_analysis.hot_node_analysis_use_case import (
    HotNodeAnalysisUseCase,
)


class TestHotNodeAnalysisUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=HotNodeAnalysisServicePort)
        expected = HotNodeAnalysisResponse(summary="All healthy.")
        service.analyze.return_value = expected
        use_case = HotNodeAnalysisUseCase(service=service)
        command = HotNodeAnalysisCommand()

        result = use_case.execute(command)

        service.analyze.assert_called_once_with(command)
        assert result is expected
