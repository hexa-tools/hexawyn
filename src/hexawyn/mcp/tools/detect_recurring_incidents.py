"""MCP tool: detect_recurring_incidents — find services with most frequent incidents."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.detect_recurring_incidents.detect_recurring_incidents_command import (
    DetectRecurringIncidentsCommand,
)
from hexawyn.application.use_case.detect_recurring_incidents.detect_recurring_incidents_use_case import (
    DetectRecurringIncidentsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_recurring_incidents(window_days: int = 30) -> dict[str, object]:
    """Detect services with the most recurring incidents for tech debt prioritization.

    Returns top 10 services ranked by incident frequency over the window,
    with recurring pattern detection (same root cause >3 times flagged),
    average duration, and investment recommendations.

    Args:
        window_days: Analysis window in days (default: 30).
    """
    from hexawyn.application.service.detect_recurring_incidents_service import (
        DetectRecurringIncidentsService,
    )
    from hexawyn.mcp.server import build_recurring_incident_adapter

    try:
        adapter = build_recurring_incident_adapter()
        service = DetectRecurringIncidentsService(incident_port=adapter)
        use_case = DetectRecurringIncidentsUseCase(service=service)
        response = use_case.execute(DetectRecurringIncidentsCommand(window_days=window_days))
        r = response.result
        return {
            "services": [
                {
                    "service_name": s.service_name,
                    "incident_count": s.incident_count,
                    "avg_duration_minutes": s.avg_duration_minutes,
                    "most_common_cause": s.most_common_cause,
                    "recurrence_count": s.recurrence_count,
                    "is_recurring": s.is_recurring,
                    "recommendation": s.recommendation,
                }
                for s in r.services
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "services": [],
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_recurring_incidents)
