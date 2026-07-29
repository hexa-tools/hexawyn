from __future__ import annotations

from hexawyn.application.ports.driven.network_policy_audit_port import (
    NetworkPolicyAuditPort,
)
from hexawyn.application.use_case.networking.east_west_network_segmentation.command import (
    EastWestNetworkSegmentationCommand,
)
from hexawyn.application.use_case.networking.east_west_network_segmentation.response import (
    EastWestNetworkSegmentationResponse,
)


class EastWestNetworkSegmentationUseCase:
    def __init__(self, port: NetworkPolicyAuditPort) -> None:
        self._port = port

    def execute(
        self,
        command: EastWestNetworkSegmentationCommand,
    ) -> EastWestNetworkSegmentationResponse:
        policies = self._port.audit_network_policies(  # type: ignore
            namespace=command.namespace,
        )
        return EastWestNetworkSegmentationResponse(
            namespace=command.namespace or "",
            total_namespaces=len(policies),
            findings=[],
        )
