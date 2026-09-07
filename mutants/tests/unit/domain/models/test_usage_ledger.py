import json
import tempfile
from pathlib import Path
from unittest.mock import patch

from hexawyn.domain.models.usage import InvestigationUsage
from hexawyn.infrastructure.monitoring.usage_ledger import UsageLedger, _parse_iso


def _make_entry(  # noqa: PLR0913
    timestamp: str = "2026-07-16T14:32:01Z",
    query: str = "why is payments-api OOM?",
    tool_name: str = "crashloop_detector",
    verdict: str = "PASS",
    cluster_name: str = "prod-eu",
    namespace: str | None = "payments",
    duration_ms: int = 4200,
    prompt_tokens: int = 450,
    completion_tokens: int = 180,
    model: str = "qwen3:8b",
    provider: str = "ollama",
) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=timestamp,
        query=query,
        tool_name=tool_name,
        verdict=verdict,
        cluster_name=cluster_name,
        namespace=namespace,
        duration_ms=duration_ms,
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        model=model,
        provider=provider,
    )


class TestUsageLedgerRecord:
    def test_record_writes_line_to_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "usage.jsonl"
            ledger = UsageLedger(path=path)

            ledger.record(_make_entry())

            assert path.exists()
            lines = path.read_text().strip().split("\n")
            assert len(lines) == 1
            entry = json.loads(lines[0])
            assert entry["tool_name"] == "crashloop_detector"
            assert entry["duration_ms"] == 4200  # noqa: PLR2004

    def test_record_creates_parent_directories(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sub" / "dir" / "usage.jsonl"
            ledger = UsageLedger(path=path)
            ledger.record(_make_entry())
            assert path.exists()

    def test_record_appends_multiple_entries(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "usage.jsonl"
            ledger = UsageLedger(path=path)
            ledger.record(_make_entry(tool_name="tool_a"))
            ledger.record(_make_entry(tool_name="tool_b"))
            ledger.record(_make_entry(tool_name="tool_c"))

            lines = path.read_text().strip().split("\n")
            assert len(lines) == 3  # noqa: PLR2004

    def test_record_does_not_crash_on_disk_full(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "usage.jsonl"
            ledger = UsageLedger(path=path)
            ledger.record(_make_entry())
            path.chmod(0o444)
            ledger.record(_make_entry())

    def test_init_uses_default_path_when_none_provided(self) -> None:
        with patch("hexawyn.infrastructure.monitoring.usage_ledger.Path.home") as mock_home:
            mock_home.return_value = Path("/mock/home")
            ledger = UsageLedger()
            assert ledger._path == Path("/mock/home") / ".hexawyn" / "usage.jsonl"


class TestUsageLedgerReadAll:
    def test_read_all_returns_entries(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "usage.jsonl"
            ledger = UsageLedger(path=path)
            ledger.record(_make_entry(tool_name="crashloop_detector"))
            ledger.record(_make_entry(tool_name="oomkilled_detector"))

            entries = ledger.read_all()
            assert len(entries) == 2  # noqa: PLR2004
            assert entries[0]["tool_name"] == "crashloop_detector"
            assert entries[1]["tool_name"] == "oomkilled_detector"

    def test_read_all_returns_empty_for_missing_file(self) -> None:
        ledger = UsageLedger(path=Path("/tmp/nonexistent_usage.jsonl"))
        assert ledger.read_all() == []

    def test_read_all_since_filters_by_timestamp(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "usage.jsonl"
            ledger = UsageLedger(path=path)
            ledger.record(_make_entry(timestamp="2026-07-15T10:00:00Z", tool_name="old"))
            ledger.record(_make_entry(timestamp="2026-07-16T14:00:00Z", tool_name="new"))
            ledger.record(_make_entry(timestamp="2026-07-17T08:00:00Z", tool_name="newest"))

            entries = ledger.read_all(since="2026-07-16T00:00:00Z")
            assert len(entries) == 2  # noqa: PLR2004
            assert all(e["tool_name"] in ("new", "newest") for e in entries)

    def test_read_all_tool_filter(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "usage.jsonl"
            ledger = UsageLedger(path=path)
            ledger.record(_make_entry(tool_name="crashloop_detector"))
            ledger.record(_make_entry(tool_name="oomkilled_detector"))
            ledger.record(_make_entry(tool_name="crashloop_detector"))

            entries = ledger.read_all(tool="crashloop_detector")
            assert len(entries) == 2  # noqa: PLR2004
            assert all(e["tool_name"] == "crashloop_detector" for e in entries)

    def test_read_all_skips_corrupted_lines(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "usage.jsonl"
            path.write_text('{"valid": true}\nnot json\n{broken\n{"valid2": true}\n')
            ledger = UsageLedger(path=path)

            entries = ledger.read_all()
            assert len(entries) == 2  # noqa: PLR2004

    def test_read_all_skips_blank_lines(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "usage.jsonl"
            path.write_text(
                '{"tool_name": "tool_a", "timestamp": "2026-07-16T10:00:00Z"}\n'
                "\n"
                '{"tool_name": "tool_b", "timestamp": "2026-07-16T11:00:00Z"}\n'
                "\n"
            )
            ledger = UsageLedger(path=path)

            entries = ledger.read_all()
            assert len(entries) == 2  # noqa: PLR2004

    def test_read_all_skips_non_dict_entries(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "usage.jsonl"
            path.write_text(
                '{"tool_name": "tool_a", "timestamp": "2026-07-16T10:00:00Z"}\n'
                '["valid json but not dict"]\n'
                "12345\n"
                '{"tool_name": "tool_b", "timestamp": "2026-07-16T11:00:00Z"}\n'
            )
            ledger = UsageLedger(path=path)

            entries = ledger.read_all()
            assert len(entries) == 2  # noqa: PLR2004

    def test_read_all_handles_os_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "usage.jsonl"
            path.write_text('{"tool_name": "tool_a", "timestamp": "2026-07-16T10:00:00Z"}\n')
            ledger = UsageLedger(path=path)

            with patch("builtins.open", side_effect=OSError("permission denied")):
                entries = ledger.read_all()
                assert entries == []

    def test_read_all_since_handles_invalid_iso_timestamp(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "usage.jsonl"
            ledger = UsageLedger(path=path)
            ledger.record(_make_entry(timestamp="2026-07-16T10:00:00Z", tool_name="valid"))

            entries = ledger.read_all(since="not-a-date")
            assert len(entries) == 1


class TestParseIso:
    def test_returns_datetime_for_valid_iso(self) -> None:
        result = _parse_iso("2026-07-16T10:00:00Z")
        assert result is not None
        assert result.month == 7  # noqa: PLR2004
        assert result.day == 16  # noqa: PLR2004

    def test_returns_none_for_invalid_string(self) -> None:
        assert _parse_iso("not-a-date") is None

    def test_returns_none_for_empty_string(self) -> None:
        assert _parse_iso("") is None


class TestUsageLedgerStats:
    def test_stats_returns_empty_for_no_entries(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ledger = UsageLedger(path=Path(tmp) / "usage.jsonl")
            stats = ledger.stats()
            assert stats["total_investigations"] == 0
            assert stats["total_tokens"] == 0

    def test_stats_computes_aggregates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "usage.jsonl"
            ledger = UsageLedger(path=path)
            ledger.record(
                _make_entry(
                    tool_name="crashloop_detector",
                    duration_ms=4000,
                    prompt_tokens=400,
                    completion_tokens=200,
                    verdict="PASS",
                )
            )
            ledger.record(
                _make_entry(
                    tool_name="crashloop_detector",
                    duration_ms=5000,
                    prompt_tokens=500,
                    completion_tokens=250,
                    verdict="PASS",
                )
            )
            ledger.record(
                _make_entry(
                    tool_name="oomkilled_detector",
                    duration_ms=6000,
                    prompt_tokens=300,
                    completion_tokens=150,
                    verdict="DEGRADED",
                )
            )

            stats = ledger.stats(days=365)
            assert stats["total_investigations"] == 3  # noqa: PLR2004
            assert stats["total_tokens"] == 400 + 200 + 500 + 250 + 300 + 150
            assert stats["total_duration_ms"] == 15000  # noqa: PLR2004
            assert stats["avg_duration_ms"] == 5000  # noqa: PLR2004
            assert stats["verdict_distribution"]["PASS"] == 2  # noqa: PLR2004
            assert stats["verdict_distribution"]["DEGRADED"] == 1

    def test_stats_top_tools_sorted_by_count(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "usage.jsonl"
            ledger = UsageLedger(path=path)
            for _ in range(5):
                ledger.record(_make_entry(tool_name="crashloop_detector", duration_ms=1000))
            for _ in range(3):
                ledger.record(_make_entry(tool_name="oomkilled_detector", duration_ms=2000))
            for _ in range(7):
                ledger.record(_make_entry(tool_name="zombie_detector", duration_ms=500))

            stats = ledger.stats(days=365)
            tools = stats["top_tools"]
            assert tools[0]["tool_name"] == "zombie_detector"
            assert tools[0]["count"] == 7  # noqa: PLR2004
            assert tools[1]["tool_name"] == "crashloop_detector"
            assert tools[2]["tool_name"] == "oomkilled_detector"

    def test_stats_models_used(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "usage.jsonl"
            ledger = UsageLedger(path=path)
            ledger.record(_make_entry(model="qwen3:8b"))
            ledger.record(_make_entry(model="qwen3:8b"))
            ledger.record(_make_entry(model="deepseek-r1:7b"))

            stats = ledger.stats(days=365)
            assert stats["models_used"]["qwen3:8b"] == 2  # noqa: PLR2004
            assert stats["models_used"]["deepseek-r1:7b"] == 1
            assert "-" not in stats["models_used"]


class TestUsageLedgerMonthlyReport:
    def test_monthly_report_groups_by_day(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "usage.jsonl"
            ledger = UsageLedger(path=path)
            ledger.record(
                _make_entry(
                    timestamp="2026-07-15T10:00:00Z",
                    tool_name="tool_a",
                    prompt_tokens=100,
                    completion_tokens=50,
                )
            )
            ledger.record(
                _make_entry(
                    timestamp="2026-07-15T14:00:00Z",
                    tool_name="tool_b",
                    prompt_tokens=200,
                    completion_tokens=100,
                )
            )
            ledger.record(
                _make_entry(
                    timestamp="2026-07-16T08:00:00Z",
                    tool_name="tool_a",
                    prompt_tokens=300,
                    completion_tokens=150,
                )
            )

            report = ledger.monthly_report(2026, 7)
            assert report.year == 2026  # noqa: PLR2004
            assert report.month == 7  # noqa: PLR2004
            assert report.stats["total_investigations"] == 3  # noqa: PLR2004
            assert len(report.daily_breakdown) == 2  # noqa: PLR2004

            day_15 = next(d for d in report.daily_breakdown if d["date"] == "2026-07-15")
            assert day_15["investigations"] == 2  # noqa: PLR2004
            assert day_15["tokens"] == 100 + 50 + 200 + 100

            day_16 = next(d for d in report.daily_breakdown if d["date"] == "2026-07-16")
            assert day_16["investigations"] == 1
            assert day_16["tokens"] == 300 + 150

    def test_monthly_report_empty_month(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ledger = UsageLedger(path=Path(tmp) / "usage.jsonl")
            report = ledger.monthly_report(2026, 7)
            assert report.stats["total_investigations"] == 0
            assert report.daily_breakdown == []

    def test_monthly_report_december_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "usage.jsonl"
            ledger = UsageLedger(path=path)
            ledger.record(
                _make_entry(
                    timestamp="2025-12-15T10:00:00Z",
                    tool_name="tool_z",
                    prompt_tokens=100,
                    completion_tokens=50,
                )
            )

            report = ledger.monthly_report(2025, 12)
            assert report.year == 2025  # noqa: PLR2004
            assert report.month == 12  # noqa: PLR2004
            assert report.stats["total_investigations"] == 1
            assert len(report.daily_breakdown) == 1
