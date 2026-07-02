from __future__ import annotations

from hexawyn.application.ports.driven.etcd_logs_port import ETCDLogsPort
from hexawyn.domain.models.etcd_logs import ETCDLogLine, ETCDLogsRequest


class KubernetesETCDLogsAdapter(ETCDLogsPort):
    def fetch_logs(self, request: ETCDLogsRequest) -> list[ETCDLogLine]:
        return []
