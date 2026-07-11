from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.budget_projection import BudgetProjectionReport


@dataclass
class ProjectBudgetResponse:
    result: BudgetProjectionReport
