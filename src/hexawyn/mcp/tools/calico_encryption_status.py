"""MCP tool: calico_encryption_status — Calico WireGuard encryption status."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.calico_encryption_status.calico_encryption_status_use_case import (  # noqa: E501
    CalicoEncryptionStatusUseCase,
)
from hexawyn.application.use_case.calico.calico_encryption_status.command import (
    CalicoEncryptionStatusCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _node_dict(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "wireguard_enabled": getattr(node, "wireguard_enabled", False),
    }


def calico_encryption_status() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(calico_encryption_status)
