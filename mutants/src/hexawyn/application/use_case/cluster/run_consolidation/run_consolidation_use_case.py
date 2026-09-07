from hexawyn.application.ports.driven.consolidation_port import ConsolidationPort
from hexawyn.application.use_case.cluster.run_consolidation.command import (
    RunConsolidationCommand,
)
from hexawyn.application.use_case.cluster.run_consolidation.response import (
    RunConsolidationResponse,
)
from hexawyn.domain.services.consolidation_job import ConsolidationJob


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁRunConsolidationUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁRunConsolidationUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class RunConsolidationUseCase:
    @_mutmut_mutated(mutants_xǁRunConsolidationUseCaseǁ__init____mutmut)
    def __init__(self, consolidation_port: ConsolidationPort) -> None:
        self._port = consolidation_port
    def xǁRunConsolidationUseCaseǁ__init____mutmut_orig(self, consolidation_port: ConsolidationPort) -> None:
        self._port = consolidation_port
    def xǁRunConsolidationUseCaseǁ__init____mutmut_1(self, consolidation_port: ConsolidationPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁRunConsolidationUseCaseǁexecute__mutmut)
    def execute(self, command: RunConsolidationCommand) -> RunConsolidationResponse:
        job = ConsolidationJob(port=self._port)
        results = job.run(cluster_name=command.cluster_name)
        return RunConsolidationResponse(
            consolidated=results,
            groups_found=len(results),
        )

    def xǁRunConsolidationUseCaseǁexecute__mutmut_orig(self, command: RunConsolidationCommand) -> RunConsolidationResponse:
        job = ConsolidationJob(port=self._port)
        results = job.run(cluster_name=command.cluster_name)
        return RunConsolidationResponse(
            consolidated=results,
            groups_found=len(results),
        )

    def xǁRunConsolidationUseCaseǁexecute__mutmut_1(self, command: RunConsolidationCommand) -> RunConsolidationResponse:
        job = None
        results = job.run(cluster_name=command.cluster_name)
        return RunConsolidationResponse(
            consolidated=results,
            groups_found=len(results),
        )

    def xǁRunConsolidationUseCaseǁexecute__mutmut_2(self, command: RunConsolidationCommand) -> RunConsolidationResponse:
        job = ConsolidationJob(port=None)
        results = job.run(cluster_name=command.cluster_name)
        return RunConsolidationResponse(
            consolidated=results,
            groups_found=len(results),
        )

    def xǁRunConsolidationUseCaseǁexecute__mutmut_3(self, command: RunConsolidationCommand) -> RunConsolidationResponse:
        job = ConsolidationJob(port=self._port)
        results = None
        return RunConsolidationResponse(
            consolidated=results,
            groups_found=len(results),
        )

    def xǁRunConsolidationUseCaseǁexecute__mutmut_4(self, command: RunConsolidationCommand) -> RunConsolidationResponse:
        job = ConsolidationJob(port=self._port)
        results = job.run(cluster_name=None)
        return RunConsolidationResponse(
            consolidated=results,
            groups_found=len(results),
        )

    def xǁRunConsolidationUseCaseǁexecute__mutmut_5(self, command: RunConsolidationCommand) -> RunConsolidationResponse:
        job = ConsolidationJob(port=self._port)
        results = job.run(cluster_name=command.cluster_name)
        return RunConsolidationResponse(
            consolidated=None,
            groups_found=len(results),
        )

    def xǁRunConsolidationUseCaseǁexecute__mutmut_6(self, command: RunConsolidationCommand) -> RunConsolidationResponse:
        job = ConsolidationJob(port=self._port)
        results = job.run(cluster_name=command.cluster_name)
        return RunConsolidationResponse(
            consolidated=results,
            groups_found=None,
        )

    def xǁRunConsolidationUseCaseǁexecute__mutmut_7(self, command: RunConsolidationCommand) -> RunConsolidationResponse:
        job = ConsolidationJob(port=self._port)
        results = job.run(cluster_name=command.cluster_name)
        return RunConsolidationResponse(
            groups_found=len(results),
        )

    def xǁRunConsolidationUseCaseǁexecute__mutmut_8(self, command: RunConsolidationCommand) -> RunConsolidationResponse:
        job = ConsolidationJob(port=self._port)
        results = job.run(cluster_name=command.cluster_name)
        return RunConsolidationResponse(
            consolidated=results,
            )

mutants_xǁRunConsolidationUseCaseǁ__init____mutmut['_mutmut_orig'] = RunConsolidationUseCase.xǁRunConsolidationUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁRunConsolidationUseCaseǁ__init____mutmut['xǁRunConsolidationUseCaseǁ__init____mutmut_1'] = RunConsolidationUseCase.xǁRunConsolidationUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁRunConsolidationUseCaseǁexecute__mutmut['_mutmut_orig'] = RunConsolidationUseCase.xǁRunConsolidationUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRunConsolidationUseCaseǁexecute__mutmut['xǁRunConsolidationUseCaseǁexecute__mutmut_1'] = RunConsolidationUseCase.xǁRunConsolidationUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRunConsolidationUseCaseǁexecute__mutmut['xǁRunConsolidationUseCaseǁexecute__mutmut_2'] = RunConsolidationUseCase.xǁRunConsolidationUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRunConsolidationUseCaseǁexecute__mutmut['xǁRunConsolidationUseCaseǁexecute__mutmut_3'] = RunConsolidationUseCase.xǁRunConsolidationUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRunConsolidationUseCaseǁexecute__mutmut['xǁRunConsolidationUseCaseǁexecute__mutmut_4'] = RunConsolidationUseCase.xǁRunConsolidationUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRunConsolidationUseCaseǁexecute__mutmut['xǁRunConsolidationUseCaseǁexecute__mutmut_5'] = RunConsolidationUseCase.xǁRunConsolidationUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRunConsolidationUseCaseǁexecute__mutmut['xǁRunConsolidationUseCaseǁexecute__mutmut_6'] = RunConsolidationUseCase.xǁRunConsolidationUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRunConsolidationUseCaseǁexecute__mutmut['xǁRunConsolidationUseCaseǁexecute__mutmut_7'] = RunConsolidationUseCase.xǁRunConsolidationUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRunConsolidationUseCaseǁexecute__mutmut['xǁRunConsolidationUseCaseǁexecute__mutmut_8'] = RunConsolidationUseCase.xǁRunConsolidationUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
