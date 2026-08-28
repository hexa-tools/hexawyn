"""GetCalicoNetworkPolicyUseCase — full detail of a Calico policy."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.get_calico_network_policy.command import (
    GetCalicoNetworkPolicyCommand,
)
from hexawyn.application.use_case.calico.get_calico_network_policy.response import (
    GetCalicoNetworkPolicyResponse,
)
from hexawyn.domain.errors import InsufficientDataError, ResourceNotFoundError
from hexawyn.domain.models.calico import CalicoNetworkPolicy

_KIND_GLOBAL = "GlobalNetworkPolicy"


class GetCalicoNetworkPolicyUseCase:
    """Orchestrates fetching one Calico policy — depends only on ``CalicoPort``."""

    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def execute(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    @staticmethod
    def _to_response(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )
