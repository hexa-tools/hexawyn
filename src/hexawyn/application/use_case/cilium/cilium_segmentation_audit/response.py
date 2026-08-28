from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict


class CiliumPathFindingOutput(TypedDict):
    source_id: str
    destination_id: str
    source_labels: list[str]
    destination_labels: list[str]
    severity: str
    note: str | None


@dataclass
class CiliumSegmentationAuditResponse:
    installed: bool = False
    status: str = "not_installed"
    view: str = "vanilla"
    total_identities: int = 0
    total_paths: int = 0
    uncovered_paths: int = 0
    findings: list[CiliumPathFindingOutput] | None = None
    summary: str = ""
    note: str | None = None
    error: str | None = None
