"""Domain service: pure waste ratio computation, ranking, and exclusion logic."""

from __future__ import annotations

from hexawyn.domain.models.namespace_waste import (
    ExcludedNamespace,
    NamespaceRawData,
    NamespaceWaste,
    OverProvisioningReport,
)

_OVER_PROVISION_THRESHOLD_PCT = 50.0
_MIN_AGE_HOURS = 24.0
_REASON_NO_REQUESTS = "No resource requests set — burstable or BestEffort pods excluded"
_REASON_TOO_RECENT = "Namespace age < 24h — insufficient data for 7-day waste analysis"


class NamespaceOverProvisioningService:
    """Computes waste ratios and produces a ranked over-provisioning report.

    Pure domain logic — no infra dependencies, no try/catch.
    """

    def analyze(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )


def _partition(
    raw_data: list[NamespaceRawData],
) -> tuple[list[NamespaceRawData], list[ExcludedNamespace]]:
    eligible: list[NamespaceRawData] = []
    excluded: list[ExcludedNamespace] = []
    for item in raw_data:
        reason = _exclusion_reason(item)
        if reason:
            excluded.append(ExcludedNamespace(namespace=item["namespace"], reason=reason))
        else:
            eligible.append(item)
    return eligible, excluded


def _exclusion_reason(item: NamespaceRawData) -> str | None:
    if not item["has_resource_requests"]:
        return _REASON_NO_REQUESTS
    if item["age_hours"] < _MIN_AGE_HOURS:
        return _REASON_TOO_RECENT
    return None


def _compute_namespace_waste(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def any_actual_usage_present(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is not None and rd["cpu_actual_avg_cores"] > 0)
        or (rd["memory_actual_avg_gb"] is not None and rd["memory_actual_avg_gb"] > 0)
        for rd in raw_data
    )


def _waste_pair(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested == 0.0:
        return 0.0, 0.0
    wasted = max(0.0, requested - actual)
    waste_pct = wasted / requested * 100.0
    return waste_pct, wasted
