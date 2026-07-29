# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.use_case.openshift.list_openshift_imagestreams.command import (  # noqa: E501
    ListOpenshiftImagestreamsCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_imagestreams.response import (  # noqa: E501
    ListOpenshiftImagestreamsResponse,
)


class ListOpenshiftImagestreamsUseCase:
    def __init__(self, port: OpenShiftResourcePort) -> None:  # noqa: F821  # type: ignore
        self._port = port

    def execute(
        self, command: ListOpenshiftImagestreamsCommand
    ) -> ListOpenshiftImagestreamsResponse:
        try:
            items = self._port.list_image_streams(namespace=command.namespace)
            return ListOpenshiftImagestreamsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftImagestreamsResponse(error=str(exc))
