from hexawyn.application.ports.driven.pod_resource_metrics_port import PodResourceMetricsPort
from hexawyn.application.use_case.check_resource_constraints.command import (
    CheckResourceConstraintsCommand,
)
from hexawyn.application.use_case.check_resource_constraints.response import (
    CheckResourceConstraintsResponse,
)


class CheckResourceConstraintsUseCase:
    def __init__(self, port: PodResourceMetricsPort) -> None:
        self._port = port

    def execute(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        return CheckResourceConstraintsResponse()
