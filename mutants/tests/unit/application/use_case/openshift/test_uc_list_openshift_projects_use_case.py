from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.openshift.list_openshift_projects.command import (
    ListOpenshiftProjectsCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_projects.list_openshift_projects_use_case import (  # noqa: E501
    ListOpenshiftProjectsUseCase,
)
from hexawyn.application.use_case.openshift.list_openshift_projects.response import (
    ListOpenshiftProjectsResponse,
)


class TestListOpenshiftProjectsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_projects.return_value = []
        use_case = ListOpenshiftProjectsUseCase(port=port)
        result = use_case.execute(ListOpenshiftProjectsCommand())
        assert isinstance(result, ListOpenshiftProjectsResponse)

    def test_execute_empty_list(self) -> None:
        port = MagicMock()
        port.list_projects.return_value = []
        use_case = ListOpenshiftProjectsUseCase(port=port)
        result = use_case.execute(ListOpenshiftProjectsCommand())
        assert result.count == 0

    def test_execute_handles_exception(self) -> None:
        port = MagicMock()
        port.list_projects.side_effect = Exception("boom")

        use_case = ListOpenshiftProjectsUseCase(port=port)
        result = use_case.execute(ListOpenshiftProjectsCommand())

        assert result.error == "boom"
