"""MCP tool: audit_secret_rotation — flags Kubernetes Secrets not rotated in
more than the configured threshold (default 90 days), maps each stale
secret to the pods/deployments that reference it, and classifies rotation
risk."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_command import (
    AuditSecretRotationCommand,
)
from hexawyn.application.use_case.audit_secret_rotation.audit_secret_rotation_use_case import (
    AuditSecretRotationUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def audit_secret_rotation(rotation_threshold_days: int = 90) -> dict[str, object]:
    from hexawyn.application.service.secret_rotation_audit_service import (
        SecretRotationAuditService,
    )
    from hexawyn.mcp.server import build_secret_rotation_audit_adapter

    try:
        service = SecretRotationAuditService(
            secret_rotation_port=build_secret_rotation_audit_adapter()
        )
        r = AuditSecretRotationUseCase(service=service).execute(
            AuditSecretRotationCommand(rotation_threshold_days=rotation_threshold_days)
        )
        return {
            "findings": r.findings,
            "excluded_secrets": r.excluded_secrets,
            "total_secrets_checked": r.total_secrets_checked,
            "rotation_threshold_days": r.rotation_threshold_days,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(audit_secret_rotation)
