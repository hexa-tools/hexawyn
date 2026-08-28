from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CiliumAgentHealth:
    """Health of a single Cilium agent pod on one node."""

    node: str
    pod_name: str
    namespace: str
    ready: bool
    phase: str
    restart_count: int
    image: str | None = None
    message: str | None = None


@dataclass(frozen=True)
class CiliumDetectionResult:
    """Observed Cilium installation state and agent health."""

    installed: bool
    status: str
    version: str | None
    mode: str
    namespace: str | None
    total_agents: int
    ready_agents: int
    degraded_summary: str | None
    agents: list[CiliumAgentHealth]
    note: str | None


@dataclass(frozen=True)
class CiliumStatusResult:
    """Aggregated health & connectivity status of the Cilium datapath."""

    installed: bool
    status: str
    ready_agents: int
    total_agents: int
    degraded_summary: str | None
    controller_errors: int
    connectivity: str | None
    nodes: list[CiliumAgentHealth]
    note: str | None
