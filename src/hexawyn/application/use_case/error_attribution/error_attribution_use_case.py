from hexawyn.application.ports.driven.error_attribution_port import ErrorAttributionPort
from hexawyn.application.use_case.error_attribution.command import ErrorAttributionCommand
from hexawyn.application.use_case.error_attribution.response import ErrorAttributionResponse


class ErrorAttributionUseCase:
    def __init__(self, port: ErrorAttributionPort) -> None:
        self._port = port

    def execute(self, cmd: ErrorAttributionCommand) -> ErrorAttributionResponse:
        return ErrorAttributionResponse()
