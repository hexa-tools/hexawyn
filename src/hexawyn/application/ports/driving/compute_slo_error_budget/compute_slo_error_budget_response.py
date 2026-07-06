from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.error_budget import SLOErrorBudgetResult


@dataclass
class ComputeSLOErrorBudgetResponse:
    result: SLOErrorBudgetResult
