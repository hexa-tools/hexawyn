from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.tekton_port import TektonPort
from hexawyn.domain.errors import ClusterUnreachableError, PipelineNotFoundError


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


class _CRDApi:
    """Fake KubernetesCRDApi that returns pre-built TaskRun dicts."""

    def __init__(self, items: list[dict[str, object]]) -> None:
        self._items = items
        self.last_label_selector: str = ""

    def list_namespaced_custom_object(
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        label_selector: str = "",
    ) -> dict[str, object]:
        self.last_label_selector = label_selector
        return {"items": self._items}


def _make_task_run(
    name: str,
    task_ref: str,
    succeeded: str,
    reason: str,
    start_time: str | None = None,
    completion_time: str | None = None,
    steps: list[dict[str, object]] | None = None,
) -> dict[str, object]:
    conditions: list[dict[str, object]] = [
        {"type": "Succeeded", "status": succeeded, "reason": reason, "message": ""}
    ]
    status: dict[str, object] = {"conditions": conditions}
    if start_time:
        status["startTime"] = start_time
    if completion_time:
        status["completionTime"] = completion_time
    if steps:
        status["steps"] = steps
    return {
        "metadata": {"name": name, "labels": {"tekton.dev/pipeline": "build-deploy"}},
        "spec": {"taskRef": {"name": task_ref}},
        "status": status,
    }


class TestVanillaAdapterTektonPort:
    def test_implements_tekton_port(self) -> None:
        adapter = VanillaAdapter("test-cluster")
        assert isinstance(adapter, TektonPort)

    def test_list_task_runs_returns_succeeded_run(self) -> None:
        item = _make_task_run(
            name="build-deploy-clone-repo-abc",
            task_ref="clone-repo",
            succeeded="True",
            reason="Succeeded",
            start_time="2024-01-01T10:00:00Z",
            completion_time="2024-01-01T10:00:12Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert len(result) == 1
        assert result[0]["name"] == "build-deploy-clone-repo-abc"
        assert result[0]["task_ref"] == "clone-repo"
        assert result[0]["status"] == "Succeeded"
        assert result[0]["start_time"] == "2024-01-01T10:00:00Z"
        assert result[0]["duration"] == "12s"
        assert result[0]["failing_step"] is None

    def test_list_task_runs_failed_exposes_step_and_error(self) -> None:
        steps: list[dict[str, object]] = [
            {
                "name": "run-tests",
                "terminated": {"exitCode": 1, "reason": "Error", "message": "exit code 1"},
            }
        ]
        item = _make_task_run(
            name="build-deploy-unit-tests-xyz",
            task_ref="unit-tests",
            succeeded="False",
            reason="Failed",
            start_time="2024-01-01T10:00:15Z",
            completion_time="2024-01-01T10:00:45Z",
            steps=steps,
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["status"] == "Failed"
        assert result[0]["failing_step"] == "run-tests"
        assert result[0]["failing_step_error"] == "exit code 1"

    def test_list_task_runs_timeout_step_shown_as_timeout(self) -> None:
        steps: list[dict[str, object]] = [
            {
                "name": "run-tests",
                "terminated": {"exitCode": 1, "reason": "DeadlineExceeded", "message": ""},
            }
        ]
        item = _make_task_run(
            name="build-deploy-unit-tests-timeout",
            task_ref="unit-tests",
            succeeded="False",
            reason="Failed",
            start_time="2024-01-01T10:00:00Z",
            steps=steps,
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["failing_step_error"] == "Timeout"

    def test_list_task_runs_running_has_no_duration(self) -> None:
        item = _make_task_run(
            name="build-deploy-lint-running",
            task_ref="lint",
            succeeded="Unknown",
            reason="Running",
            start_time="2024-01-01T10:01:00Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["status"] == "Running"
        assert result[0]["duration"] is None

    def test_list_task_runs_raises_pipeline_not_found_when_empty(self) -> None:
        crd_api = _CRDApi([])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        with pytest.raises(PipelineNotFoundError) as exc_info:
            adapter.list_task_runs("ghost-pipeline", "ci")

        assert exc_info.value.pipeline_name == "ghost-pipeline"

    def test_list_task_runs_raises_cluster_unreachable_on_api_error(self) -> None:
        crd_api = MagicMock()
        crd_api.list_namespaced_custom_object.side_effect = Exception("connection refused")
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        with pytest.raises(ClusterUnreachableError):
            adapter.list_task_runs("build-deploy", "ci")

    def test_list_task_runs_filters_by_pipeline_label(self) -> None:
        item = _make_task_run(
            name="build-deploy-clone-repo",
            task_ref="clone-repo",
            succeeded="True",
            reason="Succeeded",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        adapter.list_task_runs("build-deploy", "ci")

        assert "tekton.dev/pipeline=build-deploy" in crd_api.last_label_selector

    def test_list_task_runs_duration_minutes(self) -> None:
        item = _make_task_run(
            name="build-deploy-build-image",
            task_ref="build-image",
            succeeded="True",
            reason="Succeeded",
            start_time="2024-01-01T10:00:00Z",
            completion_time="2024-01-01T10:02:30Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["duration"] == "2m30s"

    def test_list_task_runs_duration_exact_minutes(self) -> None:
        item = _make_task_run(
            name="build-deploy-build-image",
            task_ref="build-image",
            succeeded="True",
            reason="Succeeded",
            start_time="2024-01-01T10:00:00Z",
            completion_time="2024-01-01T10:02:00Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["duration"] == "2m"

    def test_list_task_runs_duration_invalid_timestamps_returns_unknown(self) -> None:
        item: dict[str, object] = {
            "metadata": {"name": "run-abc", "labels": {}},
            "spec": {"taskRef": {"name": "build"}},
            "status": {
                "conditions": [
                    {"type": "Succeeded", "status": "True", "reason": "Succeeded", "message": ""}
                ],
                "startTime": "not-a-date",
                "completionTime": "also-not-a-date",
            },
        }
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["duration"] == "unknown"

    def test_list_task_runs_status_level_timeout_returns_timeout(self) -> None:
        item = _make_task_run(
            name="build-deploy-run-tests-timeout",
            task_ref="run-tests",
            succeeded="False",
            reason="DeadlineExceeded",
            start_time="2024-01-01T10:00:00Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["status"] == "Timeout"

    def test_list_task_runs_missing_spec_yields_unknown_task_ref(self) -> None:
        item: dict[str, object] = {
            "metadata": {"name": "run-abc", "labels": {}},
            "status": {
                "conditions": [
                    {"type": "Succeeded", "status": "True", "reason": "Succeeded", "message": ""}
                ],
            },
        }
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["task_ref"] == "unknown"

    def test_list_task_runs_spec_without_task_ref_yields_unknown(self) -> None:
        item: dict[str, object] = {
            "metadata": {"name": "run-abc", "labels": {}},
            "spec": {},
            "status": {
                "conditions": [
                    {"type": "Succeeded", "status": "True", "reason": "Succeeded", "message": ""}
                ],
            },
        }
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["task_ref"] == "unknown"

    def test_list_task_runs_failed_steps_not_list_returns_no_failing_step(self) -> None:
        item: dict[str, object] = {
            "metadata": {"name": "run-abc", "labels": {}},
            "spec": {"taskRef": {"name": "build"}},
            "status": {
                "conditions": [
                    {"type": "Succeeded", "status": "False", "reason": "Failed", "message": ""}
                ],
                "steps": "not-a-list",
            },
        }
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["failing_step"] is None

    def test_list_task_runs_step_without_terminated_is_skipped(self) -> None:
        steps: list[dict[str, object]] = [
            {"name": "setup", "running": {}},
            {
                "name": "run-tests",
                "terminated": {"exitCode": 1, "reason": "Error", "message": "fail"},
            },
        ]
        item = _make_task_run(
            name="run-abc",
            task_ref="run-tests",
            succeeded="False",
            reason="Failed",
            steps=steps,
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["failing_step"] == "run-tests"

    def test_list_task_runs_step_error_without_message_uses_exit_code(self) -> None:
        steps: list[dict[str, object]] = [
            {"name": "run-tests", "terminated": {"exitCode": 2, "reason": "Error", "message": ""}},
        ]
        item = _make_task_run(
            name="run-abc",
            task_ref="run-tests",
            succeeded="False",
            reason="Failed",
            steps=steps,
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_task_runs("build-deploy", "ci")

        assert result[0]["failing_step_error"] == "exit code 2"

    def test_list_task_runs_invalid_crd_response_raises_pipeline_not_found(self) -> None:
        crd_api = MagicMock()
        crd_api.list_namespaced_custom_object.return_value = "not-a-dict"
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        with pytest.raises(PipelineNotFoundError):
            adapter.list_task_runs("build-deploy", "ci")

    def test_crd_api_client_creates_custom_objects_api_when_not_injected(self) -> None:
        from unittest.mock import patch as _patch

        from kubernetes import client as k8s_client

        mock_crd = MagicMock()
        adapter = VanillaAdapter("test-cluster")
        with (
            _patch.object(adapter, "_api_client"),
            _patch.object(k8s_client, "CustomObjectsApi", return_value=mock_crd),
        ):
            result = adapter._crd_api_client()

        assert result is mock_crd


def _make_pipeline_run(
    name: str,
    succeeded: str,
    reason: str,
    start_time: str | None = None,
    completion_time: str | None = None,
    annotations: dict[str, str] | None = None,
    labels: dict[str, str] | None = None,
) -> dict[str, object]:
    conditions: list[dict[str, object]] = [
        {"type": "Succeeded", "status": succeeded, "reason": reason, "message": ""}
    ]
    status: dict[str, object] = {"conditions": conditions}
    if start_time:
        status["startTime"] = start_time
    if completion_time:
        status["completionTime"] = completion_time
    metadata: dict[str, object] = {"name": name}
    if annotations:
        metadata["annotations"] = annotations
    if labels:
        metadata["labels"] = labels
    return {"metadata": metadata, "status": status}


class TestVanillaAdapterListPipelineRuns:
    def test_returns_succeeded_run(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-abc",
            succeeded="True",
            reason="Succeeded",
            start_time="2024-01-15T10:00:00Z",
            completion_time="2024-01-15T10:04:30Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert len(result) == 1
        assert result[0]["name"] == "payment-service-run-abc"
        assert result[0]["status"] == "Succeeded"
        assert result[0]["start_time"] == "2024-01-15T10:00:00Z"
        assert result[0]["duration"] == "4m30s"
        assert result[0]["duration_seconds"] == 270

    def test_returns_failed_run(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-xyz",
            succeeded="False",
            reason="Failed",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["status"] == "Failed"

    def test_returns_cancelled_run(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-cancel",
            succeeded="False",
            reason="PipelineRunCancelled",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["status"] == "Cancelled"

    def test_returns_running_run(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-running",
            succeeded="Unknown",
            reason="Running",
            start_time="2024-01-15T10:00:00Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["status"] == "Running"
        assert result[0]["duration"] is None
        assert result[0]["duration_seconds"] is None

    def test_triggered_by_from_pac_annotation(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-abc",
            succeeded="True",
            reason="Succeeded",
            annotations={"pipelinesascode.tekton.dev/sender": "john.doe"},
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["triggered_by"] == "john.doe"

    def test_triggered_by_falls_back_to_event_listener_label(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-abc",
            succeeded="True",
            reason="Succeeded",
            labels={"triggers.tekton.dev/eventlistener": "github-push"},
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["triggered_by"] == "github-push"

    def test_triggered_by_is_none_when_no_metadata(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-abc",
            succeeded="True",
            reason="Succeeded",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["triggered_by"] is None

    def test_raises_service_not_found_when_empty(self) -> None:
        from hexawyn.domain.errors import ServiceNotFoundError

        crd_api = _CRDApi([])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        with pytest.raises(ServiceNotFoundError) as exc_info:
            adapter.list_pipeline_runs("ghost-service", "ci")

        assert exc_info.value.service_name == "ghost-service"

    def test_raises_cluster_unreachable_on_api_error(self) -> None:
        crd_api = MagicMock()
        crd_api.list_namespaced_custom_object.side_effect = Exception("connection refused")
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        with pytest.raises(ClusterUnreachableError):
            adapter.list_pipeline_runs("payment-service", "ci")

    def test_filters_by_pipeline_label(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-abc",
            succeeded="True",
            reason="Succeeded",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        adapter.list_pipeline_runs("payment-service", "ci")

        assert "tekton.dev/pipeline=payment-service" in crd_api.last_label_selector

    def test_duration_exact_minutes(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-abc",
            succeeded="True",
            reason="Succeeded",
            start_time="2024-01-15T10:00:00Z",
            completion_time="2024-01-15T10:03:00Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["duration"] == "3m"
        assert result[0]["duration_seconds"] == 180

    def test_duration_under_sixty_seconds(self) -> None:
        item = _make_pipeline_run(
            name="payment-service-run-fast",
            succeeded="True",
            reason="Succeeded",
            start_time="2024-01-15T10:00:00Z",
            completion_time="2024-01-15T10:00:45Z",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["duration"] == "45s"
        assert result[0]["duration_seconds"] == 45

    def test_invalid_timestamps_yield_none_duration(self) -> None:
        item: dict[str, object] = {
            "metadata": {"name": "payment-run-bad"},
            "status": {
                "conditions": [
                    {"type": "Succeeded", "status": "True", "reason": "Succeeded", "message": ""}
                ],
                "startTime": "not-a-date",
                "completionTime": "also-invalid",
            },
        }
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["duration"] is None
        assert result[0]["duration_seconds"] is None

    def test_status_none_returns_not_started(self) -> None:
        item: dict[str, object] = {
            "metadata": {"name": "payment-run-no-status"},
        }
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["status"] == "NotStarted"

    def test_empty_conditions_returns_not_started(self) -> None:
        item: dict[str, object] = {
            "metadata": {"name": "payment-run-pending"},
            "status": {"conditions": []},
        }
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["status"] == "NotStarted"

    def test_non_mapping_condition_returns_not_started(self) -> None:
        item: dict[str, object] = {
            "metadata": {"name": "payment-run-bad-cond"},
            "status": {"conditions": ["not-a-dict"]},
        }
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["status"] == "NotStarted"

    def test_unknown_status_non_running_reason_returns_not_started(self) -> None:
        item = _make_pipeline_run(
            name="payment-run-pending",
            succeeded="Unknown",
            reason="PipelineRunPending",
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["status"] == "NotStarted"

    def test_triggered_by_falls_back_to_label_when_annotation_empty(self) -> None:
        item = _make_pipeline_run(
            name="payment-run-abc",
            succeeded="True",
            reason="Succeeded",
            annotations={"pipelinesascode.tekton.dev/sender": ""},
            labels={"triggers.tekton.dev/eventlistener": "github-push"},
        )
        crd_api = _CRDApi([item])
        adapter = VanillaAdapter("test-cluster", crd_api=crd_api)

        result = adapter.list_pipeline_runs("payment-service", "ci")

        assert result[0]["triggered_by"] == "github-push"
