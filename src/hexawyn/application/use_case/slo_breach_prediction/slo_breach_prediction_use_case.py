from hexawyn.application.ports.driven.slo_breach_prediction_port import SLOBreachPredictionPort
from hexawyn.application.use_case.slo_breach_prediction.command import SloBreachPredictionCommand
from hexawyn.application.use_case.slo_breach_prediction.response import SloBreachPredictionResponse


class SloBreachPredictionUseCase:
    def __init__(self, port: SLOBreachPredictionPort) -> None:
        self._port = port

    def execute(self, command: SloBreachPredictionCommand) -> SloBreachPredictionResponse:
        return SloBreachPredictionResponse()
