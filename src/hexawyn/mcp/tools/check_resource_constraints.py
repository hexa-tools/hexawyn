"""MCP tool: check_resource_constraints — CPU/memory pressure report for a namespace."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.check_resource_constraints.check_resource_constraints_use_case import (  # noqa: E501
    CheckResourceConstraintsUseCase,
)
from hexawyn.application.use_case.cluster.check_resource_constraints.command import (
    CheckResourceConstraintsCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def check_resource_constraints(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "", "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(check_resource_constraints)
