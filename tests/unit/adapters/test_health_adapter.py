from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.adapters.secondary.vanilla.adapters.health_adapter import VanillaHealthAdapter
from hexawyn.application.ports.driven.k8s_port import ClusterHealthPort, K8sPort, PodInfo


def _healthy_pod(name: str) -> PodInfo:
    return PodInfo(
        name=name,
        namespace="default",
        status="Running",
        restarts=0,
        age="1h",
        node="node-1",
        cpu_request_millicores=100,
        memory_request_mib=128,
    )


def _unhealthy_pod(name: str, status: str, restarts: int = 0) -> PodInfo:
    return PodInfo(
        name=name,
        namespace="default",
        status=status,
        restarts=restarts,
        age="2d",
        node="node-1",
        cpu_request_millicores=200,
        memory_request_mib=256,
    )


def _fake_node_ready(name: str) -> MagicMock:
    node = MagicMock()
    metadata = MagicMock()
    metadata.name = name
    node.metadata = metadata
    status = MagicMock()
    ready_cond = MagicMock()
    ready_cond.type = "Ready"
    ready_cond.status = "True"
    status.conditions = [ready_cond]
    node.status = status
    return node


class TestVanillaHealthAdapter:
    def test_implements_cluster_health_port(self) -> None:
        k8s = MagicMock(spec=K8sPort)
        api = MagicMock()
        adapter = VanillaHealthAdapter(k8s_port=k8s, api=api)
        assert isinstance(adapter, ClusterHealthPort)

    def test_get_findings_returns_empty_when_all_healthy(self) -> None:
        k8s = MagicMock(spec=K8sPort)
        k8s.list_pods.return_value = [_healthy_pod("pod-1")]

        api = MagicMock()
        node_response = MagicMock()
        node_response.items = [_fake_node_ready("node-1")]
        api.list_node.return_value = node_response

        adapter = VanillaHealthAdapter(k8s_port=k8s, api=api)
        result = adapter.get_findings()

        assert result == []

    def test_get_findings_returns_unhealthy_pod(self) -> None:
        k8s = MagicMock(spec=K8sPort)
        k8s.list_pods.return_value = [
            _unhealthy_pod("pod-1", "CrashLoop", restarts=0),
        ]

        api = MagicMock()
        node_response = MagicMock()
        node_response.items = [_fake_node_ready("node-1")]
        api.list_node.return_value = node_response

        adapter = VanillaHealthAdapter(k8s_port=k8s, api=api)
        result = adapter.get_findings()

        assert len(result) == 1
        assert result[0]["severity"] == "critical"
        assert "CrashLoop" in result[0]["message"]

    def test_get_findings_returns_warning_for_other_status(self) -> None:
        k8s = MagicMock(spec=K8sPort)
        k8s.list_pods.return_value = [
            _unhealthy_pod("pod-1", "Pending", restarts=0),
        ]

        api = MagicMock()
        node_response = MagicMock()
        node_response.items = [_fake_node_ready("node-1")]
        api.list_node.return_value = node_response

        adapter = VanillaHealthAdapter(k8s_port=k8s, api=api)
        result = adapter.get_findings()

        assert len(result) == 1
        assert result[0]["severity"] == "warning"

    def test_get_findings_returns_restarted_pod(self) -> None:
        k8s = MagicMock(spec=K8sPort)
        k8s.list_pods.return_value = [
            _unhealthy_pod("pod-1", "Running", restarts=10),
        ]

        api = MagicMock()
        node_response = MagicMock()
        node_response.items = [_fake_node_ready("node-1")]
        api.list_node.return_value = node_response

        adapter = VanillaHealthAdapter(k8s_port=k8s, api=api)
        result = adapter.get_findings()

        assert len(result) == 1
        assert result[0]["severity"] == "warning"
        assert "restarted" in result[0]["message"]

    def test_get_health_score_all_healthy(self) -> None:
        k8s = MagicMock(spec=K8sPort)
        k8s.list_pods.return_value = [_healthy_pod("pod-1")]

        api = MagicMock()
        node_response = MagicMock()
        node_response.items = [_fake_node_ready("node-1")]
        api.list_node.return_value = node_response

        adapter = VanillaHealthAdapter(k8s_port=k8s, api=api)
        score = adapter.get_health_score()

        assert score == 100  # noqa: PLR2004

    def test_get_health_score_with_critical(self) -> None:
        k8s = MagicMock(spec=K8sPort)
        k8s.list_pods.return_value = [
            _unhealthy_pod("pod-1", "CrashLoop", restarts=0),
        ]

        api = MagicMock()
        node_response = MagicMock()
        node_response.items = [_fake_node_ready("node-1")]
        api.list_node.return_value = node_response

        adapter = VanillaHealthAdapter(k8s_port=k8s, api=api)
        score = adapter.get_health_score()

        assert score == 70  # 100 - 1*30  # noqa: PLR2004

    def test_get_health_score_with_warning(self) -> None:
        k8s = MagicMock(spec=K8sPort)
        k8s.list_pods.return_value = [
            _unhealthy_pod("pod-1", "Pending", restarts=0),
        ]

        api = MagicMock()
        node_response = MagicMock()
        node_response.items = [_fake_node_ready("node-1")]
        api.list_node.return_value = node_response

        adapter = VanillaHealthAdapter(k8s_port=k8s, api=api)
        score = adapter.get_health_score()

        assert score == 90  # 100 - 1*10  # noqa: PLR2004

    def test_get_health_score_floor_zero(self) -> None:
        k8s = MagicMock(spec=K8sPort)
        k8s.list_pods.return_value = [
            _unhealthy_pod("pod-1", "CrashLoop", restarts=0),
            _unhealthy_pod("pod-2", "CrashLoop", restarts=0),
            _unhealthy_pod("pod-3", "CrashLoop", restarts=0),
            _unhealthy_pod("pod-4", "CrashLoop", restarts=0),
        ]

        api = MagicMock()
        node_response = MagicMock()
        node_response.items = [_fake_node_ready("node-1")]
        api.list_node.return_value = node_response

        adapter = VanillaHealthAdapter(k8s_port=k8s, api=api)
        score = adapter.get_health_score()

        assert score == 0

    def test_get_health_status_healthy(self) -> None:
        k8s = MagicMock(spec=K8sPort)
        k8s.list_pods.return_value = [_healthy_pod("pod-1")]

        api = MagicMock()
        node_response = MagicMock()
        node_response.items = [_fake_node_ready("node-1")]
        api.list_node.return_value = node_response

        adapter = VanillaHealthAdapter(k8s_port=k8s, api=api)
        status = adapter.get_health_status()

        assert status == "healthy"

    def test_get_health_status_critical(self) -> None:
        k8s = MagicMock(spec=K8sPort)
        k8s.list_pods.return_value = [
            _unhealthy_pod("pod-1", "CrashLoop", restarts=0),
        ]

        api = MagicMock()
        node_response = MagicMock()
        node_response.items = [_fake_node_ready("node-1")]
        api.list_node.return_value = node_response

        adapter = VanillaHealthAdapter(k8s_port=k8s, api=api)
        status = adapter.get_health_status()

        assert status == "critical"

    def test_get_health_status_degraded(self) -> None:
        k8s = MagicMock(spec=K8sPort)
        k8s.list_pods.return_value = [
            _unhealthy_pod("pod-1", "Pending", restarts=0),
        ]

        api = MagicMock()
        node_response = MagicMock()
        node_response.items = [_fake_node_ready("node-1")]
        api.list_node.return_value = node_response

        adapter = VanillaHealthAdapter(k8s_port=k8s, api=api)
        status = adapter.get_health_status()

        assert status == "degraded"
