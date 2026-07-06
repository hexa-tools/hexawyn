from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class PatchValue:
    source_file: str
    value: str
    patch_type: str


@dataclass(frozen=True)
class PatchConflict:
    field_path: str
    resource: str
    conflicting_values: list[PatchValue]
    effective_value: str
    severity: str


@dataclass(frozen=True)
class PatchRedundancy:
    field_path: str
    resource: str
    base_value: str
    patch_value: str
    source_file: str
    severity: str


@dataclass
class KustomizePatchConflictReport:
    overlay_path: str = ""
    patch_conflicts: list[PatchConflict] = field(default_factory=list)
    patch_redundancies: list[PatchRedundancy] = field(default_factory=list)
    orphan_patches: list[str] = field(default_factory=list)
    total_conflicts: int = 0
    total_redundancies: int = 0
