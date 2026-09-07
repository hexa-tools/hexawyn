from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.openshift.list_openshift_routes.command import (
    ListOpenshiftRoutesCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_routes.list_openshift_routes_use_case import (  # noqa: E501
    ListOpenshiftRoutesUseCase,
)
from hexawyn.application.use_case.openshift.list_openshift_routes.response import (
    ListOpenshiftRoutesResponse,
)


class TestListOpenshiftRoutesUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_routes.return_value = []
        use_case = ListOpenshiftRoutesUseCase(port=port)
        result = use_case.execute(ListOpenshiftRoutesCommand())
        assert isinstance(result, ListOpenshiftRoutesResponse)

    def test_execute_empty_list(self) -> None:
        port = MagicMock()
        port.list_routes.return_value = []
        use_case = ListOpenshiftRoutesUseCase(port=port)
        result = use_case.execute(ListOpenshiftRoutesCommand())
        assert result.count == 0

    def test_execute_handles_exception(self) -> None:
        port = MagicMock()
        port.list_routes.side_effect = Exception("boom")

        use_case = ListOpenshiftRoutesUseCase(port=port)
        result = use_case.execute(ListOpenshiftRoutesCommand())

        assert result.error == "boom"
