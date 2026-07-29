# mypy: ignore-errors
"""MCP tool: diff_helm_values."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops.diff_helm_values.command import DiffHelmValuesCommand
from hexawyn.application.use_case.gitops.diff_helm_values.diff_helm_values_use_case import (
    DiffHelmValuesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def diff_helm_values(  # type: ignore
    release="test",
    source_namespace="test-source_namespace",
    target_namespace="test-target_namespace",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = DiffHelmValuesUseCase(helm_values_port=build_helm_values_diff_adapter())
        _ = use_case.execute(DiffHelmValuesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(diff_helm_values)
