from __future__ import annotations

from collections import defaultdict

from hexawyn.application.ports.driven.k8s_port import K8sPort, PodInfo
from hexawyn.application.ports.driven.pod_metrics_port import (
    PodMetricSnapshot,
    PodMetricsPort,
)
from hexawyn.application.use_case.cluster.get_resource_usage.command import (
    GetResourceUsageCommand,
)
from hexawyn.application.use_case.cluster.get_resource_usage.response import (
    GetResourceUsageResponse,
)
from hexawyn.domain.errors import MetricsUnavailableError
from hexawyn.domain.models.resource_usage import (
    NamespaceResourceUsageSummary,
    PodResourceUsage,
)

_MILLICORE_TO_CORE: float = 1.0 / 1000.0
_MIB_TO_GB: float = 1.0 / 1024.0
_SENTINEL_NO_REQUEST: float = -1.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGetResourceUsageUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut: MutantDict = {}  # type: ignore


class GetResourceUsageUseCase:
    """Compare actual resource usage (metrics-server) against requested resources (K8s spec)."""

    @_mutmut_mutated(mutants_xǁGetResourceUsageUseCaseǁ__init____mutmut)
    def __init__(self, k8s_port: K8sPort, metrics_port: PodMetricsPort) -> None:
        self._k8s = k8s_port
        self._metrics = metrics_port

    def xǁGetResourceUsageUseCaseǁ__init____mutmut_orig(self, k8s_port: K8sPort, metrics_port: PodMetricsPort) -> None:
        self._k8s = k8s_port
        self._metrics = metrics_port

    def xǁGetResourceUsageUseCaseǁ__init____mutmut_1(self, k8s_port: K8sPort, metrics_port: PodMetricsPort) -> None:
        self._k8s = None
        self._metrics = metrics_port

    def xǁGetResourceUsageUseCaseǁ__init____mutmut_2(self, k8s_port: K8sPort, metrics_port: PodMetricsPort) -> None:
        self._k8s = k8s_port
        self._metrics = None

    @_mutmut_mutated(mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut)
    def execute(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_orig(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_1(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = None
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_2(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=None)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_3(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = None

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_4(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource not in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_5(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("XXcpuXX", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_6(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("CPU", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_7(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "XXmemoryXX") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_8(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "MEMORY") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_9(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "XXbothXX"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_10(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "BOTH"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_11(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = None
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_12(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=None)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_13(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = None
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_14(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = False
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_15(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = None
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_16(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "XXmetrics-serverXX"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_17(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "METRICS-SERVER"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_18(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = None
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_19(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = None
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_20(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = True
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_21(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = None

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_22(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = "XXXX"

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_23(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = None

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_24(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["XXnameXX"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_25(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["NAME"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_26(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = None

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_27(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                None, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_28(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, None, resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_29(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), None, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_30(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, None
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_31(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_32(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_33(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_34(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_35(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(None), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_36(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get(None, "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_37(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", None)), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_38(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_39(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", )), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_40(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("XXnameXX", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_41(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("NAME", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_42(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "XXXX")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_43(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get(None)
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_44(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("XXnamespaceXX")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_45(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("NAMESPACE")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_46(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = None

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_47(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(None, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_48(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, None)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_49(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_50(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, )

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_51(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=None,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_52(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=None,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_53(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=None,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_54(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=None,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_55(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_56(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            metrics_server_available=metrics_available,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_57(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            source=source,
        )

    def xǁGetResourceUsageUseCaseǁexecute__mutmut_58(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            )

    @_mutmut_mutated(mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut)
    def _build_pod_usage(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_orig(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_1(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = None
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_2(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter not in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_3(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("XXcpuXX", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_4(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("CPU", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_5(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "XXbothXX")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_6(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "BOTH")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_7(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = None

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_8(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter not in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_9(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("XXmemoryXX", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_10(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("MEMORY", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_11(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "XXbothXX")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_12(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "BOTH")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_13(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = None
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_14(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") and 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_15(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get(None) or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_16(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("XXcpu_request_millicoresXX") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_17(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("CPU_REQUEST_MILLICORES") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_18(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 1
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_19(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = None
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_20(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") and 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_21(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get(None) or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_22(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("XXmemory_request_mibXX") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_23(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("MEMORY_REQUEST_MIB") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_24(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 1
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_25(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = None
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_26(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["XXcpu_coresXX"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_27(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["CPU_CORES"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_28(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 1.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_29(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = None

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_30(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["XXmemory_gbXX"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_31(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["MEMORY_GB"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_32(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 1.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_33(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = None
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_34(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores / _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_35(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = None

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_36(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib / _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_37(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = None
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_38(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "XXnameXX": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_39(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "NAME": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_40(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get(None, "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_41(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", None),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_42(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_43(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", ),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_44(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("XXnameXX", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_45(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("NAME", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_46(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "XXunknownXX"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_47(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "UNKNOWN"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_48(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "XXnamespaceXX": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_49(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "NAMESPACE": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_50(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get(None, "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_51(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", None),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_52(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_53(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", ),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_54(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("XXnamespaceXX", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_55(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("NAMESPACE", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_56(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "XXunknownXX"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_57(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "UNKNOWN"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_58(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "XXcpu_requested_coresXX": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_59(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "CPU_REQUESTED_CORES": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_60(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(None, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_61(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, None) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_62(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_63(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, ) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_64(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 3) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_65(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 1.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_66(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "XXcpu_used_coresXX": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_67(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "CPU_USED_CORES": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_68(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(None, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_69(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, None) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_70(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_71(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, ) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_72(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 3) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_73(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 1.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_74(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "XXcpu_utilization_pctXX": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_75(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "CPU_UTILIZATION_PCT": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_76(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                None, 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_77(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), None
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_78(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_79(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_80(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(None, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_81(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, None, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_82(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, None), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_83(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_84(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_85(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, ), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_86(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 2
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_87(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 1.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_88(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "XXmemory_requested_gbXX": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_89(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "MEMORY_REQUESTED_GB": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_90(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(None, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_91(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, None) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_92(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_93(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, ) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_94(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 3) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_95(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 1.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_96(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "XXmemory_used_gbXX": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_97(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "MEMORY_USED_GB": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_98(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(None, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_99(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, None) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_100(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_101(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, ) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_102(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 3) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_103(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 1.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_104(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "XXmemory_utilization_pctXX": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_105(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "MEMORY_UTILIZATION_PCT": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_106(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                None, 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_107(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), None
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_108(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_109(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_110(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(None, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_111(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, None, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_112(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, None), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_113(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_114(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_115(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, ), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_116(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 2
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_117(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 1.0,
        }
        return pod_usage

    @_mutmut_mutated(mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut)
    def _build_namespace_summaries(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_orig(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_1(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = None
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_2(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(None)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_3(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = None
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_4(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(None)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_5(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = None
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_6(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(None)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_7(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = None
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_8(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(None)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_9(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = None

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_10(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(None)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_11(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = None
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_12(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["XXnamespaceXX"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_13(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["NAMESPACE"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_14(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] = 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_15(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] -= 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_16(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 2
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_17(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] = p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_18(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] -= p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_19(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["XXcpu_requested_coresXX"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_20(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["CPU_REQUESTED_CORES"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_21(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] = p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_22(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] -= p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_23(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["XXcpu_used_coresXX"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_24(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["CPU_USED_CORES"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_25(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] = p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_26(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] -= p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_27(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["XXmemory_requested_gbXX"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_28(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["MEMORY_REQUESTED_GB"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_29(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] = p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_30(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] -= p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_31(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["XXmemory_used_gbXX"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_32(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["MEMORY_USED_GB"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_33(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = None
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_34(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                None
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_35(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=None,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_36(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=None,
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_37(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=None,
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_38(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=None,
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_39(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=None,
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_40(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=None,
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_41(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=None,
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_42(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=None,
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_43(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_44(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_45(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_46(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_47(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_48(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_49(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_50(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_51(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(None, 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_52(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], None),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_53(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_54(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], ),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_55(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 3),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_56(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(None, 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_57(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], None),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_58(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_59(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], ),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_60(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 3),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_61(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        None, 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_62(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), None
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_63(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_64(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_65(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(None, ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_66(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], None, metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_67(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], None), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_68(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_69(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_70(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], ), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_71(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 2
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_72(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(None, 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_73(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], None),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_74(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_75(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], ),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_76(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 3),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_77(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(None, 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_78(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], None),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_79(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_80(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], ),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_81(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 3),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_82(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        None, 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_83(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), None
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_84(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_85(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_86(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(None, ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_87(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], None, metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_88(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], None), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_89(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_90(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_91(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], ), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_92(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 2
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_93(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=None, reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_94(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=None)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_95(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_96(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], )
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_97(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: None, reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_98(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["XXtotal_cpu_requested_coresXX"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_99(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["TOTAL_CPU_REQUESTED_CORES"], reverse=True)
        return summaries

    def xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_100(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=False)
        return summaries

    @staticmethod
    @_mutmut_mutated(mutants_xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut)
    def _utilization_pct(used: float, requested: float, metrics_available: bool = True) -> float:
        if not metrics_available:
            return _SENTINEL_NO_REQUEST
        if requested <= 0:
            return _SENTINEL_NO_REQUEST
        return (used / requested) * 100.0

    @staticmethod
    def xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_orig(used: float, requested: float, metrics_available: bool = True) -> float:
        if not metrics_available:
            return _SENTINEL_NO_REQUEST
        if requested <= 0:
            return _SENTINEL_NO_REQUEST
        return (used / requested) * 100.0

    @staticmethod
    def xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_1(used: float, requested: float, metrics_available: bool = False) -> float:
        if not metrics_available:
            return _SENTINEL_NO_REQUEST
        if requested <= 0:
            return _SENTINEL_NO_REQUEST
        return (used / requested) * 100.0

    @staticmethod
    def xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_2(used: float, requested: float, metrics_available: bool = True) -> float:
        if metrics_available:
            return _SENTINEL_NO_REQUEST
        if requested <= 0:
            return _SENTINEL_NO_REQUEST
        return (used / requested) * 100.0

    @staticmethod
    def xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_3(used: float, requested: float, metrics_available: bool = True) -> float:
        if not metrics_available:
            return _SENTINEL_NO_REQUEST
        if requested < 0:
            return _SENTINEL_NO_REQUEST
        return (used / requested) * 100.0

    @staticmethod
    def xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_4(used: float, requested: float, metrics_available: bool = True) -> float:
        if not metrics_available:
            return _SENTINEL_NO_REQUEST
        if requested <= 1:
            return _SENTINEL_NO_REQUEST
        return (used / requested) * 100.0

    @staticmethod
    def xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_5(used: float, requested: float, metrics_available: bool = True) -> float:
        if not metrics_available:
            return _SENTINEL_NO_REQUEST
        if requested <= 0:
            return _SENTINEL_NO_REQUEST
        return (used / requested) / 100.0

    @staticmethod
    def xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_6(used: float, requested: float, metrics_available: bool = True) -> float:
        if not metrics_available:
            return _SENTINEL_NO_REQUEST
        if requested <= 0:
            return _SENTINEL_NO_REQUEST
        return (used * requested) * 100.0

    @staticmethod
    def xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_7(used: float, requested: float, metrics_available: bool = True) -> float:
        if not metrics_available:
            return _SENTINEL_NO_REQUEST
        if requested <= 0:
            return _SENTINEL_NO_REQUEST
        return (used / requested) * 101.0

mutants_xǁGetResourceUsageUseCaseǁ__init____mutmut['_mutmut_orig'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ__init____mutmut['xǁGetResourceUsageUseCaseǁ__init____mutmut_1'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ__init____mutmut['xǁGetResourceUsageUseCaseǁ__init____mutmut_2'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['_mutmut_orig'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_1'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_2'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_3'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_4'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_5'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_6'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_7'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_8'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_9'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_10'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_11'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_12'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_13'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_14'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_15'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_16'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_17'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_18'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_19'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_20'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_21'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_22'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_23'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_24'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_25'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_26'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_27'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_28'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_29'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_30'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_31'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_32'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_33'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_34'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_35'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_36'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_37'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_38'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_39'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_40'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_41'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_42'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_43'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_44'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_45'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_46'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_47'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_48'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_49'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_50'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_51'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_52'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_53'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_54'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_55'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_56'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_57'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_57 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁexecute__mutmut['xǁGetResourceUsageUseCaseǁexecute__mutmut_58'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁexecute__mutmut_58 # type: ignore # mutmut generated

mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['_mutmut_orig'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_1'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_2'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_3'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_4'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_5'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_6'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_7'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_8'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_9'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_10'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_11'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_12'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_13'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_14'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_15'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_16'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_17'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_18'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_19'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_20'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_21'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_22'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_23'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_24'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_25'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_26'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_27'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_28'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_29'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_30'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_31'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_32'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_33'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_34'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_35'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_36'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_37'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_38'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_39'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_40'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_41'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_42'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_42 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_43'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_43 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_44'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_44 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_45'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_45 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_46'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_46 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_47'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_47 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_48'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_48 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_49'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_49 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_50'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_50 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_51'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_51 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_52'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_52 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_53'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_53 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_54'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_54 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_55'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_55 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_56'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_56 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_57'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_57 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_58'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_58 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_59'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_59 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_60'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_60 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_61'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_61 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_62'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_62 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_63'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_63 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_64'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_64 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_65'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_65 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_66'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_66 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_67'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_67 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_68'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_68 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_69'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_69 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_70'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_70 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_71'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_71 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_72'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_72 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_73'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_73 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_74'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_74 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_75'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_75 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_76'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_76 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_77'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_77 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_78'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_78 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_79'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_79 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_80'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_80 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_81'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_81 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_82'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_82 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_83'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_83 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_84'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_84 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_85'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_85 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_86'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_86 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_87'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_87 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_88'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_88 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_89'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_89 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_90'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_90 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_91'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_91 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_92'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_92 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_93'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_93 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_94'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_94 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_95'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_95 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_96'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_96 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_97'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_97 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_98'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_98 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_99'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_99 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_100'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_100 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_101'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_101 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_102'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_102 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_103'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_103 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_104'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_104 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_105'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_105 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_106'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_106 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_107'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_107 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_108'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_108 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_109'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_109 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_110'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_110 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_111'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_111 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_112'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_112 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_113'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_113 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_114'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_114 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_115'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_115 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_116'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_116 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut['xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_117'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_pod_usage__mutmut_117 # type: ignore # mutmut generated

mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['_mutmut_orig'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_1'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_2'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_3'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_4'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_5'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_6'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_7'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_8'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_9'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_10'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_11'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_12'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_13'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_14'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_15'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_16'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_17'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_18'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_19'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_20'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_21'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_22'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_23'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_24'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_25'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_26'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_27'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_28'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_29'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_30'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_31'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_32'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_33'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_34'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_35'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_36'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_37'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_38'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_39'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_40'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_41'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_42'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_42 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_43'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_43 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_44'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_44 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_45'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_45 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_46'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_46 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_47'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_47 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_48'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_48 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_49'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_49 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_50'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_50 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_51'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_51 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_52'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_52 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_53'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_53 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_54'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_54 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_55'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_55 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_56'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_56 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_57'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_57 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_58'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_58 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_59'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_59 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_60'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_60 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_61'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_61 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_62'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_62 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_63'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_63 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_64'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_64 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_65'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_65 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_66'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_66 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_67'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_67 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_68'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_68 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_69'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_69 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_70'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_70 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_71'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_71 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_72'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_72 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_73'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_73 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_74'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_74 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_75'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_75 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_76'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_76 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_77'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_77 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_78'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_78 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_79'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_79 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_80'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_80 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_81'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_81 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_82'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_82 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_83'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_83 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_84'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_84 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_85'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_85 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_86'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_86 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_87'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_87 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_88'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_88 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_89'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_89 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_90'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_90 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_91'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_91 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_92'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_92 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_93'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_93 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_94'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_94 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_95'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_95 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_96'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_96 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_97'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_97 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_98'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_98 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_99'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_99 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut['xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_100'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_build_namespace_summaries__mutmut_100 # type: ignore # mutmut generated

mutants_xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut['_mutmut_orig'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut['xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_1'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut['xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_2'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut['xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_3'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut['xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_4'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut['xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_5'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut['xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_6'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut['xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_7'] = GetResourceUsageUseCase.xǁGetResourceUsageUseCaseǁ_utilization_pct__mutmut_7 # type: ignore # mutmut generated
