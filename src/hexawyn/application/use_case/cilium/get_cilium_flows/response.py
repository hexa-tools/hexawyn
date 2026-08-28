from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict


class CiliumFlowOutput(TypedDict):
    timestamp: str
    source: str
    destination: str
    source_namespace: str | None
    destination_namespace: str | None
    source_identity: str | None
    destination_identity: str | None
    verdict: str
    drop_reason: str | None
    protocol: str | None
    destination_port: str | None
    l7_protocol: str | None
    direction: str | None
    policy: str | None


@dataclass
class GetCiliumFlowsResponse:
    installed: bool = False
    status: str = "not_installed"
    total_flows: int = 0
    flows: list[CiliumFlowOutput] | None = None
    note: str | None = None
    error: str | None = None
