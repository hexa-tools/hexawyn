from hexawyn.application.ports.driving.run_consolidation.run_consolidation_command import (
    RunConsolidationCommand,
)
from hexawyn.application.ports.driving.run_consolidation.run_consolidation_response import (
    RunConsolidationResponse,
)
from hexawyn.application.ports.driving.run_consolidation.run_consolidation_service_port import (
    RunConsolidationServicePort,
)


class RunConsolidationUseCase:
    def __init__(self, service: RunConsolidationServicePort) -> None:
        self._service = service

    def execute(self, command: RunConsolidationCommand) -> RunConsolidationResponse:
        return self._service.execute(command)
