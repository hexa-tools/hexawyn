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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_live_topology_mapper__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_live_topology_mapper__mutmut)
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


def x_live_topology_mapper__mutmut_orig(namespace: str | None = None) -> dict[str, object]:
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


def x_live_topology_mapper__mutmut_1(namespace: str | None = None) -> dict[str, object]:
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
        snapshot_adapter = ""
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


def x_live_topology_mapper__mutmut_2(namespace: str | None = None) -> dict[str, object]:
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
            snapshot_adapter = None
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


def x_live_topology_mapper__mutmut_3(namespace: str | None = None) -> dict[str, object]:
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
            snapshot_adapter = ""

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


def x_live_topology_mapper__mutmut_4(namespace: str | None = None) -> dict[str, object]:
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

        use_case = None
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


def x_live_topology_mapper__mutmut_5(namespace: str | None = None) -> dict[str, object]:
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
            kubernetes_topology_port=None,
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


def x_live_topology_mapper__mutmut_6(namespace: str | None = None) -> dict[str, object]:
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
            istio_topology_port=None,
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


def x_live_topology_mapper__mutmut_7(namespace: str | None = None) -> dict[str, object]:
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
            snapshot_port=None,
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


def x_live_topology_mapper__mutmut_8(namespace: str | None = None) -> dict[str, object]:
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
            cluster_name=None,
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


def x_live_topology_mapper__mutmut_9(namespace: str | None = None) -> dict[str, object]:
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


def x_live_topology_mapper__mutmut_10(namespace: str | None = None) -> dict[str, object]:
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


def x_live_topology_mapper__mutmut_11(namespace: str | None = None) -> dict[str, object]:
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


def x_live_topology_mapper__mutmut_12(namespace: str | None = None) -> dict[str, object]:
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


def x_live_topology_mapper__mutmut_13(namespace: str | None = None) -> dict[str, object]:
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
        response = None

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


def x_live_topology_mapper__mutmut_14(namespace: str | None = None) -> dict[str, object]:
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
        response = use_case.execute(None)

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


def x_live_topology_mapper__mutmut_15(namespace: str | None = None) -> dict[str, object]:
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
        response = use_case.execute(LiveTopologyMapperCommand(namespace=None))

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


def x_live_topology_mapper__mutmut_16(namespace: str | None = None) -> dict[str, object]:
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
            "XXnodesXX": response.nodes,
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


def x_live_topology_mapper__mutmut_17(namespace: str | None = None) -> dict[str, object]:
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
            "NODES": response.nodes,
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


def x_live_topology_mapper__mutmut_18(namespace: str | None = None) -> dict[str, object]:
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
            "XXedgesXX": response.edges,
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


def x_live_topology_mapper__mutmut_19(namespace: str | None = None) -> dict[str, object]:
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
            "EDGES": response.edges,
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


def x_live_topology_mapper__mutmut_20(namespace: str | None = None) -> dict[str, object]:
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
            "XXsingle_points_of_failureXX": response.single_points_of_failure,
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


def x_live_topology_mapper__mutmut_21(namespace: str | None = None) -> dict[str, object]:
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
            "SINGLE_POINTS_OF_FAILURE": response.single_points_of_failure,
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


def x_live_topology_mapper__mutmut_22(namespace: str | None = None) -> dict[str, object]:
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
            "XXorphan_nodesXX": response.orphan_nodes,
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


def x_live_topology_mapper__mutmut_23(namespace: str | None = None) -> dict[str, object]:
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
            "ORPHAN_NODES": response.orphan_nodes,
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


def x_live_topology_mapper__mutmut_24(namespace: str | None = None) -> dict[str, object]:
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
            "XXcyclesXX": response.cycles,
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


def x_live_topology_mapper__mutmut_25(namespace: str | None = None) -> dict[str, object]:
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
            "CYCLES": response.cycles,
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


def x_live_topology_mapper__mutmut_26(namespace: str | None = None) -> dict[str, object]:
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
            "XXinference_sourceXX": response.inference_source,
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


def x_live_topology_mapper__mutmut_27(namespace: str | None = None) -> dict[str, object]:
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
            "INFERENCE_SOURCE": response.inference_source,
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


def x_live_topology_mapper__mutmut_28(namespace: str | None = None) -> dict[str, object]:
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
            "XXtruncatedXX": response.truncated,
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


def x_live_topology_mapper__mutmut_29(namespace: str | None = None) -> dict[str, object]:
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
            "TRUNCATED": response.truncated,
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


def x_live_topology_mapper__mutmut_30(namespace: str | None = None) -> dict[str, object]:
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
            "XXnamespace_scopeXX": response.namespace_scope,
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


def x_live_topology_mapper__mutmut_31(namespace: str | None = None) -> dict[str, object]:
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
            "NAMESPACE_SCOPE": response.namespace_scope,
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


def x_live_topology_mapper__mutmut_32(namespace: str | None = None) -> dict[str, object]:
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
            "XXmermaid_diagramXX": response.mermaid_diagram,
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


def x_live_topology_mapper__mutmut_33(namespace: str | None = None) -> dict[str, object]:
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
            "MERMAID_DIAGRAM": response.mermaid_diagram,
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


def x_live_topology_mapper__mutmut_34(namespace: str | None = None) -> dict[str, object]:
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
            "XXerrorXX": None,
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


def x_live_topology_mapper__mutmut_35(namespace: str | None = None) -> dict[str, object]:
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
            "ERROR": None,
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


def x_live_topology_mapper__mutmut_36(namespace: str | None = None) -> dict[str, object]:
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
            "XXnodesXX": [],
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


def x_live_topology_mapper__mutmut_37(namespace: str | None = None) -> dict[str, object]:
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
            "NODES": [],
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


def x_live_topology_mapper__mutmut_38(namespace: str | None = None) -> dict[str, object]:
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
            "XXedgesXX": [],
            "single_points_of_failure": [],
            "orphan_nodes": [],
            "cycles": [],
            "inference_source": "",
            "truncated": False,
            "namespace_scope": namespace,
            "mermaid_diagram": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_39(namespace: str | None = None) -> dict[str, object]:
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
            "EDGES": [],
            "single_points_of_failure": [],
            "orphan_nodes": [],
            "cycles": [],
            "inference_source": "",
            "truncated": False,
            "namespace_scope": namespace,
            "mermaid_diagram": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_40(namespace: str | None = None) -> dict[str, object]:
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
            "XXsingle_points_of_failureXX": [],
            "orphan_nodes": [],
            "cycles": [],
            "inference_source": "",
            "truncated": False,
            "namespace_scope": namespace,
            "mermaid_diagram": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_41(namespace: str | None = None) -> dict[str, object]:
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
            "SINGLE_POINTS_OF_FAILURE": [],
            "orphan_nodes": [],
            "cycles": [],
            "inference_source": "",
            "truncated": False,
            "namespace_scope": namespace,
            "mermaid_diagram": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_42(namespace: str | None = None) -> dict[str, object]:
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
            "XXorphan_nodesXX": [],
            "cycles": [],
            "inference_source": "",
            "truncated": False,
            "namespace_scope": namespace,
            "mermaid_diagram": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_43(namespace: str | None = None) -> dict[str, object]:
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
            "ORPHAN_NODES": [],
            "cycles": [],
            "inference_source": "",
            "truncated": False,
            "namespace_scope": namespace,
            "mermaid_diagram": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_44(namespace: str | None = None) -> dict[str, object]:
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
            "XXcyclesXX": [],
            "inference_source": "",
            "truncated": False,
            "namespace_scope": namespace,
            "mermaid_diagram": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_45(namespace: str | None = None) -> dict[str, object]:
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
            "CYCLES": [],
            "inference_source": "",
            "truncated": False,
            "namespace_scope": namespace,
            "mermaid_diagram": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_46(namespace: str | None = None) -> dict[str, object]:
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
            "XXinference_sourceXX": "",
            "truncated": False,
            "namespace_scope": namespace,
            "mermaid_diagram": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_47(namespace: str | None = None) -> dict[str, object]:
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
            "INFERENCE_SOURCE": "",
            "truncated": False,
            "namespace_scope": namespace,
            "mermaid_diagram": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_48(namespace: str | None = None) -> dict[str, object]:
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
            "inference_source": "XXXX",
            "truncated": False,
            "namespace_scope": namespace,
            "mermaid_diagram": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_49(namespace: str | None = None) -> dict[str, object]:
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
            "XXtruncatedXX": False,
            "namespace_scope": namespace,
            "mermaid_diagram": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_50(namespace: str | None = None) -> dict[str, object]:
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
            "TRUNCATED": False,
            "namespace_scope": namespace,
            "mermaid_diagram": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_51(namespace: str | None = None) -> dict[str, object]:
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
            "truncated": True,
            "namespace_scope": namespace,
            "mermaid_diagram": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_52(namespace: str | None = None) -> dict[str, object]:
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
            "XXnamespace_scopeXX": namespace,
            "mermaid_diagram": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_53(namespace: str | None = None) -> dict[str, object]:
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
            "NAMESPACE_SCOPE": namespace,
            "mermaid_diagram": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_54(namespace: str | None = None) -> dict[str, object]:
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
            "XXmermaid_diagramXX": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_55(namespace: str | None = None) -> dict[str, object]:
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
            "MERMAID_DIAGRAM": "",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_56(namespace: str | None = None) -> dict[str, object]:
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
            "mermaid_diagram": "XXXX",
            "error": str(exc),
        }


def x_live_topology_mapper__mutmut_57(namespace: str | None = None) -> dict[str, object]:
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
            "XXerrorXX": str(exc),
        }


def x_live_topology_mapper__mutmut_58(namespace: str | None = None) -> dict[str, object]:
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
            "ERROR": str(exc),
        }


def x_live_topology_mapper__mutmut_59(namespace: str | None = None) -> dict[str, object]:
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
            "error": str(None),
        }

mutants_x_live_topology_mapper__mutmut['_mutmut_orig'] = x_live_topology_mapper__mutmut_orig # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_1'] = x_live_topology_mapper__mutmut_1 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_2'] = x_live_topology_mapper__mutmut_2 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_3'] = x_live_topology_mapper__mutmut_3 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_4'] = x_live_topology_mapper__mutmut_4 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_5'] = x_live_topology_mapper__mutmut_5 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_6'] = x_live_topology_mapper__mutmut_6 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_7'] = x_live_topology_mapper__mutmut_7 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_8'] = x_live_topology_mapper__mutmut_8 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_9'] = x_live_topology_mapper__mutmut_9 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_10'] = x_live_topology_mapper__mutmut_10 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_11'] = x_live_topology_mapper__mutmut_11 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_12'] = x_live_topology_mapper__mutmut_12 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_13'] = x_live_topology_mapper__mutmut_13 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_14'] = x_live_topology_mapper__mutmut_14 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_15'] = x_live_topology_mapper__mutmut_15 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_16'] = x_live_topology_mapper__mutmut_16 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_17'] = x_live_topology_mapper__mutmut_17 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_18'] = x_live_topology_mapper__mutmut_18 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_19'] = x_live_topology_mapper__mutmut_19 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_20'] = x_live_topology_mapper__mutmut_20 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_21'] = x_live_topology_mapper__mutmut_21 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_22'] = x_live_topology_mapper__mutmut_22 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_23'] = x_live_topology_mapper__mutmut_23 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_24'] = x_live_topology_mapper__mutmut_24 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_25'] = x_live_topology_mapper__mutmut_25 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_26'] = x_live_topology_mapper__mutmut_26 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_27'] = x_live_topology_mapper__mutmut_27 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_28'] = x_live_topology_mapper__mutmut_28 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_29'] = x_live_topology_mapper__mutmut_29 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_30'] = x_live_topology_mapper__mutmut_30 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_31'] = x_live_topology_mapper__mutmut_31 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_32'] = x_live_topology_mapper__mutmut_32 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_33'] = x_live_topology_mapper__mutmut_33 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_34'] = x_live_topology_mapper__mutmut_34 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_35'] = x_live_topology_mapper__mutmut_35 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_36'] = x_live_topology_mapper__mutmut_36 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_37'] = x_live_topology_mapper__mutmut_37 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_38'] = x_live_topology_mapper__mutmut_38 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_39'] = x_live_topology_mapper__mutmut_39 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_40'] = x_live_topology_mapper__mutmut_40 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_41'] = x_live_topology_mapper__mutmut_41 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_42'] = x_live_topology_mapper__mutmut_42 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_43'] = x_live_topology_mapper__mutmut_43 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_44'] = x_live_topology_mapper__mutmut_44 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_45'] = x_live_topology_mapper__mutmut_45 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_46'] = x_live_topology_mapper__mutmut_46 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_47'] = x_live_topology_mapper__mutmut_47 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_48'] = x_live_topology_mapper__mutmut_48 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_49'] = x_live_topology_mapper__mutmut_49 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_50'] = x_live_topology_mapper__mutmut_50 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_51'] = x_live_topology_mapper__mutmut_51 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_52'] = x_live_topology_mapper__mutmut_52 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_53'] = x_live_topology_mapper__mutmut_53 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_54'] = x_live_topology_mapper__mutmut_54 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_55'] = x_live_topology_mapper__mutmut_55 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_56'] = x_live_topology_mapper__mutmut_56 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_57'] = x_live_topology_mapper__mutmut_57 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_58'] = x_live_topology_mapper__mutmut_58 # type: ignore # mutmut generated
mutants_x_live_topology_mapper__mutmut['x_live_topology_mapper__mutmut_59'] = x_live_topology_mapper__mutmut_59 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    """Register live_topology_mapper as an MCP tool on the given FastMCP server."""
    mcp.tool()(live_topology_mapper)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    """Register live_topology_mapper as an MCP tool on the given FastMCP server."""
    mcp.tool()(live_topology_mapper)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    """Register live_topology_mapper as an MCP tool on the given FastMCP server."""
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
