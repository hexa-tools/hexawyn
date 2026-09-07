from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.ingress.list_ingresses.command import (
    ListIngressesCommand,
)
from hexawyn.application.use_case.ingress.list_ingresses.list_ingresses_use_case import (
    ListIngressesUseCase,
)
from hexawyn.application.use_case.ingress.list_ingresses.response import (
    ListIngressesResponse,
)


class TestListIngressesUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_ingresses.return_value = []
        use_case = ListIngressesUseCase(port=port)
        result = use_case.execute(ListIngressesCommand())
        assert isinstance(result, ListIngressesResponse)

    def test_execute_empty_list(self) -> None:
        port = MagicMock()
        port.list_ingresses.return_value = []
        use_case = ListIngressesUseCase(port=port)
        result = use_case.execute(ListIngressesCommand())
        assert result.count == 0

    def test_execute_handles_exception(self) -> None:
        port = MagicMock()
        port.list_ingresses.side_effect = Exception("boom")

        use_case = ListIngressesUseCase(port=port)
        result = use_case.execute(ListIngressesCommand())

        assert result.error == "boom"

    def test_execute_passes_namespace_to_port(self) -> None:
        port = MagicMock()
        port.list_ingresses.return_value = []
        use_case = ListIngressesUseCase(port=port)
        result = use_case.execute(ListIngressesCommand(namespace="production"))
        assert result.count == 0
        port.list_ingresses.assert_called_once_with(namespace="production")
