from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict


class CiliumIdentityOutput(TypedDict):
    id: str
    labels: list[str]
    endpoint_count: int


@dataclass
class ListCiliumIdentitiesResponse:
    installed: bool = False
    status: str = "not_installed"
    total_identities: int = 0
    identities: list[CiliumIdentityOutput] | None = None
    note: str | None = None
    error: str | None = None
