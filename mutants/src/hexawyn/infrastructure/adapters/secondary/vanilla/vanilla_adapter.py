# mypy: ignore-errors
from typing import cast

from kubernetes import client

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
from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.cost_forecast_adapter import (
    VanillaCostForecastAdapter,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.cost_saving_estimation_adapter import (  # noqa: E501
    VanillaCostSavingAdapter,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.health_adapter import (
    VanillaHealthAdapter,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.k8s_adapter import (
    VanillaK8sAdapter,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.namespace_waste_adapter import (
    VanillaNamespaceWasteAdapter,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.pod_metrics_adapter import (
    VanillaPodMetricsAdapter,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.rightsizing_adapter import (
    VanillaRightsizingAdapter,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.tekton_adapter import (
    VanillaTektonAdapter,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.what_if_simulation_adapter import (
    VanillaWhatIfSimulationAdapter,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.adapters.zombie_detection_adapter import (
    VanillaZombieDetectionAdapter,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesAppsApi,
    KubernetesCoreApi,
    KubernetesCRDApi,
    KubernetesMetricsApi,
)
from hexawyn.infrastructure.config.kubeconfig_reader import load_kubeconfig

_HEALTHY_POD_STATUSES = {"Running", "Succeeded"}
_POD_CACHE_TTL_SECONDS = 5.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁVanillaAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁ_get_k8s_adapter__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁ_get_health_adapter__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁ_get_zombie_adapter__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁ_get_what_if_adapter__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁ_get_tekton_adapter__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁlist_pods__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁlist_ingresses__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁget_pod_metrics__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁlist_task_runs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁlist_pipeline_runs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁget_all_namespace_waste_data__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁ_apps_api_client__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁ_api_client__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁ_metrics_api_client__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁ_crd_api_client__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁget_daily_costs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁget_zombie_workloads__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁstore_total_saving__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁget_current_replicas__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁget_current_cpu_utilization__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁget_pdb_info__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁget_hpa_info__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁget_service_topology__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁget_dependency_graph__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaAdapterǁget_probe_audit_data__mutmut: MutantDict = {}  # type: ignore


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

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁ__init____mutmut)
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

    def xǁVanillaAdapterǁ__init____mutmut_orig(  # noqa: PLR0913
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

    def xǁVanillaAdapterǁ__init____mutmut_1(  # noqa: PLR0913
        self,
        cluster_name: str,
        api: KubernetesCoreApi | None = None,
        metrics_api: KubernetesMetricsApi | None = None,
        crd_api: KubernetesCRDApi | None = None,
        apps_api: KubernetesAppsApi | None = None,
        prometheus_url: str = "XXXX",
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

    def xǁVanillaAdapterǁ__init____mutmut_2(  # noqa: PLR0913
        self,
        cluster_name: str,
        api: KubernetesCoreApi | None = None,
        metrics_api: KubernetesMetricsApi | None = None,
        crd_api: KubernetesCRDApi | None = None,
        apps_api: KubernetesAppsApi | None = None,
        prometheus_url: str = "",
    ) -> None:
        self._cluster_name = None
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

    def xǁVanillaAdapterǁ__init____mutmut_3(  # noqa: PLR0913
        self,
        cluster_name: str,
        api: KubernetesCoreApi | None = None,
        metrics_api: KubernetesMetricsApi | None = None,
        crd_api: KubernetesCRDApi | None = None,
        apps_api: KubernetesAppsApi | None = None,
        prometheus_url: str = "",
    ) -> None:
        self._cluster_name = cluster_name
        self._api = None
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

    def xǁVanillaAdapterǁ__init____mutmut_4(  # noqa: PLR0913
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
        self._metrics_api = None
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

    def xǁVanillaAdapterǁ__init____mutmut_5(  # noqa: PLR0913
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
        self._crd_api = None
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

    def xǁVanillaAdapterǁ__init____mutmut_6(  # noqa: PLR0913
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
        self._apps_api = None
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

    def xǁVanillaAdapterǁ__init____mutmut_7(  # noqa: PLR0913
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
        self._prometheus_url = None
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

    def xǁVanillaAdapterǁ__init____mutmut_8(  # noqa: PLR0913
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
        self._pod_cache: list[PodInfo] | None = ""
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

    def xǁVanillaAdapterǁ__init____mutmut_9(  # noqa: PLR0913
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
        self._pod_cache_updated_at = None
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

    def xǁVanillaAdapterǁ__init____mutmut_10(  # noqa: PLR0913
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
        self._pod_cache_updated_at = 1.0
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

    def xǁVanillaAdapterǁ__init____mutmut_11(  # noqa: PLR0913
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
        self._k8s_adapter_inst: VanillaK8sAdapter | None = ""
        self._health_adapter_inst: VanillaHealthAdapter | None = None
        self._cost_forecast_adapter_inst: VanillaCostForecastAdapter | None = None
        self._zombie_adapter_inst: VanillaZombieDetectionAdapter | None = None
        self._namespace_waste_adapter_inst: VanillaNamespaceWasteAdapter | None = None
        self._rightsizing_adapter_inst: VanillaRightsizingAdapter | None = None
        self._cost_saving_adapter_inst: VanillaCostSavingAdapter | None = None
        self._what_if_adapter_inst: VanillaWhatIfSimulationAdapter | None = None
        self._tekton_adapter_inst: VanillaTektonAdapter | None = None
        self._pod_metrics_adapter_inst: VanillaPodMetricsAdapter | None = None

    def xǁVanillaAdapterǁ__init____mutmut_12(  # noqa: PLR0913
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
        self._health_adapter_inst: VanillaHealthAdapter | None = ""
        self._cost_forecast_adapter_inst: VanillaCostForecastAdapter | None = None
        self._zombie_adapter_inst: VanillaZombieDetectionAdapter | None = None
        self._namespace_waste_adapter_inst: VanillaNamespaceWasteAdapter | None = None
        self._rightsizing_adapter_inst: VanillaRightsizingAdapter | None = None
        self._cost_saving_adapter_inst: VanillaCostSavingAdapter | None = None
        self._what_if_adapter_inst: VanillaWhatIfSimulationAdapter | None = None
        self._tekton_adapter_inst: VanillaTektonAdapter | None = None
        self._pod_metrics_adapter_inst: VanillaPodMetricsAdapter | None = None

    def xǁVanillaAdapterǁ__init____mutmut_13(  # noqa: PLR0913
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
        self._cost_forecast_adapter_inst: VanillaCostForecastAdapter | None = ""
        self._zombie_adapter_inst: VanillaZombieDetectionAdapter | None = None
        self._namespace_waste_adapter_inst: VanillaNamespaceWasteAdapter | None = None
        self._rightsizing_adapter_inst: VanillaRightsizingAdapter | None = None
        self._cost_saving_adapter_inst: VanillaCostSavingAdapter | None = None
        self._what_if_adapter_inst: VanillaWhatIfSimulationAdapter | None = None
        self._tekton_adapter_inst: VanillaTektonAdapter | None = None
        self._pod_metrics_adapter_inst: VanillaPodMetricsAdapter | None = None

    def xǁVanillaAdapterǁ__init____mutmut_14(  # noqa: PLR0913
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
        self._zombie_adapter_inst: VanillaZombieDetectionAdapter | None = ""
        self._namespace_waste_adapter_inst: VanillaNamespaceWasteAdapter | None = None
        self._rightsizing_adapter_inst: VanillaRightsizingAdapter | None = None
        self._cost_saving_adapter_inst: VanillaCostSavingAdapter | None = None
        self._what_if_adapter_inst: VanillaWhatIfSimulationAdapter | None = None
        self._tekton_adapter_inst: VanillaTektonAdapter | None = None
        self._pod_metrics_adapter_inst: VanillaPodMetricsAdapter | None = None

    def xǁVanillaAdapterǁ__init____mutmut_15(  # noqa: PLR0913
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
        self._namespace_waste_adapter_inst: VanillaNamespaceWasteAdapter | None = ""
        self._rightsizing_adapter_inst: VanillaRightsizingAdapter | None = None
        self._cost_saving_adapter_inst: VanillaCostSavingAdapter | None = None
        self._what_if_adapter_inst: VanillaWhatIfSimulationAdapter | None = None
        self._tekton_adapter_inst: VanillaTektonAdapter | None = None
        self._pod_metrics_adapter_inst: VanillaPodMetricsAdapter | None = None

    def xǁVanillaAdapterǁ__init____mutmut_16(  # noqa: PLR0913
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
        self._rightsizing_adapter_inst: VanillaRightsizingAdapter | None = ""
        self._cost_saving_adapter_inst: VanillaCostSavingAdapter | None = None
        self._what_if_adapter_inst: VanillaWhatIfSimulationAdapter | None = None
        self._tekton_adapter_inst: VanillaTektonAdapter | None = None
        self._pod_metrics_adapter_inst: VanillaPodMetricsAdapter | None = None

    def xǁVanillaAdapterǁ__init____mutmut_17(  # noqa: PLR0913
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
        self._cost_saving_adapter_inst: VanillaCostSavingAdapter | None = ""
        self._what_if_adapter_inst: VanillaWhatIfSimulationAdapter | None = None
        self._tekton_adapter_inst: VanillaTektonAdapter | None = None
        self._pod_metrics_adapter_inst: VanillaPodMetricsAdapter | None = None

    def xǁVanillaAdapterǁ__init____mutmut_18(  # noqa: PLR0913
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
        self._what_if_adapter_inst: VanillaWhatIfSimulationAdapter | None = ""
        self._tekton_adapter_inst: VanillaTektonAdapter | None = None
        self._pod_metrics_adapter_inst: VanillaPodMetricsAdapter | None = None

    def xǁVanillaAdapterǁ__init____mutmut_19(  # noqa: PLR0913
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
        self._tekton_adapter_inst: VanillaTektonAdapter | None = ""
        self._pod_metrics_adapter_inst: VanillaPodMetricsAdapter | None = None

    def xǁVanillaAdapterǁ__init____mutmut_20(  # noqa: PLR0913
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
        self._pod_metrics_adapter_inst: VanillaPodMetricsAdapter | None = ""

    # ── Internal adapter accessors ───────────────────────────
    @_mutmut_mutated(mutants_xǁVanillaAdapterǁ_get_k8s_adapter__mutmut)
    def _get_k8s_adapter(self) -> VanillaK8sAdapter:
        if self._k8s_adapter_inst is None:
            self._k8s_adapter_inst = VanillaK8sAdapter(
                api=self._api,
                metrics_api=self._metrics_api,
                cluster_name=self._cluster_name,
                prometheus_url=self._prometheus_url,
            )
        return self._k8s_adapter_inst

    # ── Internal adapter accessors ───────────────────────────
    def xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_orig(self) -> VanillaK8sAdapter:
        if self._k8s_adapter_inst is None:
            self._k8s_adapter_inst = VanillaK8sAdapter(
                api=self._api,
                metrics_api=self._metrics_api,
                cluster_name=self._cluster_name,
                prometheus_url=self._prometheus_url,
            )
        return self._k8s_adapter_inst

    # ── Internal adapter accessors ───────────────────────────
    def xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_1(self) -> VanillaK8sAdapter:
        if self._k8s_adapter_inst is not None:
            self._k8s_adapter_inst = VanillaK8sAdapter(
                api=self._api,
                metrics_api=self._metrics_api,
                cluster_name=self._cluster_name,
                prometheus_url=self._prometheus_url,
            )
        return self._k8s_adapter_inst

    # ── Internal adapter accessors ───────────────────────────
    def xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_2(self) -> VanillaK8sAdapter:
        if self._k8s_adapter_inst is None:
            self._k8s_adapter_inst = None
        return self._k8s_adapter_inst

    # ── Internal adapter accessors ───────────────────────────
    def xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_3(self) -> VanillaK8sAdapter:
        if self._k8s_adapter_inst is None:
            self._k8s_adapter_inst = VanillaK8sAdapter(
                api=None,
                metrics_api=self._metrics_api,
                cluster_name=self._cluster_name,
                prometheus_url=self._prometheus_url,
            )
        return self._k8s_adapter_inst

    # ── Internal adapter accessors ───────────────────────────
    def xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_4(self) -> VanillaK8sAdapter:
        if self._k8s_adapter_inst is None:
            self._k8s_adapter_inst = VanillaK8sAdapter(
                api=self._api,
                metrics_api=None,
                cluster_name=self._cluster_name,
                prometheus_url=self._prometheus_url,
            )
        return self._k8s_adapter_inst

    # ── Internal adapter accessors ───────────────────────────
    def xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_5(self) -> VanillaK8sAdapter:
        if self._k8s_adapter_inst is None:
            self._k8s_adapter_inst = VanillaK8sAdapter(
                api=self._api,
                metrics_api=self._metrics_api,
                cluster_name=None,
                prometheus_url=self._prometheus_url,
            )
        return self._k8s_adapter_inst

    # ── Internal adapter accessors ───────────────────────────
    def xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_6(self) -> VanillaK8sAdapter:
        if self._k8s_adapter_inst is None:
            self._k8s_adapter_inst = VanillaK8sAdapter(
                api=self._api,
                metrics_api=self._metrics_api,
                cluster_name=self._cluster_name,
                prometheus_url=None,
            )
        return self._k8s_adapter_inst

    # ── Internal adapter accessors ───────────────────────────
    def xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_7(self) -> VanillaK8sAdapter:
        if self._k8s_adapter_inst is None:
            self._k8s_adapter_inst = VanillaK8sAdapter(
                metrics_api=self._metrics_api,
                cluster_name=self._cluster_name,
                prometheus_url=self._prometheus_url,
            )
        return self._k8s_adapter_inst

    # ── Internal adapter accessors ───────────────────────────
    def xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_8(self) -> VanillaK8sAdapter:
        if self._k8s_adapter_inst is None:
            self._k8s_adapter_inst = VanillaK8sAdapter(
                api=self._api,
                cluster_name=self._cluster_name,
                prometheus_url=self._prometheus_url,
            )
        return self._k8s_adapter_inst

    # ── Internal adapter accessors ───────────────────────────
    def xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_9(self) -> VanillaK8sAdapter:
        if self._k8s_adapter_inst is None:
            self._k8s_adapter_inst = VanillaK8sAdapter(
                api=self._api,
                metrics_api=self._metrics_api,
                prometheus_url=self._prometheus_url,
            )
        return self._k8s_adapter_inst

    # ── Internal adapter accessors ───────────────────────────
    def xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_10(self) -> VanillaK8sAdapter:
        if self._k8s_adapter_inst is None:
            self._k8s_adapter_inst = VanillaK8sAdapter(
                api=self._api,
                metrics_api=self._metrics_api,
                cluster_name=self._cluster_name,
                )
        return self._k8s_adapter_inst

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁ_get_health_adapter__mutmut)
    def _get_health_adapter(self) -> VanillaHealthAdapter:
        if self._health_adapter_inst is None:
            self._health_adapter_inst = VanillaHealthAdapter(
                k8s_port=self._get_k8s_adapter(),
                api=self._api_client(),
            )
        return self._health_adapter_inst

    def xǁVanillaAdapterǁ_get_health_adapter__mutmut_orig(self) -> VanillaHealthAdapter:
        if self._health_adapter_inst is None:
            self._health_adapter_inst = VanillaHealthAdapter(
                k8s_port=self._get_k8s_adapter(),
                api=self._api_client(),
            )
        return self._health_adapter_inst

    def xǁVanillaAdapterǁ_get_health_adapter__mutmut_1(self) -> VanillaHealthAdapter:
        if self._health_adapter_inst is not None:
            self._health_adapter_inst = VanillaHealthAdapter(
                k8s_port=self._get_k8s_adapter(),
                api=self._api_client(),
            )
        return self._health_adapter_inst

    def xǁVanillaAdapterǁ_get_health_adapter__mutmut_2(self) -> VanillaHealthAdapter:
        if self._health_adapter_inst is None:
            self._health_adapter_inst = None
        return self._health_adapter_inst

    def xǁVanillaAdapterǁ_get_health_adapter__mutmut_3(self) -> VanillaHealthAdapter:
        if self._health_adapter_inst is None:
            self._health_adapter_inst = VanillaHealthAdapter(
                k8s_port=None,
                api=self._api_client(),
            )
        return self._health_adapter_inst

    def xǁVanillaAdapterǁ_get_health_adapter__mutmut_4(self) -> VanillaHealthAdapter:
        if self._health_adapter_inst is None:
            self._health_adapter_inst = VanillaHealthAdapter(
                k8s_port=self._get_k8s_adapter(),
                api=None,
            )
        return self._health_adapter_inst

    def xǁVanillaAdapterǁ_get_health_adapter__mutmut_5(self) -> VanillaHealthAdapter:
        if self._health_adapter_inst is None:
            self._health_adapter_inst = VanillaHealthAdapter(
                api=self._api_client(),
            )
        return self._health_adapter_inst

    def xǁVanillaAdapterǁ_get_health_adapter__mutmut_6(self) -> VanillaHealthAdapter:
        if self._health_adapter_inst is None:
            self._health_adapter_inst = VanillaHealthAdapter(
                k8s_port=self._get_k8s_adapter(),
                )
        return self._health_adapter_inst

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut)
    def _get_cost_forecast_adapter(self) -> VanillaCostForecastAdapter:
        if self._cost_forecast_adapter_inst is None:
            self._cost_forecast_adapter_inst = VanillaCostForecastAdapter(
                api=self._apps_api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._cost_forecast_adapter_inst

    def xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_orig(self) -> VanillaCostForecastAdapter:
        if self._cost_forecast_adapter_inst is None:
            self._cost_forecast_adapter_inst = VanillaCostForecastAdapter(
                api=self._apps_api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._cost_forecast_adapter_inst

    def xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_1(self) -> VanillaCostForecastAdapter:
        if self._cost_forecast_adapter_inst is not None:
            self._cost_forecast_adapter_inst = VanillaCostForecastAdapter(
                api=self._apps_api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._cost_forecast_adapter_inst

    def xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_2(self) -> VanillaCostForecastAdapter:
        if self._cost_forecast_adapter_inst is None:
            self._cost_forecast_adapter_inst = None
        return self._cost_forecast_adapter_inst

    def xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_3(self) -> VanillaCostForecastAdapter:
        if self._cost_forecast_adapter_inst is None:
            self._cost_forecast_adapter_inst = VanillaCostForecastAdapter(
                api=None,
                prometheus_url=self._prometheus_url,
            )
        return self._cost_forecast_adapter_inst

    def xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_4(self) -> VanillaCostForecastAdapter:
        if self._cost_forecast_adapter_inst is None:
            self._cost_forecast_adapter_inst = VanillaCostForecastAdapter(
                api=self._apps_api_client(),
                prometheus_url=None,
            )
        return self._cost_forecast_adapter_inst

    def xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_5(self) -> VanillaCostForecastAdapter:
        if self._cost_forecast_adapter_inst is None:
            self._cost_forecast_adapter_inst = VanillaCostForecastAdapter(
                prometheus_url=self._prometheus_url,
            )
        return self._cost_forecast_adapter_inst

    def xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_6(self) -> VanillaCostForecastAdapter:
        if self._cost_forecast_adapter_inst is None:
            self._cost_forecast_adapter_inst = VanillaCostForecastAdapter(
                api=self._apps_api_client(),
                )
        return self._cost_forecast_adapter_inst

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁ_get_zombie_adapter__mutmut)
    def _get_zombie_adapter(self) -> VanillaZombieDetectionAdapter:
        if self._zombie_adapter_inst is None:
            self._zombie_adapter_inst = VanillaZombieDetectionAdapter(
                api=self._api_client(),
                prometheus_url=self._prometheus_url,
                pod_cache=self._pod_cache or [],
            )
        return self._zombie_adapter_inst

    def xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_orig(self) -> VanillaZombieDetectionAdapter:
        if self._zombie_adapter_inst is None:
            self._zombie_adapter_inst = VanillaZombieDetectionAdapter(
                api=self._api_client(),
                prometheus_url=self._prometheus_url,
                pod_cache=self._pod_cache or [],
            )
        return self._zombie_adapter_inst

    def xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_1(self) -> VanillaZombieDetectionAdapter:
        if self._zombie_adapter_inst is not None:
            self._zombie_adapter_inst = VanillaZombieDetectionAdapter(
                api=self._api_client(),
                prometheus_url=self._prometheus_url,
                pod_cache=self._pod_cache or [],
            )
        return self._zombie_adapter_inst

    def xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_2(self) -> VanillaZombieDetectionAdapter:
        if self._zombie_adapter_inst is None:
            self._zombie_adapter_inst = None
        return self._zombie_adapter_inst

    def xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_3(self) -> VanillaZombieDetectionAdapter:
        if self._zombie_adapter_inst is None:
            self._zombie_adapter_inst = VanillaZombieDetectionAdapter(
                api=None,
                prometheus_url=self._prometheus_url,
                pod_cache=self._pod_cache or [],
            )
        return self._zombie_adapter_inst

    def xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_4(self) -> VanillaZombieDetectionAdapter:
        if self._zombie_adapter_inst is None:
            self._zombie_adapter_inst = VanillaZombieDetectionAdapter(
                api=self._api_client(),
                prometheus_url=None,
                pod_cache=self._pod_cache or [],
            )
        return self._zombie_adapter_inst

    def xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_5(self) -> VanillaZombieDetectionAdapter:
        if self._zombie_adapter_inst is None:
            self._zombie_adapter_inst = VanillaZombieDetectionAdapter(
                api=self._api_client(),
                prometheus_url=self._prometheus_url,
                pod_cache=None,
            )
        return self._zombie_adapter_inst

    def xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_6(self) -> VanillaZombieDetectionAdapter:
        if self._zombie_adapter_inst is None:
            self._zombie_adapter_inst = VanillaZombieDetectionAdapter(
                prometheus_url=self._prometheus_url,
                pod_cache=self._pod_cache or [],
            )
        return self._zombie_adapter_inst

    def xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_7(self) -> VanillaZombieDetectionAdapter:
        if self._zombie_adapter_inst is None:
            self._zombie_adapter_inst = VanillaZombieDetectionAdapter(
                api=self._api_client(),
                pod_cache=self._pod_cache or [],
            )
        return self._zombie_adapter_inst

    def xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_8(self) -> VanillaZombieDetectionAdapter:
        if self._zombie_adapter_inst is None:
            self._zombie_adapter_inst = VanillaZombieDetectionAdapter(
                api=self._api_client(),
                prometheus_url=self._prometheus_url,
                )
        return self._zombie_adapter_inst

    def xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_9(self) -> VanillaZombieDetectionAdapter:
        if self._zombie_adapter_inst is None:
            self._zombie_adapter_inst = VanillaZombieDetectionAdapter(
                api=self._api_client(),
                prometheus_url=self._prometheus_url,
                pod_cache=self._pod_cache and [],
            )
        return self._zombie_adapter_inst

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut)
    def _get_namespace_waste_adapter(self) -> VanillaNamespaceWasteAdapter:
        if self._namespace_waste_adapter_inst is None:
            self._namespace_waste_adapter_inst = VanillaNamespaceWasteAdapter(
                api=self._api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._namespace_waste_adapter_inst

    def xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_orig(self) -> VanillaNamespaceWasteAdapter:
        if self._namespace_waste_adapter_inst is None:
            self._namespace_waste_adapter_inst = VanillaNamespaceWasteAdapter(
                api=self._api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._namespace_waste_adapter_inst

    def xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_1(self) -> VanillaNamespaceWasteAdapter:
        if self._namespace_waste_adapter_inst is not None:
            self._namespace_waste_adapter_inst = VanillaNamespaceWasteAdapter(
                api=self._api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._namespace_waste_adapter_inst

    def xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_2(self) -> VanillaNamespaceWasteAdapter:
        if self._namespace_waste_adapter_inst is None:
            self._namespace_waste_adapter_inst = None
        return self._namespace_waste_adapter_inst

    def xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_3(self) -> VanillaNamespaceWasteAdapter:
        if self._namespace_waste_adapter_inst is None:
            self._namespace_waste_adapter_inst = VanillaNamespaceWasteAdapter(
                api=None,
                prometheus_url=self._prometheus_url,
            )
        return self._namespace_waste_adapter_inst

    def xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_4(self) -> VanillaNamespaceWasteAdapter:
        if self._namespace_waste_adapter_inst is None:
            self._namespace_waste_adapter_inst = VanillaNamespaceWasteAdapter(
                api=self._api_client(),
                prometheus_url=None,
            )
        return self._namespace_waste_adapter_inst

    def xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_5(self) -> VanillaNamespaceWasteAdapter:
        if self._namespace_waste_adapter_inst is None:
            self._namespace_waste_adapter_inst = VanillaNamespaceWasteAdapter(
                prometheus_url=self._prometheus_url,
            )
        return self._namespace_waste_adapter_inst

    def xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_6(self) -> VanillaNamespaceWasteAdapter:
        if self._namespace_waste_adapter_inst is None:
            self._namespace_waste_adapter_inst = VanillaNamespaceWasteAdapter(
                api=self._api_client(),
                )
        return self._namespace_waste_adapter_inst

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut)
    def _get_rightsizing_adapter(self) -> VanillaRightsizingAdapter:
        if self._rightsizing_adapter_inst is None:
            self._rightsizing_adapter_inst = VanillaRightsizingAdapter(
                apps_api=self._apps_api_client(),
                metrics_api=self._metrics_api_client(),
            )
        return self._rightsizing_adapter_inst

    def xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_orig(self) -> VanillaRightsizingAdapter:
        if self._rightsizing_adapter_inst is None:
            self._rightsizing_adapter_inst = VanillaRightsizingAdapter(
                apps_api=self._apps_api_client(),
                metrics_api=self._metrics_api_client(),
            )
        return self._rightsizing_adapter_inst

    def xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_1(self) -> VanillaRightsizingAdapter:
        if self._rightsizing_adapter_inst is not None:
            self._rightsizing_adapter_inst = VanillaRightsizingAdapter(
                apps_api=self._apps_api_client(),
                metrics_api=self._metrics_api_client(),
            )
        return self._rightsizing_adapter_inst

    def xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_2(self) -> VanillaRightsizingAdapter:
        if self._rightsizing_adapter_inst is None:
            self._rightsizing_adapter_inst = None
        return self._rightsizing_adapter_inst

    def xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_3(self) -> VanillaRightsizingAdapter:
        if self._rightsizing_adapter_inst is None:
            self._rightsizing_adapter_inst = VanillaRightsizingAdapter(
                apps_api=None,
                metrics_api=self._metrics_api_client(),
            )
        return self._rightsizing_adapter_inst

    def xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_4(self) -> VanillaRightsizingAdapter:
        if self._rightsizing_adapter_inst is None:
            self._rightsizing_adapter_inst = VanillaRightsizingAdapter(
                apps_api=self._apps_api_client(),
                metrics_api=None,
            )
        return self._rightsizing_adapter_inst

    def xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_5(self) -> VanillaRightsizingAdapter:
        if self._rightsizing_adapter_inst is None:
            self._rightsizing_adapter_inst = VanillaRightsizingAdapter(
                metrics_api=self._metrics_api_client(),
            )
        return self._rightsizing_adapter_inst

    def xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_6(self) -> VanillaRightsizingAdapter:
        if self._rightsizing_adapter_inst is None:
            self._rightsizing_adapter_inst = VanillaRightsizingAdapter(
                apps_api=self._apps_api_client(),
                )
        return self._rightsizing_adapter_inst

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut)
    def _get_cost_saving_adapter(self) -> VanillaCostSavingAdapter:
        if self._cost_saving_adapter_inst is None:
            self._cost_saving_adapter_inst = VanillaCostSavingAdapter(
                api=self._api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._cost_saving_adapter_inst

    def xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_orig(self) -> VanillaCostSavingAdapter:
        if self._cost_saving_adapter_inst is None:
            self._cost_saving_adapter_inst = VanillaCostSavingAdapter(
                api=self._api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._cost_saving_adapter_inst

    def xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_1(self) -> VanillaCostSavingAdapter:
        if self._cost_saving_adapter_inst is not None:
            self._cost_saving_adapter_inst = VanillaCostSavingAdapter(
                api=self._api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._cost_saving_adapter_inst

    def xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_2(self) -> VanillaCostSavingAdapter:
        if self._cost_saving_adapter_inst is None:
            self._cost_saving_adapter_inst = None
        return self._cost_saving_adapter_inst

    def xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_3(self) -> VanillaCostSavingAdapter:
        if self._cost_saving_adapter_inst is None:
            self._cost_saving_adapter_inst = VanillaCostSavingAdapter(
                api=None,
                prometheus_url=self._prometheus_url,
            )
        return self._cost_saving_adapter_inst

    def xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_4(self) -> VanillaCostSavingAdapter:
        if self._cost_saving_adapter_inst is None:
            self._cost_saving_adapter_inst = VanillaCostSavingAdapter(
                api=self._api_client(),
                prometheus_url=None,
            )
        return self._cost_saving_adapter_inst

    def xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_5(self) -> VanillaCostSavingAdapter:
        if self._cost_saving_adapter_inst is None:
            self._cost_saving_adapter_inst = VanillaCostSavingAdapter(
                prometheus_url=self._prometheus_url,
            )
        return self._cost_saving_adapter_inst

    def xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_6(self) -> VanillaCostSavingAdapter:
        if self._cost_saving_adapter_inst is None:
            self._cost_saving_adapter_inst = VanillaCostSavingAdapter(
                api=self._api_client(),
                )
        return self._cost_saving_adapter_inst

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁ_get_what_if_adapter__mutmut)
    def _get_what_if_adapter(self) -> VanillaWhatIfSimulationAdapter:
        if self._what_if_adapter_inst is None:
            self._what_if_adapter_inst = VanillaWhatIfSimulationAdapter(
                api=self._api_client(),
                apps_api=self._apps_api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._what_if_adapter_inst

    def xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_orig(self) -> VanillaWhatIfSimulationAdapter:
        if self._what_if_adapter_inst is None:
            self._what_if_adapter_inst = VanillaWhatIfSimulationAdapter(
                api=self._api_client(),
                apps_api=self._apps_api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._what_if_adapter_inst

    def xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_1(self) -> VanillaWhatIfSimulationAdapter:
        if self._what_if_adapter_inst is not None:
            self._what_if_adapter_inst = VanillaWhatIfSimulationAdapter(
                api=self._api_client(),
                apps_api=self._apps_api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._what_if_adapter_inst

    def xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_2(self) -> VanillaWhatIfSimulationAdapter:
        if self._what_if_adapter_inst is None:
            self._what_if_adapter_inst = None
        return self._what_if_adapter_inst

    def xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_3(self) -> VanillaWhatIfSimulationAdapter:
        if self._what_if_adapter_inst is None:
            self._what_if_adapter_inst = VanillaWhatIfSimulationAdapter(
                api=None,
                apps_api=self._apps_api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._what_if_adapter_inst

    def xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_4(self) -> VanillaWhatIfSimulationAdapter:
        if self._what_if_adapter_inst is None:
            self._what_if_adapter_inst = VanillaWhatIfSimulationAdapter(
                api=self._api_client(),
                apps_api=None,
                prometheus_url=self._prometheus_url,
            )
        return self._what_if_adapter_inst

    def xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_5(self) -> VanillaWhatIfSimulationAdapter:
        if self._what_if_adapter_inst is None:
            self._what_if_adapter_inst = VanillaWhatIfSimulationAdapter(
                api=self._api_client(),
                apps_api=self._apps_api_client(),
                prometheus_url=None,
            )
        return self._what_if_adapter_inst

    def xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_6(self) -> VanillaWhatIfSimulationAdapter:
        if self._what_if_adapter_inst is None:
            self._what_if_adapter_inst = VanillaWhatIfSimulationAdapter(
                apps_api=self._apps_api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._what_if_adapter_inst

    def xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_7(self) -> VanillaWhatIfSimulationAdapter:
        if self._what_if_adapter_inst is None:
            self._what_if_adapter_inst = VanillaWhatIfSimulationAdapter(
                api=self._api_client(),
                prometheus_url=self._prometheus_url,
            )
        return self._what_if_adapter_inst

    def xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_8(self) -> VanillaWhatIfSimulationAdapter:
        if self._what_if_adapter_inst is None:
            self._what_if_adapter_inst = VanillaWhatIfSimulationAdapter(
                api=self._api_client(),
                apps_api=self._apps_api_client(),
                )
        return self._what_if_adapter_inst

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁ_get_tekton_adapter__mutmut)
    def _get_tekton_adapter(self) -> VanillaTektonAdapter:
        if self._tekton_adapter_inst is None:
            self._tekton_adapter_inst = VanillaTektonAdapter(
                crd_api=self._crd_api,
            )
        return self._tekton_adapter_inst

    def xǁVanillaAdapterǁ_get_tekton_adapter__mutmut_orig(self) -> VanillaTektonAdapter:
        if self._tekton_adapter_inst is None:
            self._tekton_adapter_inst = VanillaTektonAdapter(
                crd_api=self._crd_api,
            )
        return self._tekton_adapter_inst

    def xǁVanillaAdapterǁ_get_tekton_adapter__mutmut_1(self) -> VanillaTektonAdapter:
        if self._tekton_adapter_inst is not None:
            self._tekton_adapter_inst = VanillaTektonAdapter(
                crd_api=self._crd_api,
            )
        return self._tekton_adapter_inst

    def xǁVanillaAdapterǁ_get_tekton_adapter__mutmut_2(self) -> VanillaTektonAdapter:
        if self._tekton_adapter_inst is None:
            self._tekton_adapter_inst = None
        return self._tekton_adapter_inst

    def xǁVanillaAdapterǁ_get_tekton_adapter__mutmut_3(self) -> VanillaTektonAdapter:
        if self._tekton_adapter_inst is None:
            self._tekton_adapter_inst = VanillaTektonAdapter(
                crd_api=None,
            )
        return self._tekton_adapter_inst

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut)
    def _get_pod_metrics_adapter(self) -> VanillaPodMetricsAdapter:
        if self._pod_metrics_adapter_inst is None:
            self._pod_metrics_adapter_inst = VanillaPodMetricsAdapter(
                metrics_api=self._metrics_api,
                cluster_name=self._cluster_name,
            )
        return self._pod_metrics_adapter_inst

    def xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_orig(self) -> VanillaPodMetricsAdapter:
        if self._pod_metrics_adapter_inst is None:
            self._pod_metrics_adapter_inst = VanillaPodMetricsAdapter(
                metrics_api=self._metrics_api,
                cluster_name=self._cluster_name,
            )
        return self._pod_metrics_adapter_inst

    def xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_1(self) -> VanillaPodMetricsAdapter:
        if self._pod_metrics_adapter_inst is not None:
            self._pod_metrics_adapter_inst = VanillaPodMetricsAdapter(
                metrics_api=self._metrics_api,
                cluster_name=self._cluster_name,
            )
        return self._pod_metrics_adapter_inst

    def xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_2(self) -> VanillaPodMetricsAdapter:
        if self._pod_metrics_adapter_inst is None:
            self._pod_metrics_adapter_inst = None
        return self._pod_metrics_adapter_inst

    def xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_3(self) -> VanillaPodMetricsAdapter:
        if self._pod_metrics_adapter_inst is None:
            self._pod_metrics_adapter_inst = VanillaPodMetricsAdapter(
                metrics_api=None,
                cluster_name=self._cluster_name,
            )
        return self._pod_metrics_adapter_inst

    def xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_4(self) -> VanillaPodMetricsAdapter:
        if self._pod_metrics_adapter_inst is None:
            self._pod_metrics_adapter_inst = VanillaPodMetricsAdapter(
                metrics_api=self._metrics_api,
                cluster_name=None,
            )
        return self._pod_metrics_adapter_inst

    def xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_5(self) -> VanillaPodMetricsAdapter:
        if self._pod_metrics_adapter_inst is None:
            self._pod_metrics_adapter_inst = VanillaPodMetricsAdapter(
                cluster_name=self._cluster_name,
            )
        return self._pod_metrics_adapter_inst

    def xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_6(self) -> VanillaPodMetricsAdapter:
        if self._pod_metrics_adapter_inst is None:
            self._pod_metrics_adapter_inst = VanillaPodMetricsAdapter(
                metrics_api=self._metrics_api,
                )
        return self._pod_metrics_adapter_inst

    # ── K8sPort ───────────────────────────────────────────────
    @_mutmut_mutated(mutants_xǁVanillaAdapterǁlist_pods__mutmut)
    def list_pods(self, namespace: str | None = None) -> list[PodInfo]:
        return self._get_k8s_adapter().list_pods(namespace)

    # ── K8sPort ───────────────────────────────────────────────
    def xǁVanillaAdapterǁlist_pods__mutmut_orig(self, namespace: str | None = None) -> list[PodInfo]:
        return self._get_k8s_adapter().list_pods(namespace)

    # ── K8sPort ───────────────────────────────────────────────
    def xǁVanillaAdapterǁlist_pods__mutmut_1(self, namespace: str | None = None) -> list[PodInfo]:
        return self._get_k8s_adapter().list_pods(None)

    def get_cluster_metrics(self) -> ClusterMetrics:
        return self._get_k8s_adapter().get_cluster_metrics()

    def get_cluster_context(self) -> ClusterContext:
        return self._get_k8s_adapter().get_cluster_context()

    def list_namespaces(self) -> list[NamespaceInfo]:
        return self._get_k8s_adapter().list_namespaces()

    # ── IngressPort ───────────────────────────────────────────
    @_mutmut_mutated(mutants_xǁVanillaAdapterǁlist_ingresses__mutmut)
    def list_ingresses(self, namespace: str) -> list[IngressInfo]:
        return self._get_k8s_adapter().list_ingresses(namespace=namespace)

    # ── IngressPort ───────────────────────────────────────────
    def xǁVanillaAdapterǁlist_ingresses__mutmut_orig(self, namespace: str) -> list[IngressInfo]:
        return self._get_k8s_adapter().list_ingresses(namespace=namespace)

    # ── IngressPort ───────────────────────────────────────────
    def xǁVanillaAdapterǁlist_ingresses__mutmut_1(self, namespace: str) -> list[IngressInfo]:
        return self._get_k8s_adapter().list_ingresses(namespace=None)

    # ── PodMetricsPort ─────────────────────────────────────────
    @_mutmut_mutated(mutants_xǁVanillaAdapterǁget_pod_metrics__mutmut)
    def get_pod_metrics(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        return self._get_pod_metrics_adapter().get_pod_metrics(namespace)

    # ── PodMetricsPort ─────────────────────────────────────────
    def xǁVanillaAdapterǁget_pod_metrics__mutmut_orig(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        return self._get_pod_metrics_adapter().get_pod_metrics(namespace)

    # ── PodMetricsPort ─────────────────────────────────────────
    def xǁVanillaAdapterǁget_pod_metrics__mutmut_1(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        return self._get_pod_metrics_adapter().get_pod_metrics(None)

    # ── ClusterHealthPort ─────────────────────────────────────
    def get_findings(self) -> list[Finding]:
        return self._get_health_adapter().get_findings()

    def get_health_score(self) -> int:
        return self._get_health_adapter().get_health_score()

    def get_health_status(self) -> str:
        return self._get_health_adapter().get_health_status()

    # ── TektonPort ────────────────────────────────────────────
    @_mutmut_mutated(mutants_xǁVanillaAdapterǁlist_task_runs__mutmut)
    def list_task_runs(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        return self._get_tekton_adapter().list_task_runs(pipeline_name, namespace)

    # ── TektonPort ────────────────────────────────────────────
    def xǁVanillaAdapterǁlist_task_runs__mutmut_orig(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        return self._get_tekton_adapter().list_task_runs(pipeline_name, namespace)

    # ── TektonPort ────────────────────────────────────────────
    def xǁVanillaAdapterǁlist_task_runs__mutmut_1(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        return self._get_tekton_adapter().list_task_runs(None, namespace)

    # ── TektonPort ────────────────────────────────────────────
    def xǁVanillaAdapterǁlist_task_runs__mutmut_2(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        return self._get_tekton_adapter().list_task_runs(pipeline_name, None)

    # ── TektonPort ────────────────────────────────────────────
    def xǁVanillaAdapterǁlist_task_runs__mutmut_3(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        return self._get_tekton_adapter().list_task_runs(namespace)

    # ── TektonPort ────────────────────────────────────────────
    def xǁVanillaAdapterǁlist_task_runs__mutmut_4(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        return self._get_tekton_adapter().list_task_runs(pipeline_name, )

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁlist_pipeline_runs__mutmut)
    def list_pipeline_runs(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        return self._get_tekton_adapter().list_pipeline_runs(service_name, namespace)

    def xǁVanillaAdapterǁlist_pipeline_runs__mutmut_orig(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        return self._get_tekton_adapter().list_pipeline_runs(service_name, namespace)

    def xǁVanillaAdapterǁlist_pipeline_runs__mutmut_1(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        return self._get_tekton_adapter().list_pipeline_runs(None, namespace)

    def xǁVanillaAdapterǁlist_pipeline_runs__mutmut_2(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        return self._get_tekton_adapter().list_pipeline_runs(service_name, None)

    def xǁVanillaAdapterǁlist_pipeline_runs__mutmut_3(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        return self._get_tekton_adapter().list_pipeline_runs(namespace)

    def xǁVanillaAdapterǁlist_pipeline_runs__mutmut_4(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        return self._get_tekton_adapter().list_pipeline_runs(service_name, )

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut)
    def list_pipeline_runs_in_namespace(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        return self._get_tekton_adapter().list_pipeline_runs_in_namespace(namespace, limit)

    def xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut_orig(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        return self._get_tekton_adapter().list_pipeline_runs_in_namespace(namespace, limit)

    def xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut_1(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        return self._get_tekton_adapter().list_pipeline_runs_in_namespace(None, limit)

    def xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut_2(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        return self._get_tekton_adapter().list_pipeline_runs_in_namespace(namespace, None)

    def xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut_3(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        return self._get_tekton_adapter().list_pipeline_runs_in_namespace(limit)

    def xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut_4(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        return self._get_tekton_adapter().list_pipeline_runs_in_namespace(namespace, )

    # ── NamespaceWasteAnalysisPort ────────────────────────────
    @_mutmut_mutated(mutants_xǁVanillaAdapterǁget_all_namespace_waste_data__mutmut)
    def get_all_namespace_waste_data(self, window_days: int) -> list[NamespaceRawData]:
        return self._get_namespace_waste_adapter().get_all_namespace_waste_data(window_days)

    # ── NamespaceWasteAnalysisPort ────────────────────────────
    def xǁVanillaAdapterǁget_all_namespace_waste_data__mutmut_orig(self, window_days: int) -> list[NamespaceRawData]:
        return self._get_namespace_waste_adapter().get_all_namespace_waste_data(window_days)

    # ── NamespaceWasteAnalysisPort ────────────────────────────
    def xǁVanillaAdapterǁget_all_namespace_waste_data__mutmut_1(self, window_days: int) -> list[NamespaceRawData]:
        return self._get_namespace_waste_adapter().get_all_namespace_waste_data(None)

    # ── RightsizingPort ──────────────────────────────────────────
    def get_workload_rightsizing_data(self) -> list[WorkloadRawData]:
        return self._get_rightsizing_adapter().get_workload_rightsizing_data()

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁ_apps_api_client__mutmut)
    def _apps_api_client(self) -> KubernetesAppsApi:
        if self._apps_api is not None:
            return self._apps_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesAppsApi, client.AppsV1Api(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_apps_api_client__mutmut_orig(self) -> KubernetesAppsApi:
        if self._apps_api is not None:
            return self._apps_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesAppsApi, client.AppsV1Api(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_apps_api_client__mutmut_1(self) -> KubernetesAppsApi:
        if self._apps_api is None:
            return self._apps_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesAppsApi, client.AppsV1Api(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_apps_api_client__mutmut_2(self) -> KubernetesAppsApi:
        if self._apps_api is not None:
            return self._apps_api
        core_api = None
        return cast(KubernetesAppsApi, client.AppsV1Api(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_apps_api_client__mutmut_3(self) -> KubernetesAppsApi:
        if self._apps_api is not None:
            return self._apps_api
        core_api = cast(None, self._api_client())
        return cast(KubernetesAppsApi, client.AppsV1Api(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_apps_api_client__mutmut_4(self) -> KubernetesAppsApi:
        if self._apps_api is not None:
            return self._apps_api
        core_api = cast(client.CoreV1Api, None)
        return cast(KubernetesAppsApi, client.AppsV1Api(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_apps_api_client__mutmut_5(self) -> KubernetesAppsApi:
        if self._apps_api is not None:
            return self._apps_api
        core_api = cast(self._api_client())
        return cast(KubernetesAppsApi, client.AppsV1Api(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_apps_api_client__mutmut_6(self) -> KubernetesAppsApi:
        if self._apps_api is not None:
            return self._apps_api
        core_api = cast(client.CoreV1Api, )
        return cast(KubernetesAppsApi, client.AppsV1Api(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_apps_api_client__mutmut_7(self) -> KubernetesAppsApi:
        if self._apps_api is not None:
            return self._apps_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(None, client.AppsV1Api(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_apps_api_client__mutmut_8(self) -> KubernetesAppsApi:
        if self._apps_api is not None:
            return self._apps_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesAppsApi, None)

    def xǁVanillaAdapterǁ_apps_api_client__mutmut_9(self) -> KubernetesAppsApi:
        if self._apps_api is not None:
            return self._apps_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(client.AppsV1Api(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_apps_api_client__mutmut_10(self) -> KubernetesAppsApi:
        if self._apps_api is not None:
            return self._apps_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesAppsApi, )

    def xǁVanillaAdapterǁ_apps_api_client__mutmut_11(self) -> KubernetesAppsApi:
        if self._apps_api is not None:
            return self._apps_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesAppsApi, client.AppsV1Api(api_client=None))

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁ_api_client__mutmut)
    def _api_client(self) -> KubernetesCoreApi:
        if self._api is not None:
            return self._api
        return cast(KubernetesCoreApi, load_kubeconfig())

    def xǁVanillaAdapterǁ_api_client__mutmut_orig(self) -> KubernetesCoreApi:
        if self._api is not None:
            return self._api
        return cast(KubernetesCoreApi, load_kubeconfig())

    def xǁVanillaAdapterǁ_api_client__mutmut_1(self) -> KubernetesCoreApi:
        if self._api is None:
            return self._api
        return cast(KubernetesCoreApi, load_kubeconfig())

    def xǁVanillaAdapterǁ_api_client__mutmut_2(self) -> KubernetesCoreApi:
        if self._api is not None:
            return self._api
        return cast(None, load_kubeconfig())

    def xǁVanillaAdapterǁ_api_client__mutmut_3(self) -> KubernetesCoreApi:
        if self._api is not None:
            return self._api
        return cast(KubernetesCoreApi, None)

    def xǁVanillaAdapterǁ_api_client__mutmut_4(self) -> KubernetesCoreApi:
        if self._api is not None:
            return self._api
        return cast(load_kubeconfig())

    def xǁVanillaAdapterǁ_api_client__mutmut_5(self) -> KubernetesCoreApi:
        if self._api is not None:
            return self._api
        return cast(KubernetesCoreApi, )

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁ_metrics_api_client__mutmut)
    def _metrics_api_client(self) -> KubernetesMetricsApi:
        if self._metrics_api is not None:
            return self._metrics_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_metrics_api_client__mutmut_orig(self) -> KubernetesMetricsApi:
        if self._metrics_api is not None:
            return self._metrics_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_metrics_api_client__mutmut_1(self) -> KubernetesMetricsApi:
        if self._metrics_api is None:
            return self._metrics_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_metrics_api_client__mutmut_2(self) -> KubernetesMetricsApi:
        if self._metrics_api is not None:
            return self._metrics_api
        core_api = None
        return cast(KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_metrics_api_client__mutmut_3(self) -> KubernetesMetricsApi:
        if self._metrics_api is not None:
            return self._metrics_api
        core_api = cast(None, self._api_client())
        return cast(KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_metrics_api_client__mutmut_4(self) -> KubernetesMetricsApi:
        if self._metrics_api is not None:
            return self._metrics_api
        core_api = cast(client.CoreV1Api, None)
        return cast(KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_metrics_api_client__mutmut_5(self) -> KubernetesMetricsApi:
        if self._metrics_api is not None:
            return self._metrics_api
        core_api = cast(self._api_client())
        return cast(KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_metrics_api_client__mutmut_6(self) -> KubernetesMetricsApi:
        if self._metrics_api is not None:
            return self._metrics_api
        core_api = cast(client.CoreV1Api, )
        return cast(KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_metrics_api_client__mutmut_7(self) -> KubernetesMetricsApi:
        if self._metrics_api is not None:
            return self._metrics_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(None, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_metrics_api_client__mutmut_8(self) -> KubernetesMetricsApi:
        if self._metrics_api is not None:
            return self._metrics_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesMetricsApi, None)

    def xǁVanillaAdapterǁ_metrics_api_client__mutmut_9(self) -> KubernetesMetricsApi:
        if self._metrics_api is not None:
            return self._metrics_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_metrics_api_client__mutmut_10(self) -> KubernetesMetricsApi:
        if self._metrics_api is not None:
            return self._metrics_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesMetricsApi, )

    def xǁVanillaAdapterǁ_metrics_api_client__mutmut_11(self) -> KubernetesMetricsApi:
        if self._metrics_api is not None:
            return self._metrics_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesMetricsApi, client.CustomObjectsApi(api_client=None))

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁ_crd_api_client__mutmut)
    def _crd_api_client(self) -> KubernetesCRDApi:
        if self._crd_api is not None:
            return self._crd_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesCRDApi, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_crd_api_client__mutmut_orig(self) -> KubernetesCRDApi:
        if self._crd_api is not None:
            return self._crd_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesCRDApi, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_crd_api_client__mutmut_1(self) -> KubernetesCRDApi:
        if self._crd_api is None:
            return self._crd_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesCRDApi, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_crd_api_client__mutmut_2(self) -> KubernetesCRDApi:
        if self._crd_api is not None:
            return self._crd_api
        core_api = None
        return cast(KubernetesCRDApi, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_crd_api_client__mutmut_3(self) -> KubernetesCRDApi:
        if self._crd_api is not None:
            return self._crd_api
        core_api = cast(None, self._api_client())
        return cast(KubernetesCRDApi, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_crd_api_client__mutmut_4(self) -> KubernetesCRDApi:
        if self._crd_api is not None:
            return self._crd_api
        core_api = cast(client.CoreV1Api, None)
        return cast(KubernetesCRDApi, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_crd_api_client__mutmut_5(self) -> KubernetesCRDApi:
        if self._crd_api is not None:
            return self._crd_api
        core_api = cast(self._api_client())
        return cast(KubernetesCRDApi, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_crd_api_client__mutmut_6(self) -> KubernetesCRDApi:
        if self._crd_api is not None:
            return self._crd_api
        core_api = cast(client.CoreV1Api, )
        return cast(KubernetesCRDApi, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_crd_api_client__mutmut_7(self) -> KubernetesCRDApi:
        if self._crd_api is not None:
            return self._crd_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(None, client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_crd_api_client__mutmut_8(self) -> KubernetesCRDApi:
        if self._crd_api is not None:
            return self._crd_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesCRDApi, None)

    def xǁVanillaAdapterǁ_crd_api_client__mutmut_9(self) -> KubernetesCRDApi:
        if self._crd_api is not None:
            return self._crd_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(client.CustomObjectsApi(api_client=core_api.api_client))

    def xǁVanillaAdapterǁ_crd_api_client__mutmut_10(self) -> KubernetesCRDApi:
        if self._crd_api is not None:
            return self._crd_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesCRDApi, )

    def xǁVanillaAdapterǁ_crd_api_client__mutmut_11(self) -> KubernetesCRDApi:
        if self._crd_api is not None:
            return self._crd_api
        core_api = cast(client.CoreV1Api, self._api_client())
        return cast(KubernetesCRDApi, client.CustomObjectsApi(api_client=None))

    # ── CostForecastPort ─────────────────────────────────────
    @_mutmut_mutated(mutants_xǁVanillaAdapterǁget_daily_costs__mutmut)
    def get_daily_costs(self, days: int) -> list[DailyCostData]:
        return self._get_cost_forecast_adapter().get_daily_costs(days)

    # ── CostForecastPort ─────────────────────────────────────
    def xǁVanillaAdapterǁget_daily_costs__mutmut_orig(self, days: int) -> list[DailyCostData]:
        return self._get_cost_forecast_adapter().get_daily_costs(days)

    # ── CostForecastPort ─────────────────────────────────────
    def xǁVanillaAdapterǁget_daily_costs__mutmut_1(self, days: int) -> list[DailyCostData]:
        return self._get_cost_forecast_adapter().get_daily_costs(None)

    # ── ZombieDetectionPort ───────────────────────────────────
    @_mutmut_mutated(mutants_xǁVanillaAdapterǁget_zombie_workloads__mutmut)
    def get_zombie_workloads(self, window_hours: int) -> list[ZombiePodData]:
        return self._get_zombie_adapter().get_zombie_workloads(window_hours)

    # ── ZombieDetectionPort ───────────────────────────────────
    def xǁVanillaAdapterǁget_zombie_workloads__mutmut_orig(self, window_hours: int) -> list[ZombiePodData]:
        return self._get_zombie_adapter().get_zombie_workloads(window_hours)

    # ── ZombieDetectionPort ───────────────────────────────────
    def xǁVanillaAdapterǁget_zombie_workloads__mutmut_1(self, window_hours: int) -> list[ZombiePodData]:
        return self._get_zombie_adapter().get_zombie_workloads(None)

    # ── CostSavingEstimationPort ──────────────────────────────
    def get_pod_resource_data(self) -> list[PodResourceData]:
        return self._get_cost_saving_adapter().get_pod_resource_data()

    def get_previous_total_saving(self) -> float | None:
        return self._get_cost_saving_adapter().get_previous_total_saving()

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁstore_total_saving__mutmut)
    def store_total_saving(self, total_saving_usd: float) -> None:
        return self._get_cost_saving_adapter().store_total_saving(total_saving_usd)

    def xǁVanillaAdapterǁstore_total_saving__mutmut_orig(self, total_saving_usd: float) -> None:
        return self._get_cost_saving_adapter().store_total_saving(total_saving_usd)

    def xǁVanillaAdapterǁstore_total_saving__mutmut_1(self, total_saving_usd: float) -> None:
        return self._get_cost_saving_adapter().store_total_saving(None)

    # ── WhatIfSimulationPort ──────────────────────────────────
    @_mutmut_mutated(mutants_xǁVanillaAdapterǁget_current_replicas__mutmut)
    def get_current_replicas(self, namespace: str, service_name: str) -> int:
        return self._get_what_if_adapter().get_current_replicas(namespace, service_name)

    # ── WhatIfSimulationPort ──────────────────────────────────
    def xǁVanillaAdapterǁget_current_replicas__mutmut_orig(self, namespace: str, service_name: str) -> int:
        return self._get_what_if_adapter().get_current_replicas(namespace, service_name)

    # ── WhatIfSimulationPort ──────────────────────────────────
    def xǁVanillaAdapterǁget_current_replicas__mutmut_1(self, namespace: str, service_name: str) -> int:
        return self._get_what_if_adapter().get_current_replicas(None, service_name)

    # ── WhatIfSimulationPort ──────────────────────────────────
    def xǁVanillaAdapterǁget_current_replicas__mutmut_2(self, namespace: str, service_name: str) -> int:
        return self._get_what_if_adapter().get_current_replicas(namespace, None)

    # ── WhatIfSimulationPort ──────────────────────────────────
    def xǁVanillaAdapterǁget_current_replicas__mutmut_3(self, namespace: str, service_name: str) -> int:
        return self._get_what_if_adapter().get_current_replicas(service_name)

    # ── WhatIfSimulationPort ──────────────────────────────────
    def xǁVanillaAdapterǁget_current_replicas__mutmut_4(self, namespace: str, service_name: str) -> int:
        return self._get_what_if_adapter().get_current_replicas(namespace, )

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁget_current_cpu_utilization__mutmut)
    def get_current_cpu_utilization(self, namespace: str, service_name: str) -> float:
        return self._get_what_if_adapter().get_current_cpu_utilization(namespace, service_name)

    def xǁVanillaAdapterǁget_current_cpu_utilization__mutmut_orig(self, namespace: str, service_name: str) -> float:
        return self._get_what_if_adapter().get_current_cpu_utilization(namespace, service_name)

    def xǁVanillaAdapterǁget_current_cpu_utilization__mutmut_1(self, namespace: str, service_name: str) -> float:
        return self._get_what_if_adapter().get_current_cpu_utilization(None, service_name)

    def xǁVanillaAdapterǁget_current_cpu_utilization__mutmut_2(self, namespace: str, service_name: str) -> float:
        return self._get_what_if_adapter().get_current_cpu_utilization(namespace, None)

    def xǁVanillaAdapterǁget_current_cpu_utilization__mutmut_3(self, namespace: str, service_name: str) -> float:
        return self._get_what_if_adapter().get_current_cpu_utilization(service_name)

    def xǁVanillaAdapterǁget_current_cpu_utilization__mutmut_4(self, namespace: str, service_name: str) -> float:
        return self._get_what_if_adapter().get_current_cpu_utilization(namespace, )

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁget_pdb_info__mutmut)
    def get_pdb_info(self, namespace: str, service_name: str) -> PDBData | None:
        return self._get_what_if_adapter().get_pdb_info(namespace, service_name)

    def xǁVanillaAdapterǁget_pdb_info__mutmut_orig(self, namespace: str, service_name: str) -> PDBData | None:
        return self._get_what_if_adapter().get_pdb_info(namespace, service_name)

    def xǁVanillaAdapterǁget_pdb_info__mutmut_1(self, namespace: str, service_name: str) -> PDBData | None:
        return self._get_what_if_adapter().get_pdb_info(None, service_name)

    def xǁVanillaAdapterǁget_pdb_info__mutmut_2(self, namespace: str, service_name: str) -> PDBData | None:
        return self._get_what_if_adapter().get_pdb_info(namespace, None)

    def xǁVanillaAdapterǁget_pdb_info__mutmut_3(self, namespace: str, service_name: str) -> PDBData | None:
        return self._get_what_if_adapter().get_pdb_info(service_name)

    def xǁVanillaAdapterǁget_pdb_info__mutmut_4(self, namespace: str, service_name: str) -> PDBData | None:
        return self._get_what_if_adapter().get_pdb_info(namespace, )

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁget_hpa_info__mutmut)
    def get_hpa_info(self, namespace: str, service_name: str) -> HPAData | None:
        return self._get_what_if_adapter().get_hpa_info(namespace, service_name)

    def xǁVanillaAdapterǁget_hpa_info__mutmut_orig(self, namespace: str, service_name: str) -> HPAData | None:
        return self._get_what_if_adapter().get_hpa_info(namespace, service_name)

    def xǁVanillaAdapterǁget_hpa_info__mutmut_1(self, namespace: str, service_name: str) -> HPAData | None:
        return self._get_what_if_adapter().get_hpa_info(None, service_name)

    def xǁVanillaAdapterǁget_hpa_info__mutmut_2(self, namespace: str, service_name: str) -> HPAData | None:
        return self._get_what_if_adapter().get_hpa_info(namespace, None)

    def xǁVanillaAdapterǁget_hpa_info__mutmut_3(self, namespace: str, service_name: str) -> HPAData | None:
        return self._get_what_if_adapter().get_hpa_info(service_name)

    def xǁVanillaAdapterǁget_hpa_info__mutmut_4(self, namespace: str, service_name: str) -> HPAData | None:
        return self._get_what_if_adapter().get_hpa_info(namespace, )

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁget_service_topology__mutmut)
    def get_service_topology(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        return self._get_what_if_adapter().get_service_topology(namespace, service_name)

    def xǁVanillaAdapterǁget_service_topology__mutmut_orig(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        return self._get_what_if_adapter().get_service_topology(namespace, service_name)

    def xǁVanillaAdapterǁget_service_topology__mutmut_1(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        return self._get_what_if_adapter().get_service_topology(None, service_name)

    def xǁVanillaAdapterǁget_service_topology__mutmut_2(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        return self._get_what_if_adapter().get_service_topology(namespace, None)

    def xǁVanillaAdapterǁget_service_topology__mutmut_3(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        return self._get_what_if_adapter().get_service_topology(service_name)

    def xǁVanillaAdapterǁget_service_topology__mutmut_4(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        return self._get_what_if_adapter().get_service_topology(namespace, )

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁget_dependency_graph__mutmut)
    def get_dependency_graph(self, namespace: str) -> dict[str, list[str]]:
        return self._get_what_if_adapter().get_dependency_graph(namespace)

    def xǁVanillaAdapterǁget_dependency_graph__mutmut_orig(self, namespace: str) -> dict[str, list[str]]:
        return self._get_what_if_adapter().get_dependency_graph(namespace)

    def xǁVanillaAdapterǁget_dependency_graph__mutmut_1(self, namespace: str) -> dict[str, list[str]]:
        return self._get_what_if_adapter().get_dependency_graph(None)

    @_mutmut_mutated(mutants_xǁVanillaAdapterǁget_probe_audit_data__mutmut)
    def get_probe_audit_data(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        return self._get_what_if_adapter().get_probe_audit_data(namespace)

    def xǁVanillaAdapterǁget_probe_audit_data__mutmut_orig(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        return self._get_what_if_adapter().get_probe_audit_data(namespace)

    def xǁVanillaAdapterǁget_probe_audit_data__mutmut_1(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        return self._get_what_if_adapter().get_probe_audit_data(None)

mutants_xǁVanillaAdapterǁ__init____mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_5'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_6'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_7'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_8'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_9'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_10'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_11'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_12'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_13'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_14'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_15'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_16'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_17'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_18'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_19'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ__init____mutmut['xǁVanillaAdapterǁ__init____mutmut_20'] = VanillaAdapter.xǁVanillaAdapterǁ__init____mutmut_20 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁ_get_k8s_adapter__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_k8s_adapter__mutmut['xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_k8s_adapter__mutmut['xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_k8s_adapter__mutmut['xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_k8s_adapter__mutmut['xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_k8s_adapter__mutmut['xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_5'] = VanillaAdapter.xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_k8s_adapter__mutmut['xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_6'] = VanillaAdapter.xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_k8s_adapter__mutmut['xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_7'] = VanillaAdapter.xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_k8s_adapter__mutmut['xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_8'] = VanillaAdapter.xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_k8s_adapter__mutmut['xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_9'] = VanillaAdapter.xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_k8s_adapter__mutmut['xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_10'] = VanillaAdapter.xǁVanillaAdapterǁ_get_k8s_adapter__mutmut_10 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁ_get_health_adapter__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁ_get_health_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_health_adapter__mutmut['xǁVanillaAdapterǁ_get_health_adapter__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁ_get_health_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_health_adapter__mutmut['xǁVanillaAdapterǁ_get_health_adapter__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁ_get_health_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_health_adapter__mutmut['xǁVanillaAdapterǁ_get_health_adapter__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁ_get_health_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_health_adapter__mutmut['xǁVanillaAdapterǁ_get_health_adapter__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁ_get_health_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_health_adapter__mutmut['xǁVanillaAdapterǁ_get_health_adapter__mutmut_5'] = VanillaAdapter.xǁVanillaAdapterǁ_get_health_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_health_adapter__mutmut['xǁVanillaAdapterǁ_get_health_adapter__mutmut_6'] = VanillaAdapter.xǁVanillaAdapterǁ_get_health_adapter__mutmut_6 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut['xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut['xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut['xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut['xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut['xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_5'] = VanillaAdapter.xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut['xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_6'] = VanillaAdapter.xǁVanillaAdapterǁ_get_cost_forecast_adapter__mutmut_6 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁ_get_zombie_adapter__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_zombie_adapter__mutmut['xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_zombie_adapter__mutmut['xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_zombie_adapter__mutmut['xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_zombie_adapter__mutmut['xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_zombie_adapter__mutmut['xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_5'] = VanillaAdapter.xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_zombie_adapter__mutmut['xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_6'] = VanillaAdapter.xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_zombie_adapter__mutmut['xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_7'] = VanillaAdapter.xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_zombie_adapter__mutmut['xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_8'] = VanillaAdapter.xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_zombie_adapter__mutmut['xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_9'] = VanillaAdapter.xǁVanillaAdapterǁ_get_zombie_adapter__mutmut_9 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut['xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut['xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut['xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut['xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut['xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_5'] = VanillaAdapter.xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut['xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_6'] = VanillaAdapter.xǁVanillaAdapterǁ_get_namespace_waste_adapter__mutmut_6 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut['xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut['xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut['xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut['xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut['xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_5'] = VanillaAdapter.xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut['xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_6'] = VanillaAdapter.xǁVanillaAdapterǁ_get_rightsizing_adapter__mutmut_6 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut['xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut['xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut['xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut['xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut['xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_5'] = VanillaAdapter.xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut['xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_6'] = VanillaAdapter.xǁVanillaAdapterǁ_get_cost_saving_adapter__mutmut_6 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁ_get_what_if_adapter__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_what_if_adapter__mutmut['xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_what_if_adapter__mutmut['xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_what_if_adapter__mutmut['xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_what_if_adapter__mutmut['xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_what_if_adapter__mutmut['xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_5'] = VanillaAdapter.xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_what_if_adapter__mutmut['xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_6'] = VanillaAdapter.xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_what_if_adapter__mutmut['xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_7'] = VanillaAdapter.xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_what_if_adapter__mutmut['xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_8'] = VanillaAdapter.xǁVanillaAdapterǁ_get_what_if_adapter__mutmut_8 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁ_get_tekton_adapter__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁ_get_tekton_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_tekton_adapter__mutmut['xǁVanillaAdapterǁ_get_tekton_adapter__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁ_get_tekton_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_tekton_adapter__mutmut['xǁVanillaAdapterǁ_get_tekton_adapter__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁ_get_tekton_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_tekton_adapter__mutmut['xǁVanillaAdapterǁ_get_tekton_adapter__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁ_get_tekton_adapter__mutmut_3 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut['xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut['xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut['xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut['xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut['xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_5'] = VanillaAdapter.xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut['xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_6'] = VanillaAdapter.xǁVanillaAdapterǁ_get_pod_metrics_adapter__mutmut_6 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁlist_pods__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁlist_pods__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁlist_pods__mutmut['xǁVanillaAdapterǁlist_pods__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁlist_pods__mutmut_1 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁlist_ingresses__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁlist_ingresses__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁlist_ingresses__mutmut['xǁVanillaAdapterǁlist_ingresses__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁlist_ingresses__mutmut_1 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁget_pod_metrics__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁget_pod_metrics__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_pod_metrics__mutmut['xǁVanillaAdapterǁget_pod_metrics__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁget_pod_metrics__mutmut_1 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁlist_task_runs__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁlist_task_runs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁlist_task_runs__mutmut['xǁVanillaAdapterǁlist_task_runs__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁlist_task_runs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁlist_task_runs__mutmut['xǁVanillaAdapterǁlist_task_runs__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁlist_task_runs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁlist_task_runs__mutmut['xǁVanillaAdapterǁlist_task_runs__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁlist_task_runs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁlist_task_runs__mutmut['xǁVanillaAdapterǁlist_task_runs__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁlist_task_runs__mutmut_4 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁlist_pipeline_runs__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁlist_pipeline_runs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁlist_pipeline_runs__mutmut['xǁVanillaAdapterǁlist_pipeline_runs__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁlist_pipeline_runs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁlist_pipeline_runs__mutmut['xǁVanillaAdapterǁlist_pipeline_runs__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁlist_pipeline_runs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁlist_pipeline_runs__mutmut['xǁVanillaAdapterǁlist_pipeline_runs__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁlist_pipeline_runs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁlist_pipeline_runs__mutmut['xǁVanillaAdapterǁlist_pipeline_runs__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁlist_pipeline_runs__mutmut_4 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut['xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut['xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut['xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut['xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁlist_pipeline_runs_in_namespace__mutmut_4 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁget_all_namespace_waste_data__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁget_all_namespace_waste_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_all_namespace_waste_data__mutmut['xǁVanillaAdapterǁget_all_namespace_waste_data__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁget_all_namespace_waste_data__mutmut_1 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁ_apps_api_client__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁ_apps_api_client__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_apps_api_client__mutmut['xǁVanillaAdapterǁ_apps_api_client__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁ_apps_api_client__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_apps_api_client__mutmut['xǁVanillaAdapterǁ_apps_api_client__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁ_apps_api_client__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_apps_api_client__mutmut['xǁVanillaAdapterǁ_apps_api_client__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁ_apps_api_client__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_apps_api_client__mutmut['xǁVanillaAdapterǁ_apps_api_client__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁ_apps_api_client__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_apps_api_client__mutmut['xǁVanillaAdapterǁ_apps_api_client__mutmut_5'] = VanillaAdapter.xǁVanillaAdapterǁ_apps_api_client__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_apps_api_client__mutmut['xǁVanillaAdapterǁ_apps_api_client__mutmut_6'] = VanillaAdapter.xǁVanillaAdapterǁ_apps_api_client__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_apps_api_client__mutmut['xǁVanillaAdapterǁ_apps_api_client__mutmut_7'] = VanillaAdapter.xǁVanillaAdapterǁ_apps_api_client__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_apps_api_client__mutmut['xǁVanillaAdapterǁ_apps_api_client__mutmut_8'] = VanillaAdapter.xǁVanillaAdapterǁ_apps_api_client__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_apps_api_client__mutmut['xǁVanillaAdapterǁ_apps_api_client__mutmut_9'] = VanillaAdapter.xǁVanillaAdapterǁ_apps_api_client__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_apps_api_client__mutmut['xǁVanillaAdapterǁ_apps_api_client__mutmut_10'] = VanillaAdapter.xǁVanillaAdapterǁ_apps_api_client__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_apps_api_client__mutmut['xǁVanillaAdapterǁ_apps_api_client__mutmut_11'] = VanillaAdapter.xǁVanillaAdapterǁ_apps_api_client__mutmut_11 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁ_api_client__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁ_api_client__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_api_client__mutmut['xǁVanillaAdapterǁ_api_client__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁ_api_client__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_api_client__mutmut['xǁVanillaAdapterǁ_api_client__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁ_api_client__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_api_client__mutmut['xǁVanillaAdapterǁ_api_client__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁ_api_client__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_api_client__mutmut['xǁVanillaAdapterǁ_api_client__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁ_api_client__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_api_client__mutmut['xǁVanillaAdapterǁ_api_client__mutmut_5'] = VanillaAdapter.xǁVanillaAdapterǁ_api_client__mutmut_5 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁ_metrics_api_client__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁ_metrics_api_client__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_metrics_api_client__mutmut['xǁVanillaAdapterǁ_metrics_api_client__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁ_metrics_api_client__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_metrics_api_client__mutmut['xǁVanillaAdapterǁ_metrics_api_client__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁ_metrics_api_client__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_metrics_api_client__mutmut['xǁVanillaAdapterǁ_metrics_api_client__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁ_metrics_api_client__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_metrics_api_client__mutmut['xǁVanillaAdapterǁ_metrics_api_client__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁ_metrics_api_client__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_metrics_api_client__mutmut['xǁVanillaAdapterǁ_metrics_api_client__mutmut_5'] = VanillaAdapter.xǁVanillaAdapterǁ_metrics_api_client__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_metrics_api_client__mutmut['xǁVanillaAdapterǁ_metrics_api_client__mutmut_6'] = VanillaAdapter.xǁVanillaAdapterǁ_metrics_api_client__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_metrics_api_client__mutmut['xǁVanillaAdapterǁ_metrics_api_client__mutmut_7'] = VanillaAdapter.xǁVanillaAdapterǁ_metrics_api_client__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_metrics_api_client__mutmut['xǁVanillaAdapterǁ_metrics_api_client__mutmut_8'] = VanillaAdapter.xǁVanillaAdapterǁ_metrics_api_client__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_metrics_api_client__mutmut['xǁVanillaAdapterǁ_metrics_api_client__mutmut_9'] = VanillaAdapter.xǁVanillaAdapterǁ_metrics_api_client__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_metrics_api_client__mutmut['xǁVanillaAdapterǁ_metrics_api_client__mutmut_10'] = VanillaAdapter.xǁVanillaAdapterǁ_metrics_api_client__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_metrics_api_client__mutmut['xǁVanillaAdapterǁ_metrics_api_client__mutmut_11'] = VanillaAdapter.xǁVanillaAdapterǁ_metrics_api_client__mutmut_11 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁ_crd_api_client__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁ_crd_api_client__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_crd_api_client__mutmut['xǁVanillaAdapterǁ_crd_api_client__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁ_crd_api_client__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_crd_api_client__mutmut['xǁVanillaAdapterǁ_crd_api_client__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁ_crd_api_client__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_crd_api_client__mutmut['xǁVanillaAdapterǁ_crd_api_client__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁ_crd_api_client__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_crd_api_client__mutmut['xǁVanillaAdapterǁ_crd_api_client__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁ_crd_api_client__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_crd_api_client__mutmut['xǁVanillaAdapterǁ_crd_api_client__mutmut_5'] = VanillaAdapter.xǁVanillaAdapterǁ_crd_api_client__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_crd_api_client__mutmut['xǁVanillaAdapterǁ_crd_api_client__mutmut_6'] = VanillaAdapter.xǁVanillaAdapterǁ_crd_api_client__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_crd_api_client__mutmut['xǁVanillaAdapterǁ_crd_api_client__mutmut_7'] = VanillaAdapter.xǁVanillaAdapterǁ_crd_api_client__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_crd_api_client__mutmut['xǁVanillaAdapterǁ_crd_api_client__mutmut_8'] = VanillaAdapter.xǁVanillaAdapterǁ_crd_api_client__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_crd_api_client__mutmut['xǁVanillaAdapterǁ_crd_api_client__mutmut_9'] = VanillaAdapter.xǁVanillaAdapterǁ_crd_api_client__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_crd_api_client__mutmut['xǁVanillaAdapterǁ_crd_api_client__mutmut_10'] = VanillaAdapter.xǁVanillaAdapterǁ_crd_api_client__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁ_crd_api_client__mutmut['xǁVanillaAdapterǁ_crd_api_client__mutmut_11'] = VanillaAdapter.xǁVanillaAdapterǁ_crd_api_client__mutmut_11 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁget_daily_costs__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁget_daily_costs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_daily_costs__mutmut['xǁVanillaAdapterǁget_daily_costs__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁget_daily_costs__mutmut_1 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁget_zombie_workloads__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁget_zombie_workloads__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_zombie_workloads__mutmut['xǁVanillaAdapterǁget_zombie_workloads__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁget_zombie_workloads__mutmut_1 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁstore_total_saving__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁstore_total_saving__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁstore_total_saving__mutmut['xǁVanillaAdapterǁstore_total_saving__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁstore_total_saving__mutmut_1 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁget_current_replicas__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁget_current_replicas__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_current_replicas__mutmut['xǁVanillaAdapterǁget_current_replicas__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁget_current_replicas__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_current_replicas__mutmut['xǁVanillaAdapterǁget_current_replicas__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁget_current_replicas__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_current_replicas__mutmut['xǁVanillaAdapterǁget_current_replicas__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁget_current_replicas__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_current_replicas__mutmut['xǁVanillaAdapterǁget_current_replicas__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁget_current_replicas__mutmut_4 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁget_current_cpu_utilization__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁget_current_cpu_utilization__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaAdapterǁget_current_cpu_utilization__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁget_current_cpu_utilization__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaAdapterǁget_current_cpu_utilization__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁget_current_cpu_utilization__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaAdapterǁget_current_cpu_utilization__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁget_current_cpu_utilization__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaAdapterǁget_current_cpu_utilization__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁget_current_cpu_utilization__mutmut_4 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁget_pdb_info__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁget_pdb_info__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_pdb_info__mutmut['xǁVanillaAdapterǁget_pdb_info__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁget_pdb_info__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_pdb_info__mutmut['xǁVanillaAdapterǁget_pdb_info__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁget_pdb_info__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_pdb_info__mutmut['xǁVanillaAdapterǁget_pdb_info__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁget_pdb_info__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_pdb_info__mutmut['xǁVanillaAdapterǁget_pdb_info__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁget_pdb_info__mutmut_4 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁget_hpa_info__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁget_hpa_info__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_hpa_info__mutmut['xǁVanillaAdapterǁget_hpa_info__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁget_hpa_info__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_hpa_info__mutmut['xǁVanillaAdapterǁget_hpa_info__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁget_hpa_info__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_hpa_info__mutmut['xǁVanillaAdapterǁget_hpa_info__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁget_hpa_info__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_hpa_info__mutmut['xǁVanillaAdapterǁget_hpa_info__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁget_hpa_info__mutmut_4 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁget_service_topology__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁget_service_topology__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_service_topology__mutmut['xǁVanillaAdapterǁget_service_topology__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁget_service_topology__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_service_topology__mutmut['xǁVanillaAdapterǁget_service_topology__mutmut_2'] = VanillaAdapter.xǁVanillaAdapterǁget_service_topology__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_service_topology__mutmut['xǁVanillaAdapterǁget_service_topology__mutmut_3'] = VanillaAdapter.xǁVanillaAdapterǁget_service_topology__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_service_topology__mutmut['xǁVanillaAdapterǁget_service_topology__mutmut_4'] = VanillaAdapter.xǁVanillaAdapterǁget_service_topology__mutmut_4 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁget_dependency_graph__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁget_dependency_graph__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_dependency_graph__mutmut['xǁVanillaAdapterǁget_dependency_graph__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁget_dependency_graph__mutmut_1 # type: ignore # mutmut generated

mutants_xǁVanillaAdapterǁget_probe_audit_data__mutmut['_mutmut_orig'] = VanillaAdapter.xǁVanillaAdapterǁget_probe_audit_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaAdapterǁget_probe_audit_data__mutmut['xǁVanillaAdapterǁget_probe_audit_data__mutmut_1'] = VanillaAdapter.xǁVanillaAdapterǁget_probe_audit_data__mutmut_1 # type: ignore # mutmut generated
