"""MCP tool: memory_saturation — Predict which pods are about to OOM."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.troubleshooting.memory_saturation.command import (
    MemorySaturationCommand,
)
from hexawyn.application.use_case.troubleshooting.memory_saturation.memory_saturation_use_case import (  # noqa: E501
    MemorySaturationUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def memory_saturation(prediction_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_memory_saturation_adapter

    try:
        a = build_memory_saturation_adapter()
        r = MemorySaturationUseCase(port=a).execute(
            MemorySaturationCommand(prediction_window_minutes=prediction_window_minutes)
        )
        return {
            "prediction_window_minutes": r.prediction_window_minutes,
            "critical_pods": r.critical_pods,
            "safe_pod_count": r.safe_pod_count,
            "error": r.error,  # type: ignore
        }
    except Exception as exc:
        return {"critical_pods": [], "safe_pod_count": 0, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(memory_saturation)
