from hexawyn.application.ports.driven.helm_values_diff_port import HelmValuesDiffPort
from hexawyn.application.use_case.diff_helm_values.command import DiffHelmValuesCommand
from hexawyn.application.use_case.diff_helm_values.response import DiffHelmValuesResponse


class DiffHelmValuesUseCase:
    def __init__(self, helm_values_port: HelmValuesDiffPort) -> None:
        self._port = helm_values_port

    def execute(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        return DiffHelmValuesResponse()
