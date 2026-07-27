from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.etcd_logs_port import ETCDLogsPort
from hexawyn.application.use_case.observability.etcd_logs.command import ETCDLogsCommand
from hexawyn.application.use_case.observability.etcd_logs.response import ETCDLogsResponse
from hexawyn.domain.models.etcd_logs import ETCDLogsRequest, ETCDLogsResult


class ETCDLogsUseCase:
    def __init__(self, port: ETCDLogsPort) -> None:
        self._port = port

    def execute(self, command: ETCDLogsCommand) -> ETCDLogsResponse:
        req = ETCDLogsRequest(time_window_minutes=command.time_window_minutes)
        lines = self._port.fetch_logs(req)
        r = ETCDLogsResult.compute(request=req, log_lines=lines)
        return ETCDLogsResponse(
            etcd_accessible=r.etcd_accessible,
            total_log_lines=r.total_log_lines,
            error_count=r.error_count,
            leader_election_count=r.leader_election_count,
            compaction_errors=r.compaction_errors,
            leader_instability=r.leader_instability,
            summary=r.summary,
            errors=[asdict(e) for e in r.errors],
        )
