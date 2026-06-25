from unittest.mock import patch

from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.ports.driven.k8s_port import K8sPort


class _ContainerStateWaiting:
    def __init__(self, reason: str) -> None:
        self.reason = reason


class _ContainerState:
    def __init__(self, waiting_reason: str | None = None) -> None:
        self.waiting = _ContainerStateWaiting(waiting_reason) if waiting_reason else None


class _ContainerStatus:
    def __init__(self, restart_count: int, waiting_reason: str | None = None) -> None:
        self.restart_count = restart_count
        self.state = _ContainerState(waiting_reason)


class _PodMetadata:
    def __init__(self, name: str, namespace: str) -> None:
        self.name = name
        self.namespace = namespace


class _PodStatus:
    def __init__(
        self,
        phase: str,
        container_statuses: list[_ContainerStatus],
    ) -> None:
        self.phase = phase
        self.container_statuses = container_statuses


class _Pod:
    def __init__(
        self,
        name: str,
        namespace: str,
        phase: str,
        restarts: int,
        waiting_reason: str | None = None,
    ) -> None:
        self.metadata = _PodMetadata(name, namespace)
        self.status = _PodStatus(phase, [_ContainerStatus(restarts, waiting_reason)])


class _PodList:
    def __init__(self, items: list[_Pod]) -> None:
        self.items = items


class _NodeCondition:
    def __init__(self, condition_type: str, status: str) -> None:
        self.type = condition_type
        self.status = status


class _NodeMetadata:
    def __init__(self, name: str) -> None:
        self.name = name


class _NodeStatus:
    def __init__(self, allocatable: dict[str, str], conditions: list[_NodeCondition]) -> None:
        self.allocatable = allocatable
        self.conditions = conditions


class _Node:
    def __init__(self, name: str, allocatable: dict[str, str], ready: bool = True) -> None:
        self.metadata = _NodeMetadata(name)
        ready_status = "True" if ready else "False"
        self.status = _NodeStatus(allocatable, [_NodeCondition("Ready", ready_status)])


class _NodeList:
    def __init__(self, items: list[_Node]) -> None:
        self.items = items


class _CoreApi:
    def __init__(self, pods: list[_Pod], nodes: list[_Node] | None = None) -> None:
        self.pods = pods
        self.nodes = nodes or []
        self.requested_namespace: str | None = None
        self.all_namespace_pod_calls = 0

    def list_pod_for_all_namespaces(self, timeout_seconds: int) -> _PodList:
        self.all_namespace_pod_calls += 1
        return _PodList(self.pods)

    def list_namespaced_pod(self, namespace: str, timeout_seconds: int) -> _PodList:
        self.requested_namespace = namespace
        return _PodList(self.pods)

    def list_node(self, timeout_seconds: int) -> _NodeList:
        return _NodeList(self.nodes)


class _MetricsApi:
    def __init__(self, node_metrics: dict[str, object]) -> None:
        self.node_metrics = node_metrics

    def list_cluster_custom_object(self, group: str, version: str, plural: str) -> object:
        return self.node_metrics


class TestVanillaAdapter:
    def test_is_k8s_port(self) -> None:
        adapter = VanillaAdapter("test-cluster")
        assert isinstance(adapter, K8sPort)

    def test_list_pods_returns_real_kubernetes_pods(self) -> None:
        api = _CoreApi(
            [
                _Pod("api-7f8d9c", "default", "Running", 1),
                _Pod("worker-64d8b", "jobs", "Pending", 0),
            ]
        )
        adapter = VanillaAdapter("test-cluster", api=api)

        pods = adapter.list_pods(namespace="default")

        assert api.requested_namespace == "default"
        assert pods == [
            {
                "name": "api-7f8d9c",
                "namespace": "default",
                "status": "Running",
                "restarts": 1,
            },
            {
                "name": "worker-64d8b",
                "namespace": "jobs",
                "status": "Pending",
                "restarts": 0,
            },
        ]

    def test_list_pods_reuses_recent_all_namespace_result(self) -> None:
        api = _CoreApi([_Pod("api-7f8d9c", "default", "Running", 0)])
        adapter = VanillaAdapter("test-cluster", api=api)

        first_result = adapter.list_pods()
        second_result = adapter.list_pods()

        assert first_result == second_result
        assert api.all_namespace_pod_calls == 1

    def test_kind_context_reports_kind_provider(self) -> None:
        adapter = VanillaAdapter("kind-ecom-local", api=_CoreApi([]))

        context = adapter.get_cluster_context()

        assert context["provider"] == "kind"

    def test_unknown_cluster_name_uses_active_kubeconfig_context(self) -> None:
        api = _CoreApi([])
        with patch(
            "hexawyn.adapters.secondary.vanilla.vanilla_adapter.load_kubeconfig",
            return_value=api,
        ) as load_kubeconfig:
            adapter = VanillaAdapter("unknown")

            assert adapter.list_pods() == []

        load_kubeconfig.assert_called_once_with(context=None)

    def test_cluster_metrics_returns_real_counts_and_usage(self) -> None:
        api = _CoreApi(
            pods=[
                _Pod("api-7f8d9c", "default", "Running", 0),
                _Pod("worker-64d8b", "jobs", "Running", 0),
            ],
            nodes=[_Node("node-a", {"cpu": "2", "memory": "4Gi"})],
        )
        metrics_api = _MetricsApi(
            {
                "items": [
                    {
                        "metadata": {"name": "node-a"},
                        "usage": {"cpu": "500m", "memory": "1Gi"},
                    }
                ]
            }
        )
        adapter = VanillaAdapter("test-cluster", api=api, metrics_api=metrics_api)

        metrics = adapter.get_cluster_metrics()

        assert metrics == {
            "cpu_usage_pct": 25.0,
            "memory_usage_pct": 25.0,
            "node_count": 1,
            "pod_count": 2,
        }

    def test_findings_are_derived_from_real_pods_and_nodes(self) -> None:
        api = _CoreApi(
            pods=[
                _Pod("api-7f8d9c", "default", "Running", 4),
                _Pod("worker-64d8b", "jobs", "Pending", 0),
                _Pod("payments-555", "default", "Running", 7, "CrashLoopBackOff"),
            ],
            nodes=[_Node("node-a", {"cpu": "2", "memory": "4Gi"}, ready=False)],
        )
        adapter = VanillaAdapter("test-cluster", api=api)

        findings = adapter.get_findings()

        assert findings == [
            {
                "severity": "warning",
                "message": "Pod default/api-7f8d9c restarted 4 times",
                "remediation": "Inspect recent logs and events for this pod.",
            },
            {
                "severity": "warning",
                "message": "Pod jobs/worker-64d8b is Pending",
                "remediation": "Check scheduling events, resource requests, and node capacity.",
            },
            {
                "severity": "critical",
                "message": "Pod default/payments-555 is CrashLoop",
                "remediation": "Inspect container logs, probes, image pull errors, and recent rollout changes.",
            },
            {
                "severity": "critical",
                "message": "Node node-a is NotReady",
                "remediation": "Inspect node conditions, kubelet status, and recent node events.",
            },
        ]

    def test_health_status_and_score_follow_real_findings(self) -> None:
        api = _CoreApi(
            pods=[_Pod("payments-555", "default", "Running", 7, "CrashLoopBackOff")],
            nodes=[],
        )
        adapter = VanillaAdapter("test-cluster", api=api)

        assert adapter.get_health_score() == 70
        assert adapter.get_health_status() == "critical"

    def test_no_findings_when_cluster_objects_are_healthy(self) -> None:
        api = _CoreApi(
            pods=[_Pod("api-7f8d9c", "default", "Running", 0)],
            nodes=[_Node("node-a", {"cpu": "2", "memory": "4Gi"})],
        )
        adapter = VanillaAdapter("test-cluster", api=api)

        assert adapter.get_findings() == []
        assert adapter.get_health_score() == 100
        assert adapter.get_health_status() == "healthy"
