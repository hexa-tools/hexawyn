"""Unit tests for QueryKubeArchiveUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_service_port import (
    QueryKubeArchiveServicePort,
)
from hexawyn.application.use_case.query_kubearchive.query_kubearchive_use_case import (
    QueryKubeArchiveUseCase,
)


class TestQueryKubeArchiveUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=QueryKubeArchiveServicePort)
        use_case = QueryKubeArchiveUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.query.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=QueryKubeArchiveServicePort)
        mock_service.query.side_effect = RuntimeError("test error")
        use_case = QueryKubeArchiveUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
