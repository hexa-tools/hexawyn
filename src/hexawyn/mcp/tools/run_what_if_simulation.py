"""MCP tool: run_what_if_simulation."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.run_what_if_simulation.command import (
    RunWhatIfSimulationCommand,
)
from hexawyn.application.use_case.cluster.run_what_if_simulation.run_what_if_simulation_use_case import (  # noqa: E501
    RunWhatIfSimulationUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def run_what_if_simulation(
    target_service: str = "",
    namespace: str = "",
    proposed_replicas: int = 1,
    current_replicas: int | None = None,
    current_cpu_utilization: float | None = None,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_what_if_simulation_adapter

    try:
        use_case = RunWhatIfSimulationUseCase(simulation_port=build_what_if_simulation_adapter())
        response = use_case.execute(
            RunWhatIfSimulationCommand(
                target_service=target_service,
                namespace=namespace,
                proposed_replicas=proposed_replicas,
                current_replicas=current_replicas,
                current_cpu_utilization=current_cpu_utilization,
            )
        )
        return {
            "target_service": response.target_service,
            "namespace": response.namespace,
            "current_replicas": response.current_replicas,
            "proposed_replicas": response.proposed_replicas,
            "risk": response.risk,
            "risk_level": response.risk_level,
            "affected_services": response.affected_services,
            "estimated_latency_increase_percent": response.estimated_latency_increase_percent,
            "error_risk": response.error_risk,
            "pdb_violation": response.pdb_violation,
            "hpa_detected": response.hpa_detected,
            "circular_dependency": response.circular_dependency,
            "recommendation": response.recommendation,
            "error": None,
        }
    except Exception as exc:
        return {
            "target_service": target_service,
            "namespace": namespace,
            "current_replicas": 0,
            "proposed_replicas": proposed_replicas,
            "risk": "",
            "risk_level": 0,
            "affected_services": [],
            "estimated_latency_increase_percent": 0.0,
            "error_risk": "",
            "pdb_violation": False,
            "hpa_detected": False,
            "circular_dependency": False,
            "recommendation": "",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(run_what_if_simulation)
