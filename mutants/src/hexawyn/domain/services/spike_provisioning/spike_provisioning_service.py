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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSpikeProvisioningServiceǁplan__mutmut: MutantDict = {}  # type: ignore


class SpikeProvisioningService:
    """Domain service — decides whether to provision nodes ahead of a traffic
    spike, how many and of which type, and by when."""

    @_mutmut_mutated(mutants_xǁSpikeProvisioningServiceǁplan__mutmut)
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_orig(  # noqa: PLR0913
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_1(  # noqa: PLR0913
        self,
        snapshot: ClusterCapacitySnapshot,
        multiplier: float,
        multiplier_source: str,
        event_date: str,
        provider_lead_time_hours: int = _DEFAULT_LEAD_TIME_HOURS,
        safety_margin_days: int = _DEFAULT_SAFETY_MARGIN_DAYS,
        safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
    ) -> SpikeProvisioningReport:
        projection = None
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_2(  # noqa: PLR0913
        self,
        snapshot: ClusterCapacitySnapshot,
        multiplier: float,
        multiplier_source: str,
        event_date: str,
        provider_lead_time_hours: int = _DEFAULT_LEAD_TIME_HOURS,
        safety_margin_days: int = _DEFAULT_SAFETY_MARGIN_DAYS,
        safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
    ) -> SpikeProvisioningReport:
        projection = project_demand(None, multiplier, safe_threshold_pct)
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_3(  # noqa: PLR0913
        self,
        snapshot: ClusterCapacitySnapshot,
        multiplier: float,
        multiplier_source: str,
        event_date: str,
        provider_lead_time_hours: int = _DEFAULT_LEAD_TIME_HOURS,
        safety_margin_days: int = _DEFAULT_SAFETY_MARGIN_DAYS,
        safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
    ) -> SpikeProvisioningReport:
        projection = project_demand(snapshot, None, safe_threshold_pct)
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_4(  # noqa: PLR0913
        self,
        snapshot: ClusterCapacitySnapshot,
        multiplier: float,
        multiplier_source: str,
        event_date: str,
        provider_lead_time_hours: int = _DEFAULT_LEAD_TIME_HOURS,
        safety_margin_days: int = _DEFAULT_SAFETY_MARGIN_DAYS,
        safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
    ) -> SpikeProvisioningReport:
        projection = project_demand(snapshot, multiplier, None)
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_5(  # noqa: PLR0913
        self,
        snapshot: ClusterCapacitySnapshot,
        multiplier: float,
        multiplier_source: str,
        event_date: str,
        provider_lead_time_hours: int = _DEFAULT_LEAD_TIME_HOURS,
        safety_margin_days: int = _DEFAULT_SAFETY_MARGIN_DAYS,
        safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
    ) -> SpikeProvisioningReport:
        projection = project_demand(multiplier, safe_threshold_pct)
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_6(  # noqa: PLR0913
        self,
        snapshot: ClusterCapacitySnapshot,
        multiplier: float,
        multiplier_source: str,
        event_date: str,
        provider_lead_time_hours: int = _DEFAULT_LEAD_TIME_HOURS,
        safety_margin_days: int = _DEFAULT_SAFETY_MARGIN_DAYS,
        safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
    ) -> SpikeProvisioningReport:
        projection = project_demand(snapshot, safe_threshold_pct)
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_7(  # noqa: PLR0913
        self,
        snapshot: ClusterCapacitySnapshot,
        multiplier: float,
        multiplier_source: str,
        event_date: str,
        provider_lead_time_hours: int = _DEFAULT_LEAD_TIME_HOURS,
        safety_margin_days: int = _DEFAULT_SAFETY_MARGIN_DAYS,
        safe_threshold_pct: float = _DEFAULT_SAFE_THRESHOLD_PCT,
    ) -> SpikeProvisioningReport:
        projection = project_demand(snapshot, multiplier, )
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_8(  # noqa: PLR0913
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
        needs_capacity = None

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

    def xǁSpikeProvisioningServiceǁplan__mutmut_9(  # noqa: PLR0913
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
        needs_capacity = projection.binding_constraint == "None"

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

    def xǁSpikeProvisioningServiceǁplan__mutmut_10(  # noqa: PLR0913
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
        needs_capacity = projection.binding_constraint != "XXNoneXX"

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

    def xǁSpikeProvisioningServiceǁplan__mutmut_11(  # noqa: PLR0913
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
        needs_capacity = projection.binding_constraint != "none"

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

    def xǁSpikeProvisioningServiceǁplan__mutmut_12(  # noqa: PLR0913
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
        needs_capacity = projection.binding_constraint != "NONE"

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

    def xǁSpikeProvisioningServiceǁplan__mutmut_13(  # noqa: PLR0913
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

        verdict, autoscaler_sufficient = None
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_14(  # noqa: PLR0913
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
            None, snapshot.autoscaler_enabled
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_15(  # noqa: PLR0913
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
            needs_capacity, None
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_16(  # noqa: PLR0913
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
            snapshot.autoscaler_enabled
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_17(  # noqa: PLR0913
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
            needs_capacity, )
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_18(  # noqa: PLR0913
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
        recommendation = None

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

    def xǁSpikeProvisioningServiceǁplan__mutmut_19(  # noqa: PLR0913
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
            None, multiplier, projection.binding_constraint, safe_threshold_pct
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_20(  # noqa: PLR0913
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
            snapshot, None, projection.binding_constraint, safe_threshold_pct
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_21(  # noqa: PLR0913
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
            snapshot, multiplier, None, safe_threshold_pct
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_22(  # noqa: PLR0913
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
            snapshot, multiplier, projection.binding_constraint, None
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_23(  # noqa: PLR0913
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
            multiplier, projection.binding_constraint, safe_threshold_pct
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_24(  # noqa: PLR0913
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
            snapshot, projection.binding_constraint, safe_threshold_pct
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_25(  # noqa: PLR0913
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
            snapshot, multiplier, safe_threshold_pct
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_26(  # noqa: PLR0913
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
            snapshot, multiplier, projection.binding_constraint, )

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

    def xǁSpikeProvisioningServiceǁplan__mutmut_27(  # noqa: PLR0913
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

        provision_needed = None
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_28(  # noqa: PLR0913
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

        provision_needed = verdict != "provision"
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_29(  # noqa: PLR0913
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

        provision_needed = verdict == "XXprovisionXX"
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_30(  # noqa: PLR0913
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

        provision_needed = verdict == "PROVISION"
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_31(  # noqa: PLR0913
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
            traffic_multiplier=None,
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_32(  # noqa: PLR0913
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
            multiplier_source=None,
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_33(  # noqa: PLR0913
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
            verdict=None,
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_34(  # noqa: PLR0913
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
            current_cpu_headroom_pct=None,
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_35(  # noqa: PLR0913
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
            current_memory_headroom_pct=None,
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_36(  # noqa: PLR0913
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
            projected_cpu_pct=None,
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_37(  # noqa: PLR0913
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
            projected_memory_pct=None,
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_38(  # noqa: PLR0913
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
            recommended_nodes=None,
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_39(  # noqa: PLR0913
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
            recommended_node_type=None,
            binding_constraint=projection.binding_constraint,
            autoscaler_sufficient=autoscaler_sufficient,
            provisioning_deadline=(
                compute_deadline(event_date, provider_lead_time_hours, safety_margin_days)
                if provision_needed
                else None
            ),
            warning=_warning(multiplier_source),
        )

    def xǁSpikeProvisioningServiceǁplan__mutmut_40(  # noqa: PLR0913
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
            binding_constraint=None,
            autoscaler_sufficient=autoscaler_sufficient,
            provisioning_deadline=(
                compute_deadline(event_date, provider_lead_time_hours, safety_margin_days)
                if provision_needed
                else None
            ),
            warning=_warning(multiplier_source),
        )

    def xǁSpikeProvisioningServiceǁplan__mutmut_41(  # noqa: PLR0913
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
            autoscaler_sufficient=None,
            provisioning_deadline=(
                compute_deadline(event_date, provider_lead_time_hours, safety_margin_days)
                if provision_needed
                else None
            ),
            warning=_warning(multiplier_source),
        )

    def xǁSpikeProvisioningServiceǁplan__mutmut_42(  # noqa: PLR0913
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
            provisioning_deadline=None,
            warning=_warning(multiplier_source),
        )

    def xǁSpikeProvisioningServiceǁplan__mutmut_43(  # noqa: PLR0913
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
            warning=None,
        )

    def xǁSpikeProvisioningServiceǁplan__mutmut_44(  # noqa: PLR0913
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_45(  # noqa: PLR0913
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_46(  # noqa: PLR0913
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_47(  # noqa: PLR0913
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_48(  # noqa: PLR0913
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_49(  # noqa: PLR0913
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_50(  # noqa: PLR0913
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_51(  # noqa: PLR0913
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_52(  # noqa: PLR0913
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
            binding_constraint=projection.binding_constraint,
            autoscaler_sufficient=autoscaler_sufficient,
            provisioning_deadline=(
                compute_deadline(event_date, provider_lead_time_hours, safety_margin_days)
                if provision_needed
                else None
            ),
            warning=_warning(multiplier_source),
        )

    def xǁSpikeProvisioningServiceǁplan__mutmut_53(  # noqa: PLR0913
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
            autoscaler_sufficient=autoscaler_sufficient,
            provisioning_deadline=(
                compute_deadline(event_date, provider_lead_time_hours, safety_margin_days)
                if provision_needed
                else None
            ),
            warning=_warning(multiplier_source),
        )

    def xǁSpikeProvisioningServiceǁplan__mutmut_54(  # noqa: PLR0913
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
            provisioning_deadline=(
                compute_deadline(event_date, provider_lead_time_hours, safety_margin_days)
                if provision_needed
                else None
            ),
            warning=_warning(multiplier_source),
        )

    def xǁSpikeProvisioningServiceǁplan__mutmut_55(  # noqa: PLR0913
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
            warning=_warning(multiplier_source),
        )

    def xǁSpikeProvisioningServiceǁplan__mutmut_56(  # noqa: PLR0913
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
            )

    def xǁSpikeProvisioningServiceǁplan__mutmut_57(  # noqa: PLR0913
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
            recommended_nodes=recommendation.node_count if provision_needed else 1,
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

    def xǁSpikeProvisioningServiceǁplan__mutmut_58(  # noqa: PLR0913
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
                compute_deadline(None, provider_lead_time_hours, safety_margin_days)
                if provision_needed
                else None
            ),
            warning=_warning(multiplier_source),
        )

    def xǁSpikeProvisioningServiceǁplan__mutmut_59(  # noqa: PLR0913
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
                compute_deadline(event_date, None, safety_margin_days)
                if provision_needed
                else None
            ),
            warning=_warning(multiplier_source),
        )

    def xǁSpikeProvisioningServiceǁplan__mutmut_60(  # noqa: PLR0913
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
                compute_deadline(event_date, provider_lead_time_hours, None)
                if provision_needed
                else None
            ),
            warning=_warning(multiplier_source),
        )

    def xǁSpikeProvisioningServiceǁplan__mutmut_61(  # noqa: PLR0913
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
                compute_deadline(provider_lead_time_hours, safety_margin_days)
                if provision_needed
                else None
            ),
            warning=_warning(multiplier_source),
        )

    def xǁSpikeProvisioningServiceǁplan__mutmut_62(  # noqa: PLR0913
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
                compute_deadline(event_date, safety_margin_days)
                if provision_needed
                else None
            ),
            warning=_warning(multiplier_source),
        )

    def xǁSpikeProvisioningServiceǁplan__mutmut_63(  # noqa: PLR0913
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
                compute_deadline(event_date, provider_lead_time_hours, )
                if provision_needed
                else None
            ),
            warning=_warning(multiplier_source),
        )

    def xǁSpikeProvisioningServiceǁplan__mutmut_64(  # noqa: PLR0913
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
            warning=_warning(None),
        )

mutants_xǁSpikeProvisioningServiceǁplan__mutmut['_mutmut_orig'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_1'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_2'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_3'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_4'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_5'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_6'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_7'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_8'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_9'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_10'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_11'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_12'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_13'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_14'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_15'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_16'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_17'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_18'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_19'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_20'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_21'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_21 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_22'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_22 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_23'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_23 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_24'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_24 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_25'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_25 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_26'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_26 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_27'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_27 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_28'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_28 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_29'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_29 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_30'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_30 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_31'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_31 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_32'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_32 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_33'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_33 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_34'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_34 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_35'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_35 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_36'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_36 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_37'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_37 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_38'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_38 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_39'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_39 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_40'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_40 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_41'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_41 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_42'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_42 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_43'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_43 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_44'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_44 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_45'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_45 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_46'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_46 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_47'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_47 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_48'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_48 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_49'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_49 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_50'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_50 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_51'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_51 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_52'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_52 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_53'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_53 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_54'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_54 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_55'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_55 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_56'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_56 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_57'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_57 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_58'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_58 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_59'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_59 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_60'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_60 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_61'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_61 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_62'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_62 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_63'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_63 # type: ignore # mutmut generated
mutants_xǁSpikeProvisioningServiceǁplan__mutmut['xǁSpikeProvisioningServiceǁplan__mutmut_64'] = SpikeProvisioningService.xǁSpikeProvisioningServiceǁplan__mutmut_64 # type: ignore # mutmut generated
mutants_x__decide_verdict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__decide_verdict__mutmut)
def _decide_verdict(needs_capacity: bool, autoscaler_enabled: bool) -> tuple[str, bool]:
    if not needs_capacity:
        return "no_action", False
    if autoscaler_enabled:
        return "autoscaler_handles", True
    return "provision", False


def x__decide_verdict__mutmut_orig(needs_capacity: bool, autoscaler_enabled: bool) -> tuple[str, bool]:
    if not needs_capacity:
        return "no_action", False
    if autoscaler_enabled:
        return "autoscaler_handles", True
    return "provision", False


def x__decide_verdict__mutmut_1(needs_capacity: bool, autoscaler_enabled: bool) -> tuple[str, bool]:
    if needs_capacity:
        return "no_action", False
    if autoscaler_enabled:
        return "autoscaler_handles", True
    return "provision", False


def x__decide_verdict__mutmut_2(needs_capacity: bool, autoscaler_enabled: bool) -> tuple[str, bool]:
    if not needs_capacity:
        return "XXno_actionXX", False
    if autoscaler_enabled:
        return "autoscaler_handles", True
    return "provision", False


def x__decide_verdict__mutmut_3(needs_capacity: bool, autoscaler_enabled: bool) -> tuple[str, bool]:
    if not needs_capacity:
        return "NO_ACTION", False
    if autoscaler_enabled:
        return "autoscaler_handles", True
    return "provision", False


def x__decide_verdict__mutmut_4(needs_capacity: bool, autoscaler_enabled: bool) -> tuple[str, bool]:
    if not needs_capacity:
        return "no_action", True
    if autoscaler_enabled:
        return "autoscaler_handles", True
    return "provision", False


def x__decide_verdict__mutmut_5(needs_capacity: bool, autoscaler_enabled: bool) -> tuple[str, bool]:
    if not needs_capacity:
        return "no_action", False
    if autoscaler_enabled:
        return "XXautoscaler_handlesXX", True
    return "provision", False


def x__decide_verdict__mutmut_6(needs_capacity: bool, autoscaler_enabled: bool) -> tuple[str, bool]:
    if not needs_capacity:
        return "no_action", False
    if autoscaler_enabled:
        return "AUTOSCALER_HANDLES", True
    return "provision", False


def x__decide_verdict__mutmut_7(needs_capacity: bool, autoscaler_enabled: bool) -> tuple[str, bool]:
    if not needs_capacity:
        return "no_action", False
    if autoscaler_enabled:
        return "autoscaler_handles", False
    return "provision", False


def x__decide_verdict__mutmut_8(needs_capacity: bool, autoscaler_enabled: bool) -> tuple[str, bool]:
    if not needs_capacity:
        return "no_action", False
    if autoscaler_enabled:
        return "autoscaler_handles", True
    return "XXprovisionXX", False


def x__decide_verdict__mutmut_9(needs_capacity: bool, autoscaler_enabled: bool) -> tuple[str, bool]:
    if not needs_capacity:
        return "no_action", False
    if autoscaler_enabled:
        return "autoscaler_handles", True
    return "PROVISION", False


def x__decide_verdict__mutmut_10(needs_capacity: bool, autoscaler_enabled: bool) -> tuple[str, bool]:
    if not needs_capacity:
        return "no_action", False
    if autoscaler_enabled:
        return "autoscaler_handles", True
    return "provision", True

mutants_x__decide_verdict__mutmut['_mutmut_orig'] = x__decide_verdict__mutmut_orig # type: ignore # mutmut generated
mutants_x__decide_verdict__mutmut['x__decide_verdict__mutmut_1'] = x__decide_verdict__mutmut_1 # type: ignore # mutmut generated
mutants_x__decide_verdict__mutmut['x__decide_verdict__mutmut_2'] = x__decide_verdict__mutmut_2 # type: ignore # mutmut generated
mutants_x__decide_verdict__mutmut['x__decide_verdict__mutmut_3'] = x__decide_verdict__mutmut_3 # type: ignore # mutmut generated
mutants_x__decide_verdict__mutmut['x__decide_verdict__mutmut_4'] = x__decide_verdict__mutmut_4 # type: ignore # mutmut generated
mutants_x__decide_verdict__mutmut['x__decide_verdict__mutmut_5'] = x__decide_verdict__mutmut_5 # type: ignore # mutmut generated
mutants_x__decide_verdict__mutmut['x__decide_verdict__mutmut_6'] = x__decide_verdict__mutmut_6 # type: ignore # mutmut generated
mutants_x__decide_verdict__mutmut['x__decide_verdict__mutmut_7'] = x__decide_verdict__mutmut_7 # type: ignore # mutmut generated
mutants_x__decide_verdict__mutmut['x__decide_verdict__mutmut_8'] = x__decide_verdict__mutmut_8 # type: ignore # mutmut generated
mutants_x__decide_verdict__mutmut['x__decide_verdict__mutmut_9'] = x__decide_verdict__mutmut_9 # type: ignore # mutmut generated
mutants_x__decide_verdict__mutmut['x__decide_verdict__mutmut_10'] = x__decide_verdict__mutmut_10 # type: ignore # mutmut generated
mutants_x__warning__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__warning__mutmut)
def _warning(multiplier_source: str) -> str:
    if multiplier_source == "generic_fallback":
        return _FALLBACK_WARNING
    if multiplier_source == "pessimistic":
        return _PESSIMISTIC_WARNING
    return ""


def x__warning__mutmut_orig(multiplier_source: str) -> str:
    if multiplier_source == "generic_fallback":
        return _FALLBACK_WARNING
    if multiplier_source == "pessimistic":
        return _PESSIMISTIC_WARNING
    return ""


def x__warning__mutmut_1(multiplier_source: str) -> str:
    if multiplier_source != "generic_fallback":
        return _FALLBACK_WARNING
    if multiplier_source == "pessimistic":
        return _PESSIMISTIC_WARNING
    return ""


def x__warning__mutmut_2(multiplier_source: str) -> str:
    if multiplier_source == "XXgeneric_fallbackXX":
        return _FALLBACK_WARNING
    if multiplier_source == "pessimistic":
        return _PESSIMISTIC_WARNING
    return ""


def x__warning__mutmut_3(multiplier_source: str) -> str:
    if multiplier_source == "GENERIC_FALLBACK":
        return _FALLBACK_WARNING
    if multiplier_source == "pessimistic":
        return _PESSIMISTIC_WARNING
    return ""


def x__warning__mutmut_4(multiplier_source: str) -> str:
    if multiplier_source == "generic_fallback":
        return _FALLBACK_WARNING
    if multiplier_source != "pessimistic":
        return _PESSIMISTIC_WARNING
    return ""


def x__warning__mutmut_5(multiplier_source: str) -> str:
    if multiplier_source == "generic_fallback":
        return _FALLBACK_WARNING
    if multiplier_source == "XXpessimisticXX":
        return _PESSIMISTIC_WARNING
    return ""


def x__warning__mutmut_6(multiplier_source: str) -> str:
    if multiplier_source == "generic_fallback":
        return _FALLBACK_WARNING
    if multiplier_source == "PESSIMISTIC":
        return _PESSIMISTIC_WARNING
    return ""


def x__warning__mutmut_7(multiplier_source: str) -> str:
    if multiplier_source == "generic_fallback":
        return _FALLBACK_WARNING
    if multiplier_source == "pessimistic":
        return _PESSIMISTIC_WARNING
    return "XXXX"

mutants_x__warning__mutmut['_mutmut_orig'] = x__warning__mutmut_orig # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_1'] = x__warning__mutmut_1 # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_2'] = x__warning__mutmut_2 # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_3'] = x__warning__mutmut_3 # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_4'] = x__warning__mutmut_4 # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_5'] = x__warning__mutmut_5 # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_6'] = x__warning__mutmut_6 # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_7'] = x__warning__mutmut_7 # type: ignore # mutmut generated
