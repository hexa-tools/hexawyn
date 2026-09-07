from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda.keda_scaledobject_triggers.command import (
    KedaScaledobjectTriggersCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobject_triggers.response import (
    KedaScaledobjectTriggersResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKedaScaledobjectTriggersUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut: MutantDict = {}  # type: ignore


class KedaScaledobjectTriggersUseCase:
    @_mutmut_mutated(mutants_xǁKedaScaledobjectTriggersUseCaseǁ__init____mutmut)
    def __init__(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaScaledobjectTriggersUseCaseǁ__init____mutmut_orig(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaScaledobjectTriggersUseCaseǁ__init____mutmut_1(self, port: KedaPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut)
    def get_triggers(
        self, command: KedaScaledobjectTriggersCommand
    ) -> KedaScaledobjectTriggersResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectTriggersResponse(triggers=[asdict(t) for t in so.triggers])

    def xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_orig(
        self, command: KedaScaledobjectTriggersCommand
    ) -> KedaScaledobjectTriggersResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectTriggersResponse(triggers=[asdict(t) for t in so.triggers])

    def xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_1(
        self, command: KedaScaledobjectTriggersCommand
    ) -> KedaScaledobjectTriggersResponse:
        so = None
        return KedaScaledobjectTriggersResponse(triggers=[asdict(t) for t in so.triggers])

    def xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_2(
        self, command: KedaScaledobjectTriggersCommand
    ) -> KedaScaledobjectTriggersResponse:
        so = self._port.get_scaledobject(name=None, namespace=command.namespace)
        return KedaScaledobjectTriggersResponse(triggers=[asdict(t) for t in so.triggers])

    def xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_3(
        self, command: KedaScaledobjectTriggersCommand
    ) -> KedaScaledobjectTriggersResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=None)
        return KedaScaledobjectTriggersResponse(triggers=[asdict(t) for t in so.triggers])

    def xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_4(
        self, command: KedaScaledobjectTriggersCommand
    ) -> KedaScaledobjectTriggersResponse:
        so = self._port.get_scaledobject(namespace=command.namespace)
        return KedaScaledobjectTriggersResponse(triggers=[asdict(t) for t in so.triggers])

    def xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_5(
        self, command: KedaScaledobjectTriggersCommand
    ) -> KedaScaledobjectTriggersResponse:
        so = self._port.get_scaledobject(name=command.name, )
        return KedaScaledobjectTriggersResponse(triggers=[asdict(t) for t in so.triggers])

    def xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_6(
        self, command: KedaScaledobjectTriggersCommand
    ) -> KedaScaledobjectTriggersResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectTriggersResponse(triggers=None)

    def xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_7(
        self, command: KedaScaledobjectTriggersCommand
    ) -> KedaScaledobjectTriggersResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectTriggersResponse(triggers=[asdict(None) for t in so.triggers])

mutants_xǁKedaScaledobjectTriggersUseCaseǁ__init____mutmut['_mutmut_orig'] = KedaScaledobjectTriggersUseCase.xǁKedaScaledobjectTriggersUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectTriggersUseCaseǁ__init____mutmut['xǁKedaScaledobjectTriggersUseCaseǁ__init____mutmut_1'] = KedaScaledobjectTriggersUseCase.xǁKedaScaledobjectTriggersUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut['_mutmut_orig'] = KedaScaledobjectTriggersUseCase.xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut['xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_1'] = KedaScaledobjectTriggersUseCase.xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut['xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_2'] = KedaScaledobjectTriggersUseCase.xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut['xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_3'] = KedaScaledobjectTriggersUseCase.xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut['xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_4'] = KedaScaledobjectTriggersUseCase.xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut['xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_5'] = KedaScaledobjectTriggersUseCase.xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut['xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_6'] = KedaScaledobjectTriggersUseCase.xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut['xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_7'] = KedaScaledobjectTriggersUseCase.xǁKedaScaledobjectTriggersUseCaseǁget_triggers__mutmut_7 # type: ignore # mutmut generated
