"""MCP tool: detect_missing_probes — identify workloads without health checks."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.detect_missing_probes.detect_missing_probes_command import (
    DetectMissingProbesCommand,
)
from hexawyn.application.use_case.detect_missing_probes.detect_missing_probes_use_case import (
    DetectMissingProbesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_missing_probes(namespace: str | None = None) -> dict[str, object]:
    """Find deployments/pods with no liveness or readiness probes.

    Scans all workloads across namespaces and identifies those missing
    liveness probes, readiness probes, or both. Prioritizes critical
    workloads in production with external exposure.

    Args:
        namespace: Optional namespace filter. If omitted, scans all namespaces.
    """
    from hexawyn.application.service.detect_missing_probes_service import (
        DetectMissingProbesService,
    )
    from hexawyn.mcp.server import build_probe_audit_adapter

    try:
        adapter = build_probe_audit_adapter()
        service = DetectMissingProbesService(probe_audit_port=adapter)
        use_case = DetectMissingProbesUseCase(service=service)
        response = use_case.execute(DetectMissingProbesCommand(namespace=namespace))
        r = response.result
        return {
            "total_without_probes": r.total_without_probes,
            "critical": r.critical,
            "warning": r.warning,
            "informational": r.informational,
            "missing_probes": [
                {
                    "deployment_name": p.deployment_name,
                    "namespace": p.namespace,
                    "missing": p.missing,
                    "severity": p.severity,
                    "exposed_port": p.exposed_port,
                    "readiness_suggestion": p.readiness_suggestion,
                    "liveness_suggestion": p.liveness_suggestion,
                    "has_service": p.has_service,
                    "workload_type": p.workload_type,
                    "is_exposed_externally": p.is_exposed_externally,
                }
                for p in r.missing_probes
            ],
            "misconfigured_probes": [
                {
                    "deployment_name": p.deployment_name,
                    "namespace": p.namespace,
                    "missing": p.missing,
                    "severity": p.severity,
                    "exposed_port": p.exposed_port,
                    "has_service": p.has_service,
                    "workload_type": p.workload_type,
                    "is_exposed_externally": p.is_exposed_externally,
                }
                for p in r.misconfigured_probes
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "total_without_probes": 0,
            "critical": 0,
            "warning": 0,
            "informational": 0,
            "missing_probes": [],
            "misconfigured_probes": [],
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_missing_probes)
