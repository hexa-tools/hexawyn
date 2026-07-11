"""MCP tool: compute_prediction_roi — measures the ROI of prediction-based
prevention (avoided incidents × revenue per minute, minus infrastructure cost)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_command import (  # noqa: E501
    ComputePredictionRoiCommand,
)
from hexawyn.application.use_case.compute_prediction_roi.compute_prediction_roi_use_case import (  # noqa: E501
    ComputePredictionRoiUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP

    from hexawyn.domain.models.prediction_roi import PreventedIncident


def compute_prediction_roi(period: str) -> dict[str, object]:
    from hexawyn.application.service.compute_prediction_roi_service import (
        ComputePredictionRoiService,
    )
    from hexawyn.mcp.server import build_prediction_roi_adapter

    try:
        adapter = build_prediction_roi_adapter()
        service = ComputePredictionRoiService(prediction_roi_port=adapter)
        use_case = ComputePredictionRoiUseCase(service=service)
        response = use_case.execute(ComputePredictionRoiCommand(period=period))
        report = response.result
        return {
            "period_label": report.period_label,
            "detected_count": report.detected_count,
            "prevented_incident_count": report.prevented_incident_count,
            "avoided_downtime_minutes": report.avoided_downtime_minutes,
            "total_avoided_cost_eur": report.total_avoided_cost_eur,
            "infrastructure_cost_eur": report.infrastructure_cost_eur,
            "roi_eur": report.roi_eur,
            "prevented_incidents": [_serialize(item) for item in report.prevented_incidents],
            "config_available": report.config_available,
            "explanation": report.explanation,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": period,
            "detected_count": 0,
            "prevented_incident_count": 0,
            "avoided_downtime_minutes": 0,
            "total_avoided_cost_eur": None,
            "infrastructure_cost_eur": 0.0,
            "roi_eur": None,
            "prevented_incidents": [],
            "config_available": False,
            "explanation": "",
            "error": str(exc),
        }


def _serialize(item: PreventedIncident) -> dict[str, object]:
    return {
        "incident_ref": item.incident_ref,
        "business_service_name": item.business_service_name,
        "detected_at": item.detected_at,
        "avoided_downtime_minutes": item.avoided_downtime_minutes,
        "confidence_pct": item.confidence_pct,
        "avoided_cost_eur": item.avoided_cost_eur,
    }


def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_prediction_roi)
