from __future__ import annotations

from hexawyn.application.ports.driven.etcd_logs_port import ETCDLogsPort
from hexawyn.domain.models.etcd_logs import ETCDLogsRequest
from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_etcd_logs_adapter import (
    KubernetesETCDLogsAdapter,
)


class TestKubernetesETCDLogsAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(KubernetesETCDLogsAdapter(), ETCDLogsPort)

    def test_fetch_returns_empty(self) -> None:
        r = KubernetesETCDLogsAdapter().fetch_logs(ETCDLogsRequest(time_window_minutes=60))
        assert r == []
