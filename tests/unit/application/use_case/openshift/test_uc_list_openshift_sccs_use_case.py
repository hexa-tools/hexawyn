from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.openshift.list_openshift_sccs.command import (
    ListOpenshiftSccsCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_sccs.list_openshift_sccs_use_case import (  # noqa: E501
    ListOpenshiftSccsUseCase,
)
from hexawyn.application.use_case.openshift.list_openshift_sccs.response import (
    ListOpenshiftSccsResponse,
)


class TestListOpenshiftSccsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_security_context_constraints.return_value = []
        use_case = ListOpenshiftSccsUseCase(port=port)
        result = use_case.execute(ListOpenshiftSccsCommand())
        assert isinstance(result, ListOpenshiftSccsResponse)

    def test_execute_empty_list(self) -> None:
        port = MagicMock()
        port.list_security_context_constraints.return_value = []
        use_case = ListOpenshiftSccsUseCase(port=port)
        result = use_case.execute(ListOpenshiftSccsCommand())
        assert result.count == 0

    def test_execute_handles_exception(self) -> None:
        port = MagicMock()
        port.list_security_context_constraints.side_effect = Exception("boom")

        use_case = ListOpenshiftSccsUseCase(port=port)
        result = use_case.execute(ListOpenshiftSccsCommand())

        assert result.error == "boom"
