"""MCP tool: detect_recurring_incidents."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.troubleshooting.detect_recurring_incidents.command import (
    DetectRecurringIncidentsCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_recurring_incidents.detect_recurring_incidents_use_case import (  # noqa: E501
    DetectRecurringIncidentsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def detect_recurring_incidents() -> dict[str, object]:
    from hexawyn.mcp.server import build_recurring_incident_adapter

    try:
        service = DetectRecurringIncidentsUseCase(incident_port=build_recurring_incident_adapter())
        use_case = DetectRecurringIncidentsUseCase(service=service)  # type: ignore
        _ = use_case.execute(DetectRecurringIncidentsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_recurring_incidents)
