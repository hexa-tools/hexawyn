# mypy: ignore-errors
from typing import cast

from kubernetes import client

from hexawyn.adapters.secondary.vanilla.adapters.cost_forecast_adapter import (
    VanillaCostForecastAdapter,
)
from hexawyn.adapters.secondary.vanilla.adapters.cost_saving_estimation_adapter import (
    VanillaCostSavingAdapter,
)
from hexawyn.adapters.secondary.vanilla.adapters.health_adapter import (
    VanillaHealthAdapter,
)
from hexawyn.adapters.secondary.vanilla.adapters.k8s_adapter import (
    VanillaK8sAdapter,
)
from hexawyn.adapters.secondary.vanilla.adapters.namespace_waste_adapter import (
    VanillaNamespaceWasteAdapter,
)
from hexawyn.adapters.secondary.vanilla.adapters.pod_metrics_adapter import (
    VanillaPodMetricsAdapter,
)
from hexawyn.adapters.secondary.vanilla.adapters.rightsizing_adapter import (
    VanillaRightsizingAdapter,
)
from hexawyn.adapters.secondary.vanilla.adapters.tekton_adapter import (
    VanillaTektonAdapter,
)
from hexawyn.adapters.secondary.vanilla.adapters.what_if_simulation_adapter import (
    VanillaWhatIfSimulationAdapter,
)
from hexawyn.adapters.secondary.vanilla.adapters.zombie_detection_adapter import (
    VanillaZombieDetectionAdapter,
)
from hexawyn.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesAppsApi,
    KubernetesCoreApi,
    KubernetesCRDApi,
    KubernetesMetricsApi,
)
from hexawyn.application.ports.driven.cost_forecast_port import (
    CostForecastPort,
    DailyCostData,
)
from hexawyn.application.ports.driven.cost_saving_estimation_port import (
    CostSavingEstimationPort,
    PodResourceData,
)
from hexawyn.application.ports.driven.ingress_port import IngressInfo, IngressPort
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
from hexawyn.application.ports.driven.pod_metrics_port import (
    PodMetricSnapshot,
    PodMetricsPort,
)
from hexawyn.application.ports.driven.probe_audit_port import (
    ProbeAuditPort,
    ProbeDeploymentRawData,
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
from hexawyn.application.ports.driven.what_if_simulation_port import (
    DependentServiceData,
    HPAData,
    PDBData,
    WhatIfSimulationPort,
)
from hexawyn.application.ports.driven.zombie_detection_port import (
    ZombieDetectionPort,
    ZombiePodData,
)
from hexawyn.infrastructure.config.kubeconfig_reader import load_kubeconfig

_HEALTHY_POD_STATUSES = {"Running", "Succeeded"}
_POD_CACHE_TTL_SECONDS = 5.0


class VanillaAdapter(
    K8sPort,
    ClusterHealthPort,
    TektonPort,
    NamespaceWasteAnalysisPort,
    RightsizingPort,
    CostForecastPort,
    ZombieDetectionPort,
    ProbeAuditPort,
    CostSavingEstimationPort,
    WhatIfSimulationPort,
    PodMetricsPort,
    IngressPort,
):
    """Minimal adapter for vanilla Kubernetes with no cloud provider dependencies."""

    def __init__(  # noqa: PLR0913
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
        self._k8s_adapter_inst: VanillaK8sAdapter | None = None
        self._health_adapter_inst: VanillaHealthAdapter | None = None
        self._cost_forecast_adapter_inst: VanillaCostForecastAdapter | None = None
        self._zombie_adapter_inst: VanillaZombieDetectionAdapter | None = None
        self._namespace_waste_adapter_inst: VanillaNamespaceWasteAdapter | None = None
        self._rightsizing_adapter_inst: VanillaRightsizingAdapter | None = None
        self._cost_saving_adapter_inst: VanillaCostSavingAdapter | None = None
        self._what_if_adapter_inst: VanillaWhatIfSimulationAdapter | None = None
        self._tekton_adapter_inst: VanillaTektonAdapter | None = None
        self._pod_metrics_adapter_inst: VanillaPodMetricsAdapter | None = None

    # ── Internal adapter accessors ───────────────────────────
    def _get_k8s_adapter(self) -> VanillaK8sAdapter:
        if self._k8s_adapter_inst is None:
            self._k8s_adapter_inst = VanillaK8sAdapter(
                api=self._api,
                metrics_api=self._metrics_api,
                cluster_name=self._cluster_name,
                prometheus_url=self._prometheus_url,
            )
        return self._k8s_adapter_inst

    def _get_health_adapter(self) -> VanillaHealthAdapter:
        if self._health_adapter_inst is None:
            self._health_adapter_inst = VanillaHealthAdapter(
                k8s_port=self._get_k8s_adapter(),
                api=self._api_client(),
            )
        return self._health_adapter_inst

    def _get_cost_forecast_adapter(self) -> VanillaCostForecastAdapter:
        if self._cost_forecast_adapter_inst is None:
            self._cost_forecast_adapter_inst = VanillaCostForecastAdapter(
                api=self._apps_api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._cost_forecast_adapter_inst

    def _get_zombie_adapter(self) -> VanillaZombieDetectionAdapter:
        if self._zombie_adapter_inst is None:
            self._zombie_adapter_inst = VanillaZombieDetectionAdapter(
                api=self._api_client(),
                prometheus_url=self._prometheus_url,
                pod_cache=self._pod_cache or [],
            )
        return self._zombie_adapter_inst

    def _get_namespace_waste_adapter(self) -> VanillaNamespaceWasteAdapter:
        if self._namespace_waste_adapter_inst is None:
            self._namespace_waste_adapter_inst = VanillaNamespaceWasteAdapter(
                api=self._api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._namespace_waste_adapter_inst

    def _get_rightsizing_adapter(self) -> VanillaRightsizingAdapter:
        if self._rightsizing_adapter_inst is None:
            self._rightsizing_adapter_inst = VanillaRightsizingAdapter(
                apps_api=self._apps_api_client(),
                metrics_api=self._metrics_api_client(),
            )
        return self._rightsizing_adapter_inst

    def _get_cost_saving_adapter(self) -> VanillaCostSavingAdapter:
        if self._cost_saving_adapter_inst is None:
            self._cost_saving_adapter_inst = VanillaCostSavingAdapter(
                api=self._api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._cost_saving_adapter_inst

    def _get_what_if_adapter(self) -> VanillaWhatIfSimulationAdapter:
        if self._what_if_adapter_inst is None:
            self._what_if_adapter_inst = VanillaWhatIfSimulationAdapter(
                api=self._api_client(),
                apps_api=self._apps_api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._what_if_adapter_inst

    def _get_tekton_adapter(self) -> VanillaTektonAdapter:
        if self._tekton_adapter_inst is None:
            self._tekton_adapter_inst = VanillaTektonAdapter(
                crd_api=self._crd_api,
            )
        return self._tekton_adapter_inst

    def _get_pod_metrics_adapter(self) -> VanillaPodMetricsAdapter:
        if self._pod_metrics_adapter_inst is None:
            self._pod_metrics_adapter_inst = VanillaPodMetricsAdapter(
                metrics_api=self._metrics_api,
                cluster_name=self._cluster_name,
            )
        return self._pod_metrics_adapter_inst

    # ── K8sPort ───────────────────────────────────────────────
    def list_pods(self, namespace: str | None = None) -> list[PodInfo]:
        return self._get_k8s_adapter().list_pods(namespace)

    def get_cluster_metrics(self) -> ClusterMetrics:
        return self._get_k8s_adapter().get_cluster_metrics()

    def get_cluster_context(self) -> ClusterContext:
        return self._get_k8s_adapter().get_cluster_context()

    def list_namespaces(self) -> list[NamespaceInfo]:
        return self._get_k8s_adapter().list_namespaces()

    # ── IngressPort ───────────────────────────────────────────
    def list_ingresses(self, namespace: str) -> list[IngressInfo]:
        return self._get_k8s_adapter().list_ingresses(namespace=namespace)

    # ── PodMetricsPort ─────────────────────────────────────────
    def get_pod_metrics(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        return self._get_pod_metrics_adapter().get_pod_metrics(namespace)

    # ── ClusterHealthPort ─────────────────────────────────────
    def get_findings(self) -> list[Finding]:
        return self._get_health_adapter().get_findings()

    def get_health_score(self) -> int:
        return self._get_health_adapter().get_health_score()

    def get_health_status(self) -> str:
        return self._get_health_adapter().get_health_status()

    # ── TektonPort ────────────────────────────────────────────
    def list_task_runs(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        return self._get_tekton_adapter().list_task_runs(pipeline_name, namespace)

    def list_pipeline_runs(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        return self._get_tekton_adapter().list_pipeline_runs(service_name, namespace)

    def list_pipeline_runs_in_namespace(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        return self._get_tekton_adapter().list_pipeline_runs_in_namespace(namespace, limit)

    # ── NamespaceWasteAnalysisPort ────────────────────────────
    def get_all_namespace_waste_data(self, window_days: int) -> list[NamespaceRawData]:
        return self._get_namespace_waste_adapter().get_all_namespace_waste_data(window_days)

    # ── RightsizingPort ──────────────────────────────────────────
    def get_workload_rightsizing_data(self) -> list[WorkloadRawData]:
        return self._get_rightsizing_adapter().get_workload_rightsizing_data()

    def _apps_api_client(self) -> KubernetesAppsApi:
        if self._apps_api is not None:
            return self._apps_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesAppsApi, client.AppsV1Api(api_client=core_api.api_client))

    def _api_client(self) -> KubernetesCoreApi:
        if self._api is not None:
            return self._api
        return cast(KubernetesCoreApi, load_kubeconfig())

    def _metrics_api_client(self) -> KubernetesMetricsApi:
        if self._metrics_api is not None:
            return self._metrics_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client))

    def _crd_api_client(self) -> KubernetesCRDApi:
        if self._crd_api is not None:
            return self._crd_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesCRDApi, client.CustomObjectsApi(api_client=core_api.api_client))

    # ── CostForecastPort ─────────────────────────────────────
    def get_daily_costs(self, days: int) -> list[DailyCostData]:
        return self._get_cost_forecast_adapter().get_daily_costs(days)

    # ── ZombieDetectionPort ───────────────────────────────────
    def get_zombie_workloads(self, window_hours: int) -> list[ZombiePodData]:
        return self._get_zombie_adapter().get_zombie_workloads(window_hours)

    # ── CostSavingEstimationPort ──────────────────────────────
    def get_pod_resource_data(self) -> list[PodResourceData]:
        return self._get_cost_saving_adapter().get_pod_resource_data()

    def get_previous_total_saving(self) -> float | None:
        return self._get_cost_saving_adapter().get_previous_total_saving()

    def store_total_saving(self, total_saving_usd: float) -> None:
        return self._get_cost_saving_adapter().store_total_saving(total_saving_usd)

    # ── WhatIfSimulationPort ──────────────────────────────────
    def get_current_replicas(self, namespace: str, service_name: str) -> int:
        return self._get_what_if_adapter().get_current_replicas(namespace, service_name)

    def get_current_cpu_utilization(self, namespace: str, service_name: str) -> float:
        return self._get_what_if_adapter().get_current_cpu_utilization(namespace, service_name)

    def get_pdb_info(self, namespace: str, service_name: str) -> PDBData | None:
        return self._get_what_if_adapter().get_pdb_info(namespace, service_name)

    def get_hpa_info(self, namespace: str, service_name: str) -> HPAData | None:
        return self._get_what_if_adapter().get_hpa_info(namespace, service_name)

    def get_service_topology(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        return self._get_what_if_adapter().get_service_topology(namespace, service_name)

    def get_dependency_graph(self, namespace: str) -> dict[str, list[str]]:
        return self._get_what_if_adapter().get_dependency_graph(namespace)

    def get_probe_audit_data(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        return self._get_what_if_adapter().get_probe_audit_data(namespace)
