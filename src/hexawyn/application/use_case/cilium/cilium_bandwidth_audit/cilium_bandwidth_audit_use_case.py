from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.cilium_bandwidth_audit.command import (
    CiliumBandwidthAuditCommand,
)
from hexawyn.application.use_case.cilium.cilium_bandwidth_audit.response import (
    CiliumBandwidthAuditResponse,
    CiliumBandwidthEntryOutput,
)
from hexawyn.domain.models.cilium import CiliumBandwidthEntry


class CiliumBandwidthAuditUseCase:
    def __init__(self, port: CiliumPort) -> None:
        self._port = port

    def execute(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = self._port.bandwidth_audit()
        entries: list[CiliumBandwidthEntryOutput] | None = None
        if result.entries is not None:
            entries = [self._to_entry(entry) for entry in result.entries]
        return CiliumBandwidthAuditResponse(
            installed=result.installed,
            status=result.status,
            total_pods=result.total_pods,
            entries=entries,
            note=result.note,
        )

    @staticmethod
    def _to_entry(entry: CiliumBandwidthEntry) -> CiliumBandwidthEntryOutput:
        return {
            "namespace": entry.namespace,
            "pod": entry.pod,
            "ingress_limit": entry.ingress_limit,
            "egress_limit": entry.egress_limit,
            "usage_ratio": entry.usage_ratio,
            "state": entry.state,
            "note": entry.note,
        }
