from __future__ import annotations

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda.keda_detect.command import KedaDetectCommand
from hexawyn.application.use_case.keda.keda_detect.response import KedaDetectResponse


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKedaDetectUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁKedaDetectUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class KedaDetectUseCase:
    @_mutmut_mutated(mutants_xǁKedaDetectUseCaseǁ__init____mutmut)
    def __init__(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaDetectUseCaseǁ__init____mutmut_orig(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaDetectUseCaseǁ__init____mutmut_1(self, port: KedaPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁKedaDetectUseCaseǁexecute__mutmut)
    def execute(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_orig(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_1(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = None
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_2(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=None,
            version=r.version,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_3(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=None,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_4(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=None,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_5(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_scaledobjects=None,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_6(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=None,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_7(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=None,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_8(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=None,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_9(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=None,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_10(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=None,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_11(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            version=r.version,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_12(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_13(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_14(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_15(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_16(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_17(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            total_scaledjobs=r.total_scaledjobs,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_18(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            managed_namespaces=r.managed_namespaces,
        )

    def xǁKedaDetectUseCaseǁexecute__mutmut_19(self, command: KedaDetectCommand) -> KedaDetectResponse:
        r = self._port.detect()
        return KedaDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_scaledobjects=r.total_scaledobjects,
            ready_scaledobjects=r.ready_scaledobjects,
            error_scaledobjects=r.error_scaledobjects,
            scaled_to_zero_count=r.scaled_to_zero_count,
            total_scaledjobs=r.total_scaledjobs,
            )

mutants_xǁKedaDetectUseCaseǁ__init____mutmut['_mutmut_orig'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁ__init____mutmut['xǁKedaDetectUseCaseǁ__init____mutmut_1'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁKedaDetectUseCaseǁexecute__mutmut['_mutmut_orig'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_1'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_2'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_3'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_4'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_5'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_6'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_7'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_8'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_9'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_10'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_11'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_12'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_13'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_14'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_15'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_16'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_17'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_18'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKedaDetectUseCaseǁexecute__mutmut['xǁKedaDetectUseCaseǁexecute__mutmut_19'] = KedaDetectUseCase.xǁKedaDetectUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
