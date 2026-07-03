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


class PrometheusPodMetricsBaselineAdapter(PodMetricsBaselinePort):
    """Real Prometheus wiring: 3 bulk range queries (CPU, memory, error rate),
    one per metric for the whole namespace, matched to pods via K8sPort.

    Two fields cannot be honestly populated from this repo's current ports:
    `hours_since_last_restart` (no port exposes per-restart timestamps) and
    `is_scheduled_batch_job` (no port exposes pod owner references). Both
    always come back as their "unknown" default (None / False) — the domain
    layer already handles both correctly whenever a richer signal exists.
    """

    def __init__(self, metrics_query_port: MetricsQueryPort, k8s_port: K8sPort) -> None:
        self._metrics_query_port = metrics_query_port
        self._k8s_port = k8s_port

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


def _query_window(window_days: int) -> tuple[str, str]:
    end = datetime.now(UTC)
    start = end - timedelta(days=window_days)
    return _to_iso(start), _to_iso(end)


def _to_iso(value: datetime) -> str:
    return value.isoformat().replace("+00:00", "Z")


def _cpu_query(namespace: str) -> str:
    return (
        f'avg by (pod) (rate(container_cpu_usage_seconds_total{{namespace="{namespace}", '
        'container!=""}[5m])) * 1000'
    )


def _memory_query(namespace: str) -> str:
    return f'avg by (pod) (container_memory_working_set_bytes{{namespace="{namespace}", container!=""}})'


def _error_rate_query(namespace: str) -> str:
    return (
        f'(sum by (pod) (rate(http_requests_total{{namespace="{namespace}", status=~"5.."}}[5m])) '
        f'/ sum by (pod) (rate(http_requests_total{{namespace="{namespace}"}}[5m]))) * 100'
    )


def _split_baseline_and_current(
    sample: PrometheusRangeSample | None,
) -> tuple[list[float], float]:
    if sample is None or not sample["values"]:
        return [], 0.0
    values = [value for _, value in sample["values"]]
    return values[:-1], values[-1]


def _to_raw_data(
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
