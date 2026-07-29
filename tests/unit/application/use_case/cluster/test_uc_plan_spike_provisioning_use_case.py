from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cluster.plan_spike_provisioning.command import (
    PlanSpikeProvisioningCommand,
)
from hexawyn.application.use_case.cluster.plan_spike_provisioning.plan_spike_provisioning_use_case import (  # noqa: E501
    PlanSpikeProvisioningUseCase,
)
from hexawyn.application.use_case.cluster.plan_spike_provisioning.response import (
    PlanSpikeProvisioningResponse,
)


class TestPlanSpikeProvisioningUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_cluster_capacity.return_value = {
            "node_count": 6,
            "allocatable_cpu_cores": 24.0,
            "allocatable_memory_gb": 96.0,
            "used_cpu_cores": 15.0,
            "used_memory_gb": 60.0,
            "autoscaler_enabled": True,
        }
        port.get_historical_spike_multiplier.return_value = None

        use_case = PlanSpikeProvisioningUseCase(spike_port=port)
        result = use_case.execute(PlanSpikeProvisioningCommand(event_date="2026-12-25"))

        assert isinstance(result, PlanSpikeProvisioningResponse)

    def test_execute_with_provided_multiplier(self) -> None:
        port = MagicMock()
        port.get_cluster_capacity.return_value = {
            "node_count": 10,
            "allocatable_cpu_cores": 40.0,
            "allocatable_memory_gb": 160.0,
            "used_cpu_cores": 8.0,
            "used_memory_gb": 32.0,
            "autoscaler_enabled": False,
        }

        use_case = PlanSpikeProvisioningUseCase(spike_port=port)
        result = use_case.execute(
            PlanSpikeProvisioningCommand(
                event_date="2026-12-31",
                traffic_multiplier=5.0,
            )
        )

        assert isinstance(result, PlanSpikeProvisioningResponse)

    def test_execute_unpredictable_uses_pessimistic_multiplier(self) -> None:
        port = MagicMock()
        port.get_cluster_capacity.return_value = {
            "node_count": 4,
            "allocatable_cpu_cores": 16.0,
            "allocatable_memory_gb": 64.0,
            "used_cpu_cores": 14.0,
            "used_memory_gb": 60.0,
            "autoscaler_enabled": False,
        }

        use_case = PlanSpikeProvisioningUseCase(spike_port=port)
        result = use_case.execute(
            PlanSpikeProvisioningCommand(
                event_date="2026-11-01",
                unpredictable=True,
            )
        )

        assert isinstance(result, PlanSpikeProvisioningResponse)

    def test_execute_with_historical_multiplier(self) -> None:
        port = MagicMock()
        port.get_cluster_capacity.return_value = {
            "node_count": 6,
            "allocatable_cpu_cores": 24.0,
            "allocatable_memory_gb": 96.0,
            "used_cpu_cores": 15.0,
            "used_memory_gb": 60.0,
            "autoscaler_enabled": True,
        }
        port.get_historical_spike_multiplier.return_value = 3.5

        use_case = PlanSpikeProvisioningUseCase(spike_port=port)
        result = use_case.execute(PlanSpikeProvisioningCommand(event_date="2026-12-25"))

        assert isinstance(result, PlanSpikeProvisioningResponse)
        assert result.result.multiplier_source == "historical"
        assert result.result.traffic_multiplier == 3.5  # noqa: PLR2004
