"""MCP tool: detect_kustomize_patch_conflicts — find conflicting Kustomize overlay patches."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_command import (
    DetectKustomizePatchConflictsCommand,
)
from hexawyn.application.use_case.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_use_case import (
    DetectKustomizePatchConflictsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_kustomize_patch_conflicts(
    overlay_path: str,
) -> dict[str, object]:
    """Detect conflicting or redundant patches in Kustomize overlays.

    Parses a Kustomize overlay directory and identifies fields patched
    by multiple patch files with different values (conflicts) or same
    values (redundancies).

    Args:
        overlay_path: Path to the Kustomize overlay directory.
    """
    from hexawyn.application.service.detect_kustomize_patch_conflicts_service import (
        DetectKustomizePatchConflictsService,
    )
    from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

    try:
        adapter = build_kustomize_patch_analysis_adapter()
        service = DetectKustomizePatchConflictsService(analysis_port=adapter)
        use_case = DetectKustomizePatchConflictsUseCase(service=service)
        response = use_case.execute(DetectKustomizePatchConflictsCommand(overlay_path=overlay_path))
        r = response.result
        return {
            "overlay_path": r.overlay_path,
            "total_conflicts": r.total_conflicts,
            "total_redundancies": r.total_redundancies,
            "patch_conflicts": [
                {
                    "field_path": c.field_path,
                    "resource": c.resource,
                    "conflicting_values": [
                        {
                            "source_file": v.source_file,
                            "value": v.value,
                            "patch_type": v.patch_type,
                        }
                        for v in c.conflicting_values
                    ],
                    "effective_value": c.effective_value,
                    "severity": c.severity,
                }
                for c in r.patch_conflicts
            ],
            "patch_redundancies": [
                {
                    "field_path": rd.field_path,
                    "resource": rd.resource,
                    "base_value": rd.base_value,
                    "patch_value": rd.patch_value,
                    "source_file": rd.source_file,
                    "severity": rd.severity,
                }
                for rd in r.patch_redundancies
            ],
            "orphan_patches": r.orphan_patches,
            "error": None,
        }
    except Exception as exc:
        return {
            "overlay_path": overlay_path,
            "total_conflicts": 0,
            "total_redundancies": 0,
            "patch_conflicts": [],
            "patch_redundancies": [],
            "orphan_patches": [],
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_kustomize_patch_conflicts)
