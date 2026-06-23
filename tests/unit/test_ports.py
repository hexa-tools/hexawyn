from abc import ABC

import pytest
from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.logs_port import LogsPort
from hexawyn.application.ports.driven.metrics_port import MetricsPort
from hexawyn.application.ports.driven.traces_port import TracesPort


class TestPorts:
    def test_k8s_port_is_abstract(self):
        assert issubclass(K8sPort, ABC)

    def test_metrics_port_is_abstract(self):
        assert issubclass(MetricsPort, ABC)

    def test_traces_port_is_abstract(self):
        assert issubclass(TracesPort, ABC)

    def test_logs_port_is_abstract(self):
        assert issubclass(LogsPort, ABC)

    def test_cannot_instantiate_k8s_port_directly(self):
        with pytest.raises(TypeError):
            K8sPort()

    def test_demo_adapter_implements_all_ports(self):
        from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

        adapter = DemoAdapter()
        assert isinstance(adapter, K8sPort)
        assert isinstance(adapter, MetricsPort)
        assert isinstance(adapter, TracesPort)
        assert isinstance(adapter, LogsPort)
