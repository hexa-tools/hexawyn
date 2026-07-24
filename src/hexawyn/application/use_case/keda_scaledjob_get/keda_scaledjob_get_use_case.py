from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda_scaledjob_get.command import KedaScaledjobGetCommand
from hexawyn.application.use_case.keda_scaledjob_get.response import KedaScaledjobGetResponse


class KedaScaledJobGetUseCase:
    def __init__(self, keda_port: KedaPort) -> None:
        self._port = keda_port

    def execute(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        sj = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(name=sj.name, namespace=sj.namespace, phase=sj.phase.value)
