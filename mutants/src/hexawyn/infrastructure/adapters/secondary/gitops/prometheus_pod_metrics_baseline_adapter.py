from __future__ import annotations

from datetime import UTC, datetime, timedelta

from hexawyn.application.ports.driven.k8s_port import K8sPort, PodInfo
from hexawyn.application.ports.driven.metrics_query_port import (
    MetricsQueryPort,
    PrometheusRangeSample,
)
from hexawyn.application.ports.driven.pod_metrics_baseline_port import (
    PodMetricsBaselinePort,
    PodMetricsRawData,
)

_QUERY_TIMEOUT_SECONDS = 30.0
_BASELINE_QUERY_STEP = "1h"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut: MutantDict = {}  # type: ignore


class PrometheusPodMetricsBaselineAdapter(PodMetricsBaselinePort):
    """Real Prometheus wiring: 3 bulk range queries (CPU, memory, error rate),
    one per metric for the whole namespace, matched to pods via K8sPort.

    Two fields cannot be honestly populated from this repo's current ports:
    `hours_since_last_restart` (no port exposes per-restart timestamps) and
    `is_scheduled_batch_job` (no port exposes pod owner references). Both
    always come back as their "unknown" default (None / False) — the domain
    layer already handles both correctly whenever a richer signal exists.
    """

    @_mutmut_mutated(mutants_xǁPrometheusPodMetricsBaselineAdapterǁ__init____mutmut)
    def __init__(self, metrics_query_port: MetricsQueryPort, k8s_port: K8sPort) -> None:
        self._metrics_query_port = metrics_query_port
        self._k8s_port = k8s_port

    def xǁPrometheusPodMetricsBaselineAdapterǁ__init____mutmut_orig(self, metrics_query_port: MetricsQueryPort, k8s_port: K8sPort) -> None:
        self._metrics_query_port = metrics_query_port
        self._k8s_port = k8s_port

    def xǁPrometheusPodMetricsBaselineAdapterǁ__init____mutmut_1(self, metrics_query_port: MetricsQueryPort, k8s_port: K8sPort) -> None:
        self._metrics_query_port = None
        self._k8s_port = k8s_port

    def xǁPrometheusPodMetricsBaselineAdapterǁ__init____mutmut_2(self, metrics_query_port: MetricsQueryPort, k8s_port: K8sPort) -> None:
        self._metrics_query_port = metrics_query_port
        self._k8s_port = None

    @_mutmut_mutated(mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut)
    def get_all_pod_metrics_data(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_orig(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_1(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = None
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_2(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=None)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_3(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = None

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_4(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(None)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_5(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = None
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_6(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(None, start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_7(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), None, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_8(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, None)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_9(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_10(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_11(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, )
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_12(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(None), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_13(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = None
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_14(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(None, start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_15(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), None, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_16(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, None)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_17(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_18(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_19(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, )
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_20(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(None), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_21(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = None

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_22(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(None, start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_23(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), None, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_24(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, None)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_25(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_26(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_27(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, )

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_28(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(None), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_29(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = None
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_30(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(None)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_31(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days / 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_32(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 25)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_33(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                None,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_34(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                None,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_35(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                None,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_36(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                None,
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_37(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                None,
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_38(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                None,
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_39(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_40(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_41(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_42(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_43(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_44(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_45(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(None),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_46(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["XXnameXX"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_47(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["NAME"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_48(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(None),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_49(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["XXnameXX"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_50(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["NAME"]),
                error_rate_by_pod.get(pod["name"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_51(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(None),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_52(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["XXnameXX"]),
            )
            for pod in pods
        ]

    def xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_53(self, namespace: str, window_days: int) -> list[PodMetricsRawData]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        start, end = _query_window(window_days)

        cpu_by_pod = self._range_query_by_pod(_cpu_query(namespace), start, end)
        memory_by_pod = self._range_query_by_pod(_memory_query(namespace), start, end)
        error_rate_by_pod = self._range_query_by_pod(_error_rate_query(namespace), start, end)

        baseline_window_hours = float(window_days * 24)
        return [
            _to_raw_data(
                pod,
                namespace,
                baseline_window_hours,
                cpu_by_pod.get(pod["name"]),
                memory_by_pod.get(pod["name"]),
                error_rate_by_pod.get(pod["NAME"]),
            )
            for pod in pods
        ]

    @_mutmut_mutated(mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut)
    def _range_query_by_pod(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=start,
            end=end,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["metric"].get("pod", ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_orig(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=start,
            end=end,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["metric"].get("pod", ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_1(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = None
        return {sample["metric"].get("pod", ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_2(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            None,
            start=start,
            end=end,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["metric"].get("pod", ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_3(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=None,
            end=end,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["metric"].get("pod", ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_4(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=start,
            end=None,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["metric"].get("pod", ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_5(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=start,
            end=end,
            step=None,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["metric"].get("pod", ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_6(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=start,
            end=end,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=None,
        )
        return {sample["metric"].get("pod", ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_7(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            start=start,
            end=end,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["metric"].get("pod", ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_8(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            end=end,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["metric"].get("pod", ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_9(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=start,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["metric"].get("pod", ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_10(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=start,
            end=end,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["metric"].get("pod", ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_11(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=start,
            end=end,
            step=_BASELINE_QUERY_STEP,
            )
        return {sample["metric"].get("pod", ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_12(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=start,
            end=end,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["metric"].get(None, ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_13(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=start,
            end=end,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["metric"].get("pod", None): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_14(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=start,
            end=end,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["metric"].get(""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_15(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=start,
            end=end,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["metric"].get("pod", ): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_16(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=start,
            end=end,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["XXmetricXX"].get("pod", ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_17(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=start,
            end=end,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["METRIC"].get("pod", ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_18(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=start,
            end=end,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["metric"].get("XXpodXX", ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_19(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=start,
            end=end,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["metric"].get("POD", ""): sample for sample in samples}

    def xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_20(
        self, promql: str, start: str, end: str
    ) -> dict[str, PrometheusRangeSample]:
        samples = self._metrics_query_port.range_query(
            promql,
            start=start,
            end=end,
            step=_BASELINE_QUERY_STEP,
            timeout_seconds=_QUERY_TIMEOUT_SECONDS,
        )
        return {sample["metric"].get("pod", "XXXX"): sample for sample in samples}

mutants_xǁPrometheusPodMetricsBaselineAdapterǁ__init____mutmut['_mutmut_orig'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ__init____mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ__init____mutmut_1'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ__init____mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ__init____mutmut_2'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['_mutmut_orig'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_1'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_2'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_3'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_4'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_5'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_6'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_7'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_8'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_9'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_10'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_11'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_12'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_13'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_14'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_15'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_16'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_17'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_18'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_19'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_20'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_21'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_22'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_23'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_24'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_25'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_26'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_27'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_28'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_28 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_29'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_29 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_30'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_30 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_31'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_31 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_32'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_32 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_33'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_33 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_34'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_34 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_35'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_35 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_36'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_36 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_37'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_37 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_38'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_38 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_39'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_39 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_40'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_40 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_41'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_41 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_42'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_42 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_43'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_43 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_44'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_44 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_45'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_45 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_46'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_46 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_47'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_47 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_48'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_48 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_49'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_49 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_50'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_50 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_51'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_51 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_52'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_52 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_53'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁget_all_pod_metrics_data__mutmut_53 # type: ignore # mutmut generated

mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['_mutmut_orig'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_1'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_2'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_3'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_4'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_5'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_6'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_7'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_8'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_9'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_10'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_11'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_12'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_13'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_14'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_15'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_16'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_17'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_18'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_19'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut['xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_20'] = PrometheusPodMetricsBaselineAdapter.xǁPrometheusPodMetricsBaselineAdapterǁ_range_query_by_pod__mutmut_20 # type: ignore # mutmut generated
mutants_x__query_window__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__query_window__mutmut)
def _query_window(window_days: int) -> tuple[str, str]:
    end = datetime.now(UTC)
    start = end - timedelta(days=window_days)
    return _to_iso(start), _to_iso(end)


def x__query_window__mutmut_orig(window_days: int) -> tuple[str, str]:
    end = datetime.now(UTC)
    start = end - timedelta(days=window_days)
    return _to_iso(start), _to_iso(end)


def x__query_window__mutmut_1(window_days: int) -> tuple[str, str]:
    end = None
    start = end - timedelta(days=window_days)
    return _to_iso(start), _to_iso(end)


def x__query_window__mutmut_2(window_days: int) -> tuple[str, str]:
    end = datetime.now(None)
    start = end - timedelta(days=window_days)
    return _to_iso(start), _to_iso(end)


def x__query_window__mutmut_3(window_days: int) -> tuple[str, str]:
    end = datetime.now(UTC)
    start = None
    return _to_iso(start), _to_iso(end)


def x__query_window__mutmut_4(window_days: int) -> tuple[str, str]:
    end = datetime.now(UTC)
    start = end + timedelta(days=window_days)
    return _to_iso(start), _to_iso(end)


def x__query_window__mutmut_5(window_days: int) -> tuple[str, str]:
    end = datetime.now(UTC)
    start = end - timedelta(days=None)
    return _to_iso(start), _to_iso(end)


def x__query_window__mutmut_6(window_days: int) -> tuple[str, str]:
    end = datetime.now(UTC)
    start = end - timedelta(days=window_days)
    return _to_iso(None), _to_iso(end)


def x__query_window__mutmut_7(window_days: int) -> tuple[str, str]:
    end = datetime.now(UTC)
    start = end - timedelta(days=window_days)
    return _to_iso(start), _to_iso(None)

mutants_x__query_window__mutmut['_mutmut_orig'] = x__query_window__mutmut_orig # type: ignore # mutmut generated
mutants_x__query_window__mutmut['x__query_window__mutmut_1'] = x__query_window__mutmut_1 # type: ignore # mutmut generated
mutants_x__query_window__mutmut['x__query_window__mutmut_2'] = x__query_window__mutmut_2 # type: ignore # mutmut generated
mutants_x__query_window__mutmut['x__query_window__mutmut_3'] = x__query_window__mutmut_3 # type: ignore # mutmut generated
mutants_x__query_window__mutmut['x__query_window__mutmut_4'] = x__query_window__mutmut_4 # type: ignore # mutmut generated
mutants_x__query_window__mutmut['x__query_window__mutmut_5'] = x__query_window__mutmut_5 # type: ignore # mutmut generated
mutants_x__query_window__mutmut['x__query_window__mutmut_6'] = x__query_window__mutmut_6 # type: ignore # mutmut generated
mutants_x__query_window__mutmut['x__query_window__mutmut_7'] = x__query_window__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_iso__mutmut)
def _to_iso(value: datetime) -> str:
    return value.isoformat().replace("+00:00", "Z")


def x__to_iso__mutmut_orig(value: datetime) -> str:
    return value.isoformat().replace("+00:00", "Z")


def x__to_iso__mutmut_1(value: datetime) -> str:
    return value.isoformat().replace(None, "Z")


def x__to_iso__mutmut_2(value: datetime) -> str:
    return value.isoformat().replace("+00:00", None)


def x__to_iso__mutmut_3(value: datetime) -> str:
    return value.isoformat().replace("Z")


def x__to_iso__mutmut_4(value: datetime) -> str:
    return value.isoformat().replace("+00:00", )


def x__to_iso__mutmut_5(value: datetime) -> str:
    return value.isoformat().replace("XX+00:00XX", "Z")


def x__to_iso__mutmut_6(value: datetime) -> str:
    return value.isoformat().replace("+00:00", "XXZXX")


def x__to_iso__mutmut_7(value: datetime) -> str:
    return value.isoformat().replace("+00:00", "z")

mutants_x__to_iso__mutmut['_mutmut_orig'] = x__to_iso__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_1'] = x__to_iso__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_2'] = x__to_iso__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_3'] = x__to_iso__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_4'] = x__to_iso__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_5'] = x__to_iso__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_6'] = x__to_iso__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_7'] = x__to_iso__mutmut_7 # type: ignore # mutmut generated
mutants_x__cpu_query__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__cpu_query__mutmut)
def _cpu_query(namespace: str) -> str:
    return (
        f'avg by (pod) (rate(container_cpu_usage_seconds_total{{namespace="{namespace}", '
        'container!=""}[5m])) * 1000'
    )


def x__cpu_query__mutmut_orig(namespace: str) -> str:
    return (
        f'avg by (pod) (rate(container_cpu_usage_seconds_total{{namespace="{namespace}", '
        'container!=""}[5m])) * 1000'
    )


def x__cpu_query__mutmut_1(namespace: str) -> str:
    return (
        f'avg by (pod) (rate(container_cpu_usage_seconds_total{{namespace="{namespace}", '
        'XXcontainer!=""}[5m])) * 1000XX'
    )


def x__cpu_query__mutmut_2(namespace: str) -> str:
    return (
        f'avg by (pod) (rate(container_cpu_usage_seconds_total{{namespace="{namespace}", '
        'CONTAINER!=""}[5M])) * 1000'
    )

mutants_x__cpu_query__mutmut['_mutmut_orig'] = x__cpu_query__mutmut_orig # type: ignore # mutmut generated
mutants_x__cpu_query__mutmut['x__cpu_query__mutmut_1'] = x__cpu_query__mutmut_1 # type: ignore # mutmut generated
mutants_x__cpu_query__mutmut['x__cpu_query__mutmut_2'] = x__cpu_query__mutmut_2 # type: ignore # mutmut generated


def _memory_query(namespace: str) -> str:
    return f'avg by (pod) (container_memory_working_set_bytes{{namespace="{namespace}", container!=""}})'  # noqa: E501


def _error_rate_query(namespace: str) -> str:
    return (
        f'(sum by (pod) (rate(http_requests_total{{namespace="{namespace}", status=~"5.."}}[5m])) '
        f'/ sum by (pod) (rate(http_requests_total{{namespace="{namespace}"}}[5m]))) * 100'
    )
mutants_x__split_baseline_and_current__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__split_baseline_and_current__mutmut)
def _split_baseline_and_current(
    sample: PrometheusRangeSample | None,
) -> tuple[list[float], float]:
    if sample is None or not sample["values"]:
        return [], 0.0
    values = [value for _, value in sample["values"]]
    return values[:-1], values[-1]


def x__split_baseline_and_current__mutmut_orig(
    sample: PrometheusRangeSample | None,
) -> tuple[list[float], float]:
    if sample is None or not sample["values"]:
        return [], 0.0
    values = [value for _, value in sample["values"]]
    return values[:-1], values[-1]


def x__split_baseline_and_current__mutmut_1(
    sample: PrometheusRangeSample | None,
) -> tuple[list[float], float]:
    if sample is None and not sample["values"]:
        return [], 0.0
    values = [value for _, value in sample["values"]]
    return values[:-1], values[-1]


def x__split_baseline_and_current__mutmut_2(
    sample: PrometheusRangeSample | None,
) -> tuple[list[float], float]:
    if sample is not None or not sample["values"]:
        return [], 0.0
    values = [value for _, value in sample["values"]]
    return values[:-1], values[-1]


def x__split_baseline_and_current__mutmut_3(
    sample: PrometheusRangeSample | None,
) -> tuple[list[float], float]:
    if sample is None or sample["values"]:
        return [], 0.0
    values = [value for _, value in sample["values"]]
    return values[:-1], values[-1]


def x__split_baseline_and_current__mutmut_4(
    sample: PrometheusRangeSample | None,
) -> tuple[list[float], float]:
    if sample is None or not sample["XXvaluesXX"]:
        return [], 0.0
    values = [value for _, value in sample["values"]]
    return values[:-1], values[-1]


def x__split_baseline_and_current__mutmut_5(
    sample: PrometheusRangeSample | None,
) -> tuple[list[float], float]:
    if sample is None or not sample["VALUES"]:
        return [], 0.0
    values = [value for _, value in sample["values"]]
    return values[:-1], values[-1]


def x__split_baseline_and_current__mutmut_6(
    sample: PrometheusRangeSample | None,
) -> tuple[list[float], float]:
    if sample is None or not sample["values"]:
        return [], 1.0
    values = [value for _, value in sample["values"]]
    return values[:-1], values[-1]


def x__split_baseline_and_current__mutmut_7(
    sample: PrometheusRangeSample | None,
) -> tuple[list[float], float]:
    if sample is None or not sample["values"]:
        return [], 0.0
    values = None
    return values[:-1], values[-1]


def x__split_baseline_and_current__mutmut_8(
    sample: PrometheusRangeSample | None,
) -> tuple[list[float], float]:
    if sample is None or not sample["values"]:
        return [], 0.0
    values = [value for _, value in sample["XXvaluesXX"]]
    return values[:-1], values[-1]


def x__split_baseline_and_current__mutmut_9(
    sample: PrometheusRangeSample | None,
) -> tuple[list[float], float]:
    if sample is None or not sample["values"]:
        return [], 0.0
    values = [value for _, value in sample["VALUES"]]
    return values[:-1], values[-1]


def x__split_baseline_and_current__mutmut_10(
    sample: PrometheusRangeSample | None,
) -> tuple[list[float], float]:
    if sample is None or not sample["values"]:
        return [], 0.0
    values = [value for _, value in sample["values"]]
    return values[:+1], values[-1]


def x__split_baseline_and_current__mutmut_11(
    sample: PrometheusRangeSample | None,
) -> tuple[list[float], float]:
    if sample is None or not sample["values"]:
        return [], 0.0
    values = [value for _, value in sample["values"]]
    return values[:-2], values[-1]


def x__split_baseline_and_current__mutmut_12(
    sample: PrometheusRangeSample | None,
) -> tuple[list[float], float]:
    if sample is None or not sample["values"]:
        return [], 0.0
    values = [value for _, value in sample["values"]]
    return values[:-1], values[+1]


def x__split_baseline_and_current__mutmut_13(
    sample: PrometheusRangeSample | None,
) -> tuple[list[float], float]:
    if sample is None or not sample["values"]:
        return [], 0.0
    values = [value for _, value in sample["values"]]
    return values[:-1], values[-2]

mutants_x__split_baseline_and_current__mutmut['_mutmut_orig'] = x__split_baseline_and_current__mutmut_orig # type: ignore # mutmut generated
mutants_x__split_baseline_and_current__mutmut['x__split_baseline_and_current__mutmut_1'] = x__split_baseline_and_current__mutmut_1 # type: ignore # mutmut generated
mutants_x__split_baseline_and_current__mutmut['x__split_baseline_and_current__mutmut_2'] = x__split_baseline_and_current__mutmut_2 # type: ignore # mutmut generated
mutants_x__split_baseline_and_current__mutmut['x__split_baseline_and_current__mutmut_3'] = x__split_baseline_and_current__mutmut_3 # type: ignore # mutmut generated
mutants_x__split_baseline_and_current__mutmut['x__split_baseline_and_current__mutmut_4'] = x__split_baseline_and_current__mutmut_4 # type: ignore # mutmut generated
mutants_x__split_baseline_and_current__mutmut['x__split_baseline_and_current__mutmut_5'] = x__split_baseline_and_current__mutmut_5 # type: ignore # mutmut generated
mutants_x__split_baseline_and_current__mutmut['x__split_baseline_and_current__mutmut_6'] = x__split_baseline_and_current__mutmut_6 # type: ignore # mutmut generated
mutants_x__split_baseline_and_current__mutmut['x__split_baseline_and_current__mutmut_7'] = x__split_baseline_and_current__mutmut_7 # type: ignore # mutmut generated
mutants_x__split_baseline_and_current__mutmut['x__split_baseline_and_current__mutmut_8'] = x__split_baseline_and_current__mutmut_8 # type: ignore # mutmut generated
mutants_x__split_baseline_and_current__mutmut['x__split_baseline_and_current__mutmut_9'] = x__split_baseline_and_current__mutmut_9 # type: ignore # mutmut generated
mutants_x__split_baseline_and_current__mutmut['x__split_baseline_and_current__mutmut_10'] = x__split_baseline_and_current__mutmut_10 # type: ignore # mutmut generated
mutants_x__split_baseline_and_current__mutmut['x__split_baseline_and_current__mutmut_11'] = x__split_baseline_and_current__mutmut_11 # type: ignore # mutmut generated
mutants_x__split_baseline_and_current__mutmut['x__split_baseline_and_current__mutmut_12'] = x__split_baseline_and_current__mutmut_12 # type: ignore # mutmut generated
mutants_x__split_baseline_and_current__mutmut['x__split_baseline_and_current__mutmut_13'] = x__split_baseline_and_current__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_raw_data__mutmut)
def _to_raw_data(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_orig(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_1(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = None
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_2(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(None)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_3(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = None
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_4(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(None)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_5(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = None

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_6(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(None)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_7(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=None,
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_8(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=None,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_9(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=None,
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_10(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=None,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_11(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=None,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_12(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=None,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_13(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=None,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_14(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=None,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_15(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=None,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_16(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=None,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_17(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=None,
    )


def x__to_raw_data__mutmut_18(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_19(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_20(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_21(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_22(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_23(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_24(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_25(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_26(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_27(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_28(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_29(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        )


def x__to_raw_data__mutmut_30(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["XXnameXX"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_31(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["NAME"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_32(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(None),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_33(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["XXageXX"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_34(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["AGE"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=False,
    )


def x__to_raw_data__mutmut_35(  # noqa: PLR0913
    pod: PodInfo,
    namespace: str,
    baseline_window_hours: float,
    cpu_sample: PrometheusRangeSample | None,
    memory_sample: PrometheusRangeSample | None,
    error_rate_sample: PrometheusRangeSample | None,
) -> PodMetricsRawData:
    cpu_baseline, cpu_current = _split_baseline_and_current(cpu_sample)
    memory_baseline, memory_current = _split_baseline_and_current(memory_sample)
    error_rate_baseline, error_rate_current = _split_baseline_and_current(error_rate_sample)

    return PodMetricsRawData(
        pod_name=pod["name"],
        namespace=namespace,
        pod_age_hours=_parse_age_to_hours(pod["age"]),
        hours_since_last_restart=None,
        baseline_window_hours=baseline_window_hours,
        cpu_baseline_millicores=cpu_baseline,
        cpu_current_millicores=cpu_current,
        memory_baseline_bytes=memory_baseline,
        memory_current_bytes=memory_current,
        error_rate_baseline_pct=error_rate_baseline,
        error_rate_current_pct=error_rate_current,
        is_scheduled_batch_job=True,
    )

mutants_x__to_raw_data__mutmut['_mutmut_orig'] = x__to_raw_data__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_1'] = x__to_raw_data__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_2'] = x__to_raw_data__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_3'] = x__to_raw_data__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_4'] = x__to_raw_data__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_5'] = x__to_raw_data__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_6'] = x__to_raw_data__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_7'] = x__to_raw_data__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_8'] = x__to_raw_data__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_9'] = x__to_raw_data__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_10'] = x__to_raw_data__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_11'] = x__to_raw_data__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_12'] = x__to_raw_data__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_13'] = x__to_raw_data__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_14'] = x__to_raw_data__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_15'] = x__to_raw_data__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_16'] = x__to_raw_data__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_17'] = x__to_raw_data__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_18'] = x__to_raw_data__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_19'] = x__to_raw_data__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_20'] = x__to_raw_data__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_21'] = x__to_raw_data__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_22'] = x__to_raw_data__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_23'] = x__to_raw_data__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_24'] = x__to_raw_data__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_25'] = x__to_raw_data__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_26'] = x__to_raw_data__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_27'] = x__to_raw_data__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_28'] = x__to_raw_data__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_29'] = x__to_raw_data__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_30'] = x__to_raw_data__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_31'] = x__to_raw_data__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_32'] = x__to_raw_data__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_33'] = x__to_raw_data__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_34'] = x__to_raw_data__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_raw_data__mutmut['x__to_raw_data__mutmut_35'] = x__to_raw_data__mutmut_35 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_age_to_hours__mutmut)
def _parse_age_to_hours(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_orig(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_1(age: str) -> float:
    age = None
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_2(age: str) -> float:
    age = age.strip()
    if age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_3(age: str) -> float:
    age = age.strip()
    if not age:
        return 1.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_4(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = None
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_5(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(None)
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_6(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:+1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_7(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-2])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_8(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 1.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_9(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = None
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_10(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[+1]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_11(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-2]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_12(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit != "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_13(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "XXdXX":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_14(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "D":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_15(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value / 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_16(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 25
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_17(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit != "h":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_18(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "XXhXX":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_19(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "H":
        return value
    if unit == "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_20(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit != "m":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_21(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "XXmXX":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_22(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "M":
        return value / 60
    return 0.0


def x__parse_age_to_hours__mutmut_23(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value * 60
    return 0.0


def x__parse_age_to_hours__mutmut_24(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 61
    return 0.0


def x__parse_age_to_hours__mutmut_25(age: str) -> float:
    age = age.strip()
    if not age:
        return 0.0
    try:
        value = float(age[:-1])
    except ValueError:
        return 0.0
    unit = age[-1]
    if unit == "d":
        return value * 24
    if unit == "h":
        return value
    if unit == "m":
        return value / 60
    return 1.0

mutants_x__parse_age_to_hours__mutmut['_mutmut_orig'] = x__parse_age_to_hours__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_1'] = x__parse_age_to_hours__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_2'] = x__parse_age_to_hours__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_3'] = x__parse_age_to_hours__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_4'] = x__parse_age_to_hours__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_5'] = x__parse_age_to_hours__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_6'] = x__parse_age_to_hours__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_7'] = x__parse_age_to_hours__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_8'] = x__parse_age_to_hours__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_9'] = x__parse_age_to_hours__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_10'] = x__parse_age_to_hours__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_11'] = x__parse_age_to_hours__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_12'] = x__parse_age_to_hours__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_13'] = x__parse_age_to_hours__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_14'] = x__parse_age_to_hours__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_15'] = x__parse_age_to_hours__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_16'] = x__parse_age_to_hours__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_17'] = x__parse_age_to_hours__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_18'] = x__parse_age_to_hours__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_19'] = x__parse_age_to_hours__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_20'] = x__parse_age_to_hours__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_21'] = x__parse_age_to_hours__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_22'] = x__parse_age_to_hours__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_23'] = x__parse_age_to_hours__mutmut_23 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_24'] = x__parse_age_to_hours__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_age_to_hours__mutmut['x__parse_age_to_hours__mutmut_25'] = x__parse_age_to_hours__mutmut_25 # type: ignore # mutmut generated
