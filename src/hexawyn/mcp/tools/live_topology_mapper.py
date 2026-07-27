"""MCP tool: live_topology_mapper — Generate a live service dependency map."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.live_topology_mapper.command import (
    LiveTopologyMapperCommand,
)
from hexawyn.application.use_case.cluster.live_topology_mapper.live_topology_mapper_use_case import (  # noqa: E501
    LiveTopologyMapperUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def live_topology_mapper(namespace: str | None = None) -> dict[str, object]:
    """Generate a live dependency map of services running in the cluster.

    Discovers all Services, infers caller→callee edges from Istio
    VirtualServices (falling back to NetworkPolicies when the mesh is not
    installed), flags single points of failure and cycles, and returns a
    structured graph ready for Mermaid rendering.

    Args:
        namespace: Optional — scope discovery to a single namespace.
    """

    from hexawyn.mcp.server import (
        build_istio_topology_adapter,
        build_kubernetes_topology_adapter,
        build_topology_snapshot_adapter,
        context_name,
    )

    try:
        snapshot_adapter = None
        try:
            snapshot_adapter = build_topology_snapshot_adapter()
        except Exception:
            snapshot_adapter = None

        use_case = LiveTopologyMapperUseCase(
            kubernetes_topology_port=build_kubernetes_topology_adapter(),
            istio_topology_port=build_istio_topology_adapter(),
            snapshot_port=snapshot_adapter,
            cluster_name=context_name,
        )
        response = use_case.execute(LiveTopologyMapperCommand(namespace=namespace))

        return {
            "nodes": response.nodes,
            "edges": response.edges,
            "single_points_of_failure": response.single_points_of_failure,
            "orphan_nodes": response.orphan_nodes,
            "cycles": response.cycles,
            "inference_source": response.inference_source,
            "truncated": response.truncated,
            "namespace_scope": response.namespace_scope,
            "mermaid_diagram": response.mermaid_diagram,
            "error": None,
        }
    except Exception as exc:
        return {
            "nodes": [],
            "edges": [],
            "single_points_of_failure": [],
            "orphan_nodes": [],
            "cycles": [],
            "inference_source": "",
            "truncated": False,
            "namespace_scope": namespace,
            "mermaid_diagram": "",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    """Register live_topology_mapper as an MCP tool on the given FastMCP server."""
    mcp.tool()(live_topology_mapper)
