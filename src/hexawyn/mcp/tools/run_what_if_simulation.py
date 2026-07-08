"""MCP tool: run_what_if_simulation — Simulate impact of a cluster change."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.run_what_if_simulation.run_what_if_simulation_command import (
    RunWhatIfSimulationCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def run_what_if_simulation(
    target_service: str,
    namespace: str,
    proposed_replicas: int,
    current_replicas: int | None = None,
    current_cpu_utilization: float | None = None,
) -> dict[str, object]:
    """Simulate the impact of scaling a service in the cluster.

    Args:
        target_service: The service to simulate changes on (e.g. 'auth-service').
        namespace: The Kubernetes namespace of the target service.
        proposed_replicas: The desired replica count after the change.
        current_replicas: Optional — current replica count (auto-detected if omitted).
        current_cpu_utilization: Optional — current CPU % (auto-detected if omitted).
    """
    from hexawyn.application.service.run_what_if_simulation_service import (
        RunWhatIfSimulationService,
    )
    from hexawyn.application.use_case.run_what_if_simulation.run_what_if_simulation_use_case import (
        RunWhatIfSimulationUseCase,
    )
    from hexawyn.mcp.server import build_what_if_simulation_adapter

    try:
        adapter = build_what_if_simulation_adapter()
        service = RunWhatIfSimulationService(simulation_port=adapter)
        use_case = RunWhatIfSimulationUseCase(service=service)
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
            "risk": response.risk.name,
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
            "risk": "UNKNOWN",
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
    """Register run_what_if_simulation as an MCP tool on the given FastMCP server."""
    mcp.tool()(run_what_if_simulation)
