from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.mttr_trend import MTTRTrendReport


@dataclass
class ComputeMTTRTrendResponse:
    result: MTTRTrendReport
