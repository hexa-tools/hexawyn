"""MCP tool: detect_kustomize_patch_conflicts."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.detect_kustomize_patch_conflicts.command import (
    DetectKustomizePatchConflictsCommand,
)
from hexawyn.application.use_case.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_use_case import (
    DetectKustomizePatchConflictsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_kustomize_patch_conflicts(overlay_path="test") -> dict[str, object]:
    from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

    try:
        use_case = DetectKustomizePatchConflictsUseCase(
            port=build_kustomize_patch_analysis_adapter()
        )
        _ = use_case.execute(DetectKustomizePatchConflictsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_kustomize_patch_conflicts)
