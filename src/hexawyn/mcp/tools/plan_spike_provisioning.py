# mypy: ignore-errors
"""MCP tool: plan_spike_provisioning."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.plan_spike_provisioning.command import (
    PlanSpikeProvisioningCommand,
)
from hexawyn.application.use_case.cluster.plan_spike_provisioning.plan_spike_provisioning_use_case import (  # noqa: E501
    PlanSpikeProvisioningUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def plan_spike_provisioning(event_date: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_spike_provisioning_adapter

    try:
        use_case = PlanSpikeProvisioningUseCase(port=build_spike_provisioning_adapter())  # type: ignore
        _ = use_case.execute(PlanSpikeProvisioningCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(plan_spike_provisioning)
