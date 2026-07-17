from unittest.mock import MagicMock

from hexawyn.application.ports.driven.spike_provisioning_port import (
    ClusterCapacityRaw,
    SpikeProvisioningPort,
)
from hexawyn.application.ports.driving.plan_spike_provisioning.plan_spike_provisioning_command import (  # noqa: E501
    PlanSpikeProvisioningCommand,
)

_GENERIC_MULTIPLIER = 3.0
_PESSIMISTIC_MULTIPLIER = 4.0


def _capacity(used_cpu: float = 70.0, autoscaler: bool = False) -> ClusterCapacityRaw:
    return ClusterCapacityRaw(
        node_count=10,
        allocatable_cpu_cores=100.0,
        allocatable_memory_gb=200.0,
        used_cpu_cores=used_cpu,
        used_memory_gb=130.0,
        autoscaler_enabled=autoscaler,
    )


def _port(capacity: ClusterCapacityRaw, historical: float | None = None) -> MagicMock:
    port = MagicMock(spec=SpikeProvisioningPort)
    port.get_cluster_capacity.return_value = capacity
    port.get_historical_spike_multiplier.return_value = historical
    return port


class TestPlanSpikeProvisioningService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.plan_spike_provisioning.plan_spike_provisioning_service_port import (  # noqa: E501
            PlanSpikeProvisioningServicePort,
        )
        from hexawyn.application.service.plan_spike_provisioning_service import (
            PlanSpikeProvisioningService,
        )

        service = PlanSpikeProvisioningService(spike_port=MagicMock(spec=SpikeProvisioningPort))

        assert isinstance(service, PlanSpikeProvisioningServicePort)

    def test_uses_provided_multiplier(self) -> None:
        from hexawyn.application.service.plan_spike_provisioning_service import (
            PlanSpikeProvisioningService,
        )

        service = PlanSpikeProvisioningService(spike_port=_port(_capacity()))

        response = service.plan(
            PlanSpikeProvisioningCommand(event_date="2026-11-27", traffic_multiplier=2.8)
        )

        assert response.result.traffic_multiplier == 2.8
        assert response.result.multiplier_source == "provided"

    def test_uses_historical_when_no_multiplier_provided(self) -> None:
        from hexawyn.application.service.plan_spike_provisioning_service import (
            PlanSpikeProvisioningService,
        )

        service = PlanSpikeProvisioningService(spike_port=_port(_capacity(), historical=3.0))

        response = service.plan(PlanSpikeProvisioningCommand(event_date="2026-11-27"))

        assert response.result.traffic_multiplier == 3.0
        assert response.result.multiplier_source == "historical"

    def test_falls_back_to_generic_when_no_history(self) -> None:
        from hexawyn.application.service.plan_spike_provisioning_service import (
            PlanSpikeProvisioningService,
        )

        service = PlanSpikeProvisioningService(spike_port=_port(_capacity(), historical=None))

        response = service.plan(PlanSpikeProvisioningCommand(event_date="2026-11-27"))

        assert response.result.traffic_multiplier == _GENERIC_MULTIPLIER
        assert response.result.multiplier_source == "generic_fallback"
        assert response.result.warning != ""

    def test_unpredictable_uses_pessimistic(self) -> None:
        from hexawyn.application.service.plan_spike_provisioning_service import (
            PlanSpikeProvisioningService,
        )

        service = PlanSpikeProvisioningService(spike_port=_port(_capacity(), historical=2.5))

        response = service.plan(
            PlanSpikeProvisioningCommand(event_date="2026-11-27", unpredictable=True)
        )

        assert response.result.multiplier_source == "pessimistic"
        assert response.result.traffic_multiplier == _PESSIMISTIC_MULTIPLIER

    def test_autoscaler_handles_verdict(self) -> None:
        from hexawyn.application.service.plan_spike_provisioning_service import (
            PlanSpikeProvisioningService,
        )

        service = PlanSpikeProvisioningService(
            spike_port=_port(_capacity(autoscaler=True), historical=2.8)
        )

        response = service.plan(PlanSpikeProvisioningCommand(event_date="2026-11-27"))

        assert response.result.verdict == "autoscaler_handles"

    def test_lets_error_propagate(self) -> None:
        import pytest
        from hexawyn.application.service.plan_spike_provisioning_service import (
            PlanSpikeProvisioningService,
        )
        from hexawyn.domain.errors import ClusterUnreachableError

        port = MagicMock(spec=SpikeProvisioningPort)
        port.get_cluster_capacity.side_effect = ClusterUnreachableError("down")
        service = PlanSpikeProvisioningService(spike_port=port)

        with pytest.raises(ClusterUnreachableError):
            service.plan(PlanSpikeProvisioningCommand(event_date="2026-11-27"))
