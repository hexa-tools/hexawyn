from __future__ import annotations

from hexawyn.domain.models.spike_provisioning import (
    ClusterCapacitySnapshot,
    SpikeProvisioningReport,
)
from hexawyn.domain.services.spike_provisioning.demand_projector import project_demand
from hexawyn.domain.services.spike_provisioning.node_recommender import recommend_nodes
from hexawyn.domain.services.spike_provisioning.provisioning_deadline import compute_deadline

_DEFAULT_SAFE_THRESHOLD_PCT = 85.0
_DEFAULT_LEAD_TIME_HOURS = 24
_DEFAULT_SAFETY_MARGIN_DAYS = 3
_FALLBACK_WARNING = (
    "No historical spike data for this event — using a generic 3x traffic "
    "multiplier. Treat the recommendation as conservative guidance."
)
_PESSIMISTIC_WARNING = (
    "Traffic is unpredictable (e.g. a new product launch) — a pessimistic "
    "multiplier is applied by default; real demand may differ."
)


class SpikeProvisioningService:
    """Domain service — decides whether to provision nodes ahead of a traffic
    spike, how many and of which type, and by when."""

    def plan(  # noqa: PLR0913
        self,
        snapshot: ClusterCapacitySnapshot,
        multiplier: float,
        multiplier_source: str,
        event_date: str,
        provider_lead_time_hours: int = _DEFAULT_LEAD_TIME_HOURS,
        safety_margin_days: int = _DEFAULT_SAFETY_MARGIN_DAYS,
        safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
    ) -> SpikeProvisioningReport:
        projection = project_demand(snapshot, multiplier, safe_threshold_pct)
        needs_capacity = projection.binding_constraint != "None"

        verdict, autoscaler_sufficient = _decide_verdict(
            needs_capacity, snapshot.autoscaler_enabled
        )
        recommendation = recommend_nodes(
            snapshot, multiplier, projection.binding_constraint, safe_threshold_pct
        )

        provision_needed = verdict == "provision"
        return SpikeProvisioningReport(
            traffic_multiplier=multiplier,
            multiplier_source=multiplier_source,
            verdict=verdict,
            current_cpu_headroom_pct=projection.current_cpu_headroom_pct,
            current_memory_headroom_pct=projection.current_memory_headroom_pct,
            projected_cpu_pct=projection.projected_cpu_pct,
            projected_memory_pct=projection.projected_memory_pct,
            recommended_nodes=recommendation.node_count if provision_needed else 0,
            recommended_node_type=recommendation.node_type,
            binding_constraint=projection.binding_constraint,
            autoscaler_sufficient=autoscaler_sufficient,
            provisioning_deadline=(
                compute_deadline(event_date, provider_lead_time_hours, safety_margin_days)
                if provision_needed
                else None
            ),
            warning=_warning(multiplier_source),
        )


def _decide_verdict(needs_capacity: bool, autoscaler_enabled: bool) -> tuple[str, bool]:
    if not needs_capacity:
        return "no_action", False
    if autoscaler_enabled:
        return "autoscaler_handles", True
    return "provision", False


def _warning(multiplier_source: str) -> str:
    if multiplier_source == "generic_fallback":
        return _FALLBACK_WARNING
    if multiplier_source == "pessimistic":
        return _PESSIMISTIC_WARNING
    return ""
