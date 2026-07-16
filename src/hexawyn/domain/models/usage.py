from dataclasses import dataclass, field
from typing import TypedDict


class InvestigationUsage(TypedDict):
    timestamp: str
    query: str
    tool_name: str
    verdict: str
    cluster_name: str
    namespace: str | None
    duration_ms: int
    prompt_tokens: int
    completion_tokens: int
    model: str
    provider: str


class ToolStat(TypedDict):
    tool_name: str
    count: int
    avg_duration_ms: int


class DailyStats(TypedDict):
    date: str
    investigations: int
    tokens: int


class UsageStats(TypedDict):
    total_investigations: int
    total_tokens: int
    total_duration_ms: int
    avg_duration_ms: int
    top_tools: list[ToolStat]
    verdict_distribution: dict[str, int]
    models_used: dict[str, int]


@dataclass
class MonthlyReport:
    year: int
    month: int
    stats: UsageStats = field(
        default_factory=lambda: UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )
    )
    daily_breakdown: list[DailyStats] = field(default_factory=list)
