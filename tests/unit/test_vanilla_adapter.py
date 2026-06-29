from unittest.mock import MagicMock, patch

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
        from datetime import UTC, datetime, timedelta

        self.creation_timestamp = datetime.now(UTC) - timedelta(days=3)


class _PodSpec:
    def __init__(self, node_name: str = "node-1") -> None:
        self.node_name = node_name


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
        node_name: str = "node-1",
    ) -> None:
        self.metadata = _PodMetadata(name, namespace)
        self.spec = _PodSpec(node_name)
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


class _NamespaceMetadata:
    def __init__(self, name: str) -> None:
        self.name = name
        from datetime import UTC, datetime, timedelta

        self.creation_timestamp = datetime.now(UTC) - timedelta(days=30)


class _NamespaceStatus:
    def __init__(self, phase: str) -> None:
        self.phase = phase


class _Namespace:
    def __init__(self, name: str, phase: str = "Active") -> None:
        self.metadata = _NamespaceMetadata(name)
        self.status = _NamespaceStatus(phase)


class _NamespaceList:
    def __init__(self, items: list[_Namespace]) -> None:
        self.items = items


class _CoreApi:
    def __init__(
        self,
        pods: list[_Pod],
        nodes: list[_Node] | None = None,
        namespaces: list[_Namespace] | None = None,
    ) -> None:
        self.pods = pods
        self.nodes = nodes or []
        self.namespaces = namespaces or []
        self.requested_namespace: str | None = None
        self.all_namespace_pod_calls = 0
        self.list_namespace_calls = 0

    def list_pod_for_all_namespaces(self, timeout_seconds: int) -> _PodList:
        self.all_namespace_pod_calls += 1
        return _PodList(self.pods)

    def list_namespaced_pod(self, namespace: str, timeout_seconds: int) -> _PodList:
        self.requested_namespace = namespace
        return _PodList(self.pods)

    def list_node(self, timeout_seconds: int) -> _NodeList:
        return _NodeList(self.nodes)

    def list_namespace(self, timeout_seconds: int) -> _NamespaceList:
        self.list_namespace_calls += 1
        return _NamespaceList(self.namespaces)


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
                _Pod("api-7f8d9c", "default", "Running", 1, node_name="node-a"),
                _Pod("worker-64d8b", "jobs", "Pending", 0, node_name="node-b"),
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
                "age": "3d",
                "node": "node-a",
            },
            {
                "name": "worker-64d8b",
                "namespace": "jobs",
                "status": "Pending",
                "restarts": 0,
                "age": "3d",
                "node": "node-b",
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


class TestVanillaAdapterConfigIsolation:
    """Tests that catch the wrong-cluster bug.

    If VanillaAdapter calls load_kubeconfig() more than once, or if the cached
    CoreV1Api uses the global kubernetes Configuration, background calls to
    config.load_kube_config() for another context will silently switch which
    cluster list_pods() talks to.

    Regression: CLI was fetching pods from kind-hexawyn (127.0.0.1:33831)
    instead of hetzner-preprod because _validate_connection() was changing the
    global config between the panel refresh and the investigation call.
    """

    def test_api_client_initialized_once_reused_on_cache_expiry(self) -> None:
        """load_kubeconfig must be called exactly once per VanillaAdapter instance.

        If called again after cache expiry, it would pick up the current global
        kubernetes config (which may have been changed to a different context by
        a background task such as _validate_connection or startup_status).
        """
        mock_api = MagicMock()
        mock_api.list_pod_for_all_namespaces.return_value = MagicMock(items=[])
        mock_api.list_node.return_value = MagicMock(items=[])

        with patch(
            "hexawyn.adapters.secondary.vanilla.vanilla_adapter.load_kubeconfig",
            return_value=mock_api,
        ) as mock_load_kubeconfig:
            adapter = VanillaAdapter("hetzner-preprod")

            # First call initialises _api via load_kubeconfig
            adapter.list_pods()
            assert mock_load_kubeconfig.call_count == 1
            mock_load_kubeconfig.assert_called_with(context="hetzner-preprod")

            # Expire the pod cache to force a real K8s call
            adapter._pod_cache = None
            adapter._pod_cache_updated_at = 0.0

            # Second call must reuse the same _api — NOT call load_kubeconfig again
            adapter.list_pods()
            assert mock_load_kubeconfig.call_count == 1, (
                "load_kubeconfig() was called more than once. If the global K8s config "
                "changed between the two calls (e.g. background _validate_connection), "
                "the second call would create a CoreV1Api for the wrong cluster."
            )

    def test_list_pods_uses_correct_context_not_global_default(self) -> None:
        """VanillaAdapter must pass the cluster name as context to load_kubeconfig.

        Passing context=None would use the global current-context, which may point
        to a different cluster than the one the user selected.
        """
        mock_api = MagicMock()
        mock_api.list_pod_for_all_namespaces.return_value = MagicMock(items=[])

        with patch(
            "hexawyn.adapters.secondary.vanilla.vanilla_adapter.load_kubeconfig",
            return_value=mock_api,
        ) as mock_load_kubeconfig:
            adapter = VanillaAdapter("hetzner-preprod")
            adapter.list_pods()

        mock_load_kubeconfig.assert_called_once_with(context="hetzner-preprod")

    def test_unknown_cluster_uses_active_context_not_fixed_name(self) -> None:
        """For 'unknown' clusters the active context is used (context=None)."""
        mock_api = MagicMock()
        mock_api.list_pod_for_all_namespaces.return_value = MagicMock(items=[])

        with patch(
            "hexawyn.adapters.secondary.vanilla.vanilla_adapter.load_kubeconfig",
            return_value=mock_api,
        ) as mock_load_kubeconfig:
            adapter = VanillaAdapter("unknown")
            adapter.list_pods()

        mock_load_kubeconfig.assert_called_once_with(context=None)


class TestVanillaAdapterListNamespaces:
    def test_list_namespaces_returns_namespace_info_list(self) -> None:
        api = _CoreApi(
            pods=[],
            namespaces=[
                _Namespace("default", "Active"),
                _Namespace("kube-system", "Active"),
                _Namespace("production", "Active"),
            ],
        )
        adapter = VanillaAdapter("test-cluster", api=api)

        namespaces = adapter.list_namespaces()

        assert len(namespaces) == 3
        for ns in namespaces:
            assert ns["name"] in ("default", "kube-system", "production")
            assert ns["status"] == "Active"
            assert "d" in ns["age"]

    def test_list_namespaces_uses_k8s_api(self) -> None:
        api = _CoreApi(pods=[], namespaces=[])
        adapter = VanillaAdapter("test-cluster", api=api)

        adapter.list_namespaces()

        assert api.list_namespace_calls == 1

    def test_list_namespaces_terminating_status(self) -> None:
        api = _CoreApi(
            pods=[],
            namespaces=[_Namespace("old-ns", "Terminating")],
        )
        adapter = VanillaAdapter("test-cluster", api=api)

        namespaces = adapter.list_namespaces()

        assert namespaces[0]["status"] == "Terminating"

    def test_list_namespaces_empty_cluster(self) -> None:
        api = _CoreApi(pods=[], namespaces=[])
        adapter = VanillaAdapter("test-cluster", api=api)

        namespaces = adapter.list_namespaces()

        assert namespaces == []
