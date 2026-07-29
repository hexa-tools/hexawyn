from __future__ import annotations

from unittest.mock import Mock, patch

from hexawyn.adapters.secondary.openshift.openshift_logs_adapter import OpenShiftLogsAdapter
from hexawyn.application.ports.driven.log_search_port import LogSearchPort


class TestOpenShiftLogsAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OpenShiftLogsAdapter(), LogSearchPort)

    def test_delegates_to_logs_source(self) -> None:
        delegate = Mock(spec=LogSearchPort)
        delegate.fetch_pod_container_logs.return_value = []
        adapter = OpenShiftLogsAdapter(delegate=delegate)
        result = adapter.fetch_pod_container_logs("pod", "ns", 5)
        assert result == []
        delegate.fetch_pod_container_logs.assert_called_once_with("pod", "ns", 5)

    def test_lazy_default_delegate_is_none(self) -> None:
        adapter = OpenShiftLogsAdapter()
        assert adapter._delegate is None

    def test_lazy_init_fetch_creates_and_uses_delegate(self) -> None:
        mock_kubernetes_adapter = Mock(spec=LogSearchPort)
        mock_kubernetes_adapter.fetch_pod_container_logs.return_value = []

        with patch(
            "hexawyn.adapters.secondary.gitops.kubernetes_pod_log_search_adapter"
            ".KubernetesPodLogSearchAdapter",
            return_value=mock_kubernetes_adapter,
        ):
            adapter = OpenShiftLogsAdapter()
            result = adapter.fetch_pod_container_logs("mypod", "myns", 10)
            assert result == []
            mock_kubernetes_adapter.fetch_pod_container_logs.assert_called_once_with(
                "mypod", "myns", 10
            )
            assert adapter._delegate is mock_kubernetes_adapter
