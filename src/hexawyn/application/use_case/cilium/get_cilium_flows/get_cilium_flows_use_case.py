from __future__ import annotations

from hexawyn.application.ports.driven.cilium_hubble_port import CiliumHubblePort
from hexawyn.application.use_case.cilium.get_cilium_flows.command import (
    GetCiliumFlowsCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_flows.response import (
    CiliumFlowOutput,
    GetCiliumFlowsResponse,
)
from hexawyn.domain.models.cilium import CiliumFlowEntry, CiliumFlowQuery


class GetCiliumFlowsUseCase:
    def __init__(self, port: CiliumHubblePort) -> None:
        self._port = port

    def execute(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    @staticmethod
    def _to_flow(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }
