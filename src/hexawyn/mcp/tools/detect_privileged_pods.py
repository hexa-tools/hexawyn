"""MCP tool: detect_privileged_pods."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.detect_privileged_pods.command import (
    DetectPrivilegedPodsCommand,
)
from hexawyn.application.use_case.security.detect_privileged_pods.detect_privileged_pods_use_case import (  # noqa: E501
    DetectPrivilegedPodsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_privileged_pods() -> dict[str, object]:
    from hexawyn.mcp.server import build_pod_security_adapter

    try:
        use_case = DetectPrivilegedPodsUseCase(port=build_pod_security_adapter())
        _ = use_case.execute(DetectPrivilegedPodsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_privileged_pods)
