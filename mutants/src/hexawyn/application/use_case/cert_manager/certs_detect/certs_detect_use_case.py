from __future__ import annotations

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.use_case.cert_manager.certs_detect.command import CertsDetectCommand
from hexawyn.application.use_case.cert_manager.certs_detect.response import CertsDetectResponse


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCertsDetectUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCertsDetectUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CertsDetectUseCase:
    @_mutmut_mutated(mutants_xǁCertsDetectUseCaseǁ__init____mutmut)
    def __init__(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsDetectUseCaseǁ__init____mutmut_orig(self, port: CertManagerPort) -> None:
        self._port = port
    def xǁCertsDetectUseCaseǁ__init____mutmut_1(self, port: CertManagerPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCertsDetectUseCaseǁexecute__mutmut)
    def execute(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_certs=r.total_certs,
            ready_certs=r.ready_certs,
            expiring_soon=r.expiring_soon,
            failed_certs=r.failed_certs,
            active_challenges=r.active_challenges,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_orig(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_certs=r.total_certs,
            ready_certs=r.ready_certs,
            expiring_soon=r.expiring_soon,
            failed_certs=r.failed_certs,
            active_challenges=r.active_challenges,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_1(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = None
        return CertsDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_certs=r.total_certs,
            ready_certs=r.ready_certs,
            expiring_soon=r.expiring_soon,
            failed_certs=r.failed_certs,
            active_challenges=r.active_challenges,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_2(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=None,
            version=r.version,
            namespace=r.namespace,
            total_certs=r.total_certs,
            ready_certs=r.ready_certs,
            expiring_soon=r.expiring_soon,
            failed_certs=r.failed_certs,
            active_challenges=r.active_challenges,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_3(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=r.installed,
            version=None,
            namespace=r.namespace,
            total_certs=r.total_certs,
            ready_certs=r.ready_certs,
            expiring_soon=r.expiring_soon,
            failed_certs=r.failed_certs,
            active_challenges=r.active_challenges,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_4(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=None,
            total_certs=r.total_certs,
            ready_certs=r.ready_certs,
            expiring_soon=r.expiring_soon,
            failed_certs=r.failed_certs,
            active_challenges=r.active_challenges,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_5(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_certs=None,
            ready_certs=r.ready_certs,
            expiring_soon=r.expiring_soon,
            failed_certs=r.failed_certs,
            active_challenges=r.active_challenges,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_6(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_certs=r.total_certs,
            ready_certs=None,
            expiring_soon=r.expiring_soon,
            failed_certs=r.failed_certs,
            active_challenges=r.active_challenges,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_7(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_certs=r.total_certs,
            ready_certs=r.ready_certs,
            expiring_soon=None,
            failed_certs=r.failed_certs,
            active_challenges=r.active_challenges,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_8(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_certs=r.total_certs,
            ready_certs=r.ready_certs,
            expiring_soon=r.expiring_soon,
            failed_certs=None,
            active_challenges=r.active_challenges,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_9(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_certs=r.total_certs,
            ready_certs=r.ready_certs,
            expiring_soon=r.expiring_soon,
            failed_certs=r.failed_certs,
            active_challenges=None,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_10(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            version=r.version,
            namespace=r.namespace,
            total_certs=r.total_certs,
            ready_certs=r.ready_certs,
            expiring_soon=r.expiring_soon,
            failed_certs=r.failed_certs,
            active_challenges=r.active_challenges,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_11(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=r.installed,
            namespace=r.namespace,
            total_certs=r.total_certs,
            ready_certs=r.ready_certs,
            expiring_soon=r.expiring_soon,
            failed_certs=r.failed_certs,
            active_challenges=r.active_challenges,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_12(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=r.installed,
            version=r.version,
            total_certs=r.total_certs,
            ready_certs=r.ready_certs,
            expiring_soon=r.expiring_soon,
            failed_certs=r.failed_certs,
            active_challenges=r.active_challenges,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_13(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            ready_certs=r.ready_certs,
            expiring_soon=r.expiring_soon,
            failed_certs=r.failed_certs,
            active_challenges=r.active_challenges,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_14(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_certs=r.total_certs,
            expiring_soon=r.expiring_soon,
            failed_certs=r.failed_certs,
            active_challenges=r.active_challenges,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_15(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_certs=r.total_certs,
            ready_certs=r.ready_certs,
            failed_certs=r.failed_certs,
            active_challenges=r.active_challenges,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_16(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_certs=r.total_certs,
            ready_certs=r.ready_certs,
            expiring_soon=r.expiring_soon,
            active_challenges=r.active_challenges,
        )

    def xǁCertsDetectUseCaseǁexecute__mutmut_17(self, command: CertsDetectCommand) -> CertsDetectResponse:
        r = self._port.detect()
        return CertsDetectResponse(
            installed=r.installed,
            version=r.version,
            namespace=r.namespace,
            total_certs=r.total_certs,
            ready_certs=r.ready_certs,
            expiring_soon=r.expiring_soon,
            failed_certs=r.failed_certs,
            )

mutants_xǁCertsDetectUseCaseǁ__init____mutmut['_mutmut_orig'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁ__init____mutmut['xǁCertsDetectUseCaseǁ__init____mutmut_1'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCertsDetectUseCaseǁexecute__mutmut['_mutmut_orig'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁexecute__mutmut['xǁCertsDetectUseCaseǁexecute__mutmut_1'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁexecute__mutmut['xǁCertsDetectUseCaseǁexecute__mutmut_2'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁexecute__mutmut['xǁCertsDetectUseCaseǁexecute__mutmut_3'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁexecute__mutmut['xǁCertsDetectUseCaseǁexecute__mutmut_4'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁexecute__mutmut['xǁCertsDetectUseCaseǁexecute__mutmut_5'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁexecute__mutmut['xǁCertsDetectUseCaseǁexecute__mutmut_6'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁexecute__mutmut['xǁCertsDetectUseCaseǁexecute__mutmut_7'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁexecute__mutmut['xǁCertsDetectUseCaseǁexecute__mutmut_8'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁexecute__mutmut['xǁCertsDetectUseCaseǁexecute__mutmut_9'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁexecute__mutmut['xǁCertsDetectUseCaseǁexecute__mutmut_10'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁexecute__mutmut['xǁCertsDetectUseCaseǁexecute__mutmut_11'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁexecute__mutmut['xǁCertsDetectUseCaseǁexecute__mutmut_12'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁexecute__mutmut['xǁCertsDetectUseCaseǁexecute__mutmut_13'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁexecute__mutmut['xǁCertsDetectUseCaseǁexecute__mutmut_14'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁexecute__mutmut['xǁCertsDetectUseCaseǁexecute__mutmut_15'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁexecute__mutmut['xǁCertsDetectUseCaseǁexecute__mutmut_16'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCertsDetectUseCaseǁexecute__mutmut['xǁCertsDetectUseCaseǁexecute__mutmut_17'] = CertsDetectUseCase.xǁCertsDetectUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
