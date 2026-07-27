"""MCP tool: audit_secret_rotation."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.audit_secret_rotation.audit_secret_rotation_use_case import (  # noqa: E501
    AuditSecretRotationUseCase,
)
from hexawyn.application.use_case.security.audit_secret_rotation.command import (
    AuditSecretRotationCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def audit_secret_rotation() -> dict[str, object]:
    from hexawyn.mcp.server import build_secret_rotation_audit_adapter

    try:
        use_case = AuditSecretRotationUseCase(port=build_secret_rotation_audit_adapter())
        _ = use_case.execute(AuditSecretRotationCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(audit_secret_rotation)
