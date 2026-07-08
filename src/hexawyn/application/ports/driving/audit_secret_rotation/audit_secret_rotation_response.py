from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal, TypedDict


class StaleSecretFindingDict(TypedDict):
    name: str
    namespace: str
    secret_type: str
    age_days: int
    last_modified: str
    referenced_by: list[str]
    risk_level: Literal["critical", "medium", "low"]
    urgency_score: int
    note: str | None


class ExcludedSecretDict(TypedDict):
    name: str
    namespace: str
    reason: str


@dataclass
class AuditSecretRotationResponse:
    findings: list[StaleSecretFindingDict] = field(default_factory=list)
    excluded_secrets: list[ExcludedSecretDict] = field(default_factory=list)
    total_secrets_checked: int = 0
    rotation_threshold_days: int = 0
    summary: str = ""
    error: str | None = None
