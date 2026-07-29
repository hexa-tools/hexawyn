from __future__ import annotations

from datetime import UTC, datetime

from hexawyn.domain.models.constants import STUCK_PIPELINE_RUN_THRESHOLD_SECONDS


def find_stuck_runs(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck
