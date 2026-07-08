"""keda_scaledjobs_list.py"""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.keda_scaledjobs_list.keda_scaledjobs_list_command import (
    KedaScaledJobsListCommand,
)
from hexawyn.application.use_case.keda_scaledjobs_list.keda_scaledjobs_list_use_case import (
    KedaScaledJobsListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def keda_scaledjobs_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.application.service.keda_scaledjobs_list_service import KedaScaledJobsListService
    from hexawyn.mcp.server import build_keda_adapter

    try:
        a = build_keda_adapter()
        svc = KedaScaledJobsListService(port=a)
        uc = KedaScaledJobsListUseCase(service=svc)
        r = uc.execute(KedaScaledJobsListCommand(namespace))
        return {k: v for k, v in r.__dict__.items()}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_scaledjobs_list)
