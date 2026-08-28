"""MCP tool: cilium_encryption_status — Cilium wire-level encryption state."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.cilium_encryption_status.cilium_encryption_status_use_case import (  # noqa: E501
    CiliumEncryptionStatusUseCase,
)
from hexawyn.application.use_case.cilium.cilium_encryption_status.command import (
    CiliumEncryptionStatusCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def cilium_encryption_status() -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = CiliumEncryptionStatusUseCase(port=adapter)
        result = use_case.execute(CiliumEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "status": result.status,
            "mode": result.mode,
            "encrypted_nodes": result.encrypted_nodes,
            "total_nodes": result.total_nodes,
            "coverage": result.coverage,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "mode": "UNKNOWN",
            "encrypted_nodes": 0,
            "total_nodes": 0,
            "coverage": None,
            "note": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(cilium_encryption_status)
