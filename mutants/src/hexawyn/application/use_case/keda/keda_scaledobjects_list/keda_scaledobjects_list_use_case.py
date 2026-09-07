from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda.keda_scaledobjects_list.command import (
    KedaScaledobjectsListCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobjects_list.response import (
    KedaScaledobjectsListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKedaScaledobjectsListUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁKedaScaledobjectsListUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class KedaScaledobjectsListUseCase:
    @_mutmut_mutated(mutants_xǁKedaScaledobjectsListUseCaseǁ__init____mutmut)
    def __init__(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaScaledobjectsListUseCaseǁ__init____mutmut_orig(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaScaledobjectsListUseCaseǁ__init____mutmut_1(self, port: KedaPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁKedaScaledobjectsListUseCaseǁexecute__mutmut)
    def execute(self, command: KedaScaledobjectsListCommand) -> KedaScaledobjectsListResponse:
        objs = self._port.list_scaledobjects(namespace=command.namespace)
        return KedaScaledobjectsListResponse(scaled_objects=[asdict(o) for o in objs])

    def xǁKedaScaledobjectsListUseCaseǁexecute__mutmut_orig(self, command: KedaScaledobjectsListCommand) -> KedaScaledobjectsListResponse:
        objs = self._port.list_scaledobjects(namespace=command.namespace)
        return KedaScaledobjectsListResponse(scaled_objects=[asdict(o) for o in objs])

    def xǁKedaScaledobjectsListUseCaseǁexecute__mutmut_1(self, command: KedaScaledobjectsListCommand) -> KedaScaledobjectsListResponse:
        objs = None
        return KedaScaledobjectsListResponse(scaled_objects=[asdict(o) for o in objs])

    def xǁKedaScaledobjectsListUseCaseǁexecute__mutmut_2(self, command: KedaScaledobjectsListCommand) -> KedaScaledobjectsListResponse:
        objs = self._port.list_scaledobjects(namespace=None)
        return KedaScaledobjectsListResponse(scaled_objects=[asdict(o) for o in objs])

    def xǁKedaScaledobjectsListUseCaseǁexecute__mutmut_3(self, command: KedaScaledobjectsListCommand) -> KedaScaledobjectsListResponse:
        objs = self._port.list_scaledobjects(namespace=command.namespace)
        return KedaScaledobjectsListResponse(scaled_objects=None)

    def xǁKedaScaledobjectsListUseCaseǁexecute__mutmut_4(self, command: KedaScaledobjectsListCommand) -> KedaScaledobjectsListResponse:
        objs = self._port.list_scaledobjects(namespace=command.namespace)
        return KedaScaledobjectsListResponse(scaled_objects=[asdict(None) for o in objs])

mutants_xǁKedaScaledobjectsListUseCaseǁ__init____mutmut['_mutmut_orig'] = KedaScaledobjectsListUseCase.xǁKedaScaledobjectsListUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectsListUseCaseǁ__init____mutmut['xǁKedaScaledobjectsListUseCaseǁ__init____mutmut_1'] = KedaScaledobjectsListUseCase.xǁKedaScaledobjectsListUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁKedaScaledobjectsListUseCaseǁexecute__mutmut['_mutmut_orig'] = KedaScaledobjectsListUseCase.xǁKedaScaledobjectsListUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectsListUseCaseǁexecute__mutmut['xǁKedaScaledobjectsListUseCaseǁexecute__mutmut_1'] = KedaScaledobjectsListUseCase.xǁKedaScaledobjectsListUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectsListUseCaseǁexecute__mutmut['xǁKedaScaledobjectsListUseCaseǁexecute__mutmut_2'] = KedaScaledobjectsListUseCase.xǁKedaScaledobjectsListUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectsListUseCaseǁexecute__mutmut['xǁKedaScaledobjectsListUseCaseǁexecute__mutmut_3'] = KedaScaledobjectsListUseCase.xǁKedaScaledobjectsListUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectsListUseCaseǁexecute__mutmut['xǁKedaScaledobjectsListUseCaseǁexecute__mutmut_4'] = KedaScaledobjectsListUseCase.xǁKedaScaledobjectsListUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
