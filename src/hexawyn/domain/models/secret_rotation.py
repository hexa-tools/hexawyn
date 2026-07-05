from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Literal

RiskLevel = Literal["critical", "medium", "low"]


@dataclass(frozen=True)
class ManagedFieldsEntry:
    manager: str
    operation: str
    time: str
    fields_v1_raw: Mapping[str, object]


@dataclass(frozen=True)
class StaleSecretFinding:
    name: str
    namespace: str
    secret_type: str
    age_days: int
    last_modified: str
    referenced_by: list[str]
    risk_level: RiskLevel
    urgency_score: int
    note: str | None


@dataclass(frozen=True)
class ExcludedSecret:
    name: str
    namespace: str
    reason: str


@dataclass(frozen=True)
class SecretRotationReport:
    findings: list[StaleSecretFinding]
    excluded_secrets: list[ExcludedSecret]
    total_secrets_checked: int
    rotation_threshold_days: int
    summary: str
