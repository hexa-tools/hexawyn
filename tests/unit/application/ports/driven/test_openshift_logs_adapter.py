from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.log_search_port import LogSearchPort, RawContainerLog


def _log(container: str) -> RawContainerLog:
    return RawContainerLog(container=container, lines=["boot", "ready"], truncated=False)


class TestPortImplementation:
    def test_is_a_log_search_port(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_logs_adapter import (
            OpenShiftLogsAdapter,
        )

        adapter = OpenShiftLogsAdapter(delegate=MagicMock(spec=LogSearchPort))

        assert isinstance(adapter, LogSearchPort)


class TestFetchPodContainerLogs:
    def test_delegates_to_injected_port(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_logs_adapter import (
            OpenShiftLogsAdapter,
        )

        delegate = MagicMock(spec=LogSearchPort)
        delegate.fetch_pod_container_logs.return_value = [_log("web")]
        adapter = OpenShiftLogsAdapter(delegate=delegate)

        result = adapter.fetch_pod_container_logs("web-0", "team-a", 15)

        delegate.fetch_pod_container_logs.assert_called_once_with("web-0", "team-a", 15)
        assert result[0]["container"] == "web"

    def test_defaults_to_kubernetes_pod_log_search_adapter(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_logs_adapter import (
            OpenShiftLogsAdapter,
        )

        fake_delegate = MagicMock(spec=LogSearchPort)
        fake_delegate.fetch_pod_container_logs.return_value = []
        adapter = OpenShiftLogsAdapter()

        with patch(
            "hexawyn.adapters.secondary.gitops.kubernetes_pod_log_search_adapter."
            "KubernetesPodLogSearchAdapter",
            return_value=fake_delegate,
        ) as adapter_cls:
            result = adapter.fetch_pod_container_logs("web-0", "team-a", 30)

        adapter_cls.assert_called_once_with()
        assert result == []
