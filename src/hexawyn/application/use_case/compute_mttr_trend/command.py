from dataclasses import dataclass, field


@dataclass(frozen=True)
class ComputeMttrTrendCommand:
    months: list[str] = field(default_factory=list)
