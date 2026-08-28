from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict


class CiliumDenialGroupOutput(TypedDict):
    policy: str | None
    source: str
    destination: str
    source_namespace: str | None
    destination_namespace: str | None
    reason: str
    count: int


@dataclass
class DetectCiliumDenialsResponse:
    installed: bool = False
    status: str = "not_installed"
    total_denials: int = 0
    groups: list[CiliumDenialGroupOutput] | None = None
    note: str | None = None
    error: str | None = None
