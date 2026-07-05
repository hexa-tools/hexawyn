"""MCP tool: detect_privileged_pods — flags pods running as root or with a
privileged security context (privileged, hostPID/hostNetwork/hostIPC, allowed
privilege escalation, dangerous added capabilities) and maps each violation
to the Pod Security Standards level it breaks."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.detect_privileged_pods.detect_privileged_pods_command import (
    DetectPrivilegedPodsCommand,
)
from hexawyn.application.use_case.detect_privileged_pods.detect_privileged_pods_use_case import (
    DetectPrivilegedPodsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_privileged_pods(namespaces: list[str] | None = None) -> dict[str, object]:
    from hexawyn.application.service.pod_security_standards_audit_service import (
        PodSecurityStandardsAuditService,
    )
    from hexawyn.mcp.server import build_pod_security_adapter

    try:
        service = PodSecurityStandardsAuditService(pod_security_port=build_pod_security_adapter())
        r = DetectPrivilegedPodsUseCase(service=service).execute(
            DetectPrivilegedPodsCommand(namespaces=namespaces)
        )
        return {
            "findings": r.findings,
            "compliant_pod_count": r.compliant_pod_count,
            "total_pods_checked": r.total_pods_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_privileged_pods)
