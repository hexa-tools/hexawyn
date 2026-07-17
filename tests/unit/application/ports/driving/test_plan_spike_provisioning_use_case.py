from unittest.mock import MagicMock

from hexawyn.application.ports.driving.plan_spike_provisioning.plan_spike_provisioning_command import (  # noqa: E501
    PlanSpikeProvisioningCommand,
)
from hexawyn.application.ports.driving.plan_spike_provisioning.plan_spike_provisioning_response import (  # noqa: E501
    PlanSpikeProvisioningResponse,
)
from hexawyn.application.ports.driving.plan_spike_provisioning.plan_spike_provisioning_service_port import (  # noqa: E501
    PlanSpikeProvisioningServicePort,
)
from hexawyn.domain.models.spike_provisioning import SpikeProvisioningReport


class TestPlanSpikeProvisioningUseCase:
    def test_execute_delegates_to_service(self) -> None:
        from hexawyn.application.use_case.plan_spike_provisioning.plan_spike_provisioning_use_case import (  # noqa: E501
            PlanSpikeProvisioningUseCase,
        )

        service = MagicMock(spec=PlanSpikeProvisioningServicePort)
        expected = PlanSpikeProvisioningResponse(
            result=SpikeProvisioningReport(
                traffic_multiplier=2.8, multiplier_source="historical", verdict="provision"
            )
        )
        service.plan.return_value = expected
        use_case = PlanSpikeProvisioningUseCase(service=service)
        command = PlanSpikeProvisioningCommand(event_date="2026-11-27")

        response = use_case.execute(command)

        service.plan.assert_called_once_with(command)
        assert response is expected
