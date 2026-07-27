# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.use_case.openshift.list_openshift_projects.command import (
    ListOpenshiftProjectsCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_projects.response import (
    ListOpenshiftProjectsResponse,
)


class ListOpenshiftProjectsUseCase:
    def __init__(self, port: OpenShiftResourcePort) -> None:  # noqa: F821  # type: ignore
        self._port = port

    def execute(self, command: ListOpenshiftProjectsCommand) -> ListOpenshiftProjectsResponse:
        try:
            items = self._port.list_projects()
            return ListOpenshiftProjectsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftProjectsResponse(error=str(exc))
