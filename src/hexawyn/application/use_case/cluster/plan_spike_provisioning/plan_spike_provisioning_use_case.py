from __future__ import annotations

from hexawyn.application.ports.driven.spike_provisioning_port import (
    ClusterCapacityRaw,
    SpikeProvisioningPort,
)
from hexawyn.application.use_case.cluster.plan_spike_provisioning.command import (  # noqa: E501
    PlanSpikeProvisioningCommand,
)
from hexawyn.application.use_case.cluster.plan_spike_provisioning.response import (  # noqa: E501
    PlanSpikeProvisioningResponse,
)
from hexawyn.domain.models.spike_provisioning import ClusterCapacitySnapshot
from hexawyn.domain.services.spike_provisioning.spike_provisioning_service import (
    SpikeProvisioningService,
)

_GENERIC_MULTIPLIER = 3.0
_PESSIMISTIC_MULTIPLIER = 4.0


class PlanSpikeProvisioningUseCase:
    def __init__(self, spike_port: SpikeProvisioningPort) -> None:
        self._port = spike_port
        self._engine = SpikeProvisioningService()

    def execute(self, command: PlanSpikeProvisioningCommand) -> PlanSpikeProvisioningResponse:
        capacity = self._port.get_cluster_capacity()
        multiplier, source = self._resolve_multiplier(command)
        result = self._engine.plan(
            snapshot=_to_snapshot(capacity),
            multiplier=multiplier,
            multiplier_source=source,
            event_date=command.event_date,
            provider_lead_time_hours=command.provider_lead_time_hours,
            safety_margin_days=command.safety_margin_days,
            safe_threshold_pct=command.safe_threshold_pct,
        )
        return PlanSpikeProvisioningResponse(result=result)  # type: ignore

    def _resolve_multiplier(self, command: PlanSpikeProvisioningCommand) -> tuple[float, str]:
        if command.unpredictable:
            return _PESSIMISTIC_MULTIPLIER, "pessimistic"
        if command.traffic_multiplier is not None:
            return command.traffic_multiplier, "provided"
        historical = self._port.get_historical_spike_multiplier()
        if historical is not None:
            return historical, "historical"
        return _GENERIC_MULTIPLIER, "generic_fallback"


def _to_snapshot(capacity: ClusterCapacityRaw) -> ClusterCapacitySnapshot:
    return ClusterCapacitySnapshot(
        node_count=capacity["node_count"],
        allocatable_cpu_cores=capacity["allocatable_cpu_cores"],
        allocatable_memory_gb=capacity["allocatable_memory_gb"],
        used_cpu_cores=capacity["used_cpu_cores"],
        used_memory_gb=capacity["used_memory_gb"],
        autoscaler_enabled=capacity["autoscaler_enabled"],
    )
