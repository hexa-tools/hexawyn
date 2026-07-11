from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.helm_values_diff import HelmValuesDiffReport


@dataclass
class DiffHelmValuesResponse:
    result: HelmValuesDiffReport
