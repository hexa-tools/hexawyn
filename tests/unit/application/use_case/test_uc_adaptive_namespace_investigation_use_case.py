"""Unit tests for AdaptiveNamespaceInvestigationUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.adaptive_namespace_investigation.adaptive_namespace_investigation_service_port import (
    AdaptiveNamespaceInvestigationServicePort,
)
from hexawyn.application.use_case.adaptive_namespace_investigation.adaptive_namespace_investigation_use_case import (
    AdaptiveNamespaceInvestigationUseCase,
)


class TestAdaptiveNamespaceInvestigationUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=AdaptiveNamespaceInvestigationServicePort)
        use_case = AdaptiveNamespaceInvestigationUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.investigate.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=AdaptiveNamespaceInvestigationServicePort)
        mock_service.investigate.side_effect = RuntimeError("test error")
        use_case = AdaptiveNamespaceInvestigationUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
