from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.use_case.workloads.rollouts_list.command import (
    RolloutsListCommand,
)
from hexawyn.application.use_case.workloads.rollouts_list.response import (
    RolloutsListResponse,
)


class RolloutsListUseCase:
    def __init__(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port

    def execute(self, command: RolloutsListCommand) -> RolloutsListResponse:
        rollouts = self._rollouts.list_rollouts(namespace=command.namespace)
        return RolloutsListResponse(
            rollouts=[asdict(r) for r in rollouts],
        )
