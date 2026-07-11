"""MCP tool: check_disruption_risks — predicted service disruption risks
within the next N days, in business language."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.check_disruption_risks.check_disruption_risks_command import (  # noqa: E501
    CheckDisruptionRisksCommand,
)
from hexawyn.application.use_case.check_disruption_risks.check_disruption_risks_use_case import (  # noqa: E501
    CheckDisruptionRisksUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP

    from hexawyn.domain.models.disruption_risk import RiskEvent


def check_disruption_risks(warning_days: int = 7) -> dict[str, object]:
    from hexawyn.application.service.check_disruption_risks_service import (
        CheckDisruptionRisksService,
    )
    from hexawyn.mcp.server import build_disruption_risk_adapter

    try:
        adapter = build_disruption_risk_adapter()
        service = CheckDisruptionRisksService(disruption_risk_port=adapter)
        use_case = CheckDisruptionRisksUseCase(service=service)
        response = use_case.execute(CheckDisruptionRisksCommand(warning_days=warning_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "has_risks": r.has_risks,
            "has_data": r.has_data,
            "risks": [_serialize(risk) for risk in r.risks],
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Semaine en cours",
            "has_risks": False,
            "has_data": False,
            "risks": [],
            "warning": "",
            "error": str(exc),
        }


def _serialize(risk: RiskEvent) -> dict[str, object]:
    return {
        "business_service_name": risk.business_service_name,
        "risk_type": risk.risk_type,
        "predicted_date": risk.predicted_date,
        "days_from_now": risk.days_from_now,
        "detail": risk.detail,
    }


def register(mcp: FastMCP) -> None:
    mcp.tool()(check_disruption_risks)
