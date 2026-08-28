"""MCP tool: get_cilium_network_policy — full detail of one Cilium policy."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.get_cilium_network_policy.command import (
    GetCiliumNetworkPolicyCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_network_policy.get_cilium_network_policy_use_case import (  # noqa: E501
    GetCiliumNetworkPolicyUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def get_cilium_network_policy(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(get_cilium_network_policy)
