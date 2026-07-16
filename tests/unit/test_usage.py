from hexawyn.domain.models.usage import (
    DailyStats,
    InvestigationUsage,
    UsageStats,
)


class TestInvestigationUsageTypedDict:
    def test_required_fields(self) -> None:
        entry: InvestigationUsage = {
            "timestamp": "2026-07-16T14:32:01Z",
            "query": "why is payments-api OOM?",
            "tool_name": "crashloop_detector",
            "verdict": "PASS",
            "cluster_name": "prod-eu",
            "namespace": "payments",
            "duration_ms": 4200,
            "prompt_tokens": 450,
            "completion_tokens": 180,
            "model": "qwen3:8b",
            "provider": "ollama",
        }
        assert entry["timestamp"] == "2026-07-16T14:32:01Z"
        assert entry["tool_name"] == "crashloop_detector"
        assert entry["verdict"] == "PASS"
        assert entry["duration_ms"] == 4200

    def test_namespace_can_be_none(self) -> None:
        entry: InvestigationUsage = {
            "timestamp": "",
            "query": "",
            "tool_name": "-",
            "verdict": "N/A",
            "cluster_name": "",
            "namespace": None,
            "duration_ms": 0,
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "model": "-",
            "provider": "-",
        }
        assert entry["namespace"] is None

    def test_zero_tokens_for_non_llm_investigation(self) -> None:
        entry: InvestigationUsage = {
            "timestamp": "2026-07-16T14:32:45Z",
            "query": "list pods in payments",
            "tool_name": "list_pods",
            "verdict": "N/A",
            "cluster_name": "prod-eu",
            "namespace": "payments",
            "duration_ms": 120,
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "model": "-",
            "provider": "-",
        }
        assert entry["prompt_tokens"] == 0
        assert entry["completion_tokens"] == 0
        assert entry["model"] == "-"


class TestUsageStatsTypedDict:
    def test_empty_stats(self) -> None:
        stats = UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )
        assert stats["total_investigations"] == 0

    def test_populated_stats(self) -> None:
        stats = UsageStats(
            total_investigations=10,
            total_tokens=5000,
            total_duration_ms=45000,
            avg_duration_ms=4500,
            top_tools=[
                {"tool_name": "crashloop_detector", "count": 5, "avg_duration_ms": 4200},
            ],
            verdict_distribution={"PASS": 8, "DEGRADED": 2},
            models_used={"qwen3:8b": 10},
        )
        assert stats["total_investigations"] == 10
        assert stats["verdict_distribution"]["PASS"] == 8
        assert len(stats["top_tools"]) == 1


class TestDailyStatsTypedDict:
    def test_empty_daily(self) -> None:
        daily = DailyStats(date="2026-07-16", investigations=0, tokens=0)
        assert daily["date"] == "2026-07-16"


class TestMonthlyReportDataclass:
    def test_default_empty(self) -> None:
        from hexawyn.domain.models.usage import MonthlyReport

        report = MonthlyReport(year=2026, month=7)
        assert report.year == 2026
        assert report.month == 7
        assert report.stats["total_investigations"] == 0
        assert report.daily_breakdown == []
