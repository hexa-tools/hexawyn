from datetime import UTC, datetime

from hexawyn.application.ports.driven.tekton_port import NamespacedPipelineRunInfo

_STUCK_THRESHOLD_SECONDS = 3600
_STATUS_PRIORITY: dict[str, int] = {"Failed": 0, "Running": 1, "Succeeded": 2}


def sort_by_status_then_time(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def find_stuck_runs(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck
