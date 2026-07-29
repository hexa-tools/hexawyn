import json
import logging
from datetime import UTC, datetime, timedelta
from pathlib import Path

from hexawyn.application.ports.driven.usage_ledger_port import UsageLedgerPort
from hexawyn.domain.models.usage import (
    DailyStats,
    InvestigationUsage,
    MonthlyReport,
    ToolStat,
    UsageStats,
)

logger = logging.getLogger(__name__)

_MAX_MONTHLY_LINES = 100_000


class UsageLedger(UsageLedgerPort):
    def __init__(self, path: Path | None = None) -> None:
        if path is None:
            path = Path.home() / ".hexawyn" / "usage.jsonl"
        self._path = path

    def record(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def read_all(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def stats(self, days: int = 30) -> UsageStats:
        entries = self.read_all(since=_iso_days_ago(days))
        return _compute_stats(entries)

    def monthly_report(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )


def _coerce_entry(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def _compute_stats(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def _parse_iso(value: str) -> datetime | None:
    try:
        val = value.replace("Z", "+00:00")
        return datetime.fromisoformat(val)
    except (ValueError, TypeError):
        return None


def _iso_days_ago(days: int) -> str:
    return (datetime.now(UTC) - timedelta(days=days)).isoformat()
