"""MCP tool: list_calico_network_policies — list Calico NetworkPolicy + GNP."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.list_calico_network_policies.command import (
    ListCalicoNetworkPoliciesCommand,
)
from hexawyn.application.use_case.calico.list_calico_network_policies.list_calico_network_policies_use_case import (  # noqa: E501
    ListCalicoNetworkPoliciesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _policy_dict(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "kind": getattr(policy, "kind", None),
        "namespace": getattr(policy, "namespace", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def _empty(namespace: str | None, error: str | None = None) -> dict[str, object]:
    return {
        "installed": False,
        "not_installed_marker": "NOT_INSTALLED",
        "total": 0,
        "global_count": 0,
        "namespaced_count": 0,
        "namespace": namespace,
        "policies": [],
        "error": error,
    }


def list_calico_network_policies(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = ListCalicoNetworkPoliciesUseCase(port=build_calico_adapter())
        result = use_case.execute(ListCalicoNetworkPoliciesCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "total": result.total,
            "global_count": result.global_count,
            "namespaced_count": result.namespaced_count,
            "namespace": namespace,
            "policies": [_policy_dict(policy) for policy in result.policies],
            "error": result.error,
        }
    except Exception as exc:
        return _empty(namespace, error=str(exc))


def register(mcp: FastMCP) -> None:
    mcp.tool()(list_calico_network_policies)
