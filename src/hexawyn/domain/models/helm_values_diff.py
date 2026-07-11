from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

DiffSeverity = Literal["critical", "warning", "informational"]
ChangeType = Literal["added", "removed", "changed"]


@dataclass(frozen=True)
class ValueDiff:
    key_path: str
    source_value: str
    target_value: str
    change_type: ChangeType
    severity: DiffSeverity
    is_secret: bool
    type_mismatch: bool
    suggestion: str


@dataclass
class HelmValuesDiffReport:
    release: str
    source_env: str
    target_env: str
    critical: list[ValueDiff] = field(default_factory=list)
    warning: list[ValueDiff] = field(default_factory=list)
    informational: list[ValueDiff] = field(default_factory=list)
    total_differences: int = 0
    in_sync: bool = True
