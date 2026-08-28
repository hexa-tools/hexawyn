"""CalicoPrometheusAdapter — Felix metrics & connectivity via Prometheus.

A read-only collaborator used by ``CalicoK8sAdapter`` for the metric-backed
``felix_metrics`` / ``connectivity_health`` endpoints. It degrades to an honest
``available: False`` envelope rather than raising, mirroring the no-crash
convention.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort

_FELIX_AGENT_METRICS = (
    "felix_active_local_endpoints",
    "felix_cluster_num_host_endpoints",
)
_CONNECTIVITY_PROBE = "felix_active_local_endpoints"
_TIMEOUT_SECONDS = 10.0


class CalicoPrometheusAdapter:
    """Metrics-backed Calico introspection intended for ``felix_metrics``."""

    def __init__(self, metrics_query_port: MetricsQueryPort | None = None) -> None:
        self._mq = metrics_query_port

    def felix_metrics(self) -> dict[str, object]:
        """Aggregate Felix metrics names into a flat ``{metric: value}`` map."""
        if self._mq is None:
            return {"available": False, "metrics": {}, "error": "no metrics query port configured"}
        metrics: dict[str, float] = {}
        try:
            for name in _FELIX_AGENT_METRICS:
                samples = self._mq.instant_query(name, _TIMEOUT_SECONDS)
                metrics[name] = sum(float(sample.get("value", 0.0)) for sample in samples)
        except Exception as exc:  # noqa: BLE001 — degrade, never crash
            return {"available": False, "metrics": {}, "error": str(exc)}
        return {"available": True, "metrics": metrics}

    def connectivity_health(self) -> dict[str, object]:
        """Derive dataplane connectivity from Felix endpoint activity."""
        if self._mq is None:
            return {
                "available": False,
                "status": "degraded",
                "detail": "no metrics query port configured",
            }
        try:
            samples = self._mq.instant_query(_CONNECTIVITY_PROBE, _TIMEOUT_SECONDS)
        except Exception as exc:  # noqa: BLE001 — degrade, never crash
            return {"available": False, "status": "degraded", "detail": str(exc)}
        active = len(samples)
        status = "healthy" if active > 0 else "degraded"
        return {"available": True, "status": status, "active_endpoint_agents": active}
