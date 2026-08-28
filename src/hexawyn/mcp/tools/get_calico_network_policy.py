"""MCP tool: get_calico_network_policy — full detail of a Calico policy."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.get_calico_network_policy.command import (
    GetCalicoNetworkPolicyCommand,
)
from hexawyn.application.use_case.calico.get_calico_network_policy.get_calico_network_policy_use_case import (  # noqa: E501
    GetCalicoNetworkPolicyUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _policy_fields(policy: object) -> dict[str, object]:
    """Project a CalicoNetworkPolicy into a plain, serialisable dict."""
    return {
        "name": getattr(policy, "name", None),
        "namespace": getattr(policy, "namespace", None),
        "kind": getattr(policy, "kind", None),
        "selector": getattr(policy, "selector", None),
        "action": getattr(policy, "action", None),
        "ingress_rules": list(getattr(policy, "ingress_rules", ())),
        "egress_rules": list(getattr(policy, "egress_rules", ())),
        "ingress_rule_count": getattr(policy, "ingress_rule_count", 0),
        "egress_rule_count": getattr(policy, "egress_rule_count", 0),
        "order": getattr(policy, "order", 0.0),
        "apply_on_forward": getattr(policy, "apply_on_forward", False),
    }


def get_calico_network_policy(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = GetCalicoNetworkPolicyUseCase(port=build_calico_adapter())
        result = use_case.execute(GetCalicoNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "found": result.found,
            "name": result.name,
            "namespace": result.namespace,
            "scope": result.scope,
            "kind": result.kind,
            "selector": result.selector,
            "action": result.action,
            "ingress_rules": list(result.ingress_rules),
            "egress_rules": list(result.egress_rules),
            "ingress_rule_count": result.ingress_rule_count,
            "egress_rule_count": result.egress_rule_count,
            "order": result.order,
            "apply_on_forward": result.apply_on_forward,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "found": False,
            "name": name,
            "namespace": namespace,
            "scope": None,
            "kind": None,
            "selector": None,
            "action": None,
            "ingress_rules": [],
            "egress_rules": [],
            "ingress_rule_count": 0,
            "egress_rule_count": 0,
            "order": 0.0,
            "apply_on_forward": False,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(get_calico_network_policy)
