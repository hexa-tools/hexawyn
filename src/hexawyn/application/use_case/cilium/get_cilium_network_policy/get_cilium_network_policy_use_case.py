from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.get_cilium_network_policy.command import (
    GetCiliumNetworkPolicyCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_network_policy.response import (
    CiliumRuleOutput,
    GetCiliumNetworkPolicyResponse,
)
from hexawyn.domain.models.cilium import CiliumRuleSummary


class GetCiliumNetworkPolicyUseCase:
    def __init__(self, port: CiliumPort) -> None:
        self._port = port

    def execute(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    @staticmethod
    def _to_rule(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "direction": rule.direction,
            "endpoints": list(rule.endpoints),
            "ports": list(rule.ports),
            "l7": [{"protocol": l7.protocol, "match": list(l7.match)} for l7 in rule.l7],
        }
