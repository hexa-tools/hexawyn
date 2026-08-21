from __future__ import annotations

from hexawyn.application.ports.driven.ingress_port import IngressPort
from hexawyn.application.use_case.ingress.list_ingresses.command import (
    ListIngressesCommand,
)
from hexawyn.application.use_case.ingress.list_ingresses.response import (
    ListIngressesResponse,
)


class ListIngressesUseCase:
    def __init__(self, port: IngressPort) -> None:
        self._port = port

    def execute(self, command: ListIngressesCommand) -> ListIngressesResponse:
        try:
            namespace = command.namespace or "default"
            items = self._port.list_ingresses(namespace=namespace)
            return ListIngressesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListIngressesResponse(error=str(exc))
