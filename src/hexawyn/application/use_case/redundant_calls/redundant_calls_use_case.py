from __future__ import annotations

from hexawyn.application.ports.driving.redundant_calls.redundant_calls_command import (
    RedundantCallsCommand,
)
from hexawyn.application.ports.driving.redundant_calls.redundant_calls_response import (
    RedundantCallsResponse,
)
from hexawyn.application.ports.driving.redundant_calls.redundant_calls_service_port import (
    RedundantCallsServicePort,
)


class RedundantCallsUseCase:
    def __init__(self, service: RedundantCallsServicePort) -> None:
        self._svc = service

    def execute(self, cmd: RedundantCallsCommand) -> RedundantCallsResponse:
        return self._svc.detect(cmd)
