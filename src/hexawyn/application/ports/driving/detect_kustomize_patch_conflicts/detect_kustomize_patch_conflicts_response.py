from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.kustomize_patch_conflict import (
    KustomizePatchConflictReport,
)


@dataclass
class DetectKustomizePatchConflictsResponse:
    result: KustomizePatchConflictReport
