from dataclasses import dataclass, field


@dataclass
class ComputeSLOErrorBudgetResponse:
    result: dict[str, object] = field(default_factory=dict)
