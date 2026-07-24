from hexawyn.application.ports.driven.cluster_operator_status_port import ClusterOperatorStatusPort
from hexawyn.application.use_case.check_cluster_operator_health.command import (
    CheckClusterOperatorHealthCommand,
)
from hexawyn.application.use_case.check_cluster_operator_health.response import (
    CheckClusterOperatorHealthResponse,
)
from hexawyn.domain.services.cluster_operator_health.cluster_operator_health_service import (
    ClusterOperatorHealthService,
)


class CheckClusterOperatorHealthUseCase:
    def __init__(self, operator_port: ClusterOperatorStatusPort) -> None:
        self._port = operator_port
        self._engine = ClusterOperatorHealthService()

    def execute(
        self, command: CheckClusterOperatorHealthCommand
    ) -> CheckClusterOperatorHealthResponse:
        operators = self._port.list_cluster_operators()
        result = self._engine.evaluate(operators)
        return CheckClusterOperatorHealthResponse(result=result)
