from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict


class CiliumAgentOutput(TypedDict):
    node: str
    pod_name: str
    namespace: str
    ready: bool
    phase: str
    restart_count: int
    image: str | None
    message: str | None


@dataclass
class CiliumDetectResponse:
    installed: bool = False
    status: str = "not_installed"
    version: str | None = None
    mode: str = "UNKNOWN"
    namespace: str | None = None
    total_agents: int = 0
    ready_agents: int = 0
    degraded_summary: str | None = None
    agents: list[CiliumAgentOutput] | None = None
    note: str | None = None
    error: str | None = None
