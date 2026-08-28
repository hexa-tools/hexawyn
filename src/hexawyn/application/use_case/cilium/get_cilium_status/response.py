from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict


class CiliumStatusNodeOutput(TypedDict):
    node: str
    pod_name: str
    namespace: str
    ready: bool
    phase: str
    restart_count: int
    image: str | None
    message: str | None


@dataclass
class GetCiliumStatusResponse:
    installed: bool = False
    status: str = "not_installed"
    ready_agents: int = 0
    total_agents: int = 0
    degraded_summary: str | None = None
    controller_errors: int = 0
    connectivity: str | None = None
    nodes: list[CiliumStatusNodeOutput] | None = None
    note: str | None = None
    error: str | None = None
