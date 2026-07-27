# mypy: ignore-errors
"""MCP tool: detect_kustomize_patch_conflicts."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops.detect_kustomize_patch_conflicts.command import (
    DetectKustomizePatchConflictsCommand,
)
from hexawyn.application.use_case.gitops.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_use_case import (  # noqa: E501
    DetectKustomizePatchConflictsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_kustomize_patch_conflicts(overlay_path: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

    try:
        use_case = DetectKustomizePatchConflictsUseCase(  # type: ignore
            port=build_kustomize_patch_analysis_adapter()
        )
        _ = use_case.execute(DetectKustomizePatchConflictsCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(detect_kustomize_patch_conflicts)
