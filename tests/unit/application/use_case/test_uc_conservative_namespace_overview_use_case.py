"""Unit tests for ConservativeNamespaceOverviewUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_service_port import (
    ConservativeNamespaceOverviewServicePort,
)
from hexawyn.application.use_case.conservative_namespace_overview.conservative_namespace_overview_use_case import (
    ConservativeNamespaceOverviewUseCase,
)


class TestConservativeNamespaceOverviewUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ConservativeNamespaceOverviewServicePort)
        use_case = ConservativeNamespaceOverviewUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_overview.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ConservativeNamespaceOverviewServicePort)
        mock_service.get_overview.side_effect = RuntimeError("test error")
        use_case = ConservativeNamespaceOverviewUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
