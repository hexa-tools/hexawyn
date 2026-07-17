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

    def test_verdict_fail(self) -> None:
        entry: InvestigationUsage = {
            "timestamp": "",
            "query": "",
            "tool_name": "",
            "verdict": "FAIL",
            "cluster_name": "",
            "namespace": None,
            "duration_ms": 0,
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "model": "-",
            "provider": "-",
        }
        assert entry["verdict"] == "FAIL"

    def test_verdict_degraded(self) -> None:
        entry: InvestigationUsage = {
            "timestamp": "",
            "query": "",
            "tool_name": "",
            "verdict": "DEGRADED",
            "cluster_name": "",
            "namespace": None,
            "duration_ms": 0,
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "model": "-",
            "provider": "-",
        }
        assert entry["verdict"] == "DEGRADED"

    def test_verdict_blocked(self) -> None:
        entry: InvestigationUsage = {
            "timestamp": "",
            "query": "",
            "tool_name": "",
            "verdict": "BLOCKED",
            "cluster_name": "",
            "namespace": None,
            "duration_ms": 0,
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "model": "-",
            "provider": "-",
        }
        assert entry["verdict"] == "BLOCKED"

    def test_verdict_flag(self) -> None:
        entry: InvestigationUsage = {
            "timestamp": "",
            "query": "",
            "tool_name": "",
            "verdict": "FLAG",
            "cluster_name": "",
            "namespace": None,
            "duration_ms": 0,
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "model": "-",
            "provider": "-",
        }
        assert entry["verdict"] == "FLAG"

    def test_large_token_counts(self) -> None:
        entry: InvestigationUsage = {
            "timestamp": "",
            "query": "",
            "tool_name": "",
            "verdict": "PASS",
            "cluster_name": "",
            "namespace": None,
            "duration_ms": 999999,
            "prompt_tokens": 100000,
            "completion_tokens": 50000,
            "model": "large-model",
            "provider": "openai",
        }
        assert entry["prompt_tokens"] == 100000

    def test_empty_cluster_name(self) -> None:
        entry: InvestigationUsage = {
            "timestamp": "",
            "query": "",
            "tool_name": "",
            "verdict": "N/A",
            "cluster_name": "",
            "namespace": None,
            "duration_ms": 0,
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "model": "-",
            "provider": "-",
        }
        assert entry["cluster_name"] == ""


class TestToolStatTypedDict:
    def test_construction(self) -> None:
        from hexawyn.domain.models.usage import ToolStat

        ts: ToolStat = {"tool_name": "crashloop", "count": 5, "avg_duration_ms": 4200}
        assert ts["tool_name"] == "crashloop"
        assert ts["count"] == 5
        assert ts["avg_duration_ms"] == 4200


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

    def test_top_tools_multiple_entries(self) -> None:
        stats = UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[
                {"tool_name": "crashloop", "count": 5, "avg_duration_ms": 1000},
                {"tool_name": "oomkilled", "count": 3, "avg_duration_ms": 2000},
            ],
            verdict_distribution={},
            models_used={},
        )
        assert len(stats["top_tools"]) == 2

    def test_models_used_multiple_models(self) -> None:
        stats = UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={"qwen3:8b": 5, "deepseek-r1:7b": 3},
        )
        assert stats["models_used"]["qwen3:8b"] == 5
        assert stats["models_used"]["deepseek-r1:7b"] == 3

    def test_verdict_distribution_multiple_keys(self) -> None:
        stats = UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={"PASS": 5, "FAIL": 2, "FLAG": 1},
            models_used={},
        )
        assert len(stats["verdict_distribution"]) == 3


class TestDailyStatsTypedDict:
    def test_empty_daily(self) -> None:
        daily = DailyStats(date="2026-07-16", investigations=0, tokens=0)
        assert daily["date"] == "2026-07-16"

    def test_populated_daily(self) -> None:
        daily = DailyStats(date="2026-07-16", investigations=10, tokens=5000)
        assert daily["investigations"] == 10
        assert daily["tokens"] == 5000


class TestMonthlyReportDataclass:
    def test_default_empty(self) -> None:
        from hexawyn.domain.models.usage import MonthlyReport

        report = MonthlyReport(year=2026, month=7)
        assert report.year == 2026
        assert report.month == 7
        assert report.stats["total_investigations"] == 0
        assert report.daily_breakdown == []

    def test_with_daily_breakdown(self) -> None:
        from hexawyn.domain.models.usage import DailyStats, MonthlyReport

        report = MonthlyReport(
            year=2026,
            month=7,
            daily_breakdown=[
                DailyStats(date="2026-07-16", investigations=5, tokens=2500),
                DailyStats(date="2026-07-17", investigations=3, tokens=1500),
            ],
        )
        assert len(report.daily_breakdown) == 2

    def test_month_boundary_january(self) -> None:
        from hexawyn.domain.models.usage import MonthlyReport

        report = MonthlyReport(year=2026, month=1)
        assert report.month == 1

    def test_month_boundary_december(self) -> None:
        from hexawyn.domain.models.usage import MonthlyReport

        report = MonthlyReport(year=2026, month=12)
        assert report.month == 12
