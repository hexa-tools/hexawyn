from __future__ import annotations

from hexawyn.application.ports.driven.cilium_hubble_port import CiliumHubblePort
from hexawyn.application.use_case.cilium.detect_cilium_denials.command import (
    DetectCiliumDenialsCommand,
)
from hexawyn.application.use_case.cilium.detect_cilium_denials.response import (
    CiliumDenialGroupOutput,
    DetectCiliumDenialsResponse,
)
from hexawyn.domain.models.cilium import CiliumDenialGroup, CiliumDenialsQuery


class DetectCiliumDenialsUseCase:
    def __init__(self, port: CiliumHubblePort) -> None:
        self._port = port

    def execute(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    @staticmethod
    def _to_group(group: CiliumDenialGroup) -> CiliumDenialGroupOutput:
        return {
            "policy": group.policy,
            "source": group.source,
            "destination": group.destination,
            "source_namespace": group.source_namespace,
            "destination_namespace": group.destination_namespace,
            "reason": group.reason,
            "count": group.count,
        }
