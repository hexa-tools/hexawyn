from hexawyn.application.ports.driven.consolidation_port import ConsolidationPort
from hexawyn.application.use_case.cluster.run_consolidation.command import (
    RunConsolidationCommand,
)
from hexawyn.application.use_case.cluster.run_consolidation.response import (
    RunConsolidationResponse,
)
from hexawyn.domain.services.consolidation_job import ConsolidationJob


class RunConsolidationUseCase:
    def __init__(self, consolidation_port: ConsolidationPort) -> None:
        self._port = consolidation_port

    def execute(self, command: RunConsolidationCommand) -> RunConsolidationResponse:
        job = ConsolidationJob(port=self._port)
        results = job.run(cluster_name=command.cluster_name)
        return RunConsolidationResponse(
            consolidated=results,
            groups_found=len(results),
        )
