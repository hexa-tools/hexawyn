from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.workloads.rollout_get.command import (
    RolloutGetCommand,
)
from hexawyn.application.use_case.workloads.rollout_get.response import (
    RolloutGetResponse,
)
from hexawyn.application.use_case.workloads.rollout_get.rollout_get_use_case import (
    RolloutGetUseCase,
)
from hexawyn.domain.models.rollouts import (
    Rollout,
    RolloutPhase,
    RolloutStepStatus,
    RolloutStrategy,
)


class TestRolloutGetUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_rollout.return_value = Rollout(
            name="canary-demo",
            namespace="default",
            strategy=RolloutStrategy.CANARY,
            phase=RolloutPhase.PROGRESSING,
            desired_replicas=5,
            ready_replicas=3,
            current_image="nginx:2.0",
            canary_replicas=1,
            stable_replicas=2,
            current_step=RolloutStepStatus(
                step_index=1,
                total_steps=3,
                current_step_type="canary",
                canary_weight=20,
                paused_at=None,
                pause_reason=None,
            ),
            stable_image="nginx:1.0",
            message=None,
            analysis_run_name="canary-demo-p5s7t",
        )

        use_case = RolloutGetUseCase(rollouts_port=port)
        result = use_case.execute(RolloutGetCommand(name="canary-demo", namespace="default"))

        assert isinstance(result, RolloutGetResponse)
        assert result.name == "canary-demo"
        assert result.strategy == "canary"
        assert result.phase == "progressing"
        assert result.step_index == 1  # noqa: PLR2004
        assert result.total_steps == 3  # noqa: PLR2004

    def test_execute_without_step_handles_none(self) -> None:
        port = MagicMock()
        port.get_rollout.return_value = Rollout(
            name="no-step",
            namespace="default",
            strategy=RolloutStrategy.BLUE_GREEN,
            phase=RolloutPhase.HEALTHY,
            desired_replicas=3,
            ready_replicas=3,
            current_image="nginx:1.0",
            current_step=None,
        )

        use_case = RolloutGetUseCase(rollouts_port=port)
        result = use_case.execute(RolloutGetCommand(name="no-step", namespace="default"))

        assert isinstance(result, RolloutGetResponse)
        assert result.step_index is None
        assert result.total_steps is None
