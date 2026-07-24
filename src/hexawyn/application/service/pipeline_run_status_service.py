from __future__ import annotations

from datetime import UTC, datetime, timedelta

from hexawyn.application.ports.driven.tekton_pipeline_status_port import (
    PipelineRunRecord,
    TektonPipelineStatusPort,
)
from hexawyn.application.use_case.get_pipeline_run_status.command import (
    GetPipelineRunStatusCommand,
)
from hexawyn.application.use_case.get_pipeline_run_status.response import (
    GetPipelineRunStatusResponse,
)
from hexawyn.application.ports.driving.get_pipeline_run_status.get_pipeline_run_status_service_port import (
    GetPipelineRunStatusServicePort,
)
from hexawyn.domain.models.pipeline import PipelineRunStatusReport, PipelineRunSummary


def _filter_by_window(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def _to_summary(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def _find_most_recent_failed(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "Failed"]
    if not failed:
        return None
    most_recent = max(failed, key=lambda r: r["start_time"] or "")
    return _to_summary(most_recent)


def _find_slowest_run(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


class PipelineRunStatusService(GetPipelineRunStatusServicePort):
    def __init__(self, port: TektonPipelineStatusPort) -> None:
        self._port = port

    def get_pipeline_run_status(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)
