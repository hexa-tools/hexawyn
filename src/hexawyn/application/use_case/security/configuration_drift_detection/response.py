from dataclasses import dataclass, field
from typing import TypedDict


class DriftedFieldDict(TypedDict):
    field_path: str
    desired_value: str
    live_value: str
    severity: str


class DriftResultDict(TypedDict):
    kind: str
    name: str
    namespace: str
    managed_by: str
    release_or_source: str | None
    drifted_fields: list[DriftedFieldDict]
    has_critical_drift: bool
    is_orphaned: bool


@dataclass
class ConfigurationDriftDetectionResponse:
    drifted_resources: list[DriftResultDict] = field(default_factory=list)
    drifted_by_namespace: dict[str, list[DriftResultDict]] = field(
        default_factory=dict,
    )
    in_sync_count: int = 0
    excluded_resources: int = 0
    total_checked: int = 0
    summary: str = ""
    error: str | None = None
