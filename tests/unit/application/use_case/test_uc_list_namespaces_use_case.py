"""Unit tests for ListNamespacesUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.list_namespaces.list_namespaces_service_port import (
    ListNamespacesServicePort,
)
from hexawyn.application.use_case.list_namespaces.list_namespaces_use_case import (
    ListNamespacesUseCase,
)


class TestListNamespacesUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ListNamespacesServicePort)
        use_case = ListNamespacesUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_namespaces.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ListNamespacesServicePort)
        mock_service.list_namespaces.side_effect = RuntimeError("test error")
        use_case = ListNamespacesUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
