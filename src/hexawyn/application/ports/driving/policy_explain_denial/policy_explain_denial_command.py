from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PolicyExplainDenialCommand:
    resource_kind: str
    resource_name: str
    namespace: str
