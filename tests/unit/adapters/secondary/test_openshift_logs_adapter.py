from __future__ import annotations

from unittest.mock import Mock

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

    def test_lazy_default_delegate(self) -> None:
        adapter = OpenShiftLogsAdapter()
        assert isinstance(adapter._delegate, LogSearchPort) or adapter._delegate is None
