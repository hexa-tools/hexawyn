from hexawyn.application.ports.driven.memory_saturation_port import MemorySaturationPort
from hexawyn.application.use_case.memory_saturation.command import MemorySaturationCommand
from hexawyn.application.use_case.memory_saturation.response import MemorySaturationResponse


class MemorySaturationUseCase:
    def __init__(self, port: MemorySaturationPort) -> None:
        self._port = port

    def execute(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        return MemorySaturationResponse()
