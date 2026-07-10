from __future__ import annotations

from hexawyn.application.ports.driven.log_search_port import LogSearchPort, RawContainerLog


class OpenShiftLogsAdapter(LogSearchPort):
    """LogSearchPort for OpenShift clusters.

    Pod logs on OpenShift are served by the same Kubernetes API as vanilla
    clusters (`oc logs` wraps `kubectl logs`), so container log reads are
    delegated to the shared Kubernetes pod-log adapter.
    """

    def __init__(self, delegate: LogSearchPort | None = None) -> None:
        self._delegate = delegate

    def fetch_pod_container_logs(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        return self._logs_source().fetch_pod_container_logs(
            pod_name, namespace, time_window_minutes
        )

    def _logs_source(self) -> LogSearchPort:
        if self._delegate is None:
            from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
                KubernetesPodLogSearchAdapter,
            )

            self._delegate = KubernetesPodLogSearchAdapter()
        return self._delegate
