from collections.abc import Mapping, Sequence
from time import monotonic
from typing import Protocol, cast

from kubernetes import client

from hexawyn.application.ports.driven.cost_forecast_port import (
    CostForecastPort,
    DailyCostData,
    NamespaceCostData,
)
from hexawyn.application.ports.driven.k8s_port import (
    ClusterContext,
    ClusterHealthPort,
    ClusterMetrics,
    Finding,
    K8sPort,
    NamespaceInfo,
    PodInfo,
)
from hexawyn.application.ports.driven.namespace_waste_port import (
    NamespaceRawData,
    NamespaceWasteAnalysisPort,
)
from hexawyn.application.ports.driven.rightsizing_port import (
    RightsizingPort,
    WorkloadRawData,
)
from hexawyn.application.ports.driven.tekton_port import (
    NamespacedPipelineRunInfo,
    PipelineRunInfo,
    TaskRunInfo,
    TektonPort,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    PipelineNotFoundError,
    PrometheusUnavailableError,
    ServiceNotFoundError,
    TektonNotInstalledError,
)
from hexawyn.infrastructure.config.kubeconfig_reader import load_kubeconfig

_HEALTHY_POD_STATUSES = {"Running", "Succeeded"}
_POD_CACHE_TTL_SECONDS = 5.0

_TEKTON_GROUP = "tekton.dev"
_TEKTON_VERSION = "v1"
_TEKTON_TASKRUNS_PLURAL = "taskruns"
_TEKTON_PIPELINERUNS_PLURAL = "pipelineruns"


class KubernetesCoreApi(Protocol):
    def list_pod_for_all_namespaces(self, timeout_seconds: int) -> object:
        """List pods across all namespaces."""

    def list_namespaced_pod(self, namespace: str, timeout_seconds: int) -> object:
        """List pods in a namespace."""

    def list_node(self, timeout_seconds: int) -> object:
        """List cluster nodes."""

    def list_namespace(self, timeout_seconds: int) -> object:
        """List all namespaces."""


class KubernetesAppsApi(Protocol):
    def list_deployment_for_all_namespaces(self, timeout_seconds: int) -> object:
        """List all deployments across namespaces."""

    def list_stateful_set_for_all_namespaces(self, timeout_seconds: int) -> object:
        """List all stateful sets across namespaces."""


class KubernetesMetricsApi(Protocol):
    def list_cluster_custom_object(self, group: str, version: str, plural: str) -> object:
        """List cluster-scoped custom objects."""


class KubernetesCRDApi(Protocol):
    def list_namespaced_custom_object(
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        label_selector: str = "",
    ) -> object:
        """List namespace-scoped custom objects."""


_CPU_MILLI_FACTOR = 1000.0
_MEM_GIB_FACTOR = 1024**3
_K8S_TIMEOUT = 10
_PROMETHEUS_QUERY_TIMEOUT = 15.0

_CPU_REQUEST_QUERY = "sum by (namespace) (kube_pod_container_resource_requests{{resource='cpu'}})"
_MEM_REQUEST_QUERY = (
    "sum by (namespace) (kube_pod_container_resource_requests{{resource='memory'}})"
)
_CPU_USAGE_QUERY = (
    "avg_over_time("
    "sum by (namespace) (rate(container_cpu_usage_seconds_total{{container!=''}}[5m]))"
    "[{window}d:1h])"
)
_MEM_USAGE_QUERY = (
    "avg_over_time("
    "sum by (namespace) (container_memory_working_set_bytes{{container!=''}})"
    "[{window}d:1h])"
)


_METRICS_GROUP = "metrics.k8s.io"
_METRICS_VERSION = "v1beta1"
_METRICS_PODS_PLURAL = "pods"
_NANOCORES_FACTOR = 1_000_000_000.0
_BYTES_TO_MI = 1024.0 * 1024.0


class VanillaAdapter(
    K8sPort,
    ClusterHealthPort,
    TektonPort,
    NamespaceWasteAnalysisPort,
    RightsizingPort,
    CostForecastPort,
):
    """Minimal adapter for vanilla Kubernetes with no cloud provider dependencies."""

    def __init__(
        self,
        cluster_name: str,
        api: KubernetesCoreApi | None = None,
        metrics_api: KubernetesMetricsApi | None = None,
        crd_api: KubernetesCRDApi | None = None,
        apps_api: KubernetesAppsApi | None = None,
        prometheus_url: str = "",
    ) -> None:
        self._cluster_name = cluster_name
        self._api = api
        self._metrics_api = metrics_api
        self._crd_api = crd_api
        self._apps_api = apps_api
        self._prometheus_url = prometheus_url
        self._pod_cache: list[PodInfo] | None = None
        self._pod_cache_updated_at = 0.0

    # ── K8sPort ───────────────────────────────────────────────

    def list_pods(self, namespace: str | None = None) -> list[PodInfo]:
        if namespace is None and self._pod_cache_is_fresh():
            return list(self._pod_cache or [])

        pod_list = self._list_kubernetes_pods(namespace)
        pods = [self._to_pod_info(pod) for pod in self._items_from(pod_list)]
        if namespace is None:
            self._refresh_pod_cache(pods)
        return pods

    def get_cluster_metrics(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = self._items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": self._percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": self._percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def get_cluster_context(self) -> ClusterContext:
        return {
            "name": self._cluster_name,
            "cluster": self._cluster_name,
            "provider": self._provider_name(),
            "namespace": "default",
        }

    def list_namespaces(self) -> list[NamespaceInfo]:
        api = self._api_client()
        ns_list = api.list_namespace(timeout_seconds=5)
        return [self._to_namespace_info(ns) for ns in self._items_from(ns_list)]

    # ── ClusterHealthPort ─────────────────────────────────────

    def get_findings(self) -> list[Finding]:
        return [*self._pod_findings(), *self._node_findings()]

    def get_health_score(self) -> int:
        findings = self.get_findings()
        critical_count = self._severity_count(findings, "critical")
        warning_count = self._severity_count(findings, "warning")
        return max(0, 100 - critical_count * 30 - warning_count * 10)

    def get_health_status(self) -> str:
        findings = self.get_findings()
        if self._severity_count(findings, "critical") > 0:
            return "critical"
        if self._severity_count(findings, "warning") > 0:
            return "degraded"
        return "healthy"

    # ── TektonPort ────────────────────────────────────────────

    def list_task_runs(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        raw = self._fetch_task_runs(pipeline_name, namespace)
        items = self._crd_items(raw)
        if not items:
            raise PipelineNotFoundError(pipeline_name=pipeline_name)
        return [self._to_task_run_info(item) for item in items]

    def list_pipeline_runs(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        raw = self._fetch_pipeline_runs(service_name, namespace)
        items = self._crd_items(raw)
        if not items:
            raise ServiceNotFoundError(service_name=service_name)
        return [self._to_pipeline_run_info(item) for item in items]

    def list_pipeline_runs_in_namespace(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        raw = self._fetch_pipeline_runs_in_namespace(namespace)
        items = self._crd_items(raw)
        return [self._to_namespaced_pipeline_run_info(item) for item in items]

    def _fetch_pipeline_runs_in_namespace(self, namespace: str) -> object:
        from kubernetes.client.exceptions import ApiException

        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:
                raise TektonNotInstalledError() from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def _to_namespaced_pipeline_run_info(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))

        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)

        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def _extract_pipeline_ref(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def _fetch_pipeline_runs(self, service_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={service_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def _to_pipeline_run_info(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))

        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)

        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def _pipeline_run_status(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def _pipeline_run_duration_seconds(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        from datetime import datetime

        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def _seconds_to_human(self, seconds: int | None) -> str | None:
        if seconds is None:
            return None
        if seconds >= 60:
            minutes, remaining = divmod(seconds, 60)
            return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
        return f"{seconds}s"

    def _extract_triggered_by(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def _fetch_task_runs(self, pipeline_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_TASKRUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={pipeline_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def _to_task_run_info(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))

        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)

        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def _extract_task_ref(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(task_ref, "name", "unknown")
        return "unknown"

    def _task_run_status(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def _task_run_duration(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is None:
            return None
        completion_time = self._crd_optional_str(status, "completionTime")
        if completion_time is None:
            return None
        return self._elapsed_between(start_time, completion_time)

    def _extract_failing_step(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def _step_error(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def _elapsed_between(self, start: str, end: str) -> str:
        from datetime import datetime

        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def _crd_items(self, raw: object) -> list[Mapping[str, object]]:
        mapping = self._crd_mapping(raw)
        if mapping is None:
            return []
        items = mapping.get("items", [])
        if not isinstance(items, list):
            return []
        return [item for item in items if isinstance(item, Mapping)]

    def _crd_mapping(self, value: object) -> Mapping[str, object] | None:
        if isinstance(value, Mapping):
            return cast(Mapping[str, object], value)
        return None

    def _crd_str(
        self,
        data: Mapping[str, object] | None,
        key: str,
        default: str = "",
    ) -> str:
        if data is None:
            return default
        value = data.get(key, default)
        return value if isinstance(value, str) else default

    def _crd_optional_str(
        self,
        data: Mapping[str, object] | None,
        key: str,
    ) -> str | None:
        if data is None:
            return None
        value = data.get(key)
        return value if isinstance(value, str) else None

    def _crd_api_client(self) -> KubernetesCRDApi:
        if self._crd_api is None:
            self._api_client()
            self._crd_api = cast(KubernetesCRDApi, client.CustomObjectsApi())
        return self._crd_api

    # ── Namespace parsing ─────────────────────────────────────

    def _to_namespace_info(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = self._text_attr(metadata, "name", "unknown")
        status = self._text_attr(getattr(ns, "status", None), "phase", "Active")
        age = self._namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def _namespace_age(self, metadata: object) -> str:
        from datetime import UTC, datetime

        timestamp = getattr(metadata, "creation_timestamp", None)
        if timestamp is None:
            return "unknown"
        now = datetime.now(UTC)
        delta = now - timestamp
        days = delta.days
        if days > 0:
            return f"{days}d"
        hours = delta.seconds // 3600
        if hours > 0:
            return f"{hours}h"
        minutes = delta.seconds // 60
        return f"{minutes}m"

    def _pod_age(self, metadata: object) -> str:
        return self._namespace_age(metadata)

    def _provider_name(self) -> str:
        if self._cluster_name.startswith("kind-"):
            return "kind"
        return "vanilla"

    def _list_kubernetes_pods(self, namespace: str | None) -> object:
        api = self._api_client()
        if namespace:
            return api.list_namespaced_pod(namespace=namespace, timeout_seconds=5)
        return api.list_pod_for_all_namespaces(timeout_seconds=5)

    def _api_client(self) -> KubernetesCoreApi:
        if self._api is None:
            self._api = cast(KubernetesCoreApi, load_kubeconfig(context=self._context_name()))
        return self._api

    def _context_name(self) -> str | None:
        return None if self._cluster_name == "unknown" else self._cluster_name

    def _pod_cache_is_fresh(self) -> bool:
        cache_age_seconds = monotonic() - self._pod_cache_updated_at
        return self._pod_cache is not None and cache_age_seconds <= _POD_CACHE_TTL_SECONDS

    def _refresh_pod_cache(self, pods: list[PodInfo]) -> None:
        self._pod_cache = list(pods)
        self._pod_cache_updated_at = monotonic()

    def _metrics_api_client(self) -> KubernetesMetricsApi:
        if self._metrics_api is None:
            self._api_client()
            self._metrics_api = cast(KubernetesMetricsApi, client.CustomObjectsApi())
        return self._metrics_api

    def _to_pod_info(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        return {
            "name": self._text_attr(metadata, "name", "unknown"),
            "namespace": self._text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": self._restart_count(status),
            "age": self._pod_age(metadata),
            "node": self._text_attr(spec, "node_name", "unknown"),
        }

    def _pod_status(self, status: object) -> str:
        waiting_reason = self._waiting_reason(status)
        if waiting_reason:
            return waiting_reason
        return self._text_attr(status, "phase", "Unknown")

    def _pod_findings(self) -> list[Finding]:
        findings: list[Finding] = []
        for pod in self.list_pods():
            if pod["status"] not in _HEALTHY_POD_STATUSES:
                findings.append(self._unhealthy_pod_finding(pod))
            elif pod["restarts"] > 0:
                findings.append(self._restarted_pod_finding(pod))
        return findings

    def _node_findings(self) -> list[Finding]:
        findings: list[Finding] = []
        for node in self._node_items():
            if not self._node_is_ready(node):
                findings.append(self._not_ready_node_finding(node))
        return findings

    def _unhealthy_pod_finding(self, pod: PodInfo) -> Finding:
        return {
            "severity": "critical" if pod["status"] == "CrashLoop" else "warning",
            "message": f"Pod {pod['namespace']}/{pod['name']} is {pod['status']}",
            "remediation": self._pod_remediation(pod["status"]),
        }

    def _restarted_pod_finding(self, pod: PodInfo) -> Finding:
        return {
            "severity": "warning",
            "message": f"Pod {pod['namespace']}/{pod['name']} restarted {pod['restarts']} times",
            "remediation": "Inspect recent logs and events for this pod.",
        }

    def _not_ready_node_finding(self, node: object) -> Finding:
        node_name = self._text_attr(getattr(node, "metadata", None), "name", "unknown")
        return {
            "severity": "critical",
            "message": f"Node {node_name} is NotReady",
            "remediation": "Inspect node conditions, kubelet status, and recent node events.",
        }

    def _pod_remediation(self, status: str) -> str:
        if status == "CrashLoop":
            return "Inspect container logs, probes, image pull errors, and recent rollout changes."
        if status == "Pending":
            return "Check scheduling events, resource requests, and node capacity."
        return "Inspect pod events and container state for the reported status."

    def _node_is_ready(self, node: object) -> bool:
        node_status = getattr(node, "status", None)
        for condition in self._conditions(node_status):
            if self._text_attr(condition, "type", "") == "Ready":
                return self._text_attr(condition, "status", "False") == "True"
        return False

    def _node_items(self) -> list[object]:
        return self._items_from(self._api_client().list_node(timeout_seconds=5))

    def _node_metrics_usage(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                group="metrics.k8s.io",
                version="v1beta1",
                plural="nodes",
            )
        except Exception:
            return 0.0, 0.0
        return self._sum_node_metrics(metrics)

    def _sum_node_metrics(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in self._metric_items(metrics):
            usage = self._mapping(metric.get("usage"))
            if usage is not None:
                cpu_usage += self._cpu_to_cores(self._mapping_text(usage, "cpu"))
                memory_usage += self._memory_to_bytes(self._mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def _cpu_capacity(self, nodes: list[object]) -> float:
        return sum(self._node_allocatable_cpu(node) for node in nodes)

    def _memory_capacity(self, nodes: list[object]) -> float:
        return sum(self._node_allocatable_memory(node) for node in nodes)

    def _node_allocatable_cpu(self, node: object) -> float:
        allocatable = self._node_allocatable(node)
        return self._cpu_to_cores(self._mapping_text(allocatable, "cpu"))

    def _node_allocatable_memory(self, node: object) -> float:
        allocatable = self._node_allocatable(node)
        return self._memory_to_bytes(self._mapping_text(allocatable, "memory"))

    def _node_allocatable(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", None)
        allocatable = getattr(node_status, "allocatable", {})
        mapping = self._mapping(allocatable)
        return mapping if mapping is not None else {}

    def _waiting_reason(self, status: object) -> str | None:
        for container_status in self._container_statuses(status):
            state = getattr(container_status, "state", None)
            waiting = getattr(state, "waiting", None)
            reason = self._optional_text_attr(waiting, "reason")
            if reason:
                return "CrashLoop" if reason == "CrashLoopBackOff" else reason
        return None

    def _restart_count(self, status: object) -> int:
        return sum(
            self._integer_attr(container_status, "restart_count")
            for container_status in self._container_statuses(status)
        )

    def _conditions(self, status: object) -> list[object]:
        conditions = getattr(status, "conditions", [])
        return self._object_sequence(conditions)

    def _container_statuses(self, status: object) -> list[object]:
        container_statuses = getattr(status, "container_statuses", [])
        return self._object_sequence(container_statuses)

    def _items_from(self, item_list: object) -> list[object]:
        items = getattr(item_list, "items", [])
        return self._object_sequence(items)

    def _metric_items(self, metrics: object) -> list[Mapping[object, object]]:
        mapping = self._mapping(metrics)
        if mapping is None:
            return []
        items = mapping.get("items", [])
        return [item for item in self._object_sequence(items) if isinstance(item, Mapping)]

    def _object_sequence(self, value: object) -> list[object]:
        if isinstance(value, Sequence) and not isinstance(value, str | bytes):
            return list(cast(Sequence[object], value))
        return []

    def _mapping(self, value: object) -> Mapping[object, object] | None:
        return value if isinstance(value, Mapping) else None

    def _mapping_text(self, mapping: Mapping[object, object], key: str) -> str:
        value = mapping.get(key, "")
        return value if isinstance(value, str) else ""

    def _text_attr(self, source: object, attr_name: str, default: str) -> str:
        value = self._optional_text_attr(source, attr_name)
        return value if value is not None else default

    def _optional_text_attr(self, source: object, attr_name: str) -> str | None:
        value = getattr(source, attr_name, None)
        if isinstance(value, str) and value:
            return value
        return None

    def _integer_attr(self, source: object, attr_name: str) -> int:
        value = getattr(source, attr_name, 0)
        return value if isinstance(value, int) else 0

    def _cpu_to_cores(self, value: str) -> float:
        if value.endswith("n"):
            return self._float_prefix(value, "n") / 1_000_000_000
        if value.endswith("u"):
            return self._float_prefix(value, "u") / 1_000_000
        if value.endswith("m"):
            return self._float_prefix(value, "m") / 1_000
        return self._safe_float(value)

    def _memory_to_bytes(self, value: str) -> float:
        multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
        for suffix, multiplier in multipliers.items():
            if value.endswith(suffix):
                return self._float_prefix(value, suffix) * multiplier
        return self._safe_float(value)

    def _float_prefix(self, value: str, suffix: str) -> float:
        return self._safe_float(value[: -len(suffix)])

    def _safe_float(self, value: str) -> float:
        try:
            return float(value)
        except ValueError:
            return 0.0

    def _percentage(self, used: float, capacity: float) -> float:
        if capacity <= 0:
            return 0.0
        return round((used / capacity) * 100, 2)

    def _severity_count(self, findings: list[Finding], severity: str) -> int:
        return sum(1 for finding in findings if finding["severity"] == severity)

    # ── NamespaceWasteAnalysisPort ────────────────────────────

    def get_all_namespace_waste_data(self, window_days: int) -> list[NamespaceRawData]:
        namespace_ages = self._fetch_namespace_ages()
        cpu_requests = self._fetch_k8s_resource_requests("cpu")
        mem_requests = self._fetch_k8s_resource_requests("memory")
        cpu_usage = self._fetch_prometheus_usage(_CPU_USAGE_QUERY.format(window=window_days))
        mem_usage = self._fetch_prometheus_usage(_MEM_USAGE_QUERY.format(window=window_days))

        all_namespaces = namespace_ages.keys() | cpu_requests.keys() | mem_requests.keys()
        return [
            self._build_namespace_raw_data(
                ns, namespace_ages, cpu_requests, mem_requests, cpu_usage, mem_usage
            )
            for ns in sorted(all_namespaces)
        ]

    def _build_namespace_raw_data(
        self,
        namespace: str,
        ages: dict[str, float],
        cpu_req: dict[str, float],
        mem_req: dict[str, float],
        cpu_usage: dict[str, float],
        mem_usage: dict[str, float],
    ) -> NamespaceRawData:
        cpu_requested = cpu_req.get(namespace)
        mem_requested = mem_req.get(namespace)
        return {
            "namespace": namespace,
            "cpu_requested_cores": cpu_requested,
            "memory_requested_gb": mem_requested,
            "cpu_actual_avg_cores": cpu_usage.get(namespace),
            "memory_actual_avg_gb": mem_usage.get(namespace),
            "age_hours": ages.get(namespace, 999.0),
            "has_resource_requests": cpu_requested is not None or mem_requested is not None,
        }

    def _fetch_namespace_ages(self) -> dict[str, float]:
        from datetime import UTC, datetime

        try:
            raw = self._core_api().list_namespace(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list namespaces: {exc}") from exc

        ages: dict[str, float] = {}
        for item in self._items_from(raw):
            meta = getattr(item, "metadata", None)
            if meta is None:
                continue
            name = getattr(meta, "name", None) or ""
            creation = getattr(meta, "creation_timestamp", None)
            if name and creation:
                elapsed = (datetime.now(UTC) - creation).total_seconds()
                ages[name] = elapsed / 3600.0
        return ages

    def _fetch_k8s_resource_requests(self, resource: str) -> dict[str, float]:
        try:
            raw = self._core_api().list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods: {exc}") from exc

        totals: dict[str, float] = {}
        for pod in self._items_from(raw):
            namespace = _pod_namespace(pod)
            if not namespace:
                continue
            for container in _pod_containers(pod):
                value = _container_request(container, resource)
                if value is not None:
                    totals[namespace] = totals.get(namespace, 0.0) + value
        return totals

    def _fetch_prometheus_usage(self, query: str) -> dict[str, float]:
        if not self._prometheus_url:
            return {}
        import httpx

        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._prometheus_url) from exc
        except Exception as exc:
            raise PrometheusUnavailableError(self._prometheus_url) from exc

        return _parse_prometheus_vector(resp.json())

    def _core_api(self) -> KubernetesCoreApi:
        if self._api is not None:
            return self._api
        load_kubeconfig()
        return cast(KubernetesCoreApi, client.CoreV1Api())

    # ── RightsizingPort ──────────────────────────────────────────

    def get_workload_rightsizing_data(self) -> list[WorkloadRawData]:
        deployments = self._fetch_deployments()
        pod_metrics = self._fetch_pod_metrics_by_workload()
        return [
            self._build_workload_raw_data(dep, "Deployment", pod_metrics) for dep in deployments
        ]

    def _fetch_deployments(self) -> list[object]:
        try:
            raw = self._apps_api_client().list_deployment_for_all_namespaces(
                timeout_seconds=_K8S_TIMEOUT
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list deployments: {exc}") from exc
        return list(self._items_from(raw))

    def _fetch_pod_metrics_by_workload(self) -> dict[str, dict[str, float]]:
        """Returns {namespace/workload-prefix: {cpu_cores, memory_mi}}."""
        try:
            raw = self._metrics_api_client().list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}

        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def _build_workload_raw_data(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)

        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count

        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def _apps_api_client(self) -> KubernetesAppsApi:
        if self._apps_api is not None:
            return self._apps_api
        load_kubeconfig()
        return cast(KubernetesAppsApi, client.AppsV1Api())

    # ── CostForecastPort ─────────────────────────────────────

    def get_daily_costs(self, days: int) -> list[DailyCostData]:
        """Estimate daily cluster cost from K8s resource requests.

        Returns `days` data points all with the same estimated daily rate
        (Free tier — no real billing history, trend_factor will be 1.0).
        """
        try:
            raw = self._apps_api_client().list_deployment_for_all_namespaces(
                timeout_seconds=_K8S_TIMEOUT
            )
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc

        deployments = list(self._items_from(raw))
        ns_daily_costs = _compute_namespace_daily_costs(deployments)
        total_daily = sum(ns_daily_costs.values())
        return _build_daily_cost_entries(ns_daily_costs, total_daily, days)


_CPU_COST_PER_CORE_DAY = 21.6 / 30.0  # $21.6/core/month ÷ 30
_MEM_COST_PER_GIB_DAY = 2.88 / 30.0  # $2.88/GiB/month ÷ 30


def _compute_namespace_daily_costs(deployments: list[object]) -> dict[str, float]:
    """Returns {namespace: daily_cost_usd} from deployment resource requests."""
    ns_costs: dict[str, float] = {}
    for dep in deployments:
        meta = getattr(dep, "metadata", None)
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_cores, mem_mi = _workload_resource_requests(dep)
        mem_gib = mem_mi / 1024.0
        daily = cpu_cores * _CPU_COST_PER_CORE_DAY + mem_gib * _MEM_COST_PER_GIB_DAY
        ns_costs[namespace] = ns_costs.get(namespace, 0.0) + daily
    return ns_costs


def _build_daily_cost_entries(
    ns_costs: dict[str, float],
    total_daily: float,
    days: int,
) -> list[DailyCostData]:
    from datetime import date, timedelta

    today = date.today()
    ns_list: list[NamespaceCostData] = [
        NamespaceCostData(name=ns, cost_usd=round(cost, 4))
        for ns, cost in sorted(ns_costs.items(), key=lambda x: x[1], reverse=True)
    ]
    return [
        DailyCostData(
            date=(today - timedelta(days=days - 1 - i)).strftime("%Y-%m-%d"),
            total_usd=round(total_daily, 4),
            namespace_costs=ns_list,
        )
        for i in range(days)
    ]


def _workload_resource_requests(workload: object) -> tuple[float, float]:
    """Returns (cpu_cores, memory_mi) summed across all containers in the pod template."""
    spec = getattr(workload, "spec", None)
    template = getattr(spec, "template", None) if spec else None
    pod_spec = getattr(template, "spec", None) if template else None
    containers = list(getattr(pod_spec, "containers", None) or []) if pod_spec else []
    cpu_total = 0.0
    mem_total_mi = 0.0
    for container in containers:
        cpu = _container_request(container, "cpu")
        mem_gib = _container_request(container, "memory")
        if cpu is not None:
            cpu_total += cpu
        if mem_gib is not None:
            mem_total_mi += mem_gib * 1024.0
    return cpu_total, mem_total_mi


def _sum_container_metrics(containers: object) -> tuple[float, float]:
    """Returns (cpu_cores, memory_mi) summed from metrics-server container list."""
    if not isinstance(containers, list):
        return 0.0, 0.0
    cpu_total = 0.0
    mem_total_mi = 0.0
    for container in containers:
        if not isinstance(container, dict):
            continue
        usage = container.get("usage", {})
        if not isinstance(usage, dict):
            continue
        cpu_raw = str(usage.get("cpu", "0"))
        mem_raw = str(usage.get("memory", "0"))
        cpu_total += _parse_nanocores(cpu_raw)
        mem_total_mi += _parse_memory_to_mi(mem_raw)
    return cpu_total, mem_total_mi


def _parse_nanocores(value: str) -> float:
    if value.endswith("n"):
        return float(value[:-1]) / _NANOCORES_FACTOR
    if value.endswith("m"):
        return float(value[:-1]) / _CPU_MILLI_FACTOR
    return float(value)


def _parse_memory_to_mi(value: str) -> float:
    """Parse K8s memory string to MiB."""
    for suffix, factor in (
        ("Ki", 1.0 / 1024.0),
        ("Mi", 1.0),
        ("Gi", 1024.0),
        ("Ti", 1024.0 * 1024.0),
        ("K", 1000.0 / (1024.0 * 1024.0)),
        ("M", 1000.0 * 1000.0 / (1024.0 * 1024.0)),
        ("G", 1000.0 * 1000.0 * 1000.0 / (1024.0 * 1024.0)),
    ):
        if value.endswith(suffix):
            return float(value[: -len(suffix)]) * factor
    return float(value) / _BYTES_TO_MI


def _workload_key_from_pod_name(pod_name: str, namespace: str) -> str | None:
    """Extracts workload name from pod name using ReplicaSet suffix convention.

    Pod names follow the pattern: {deployment-name}-{rs-hash}-{pod-hash}
    We strip the last two dash-separated suffixes to get the deployment name.
    """
    parts = pod_name.rsplit("-", 2)
    if len(parts) >= 3:
        workload_name = parts[0]
        return f"{namespace}/{workload_name}"
    if len(parts) == 2:
        return f"{namespace}/{parts[0]}"
    return None


def _pod_namespace(pod: object) -> str:
    meta = getattr(pod, "metadata", None)
    return str(getattr(meta, "namespace", "") or "") if meta else ""


def _pod_containers(pod: object) -> list[object]:
    spec = getattr(pod, "spec", None)
    if spec is None:
        return []
    return list(getattr(spec, "containers", None) or [])


def _container_request(container: object, resource: str) -> float | None:
    resources = getattr(container, "resources", None)
    if resources is None:
        return None
    requests = getattr(resources, "requests", None)
    if not isinstance(requests, dict) or resource not in requests:
        return None
    raw = requests[resource]
    if resource == "cpu":
        return _parse_cpu(str(raw))
    if resource == "memory":
        return _parse_memory(str(raw))
    return None


def _parse_cpu(value: str) -> float:
    if value.endswith("m"):
        return float(value[:-1]) / _CPU_MILLI_FACTOR
    return float(value)


def _parse_memory(value: str) -> float:
    for suffix, factor in (
        ("Gi", 1.0),
        ("Mi", 1.0 / 1024),
        ("Ki", 1.0 / (1024**2)),
        ("G", 1.0 / 1.073741824),
        ("M", 1.0 / (1.073741824 * 1024)),
        ("K", 1.0 / (1.073741824 * 1024**2)),
    ):
        if value.endswith(suffix):
            return float(value[: -len(suffix)]) * factor
    return float(value) / _MEM_GIB_FACTOR


def _parse_prometheus_vector(payload: dict[str, object]) -> dict[str, float]:
    result: dict[str, float] = {}
    data = payload.get("data") if isinstance(payload, dict) else None
    if not isinstance(data, dict):
        return result
    result_list = data.get("result")
    if not isinstance(result_list, list):
        return result
    for entry in result_list:
        if not isinstance(entry, dict):
            continue
        metric = entry.get("metric")
        value_pair = entry.get("value")
        if not isinstance(metric, dict) or not isinstance(value_pair, list):
            continue
        namespace = metric.get("namespace")
        if not isinstance(namespace, str) or len(value_pair) < 2:
            continue
        try:
            result[namespace] = float(str(value_pair[1]))
        except (ValueError, TypeError):
            continue
    return result
