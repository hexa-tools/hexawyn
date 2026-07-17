"""Unit tests for SearchResourcesByLabelsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.search_resources_by_labels.search_resources_by_labels_service_port import (
    SearchResourcesByLabelsServicePort,
)
from hexawyn.application.use_case.search_resources_by_labels.search_resources_by_labels_use_case import (
    SearchResourcesByLabelsUseCase,
)


class TestSearchResourcesByLabelsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=SearchResourcesByLabelsServicePort)
        use_case = SearchResourcesByLabelsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.search.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=SearchResourcesByLabelsServicePort)
        mock_service.search.side_effect = RuntimeError("test error")
        use_case = SearchResourcesByLabelsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
