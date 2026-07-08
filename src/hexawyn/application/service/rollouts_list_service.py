from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.ports.driving.rollouts_list.rollouts_list_command import (
    RolloutsListCommand,
)
from hexawyn.application.ports.driving.rollouts_list.rollouts_list_response import (
    RolloutsListResponse,
)
from hexawyn.application.ports.driving.rollouts_list.rollouts_list_service_port import (
    RolloutsListServicePort,
)


class RolloutsListService(RolloutsListServicePort):
    def __init__(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port

    def list_rollouts(self, command: RolloutsListCommand) -> RolloutsListResponse:
        rollouts = self._rollouts.list_rollouts(namespace=command.namespace)
        return RolloutsListResponse(
            rollouts=[asdict(r) for r in rollouts],
        )
