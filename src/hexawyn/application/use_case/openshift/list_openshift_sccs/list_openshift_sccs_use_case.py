# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.use_case.openshift.list_openshift_sccs.command import (
    ListOpenshiftSccsCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_sccs.response import (
    ListOpenshiftSccsResponse,
)


class ListOpenshiftSccsUseCase:
    def __init__(self, port: OpenShiftResourcePort) -> None:  # noqa: F821  # type: ignore
        self._port = port

    def execute(self, command: ListOpenshiftSccsCommand) -> ListOpenshiftSccsResponse:
        try:
            items = self._port.list_security_context_constraints()
            return ListOpenshiftSccsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftSccsResponse(error=str(exc))
