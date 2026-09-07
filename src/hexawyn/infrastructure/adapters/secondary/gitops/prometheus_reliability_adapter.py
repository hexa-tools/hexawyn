from __future__ import annotations

from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort
from hexawyn.application.ports.driven.weekly_reliability_report_port import (
    IncidentRawData,
    ServiceReliabilityRawData,
    WeeklyReliabilityReportPort,
)


class PrometheusReliabilityAdapter(WeeklyReliabilityReportPort):
    def __init__(self, metrics_query_port: MetricsQueryPort) -> None:
        self._metrics = metrics_query_port

    def fetch_service_reliability(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def fetch_incidents(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []


def _build_uptime_query(window_seconds: int) -> str:
    return (
        f'avg(rate(http_requests_total{{code!~"5.."}}[{window_seconds}s]))'
        f" / "
        f"avg(rate(http_requests_total[{window_seconds}s]))"
    )
