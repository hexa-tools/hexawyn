from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.ports.driven.k8s_port import K8sPort


class TestVanillaAdapter:
    def test_is_k8s_port(self):
        adapter = VanillaAdapter("test-cluster")
        assert isinstance(adapter, K8sPort)

    def test_health_score_is_100(self):
        adapter = VanillaAdapter("test-cluster")
        assert adapter.get_health_score() == 100

    def test_health_status_is_healthy(self):
        adapter = VanillaAdapter("test-cluster")
        assert adapter.get_health_status() == "healthy"

    def test_no_pods(self):
        adapter = VanillaAdapter("test-cluster")
        assert adapter.list_pods() == []

    def test_no_findings(self):
        adapter = VanillaAdapter("test-cluster")
        assert adapter.get_findings() == []
