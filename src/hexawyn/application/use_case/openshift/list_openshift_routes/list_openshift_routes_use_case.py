# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.use_case.openshift.list_openshift_routes.command import (
    ListOpenshiftRoutesCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_routes.response import (
    ListOpenshiftRoutesResponse,
)


class ListOpenshiftRoutesUseCase:
    def __init__(self, port: OpenShiftResourcePort) -> None:  # noqa: F821  # type: ignore
        self._port = port

    def execute(self, command: ListOpenshiftRoutesCommand) -> ListOpenshiftRoutesResponse:
        try:
            items = self._port.list_routes(namespace=command.namespace)
            return ListOpenshiftRoutesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftRoutesResponse(error=str(exc))
