from hexawyn.application.ports.driven.pod_resource_metrics_port import PodResourceMetricsPort
from hexawyn.application.use_case.cluster.check_resource_constraints.command import (
    CheckResourceConstraintsCommand,
)
from hexawyn.application.use_case.cluster.check_resource_constraints.response import (
    CheckResourceConstraintsResponse,
)


class CheckResourceConstraintsUseCase:
    def __init__(self, port: PodResourceMetricsPort) -> None:
        self._port = port

    def execute(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )
