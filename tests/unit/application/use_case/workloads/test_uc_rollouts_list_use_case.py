from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.workloads.rollouts_list.command import (
    RolloutsListCommand,
)
from hexawyn.application.use_case.workloads.rollouts_list.response import (
    RolloutsListResponse,
)
from hexawyn.application.use_case.workloads.rollouts_list.rollouts_list_use_case import (
    RolloutsListUseCase,
)
from hexawyn.domain.models.rollouts import (
    Rollout,
    RolloutPhase,
    RolloutStrategy,
)


class TestRolloutsListUseCase:
    def test_execute_returns_response_empty(self) -> None:
        port = MagicMock()
        port.list_rollouts.return_value = []

        use_case = RolloutsListUseCase(rollouts_port=port)
        result = use_case.execute(RolloutsListCommand())

        assert isinstance(result, RolloutsListResponse)
        assert result.rollouts == []

    def test_execute_returns_rollouts(self) -> None:
        port = MagicMock()
        port.list_rollouts.return_value = [
            Rollout(
                name="canary-demo",
                namespace="default",
                strategy=RolloutStrategy.CANARY,
                phase=RolloutPhase.PROGRESSING,
                desired_replicas=5,
                ready_replicas=3,
                current_image="nginx:2.0",
            ),
        ]

        use_case = RolloutsListUseCase(rollouts_port=port)
        result = use_case.execute(RolloutsListCommand(namespace="default"))

        assert isinstance(result, RolloutsListResponse)
        assert len(result.rollouts) == 1
        assert result.rollouts[0]["name"] == "canary-demo"
