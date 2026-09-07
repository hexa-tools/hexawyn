"""MCP tool: get_resource_usage — Real CPU/memory usage per pod/namespace from metrics-server."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.get_resource_usage.command import (
    GetResourceUsageCommand,
)
from hexawyn.application.use_case.cluster.get_resource_usage.get_resource_usage_use_case import (
    GetResourceUsageUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_resource_usage__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_resource_usage__mutmut)
def get_resource_usage(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_orig(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_1(namespace: str | None = None, resource: str = "XXbothXX") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_2(namespace: str | None = None, resource: str = "BOTH") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_3(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = None
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_4(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=None,
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_5(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=None,
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_6(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_7(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_8(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = None
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_9(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(None)
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_10(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=None, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_11(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=None))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_12(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_13(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, ))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_14(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "XXpodsXX": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_15(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "PODS": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_16(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(None),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_17(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "XXnamespace_summaryXX": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_18(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "NAMESPACE_SUMMARY": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_19(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(None),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_20(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "XXmetrics_server_availableXX": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_21(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "METRICS_SERVER_AVAILABLE": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_22(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "XXsourceXX": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_23(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "SOURCE": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_24(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_25(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "ERROR": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_26(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "XXpodsXX": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_27(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "PODS": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_28(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "XXnamespace_summaryXX": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_29(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "NAMESPACE_SUMMARY": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_30(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "XXmetrics_server_availableXX": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_31(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "METRICS_SERVER_AVAILABLE": False,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_32(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": True,
            "source": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_33(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "XXsourceXX": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_34(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "SOURCE": "",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_35(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "XXXX",
            "error": str(exc),
        }


def x_get_resource_usage__mutmut_36(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "XXerrorXX": str(exc),
        }


def x_get_resource_usage__mutmut_37(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "ERROR": str(exc),
        }


def x_get_resource_usage__mutmut_38(namespace: str | None = None, resource: str = "both") -> dict[str, object]:
    """Report real CPU/memory usage per pod and namespace from metrics-server."""
    from hexawyn.mcp.server import build_k8s_adapter, build_pod_metrics_adapter

    try:
        use_case = GetResourceUsageUseCase(
            k8s_port=build_k8s_adapter(),
            metrics_port=build_pod_metrics_adapter(),
        )
        response = use_case.execute(GetResourceUsageCommand(namespace=namespace, resource=resource))
        return {
            "pods": list(response.pods),
            "namespace_summary": list(response.namespace_summary),
            "metrics_server_available": response.metrics_server_available,
            "source": response.source,
            "error": None,
        }
    except Exception as exc:
        return {
            "pods": [],
            "namespace_summary": [],
            "metrics_server_available": False,
            "source": "",
            "error": str(None),
        }

mutants_x_get_resource_usage__mutmut['_mutmut_orig'] = x_get_resource_usage__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_1'] = x_get_resource_usage__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_2'] = x_get_resource_usage__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_3'] = x_get_resource_usage__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_4'] = x_get_resource_usage__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_5'] = x_get_resource_usage__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_6'] = x_get_resource_usage__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_7'] = x_get_resource_usage__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_8'] = x_get_resource_usage__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_9'] = x_get_resource_usage__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_10'] = x_get_resource_usage__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_11'] = x_get_resource_usage__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_12'] = x_get_resource_usage__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_13'] = x_get_resource_usage__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_14'] = x_get_resource_usage__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_15'] = x_get_resource_usage__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_16'] = x_get_resource_usage__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_17'] = x_get_resource_usage__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_18'] = x_get_resource_usage__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_19'] = x_get_resource_usage__mutmut_19 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_20'] = x_get_resource_usage__mutmut_20 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_21'] = x_get_resource_usage__mutmut_21 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_22'] = x_get_resource_usage__mutmut_22 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_23'] = x_get_resource_usage__mutmut_23 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_24'] = x_get_resource_usage__mutmut_24 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_25'] = x_get_resource_usage__mutmut_25 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_26'] = x_get_resource_usage__mutmut_26 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_27'] = x_get_resource_usage__mutmut_27 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_28'] = x_get_resource_usage__mutmut_28 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_29'] = x_get_resource_usage__mutmut_29 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_30'] = x_get_resource_usage__mutmut_30 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_31'] = x_get_resource_usage__mutmut_31 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_32'] = x_get_resource_usage__mutmut_32 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_33'] = x_get_resource_usage__mutmut_33 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_34'] = x_get_resource_usage__mutmut_34 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_35'] = x_get_resource_usage__mutmut_35 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_36'] = x_get_resource_usage__mutmut_36 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_37'] = x_get_resource_usage__mutmut_37 # type: ignore # mutmut generated
mutants_x_get_resource_usage__mutmut['x_get_resource_usage__mutmut_38'] = x_get_resource_usage__mutmut_38 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(get_resource_usage)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(get_resource_usage)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
