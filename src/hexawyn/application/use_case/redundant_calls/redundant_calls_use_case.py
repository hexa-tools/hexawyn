from dataclasses import asdict

from hexawyn.application.ports.driven.redundant_call_detection_port import (
    RedundantCallDetectionPort,
)
from hexawyn.application.use_case.redundant_calls.command import RedundantCallsCommand
from hexawyn.application.use_case.redundant_calls.response import RedundantCallsResponse


class RedundantCallsUseCase:
    def __init__(self, port: RedundantCallDetectionPort) -> None:
        self._port = port

    def execute(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        calls = self._port.detect_redundant_calls(namespace=command.namespace)
        return RedundantCallsResponse(calls=[asdict(c) for c in calls])
