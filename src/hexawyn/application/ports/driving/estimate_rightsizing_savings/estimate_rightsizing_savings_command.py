from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EstimateRightsizingSavingsCommand:
    top_n: int = 5
