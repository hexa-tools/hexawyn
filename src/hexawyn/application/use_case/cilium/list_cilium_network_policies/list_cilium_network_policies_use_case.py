from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.list_cilium_network_policies.command import (
    ListCiliumNetworkPoliciesCommand,
)
from hexawyn.application.use_case.cilium.list_cilium_network_policies.response import (
    CiliumNetworkPolicyOutput,
    ListCiliumNetworkPoliciesResponse,
)
from hexawyn.domain.models.cilium import CiliumNetworkPolicyInfo


class ListCiliumNetworkPoliciesUseCase:
    def __init__(self, port: CiliumPort) -> None:
        self._port = port

    def execute(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            note=result.note,
        )

    @staticmethod
    def _to_output(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "name": policy.name,
            "namespace": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "l7_protocols": list(policy.l7_protocols),
        }
