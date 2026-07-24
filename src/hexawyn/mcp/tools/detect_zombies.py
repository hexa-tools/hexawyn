"""MCP tool: detect_zombies — identify idle workloads with zero network traffic."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.detect_zombies.command import DetectZombiesCommand
from hexawyn.application.use_case.detect_zombies.detect_zombies_use_case import DetectZombiesUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_zombies(analysis_window_hours: int = 24) -> dict[str, object]:
    """Find pods with zero network traffic — zombie deployments that waste resources."""
    from hexawyn.mcp.server import build_zombie_detection_adapter

    try:
        adapter = build_zombie_detection_adapter()
        use_case = DetectZombiesUseCase(zombie_detection_port=adapter)
        response = use_case.execute(
            DetectZombiesCommand(analysis_window_hours=analysis_window_hours)
        )
        r = response.result
        return {
            "analysis_window_hours": r.analysis_window_hours,
            "zombie_count": len(r.zombie_candidates),
            "zombie_candidates": [
                {
                    "pod_name": c.pod_name,
                    "namespace": c.namespace,
                    "age_days": c.age_days,
                    "traffic_rps": c.traffic_rps,
                    "cpu_cores": c.cpu_cores,
                    "memory_gb": c.memory_gb,
                    "risk": c.risk,
                    "reason": c.reason,
                }
                for c in r.zombie_candidates
            ],
            "total_wasted_cores": r.total_wasted_cores,
            "total_wasted_gb": r.total_wasted_gb,
            "prometheus_available": r.prometheus_available,
            "data_source": r.data_source,
            "error": None,
        }
    except Exception as exc:
        return {
            "analysis_window_hours": 0,
            "zombie_count": 0,
            "zombie_candidates": [],
            "total_wasted_cores": 0.0,
            "total_wasted_gb": 0.0,
            "prometheus_available": False,
            "data_source": "estimated",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_zombies)
