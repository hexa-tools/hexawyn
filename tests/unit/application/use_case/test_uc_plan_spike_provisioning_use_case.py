"""Unit tests for PlanSpikeProvisioningUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.plan_spike_provisioning.plan_spike_provisioning_service_port import (
    PlanSpikeProvisioningServicePort,
)
from hexawyn.application.use_case.plan_spike_provisioning.plan_spike_provisioning_use_case import (
    PlanSpikeProvisioningUseCase,
)


class TestPlanSpikeProvisioningUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=PlanSpikeProvisioningServicePort)
        use_case = PlanSpikeProvisioningUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.plan.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=PlanSpikeProvisioningServicePort)
        mock_service.plan.side_effect = RuntimeError("test error")
        use_case = PlanSpikeProvisioningUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
