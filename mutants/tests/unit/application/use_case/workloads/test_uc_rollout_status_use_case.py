from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.workloads.rollout_status.command import (
    RolloutStatusCommand,
)
from hexawyn.application.use_case.workloads.rollout_status.response import (
    RolloutStatusResponse,
)
from hexawyn.application.use_case.workloads.rollout_status.rollout_status_use_case import (  # noqa: E501
    RolloutStatusUseCase,
)


class TestRolloutStatusUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        rollout = MagicMock()
        rollout.name = "my-app"
        rollout.namespace = "default"
        rollout.status = "Progressing"
        rollout.replicas = 3
        rollout.ready_replicas = 2
        port.get_rollout.return_value = rollout

        use_case = RolloutStatusUseCase(rollouts_port=port)
        result = use_case.execute(RolloutStatusCommand(name="my-app", namespace="default"))

        assert isinstance(result, RolloutStatusResponse)
