from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda.keda_scaledjobs_list.command import (
    KedaScaledjobsListCommand,
)
from hexawyn.application.use_case.keda.keda_scaledjobs_list.response import (
    KedaScaledjobsListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKedaScaledjobsListUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁKedaScaledjobsListUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class KedaScaledjobsListUseCase:
    @_mutmut_mutated(mutants_xǁKedaScaledjobsListUseCaseǁ__init____mutmut)
    def __init__(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaScaledjobsListUseCaseǁ__init____mutmut_orig(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaScaledjobsListUseCaseǁ__init____mutmut_1(self, port: KedaPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁKedaScaledjobsListUseCaseǁexecute__mutmut)
    def execute(self, command: KedaScaledjobsListCommand) -> KedaScaledjobsListResponse:
        jobs = self._port.list_scaledjobs(namespace=command.namespace)
        return KedaScaledjobsListResponse(scaled_jobs=[asdict(j) for j in jobs])

    def xǁKedaScaledjobsListUseCaseǁexecute__mutmut_orig(self, command: KedaScaledjobsListCommand) -> KedaScaledjobsListResponse:
        jobs = self._port.list_scaledjobs(namespace=command.namespace)
        return KedaScaledjobsListResponse(scaled_jobs=[asdict(j) for j in jobs])

    def xǁKedaScaledjobsListUseCaseǁexecute__mutmut_1(self, command: KedaScaledjobsListCommand) -> KedaScaledjobsListResponse:
        jobs = None
        return KedaScaledjobsListResponse(scaled_jobs=[asdict(j) for j in jobs])

    def xǁKedaScaledjobsListUseCaseǁexecute__mutmut_2(self, command: KedaScaledjobsListCommand) -> KedaScaledjobsListResponse:
        jobs = self._port.list_scaledjobs(namespace=None)
        return KedaScaledjobsListResponse(scaled_jobs=[asdict(j) for j in jobs])

    def xǁKedaScaledjobsListUseCaseǁexecute__mutmut_3(self, command: KedaScaledjobsListCommand) -> KedaScaledjobsListResponse:
        jobs = self._port.list_scaledjobs(namespace=command.namespace)
        return KedaScaledjobsListResponse(scaled_jobs=None)

    def xǁKedaScaledjobsListUseCaseǁexecute__mutmut_4(self, command: KedaScaledjobsListCommand) -> KedaScaledjobsListResponse:
        jobs = self._port.list_scaledjobs(namespace=command.namespace)
        return KedaScaledjobsListResponse(scaled_jobs=[asdict(None) for j in jobs])

mutants_xǁKedaScaledjobsListUseCaseǁ__init____mutmut['_mutmut_orig'] = KedaScaledjobsListUseCase.xǁKedaScaledjobsListUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaScaledjobsListUseCaseǁ__init____mutmut['xǁKedaScaledjobsListUseCaseǁ__init____mutmut_1'] = KedaScaledjobsListUseCase.xǁKedaScaledjobsListUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁKedaScaledjobsListUseCaseǁexecute__mutmut['_mutmut_orig'] = KedaScaledjobsListUseCase.xǁKedaScaledjobsListUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaScaledjobsListUseCaseǁexecute__mutmut['xǁKedaScaledjobsListUseCaseǁexecute__mutmut_1'] = KedaScaledjobsListUseCase.xǁKedaScaledjobsListUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobsListUseCaseǁexecute__mutmut['xǁKedaScaledjobsListUseCaseǁexecute__mutmut_2'] = KedaScaledjobsListUseCase.xǁKedaScaledjobsListUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobsListUseCaseǁexecute__mutmut['xǁKedaScaledjobsListUseCaseǁexecute__mutmut_3'] = KedaScaledjobsListUseCase.xǁKedaScaledjobsListUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobsListUseCaseǁexecute__mutmut['xǁKedaScaledjobsListUseCaseǁexecute__mutmut_4'] = KedaScaledjobsListUseCase.xǁKedaScaledjobsListUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
