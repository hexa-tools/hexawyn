"""ListCalicoNetworkPoliciesUseCase — lists Calico namespaced + global policies."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.list_calico_network_policies.command import (
    ListCalicoNetworkPoliciesCommand,
)
from hexawyn.application.use_case.calico.list_calico_network_policies.response import (
    ListCalicoNetworkPoliciesResponse,
)

_KIND_GLOBAL = "GlobalNetworkPolicy"
_KIND_NAMESPACED = "CalicoNetworkPolicy"


class ListCalicoNetworkPoliciesUseCase:
    """Orchestrates Calico policy listing — depends only on ``CalicoPort``."""

    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def execute(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )
