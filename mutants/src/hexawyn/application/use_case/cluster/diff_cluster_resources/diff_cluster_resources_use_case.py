from __future__ import annotations

from hexawyn.application.ports.driven.cluster_diff_port import ClusterDiffPort
from hexawyn.application.use_case.cluster.diff_cluster_resources.command import (  # noqa: E501
    DiffClusterResourcesCommand,
)
from hexawyn.application.use_case.cluster.diff_cluster_resources.response import (  # noqa: E501
    DiffClusterResourcesResponse,
)
from hexawyn.domain.services.cluster_diff.cluster_diff_service import (
    compute_diff,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDiffClusterResourcesUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDiffClusterResourcesUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class DiffClusterResourcesUseCase:
    @_mutmut_mutated(mutants_xǁDiffClusterResourcesUseCaseǁ__init____mutmut)
    def __init__(self, cluster_diff_port: ClusterDiffPort) -> None:
        self._port = cluster_diff_port
    def xǁDiffClusterResourcesUseCaseǁ__init____mutmut_orig(self, cluster_diff_port: ClusterDiffPort) -> None:
        self._port = cluster_diff_port
    def xǁDiffClusterResourcesUseCaseǁ__init____mutmut_1(self, cluster_diff_port: ClusterDiffPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁDiffClusterResourcesUseCaseǁexecute__mutmut)
    def execute(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse:
        staging = self._port.get_resource_inventory(command.source_context)
        prod = self._port.get_resource_inventory(command.target_context)
        result = compute_diff(staging, prod)
        return DiffClusterResourcesResponse(result=result)

    def xǁDiffClusterResourcesUseCaseǁexecute__mutmut_orig(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse:
        staging = self._port.get_resource_inventory(command.source_context)
        prod = self._port.get_resource_inventory(command.target_context)
        result = compute_diff(staging, prod)
        return DiffClusterResourcesResponse(result=result)

    def xǁDiffClusterResourcesUseCaseǁexecute__mutmut_1(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse:
        staging = None
        prod = self._port.get_resource_inventory(command.target_context)
        result = compute_diff(staging, prod)
        return DiffClusterResourcesResponse(result=result)

    def xǁDiffClusterResourcesUseCaseǁexecute__mutmut_2(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse:
        staging = self._port.get_resource_inventory(None)
        prod = self._port.get_resource_inventory(command.target_context)
        result = compute_diff(staging, prod)
        return DiffClusterResourcesResponse(result=result)

    def xǁDiffClusterResourcesUseCaseǁexecute__mutmut_3(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse:
        staging = self._port.get_resource_inventory(command.source_context)
        prod = None
        result = compute_diff(staging, prod)
        return DiffClusterResourcesResponse(result=result)

    def xǁDiffClusterResourcesUseCaseǁexecute__mutmut_4(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse:
        staging = self._port.get_resource_inventory(command.source_context)
        prod = self._port.get_resource_inventory(None)
        result = compute_diff(staging, prod)
        return DiffClusterResourcesResponse(result=result)

    def xǁDiffClusterResourcesUseCaseǁexecute__mutmut_5(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse:
        staging = self._port.get_resource_inventory(command.source_context)
        prod = self._port.get_resource_inventory(command.target_context)
        result = None
        return DiffClusterResourcesResponse(result=result)

    def xǁDiffClusterResourcesUseCaseǁexecute__mutmut_6(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse:
        staging = self._port.get_resource_inventory(command.source_context)
        prod = self._port.get_resource_inventory(command.target_context)
        result = compute_diff(None, prod)
        return DiffClusterResourcesResponse(result=result)

    def xǁDiffClusterResourcesUseCaseǁexecute__mutmut_7(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse:
        staging = self._port.get_resource_inventory(command.source_context)
        prod = self._port.get_resource_inventory(command.target_context)
        result = compute_diff(staging, None)
        return DiffClusterResourcesResponse(result=result)

    def xǁDiffClusterResourcesUseCaseǁexecute__mutmut_8(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse:
        staging = self._port.get_resource_inventory(command.source_context)
        prod = self._port.get_resource_inventory(command.target_context)
        result = compute_diff(prod)
        return DiffClusterResourcesResponse(result=result)

    def xǁDiffClusterResourcesUseCaseǁexecute__mutmut_9(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse:
        staging = self._port.get_resource_inventory(command.source_context)
        prod = self._port.get_resource_inventory(command.target_context)
        result = compute_diff(staging, )
        return DiffClusterResourcesResponse(result=result)

    def xǁDiffClusterResourcesUseCaseǁexecute__mutmut_10(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse:
        staging = self._port.get_resource_inventory(command.source_context)
        prod = self._port.get_resource_inventory(command.target_context)
        result = compute_diff(staging, prod)
        return DiffClusterResourcesResponse(result=None)

mutants_xǁDiffClusterResourcesUseCaseǁ__init____mutmut['_mutmut_orig'] = DiffClusterResourcesUseCase.xǁDiffClusterResourcesUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDiffClusterResourcesUseCaseǁ__init____mutmut['xǁDiffClusterResourcesUseCaseǁ__init____mutmut_1'] = DiffClusterResourcesUseCase.xǁDiffClusterResourcesUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁDiffClusterResourcesUseCaseǁexecute__mutmut['_mutmut_orig'] = DiffClusterResourcesUseCase.xǁDiffClusterResourcesUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDiffClusterResourcesUseCaseǁexecute__mutmut['xǁDiffClusterResourcesUseCaseǁexecute__mutmut_1'] = DiffClusterResourcesUseCase.xǁDiffClusterResourcesUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDiffClusterResourcesUseCaseǁexecute__mutmut['xǁDiffClusterResourcesUseCaseǁexecute__mutmut_2'] = DiffClusterResourcesUseCase.xǁDiffClusterResourcesUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDiffClusterResourcesUseCaseǁexecute__mutmut['xǁDiffClusterResourcesUseCaseǁexecute__mutmut_3'] = DiffClusterResourcesUseCase.xǁDiffClusterResourcesUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDiffClusterResourcesUseCaseǁexecute__mutmut['xǁDiffClusterResourcesUseCaseǁexecute__mutmut_4'] = DiffClusterResourcesUseCase.xǁDiffClusterResourcesUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDiffClusterResourcesUseCaseǁexecute__mutmut['xǁDiffClusterResourcesUseCaseǁexecute__mutmut_5'] = DiffClusterResourcesUseCase.xǁDiffClusterResourcesUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDiffClusterResourcesUseCaseǁexecute__mutmut['xǁDiffClusterResourcesUseCaseǁexecute__mutmut_6'] = DiffClusterResourcesUseCase.xǁDiffClusterResourcesUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDiffClusterResourcesUseCaseǁexecute__mutmut['xǁDiffClusterResourcesUseCaseǁexecute__mutmut_7'] = DiffClusterResourcesUseCase.xǁDiffClusterResourcesUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDiffClusterResourcesUseCaseǁexecute__mutmut['xǁDiffClusterResourcesUseCaseǁexecute__mutmut_8'] = DiffClusterResourcesUseCase.xǁDiffClusterResourcesUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDiffClusterResourcesUseCaseǁexecute__mutmut['xǁDiffClusterResourcesUseCaseǁexecute__mutmut_9'] = DiffClusterResourcesUseCase.xǁDiffClusterResourcesUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDiffClusterResourcesUseCaseǁexecute__mutmut['xǁDiffClusterResourcesUseCaseǁexecute__mutmut_10'] = DiffClusterResourcesUseCase.xǁDiffClusterResourcesUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
