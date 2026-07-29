from __future__ import annotations

from unittest.mock import MagicMock


class TestPlanSpikeProvisioningUseCase:
    def test_execute_returns_response(self) -> None:
        from hexawyn.application.use_case.cluster.plan_spike_provisioning.command import (
            PlanSpikeProvisioningCommand,
        )
        from hexawyn.application.use_case.cluster.plan_spike_provisioning.plan_spike_provisioning_use_case import (  # noqa: E501
            PlanSpikeProvisioningUseCase,
        )
        from hexawyn.application.use_case.cluster.plan_spike_provisioning.response import (
            PlanSpikeProvisioningResponse,
        )

        port = MagicMock()
        port.get_cluster_capacity.return_value = {
            "node_count": 1,
            "allocatable_cpu_cores": 4,
            "allocatable_memory_gb": 16,
            "used_cpu_cores": 1,
            "used_memory_gb": 4,
            "autoscaler_enabled": False,
        }
        port.get_historical_spike_multiplier.return_value = None
        use_case = PlanSpikeProvisioningUseCase(spike_port=port)
        result = use_case.execute(PlanSpikeProvisioningCommand(event_date="2026-08-01"))
        assert isinstance(result, PlanSpikeProvisioningResponse)
