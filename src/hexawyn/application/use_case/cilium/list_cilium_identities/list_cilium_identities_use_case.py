from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.list_cilium_identities.command import (
    ListCiliumIdentitiesCommand,
)
from hexawyn.application.use_case.cilium.list_cilium_identities.response import (
    CiliumIdentityOutput,
    ListCiliumIdentitiesResponse,
)
from hexawyn.domain.models.cilium import CiliumIdentityInfo


class ListCiliumIdentitiesUseCase:
    def __init__(self, port: CiliumPort) -> None:
        self._port = port

    def execute(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = self._port.list_identities()
        identities: list[CiliumIdentityOutput] | None = None
        if result.identities is not None:
            identities = [self._to_output(identity) for identity in result.identities]
        return ListCiliumIdentitiesResponse(
            installed=result.installed,
            status=result.status,
            total_identities=result.total_identities,
            identities=identities,
            note=result.note,
        )

    @staticmethod
    def _to_output(identity: CiliumIdentityInfo) -> CiliumIdentityOutput:
        return {
            "id": identity.id,
            "labels": list(identity.labels),
            "endpoint_count": identity.endpoint_count,
        }
