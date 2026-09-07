from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.cilium_encryption_status.command import (
    CiliumEncryptionStatusCommand,
)
from hexawyn.application.use_case.cilium.cilium_encryption_status.response import (
    CiliumEncryptionStatusResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCiliumEncryptionStatusUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CiliumEncryptionStatusUseCase:
    @_mutmut_mutated(mutants_xǁCiliumEncryptionStatusUseCaseǁ__init____mutmut)
    def __init__(self, port: CiliumPort) -> None:
        self._port = port
    def xǁCiliumEncryptionStatusUseCaseǁ__init____mutmut_orig(self, port: CiliumPort) -> None:
        self._port = port
    def xǁCiliumEncryptionStatusUseCaseǁ__init____mutmut_1(self, port: CiliumPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut)
    def execute(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = self._port.encryption_status()
        return CiliumEncryptionStatusResponse(
            installed=result.installed,
            status=result.status,
            mode=result.mode,
            encrypted_nodes=result.encrypted_nodes,
            total_nodes=result.total_nodes,
            coverage=result.coverage,
            note=result.note,
        )

    def xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_orig(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = self._port.encryption_status()
        return CiliumEncryptionStatusResponse(
            installed=result.installed,
            status=result.status,
            mode=result.mode,
            encrypted_nodes=result.encrypted_nodes,
            total_nodes=result.total_nodes,
            coverage=result.coverage,
            note=result.note,
        )

    def xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_1(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = None
        return CiliumEncryptionStatusResponse(
            installed=result.installed,
            status=result.status,
            mode=result.mode,
            encrypted_nodes=result.encrypted_nodes,
            total_nodes=result.total_nodes,
            coverage=result.coverage,
            note=result.note,
        )

    def xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_2(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = self._port.encryption_status()
        return CiliumEncryptionStatusResponse(
            installed=None,
            status=result.status,
            mode=result.mode,
            encrypted_nodes=result.encrypted_nodes,
            total_nodes=result.total_nodes,
            coverage=result.coverage,
            note=result.note,
        )

    def xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_3(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = self._port.encryption_status()
        return CiliumEncryptionStatusResponse(
            installed=result.installed,
            status=None,
            mode=result.mode,
            encrypted_nodes=result.encrypted_nodes,
            total_nodes=result.total_nodes,
            coverage=result.coverage,
            note=result.note,
        )

    def xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_4(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = self._port.encryption_status()
        return CiliumEncryptionStatusResponse(
            installed=result.installed,
            status=result.status,
            mode=None,
            encrypted_nodes=result.encrypted_nodes,
            total_nodes=result.total_nodes,
            coverage=result.coverage,
            note=result.note,
        )

    def xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_5(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = self._port.encryption_status()
        return CiliumEncryptionStatusResponse(
            installed=result.installed,
            status=result.status,
            mode=result.mode,
            encrypted_nodes=None,
            total_nodes=result.total_nodes,
            coverage=result.coverage,
            note=result.note,
        )

    def xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_6(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = self._port.encryption_status()
        return CiliumEncryptionStatusResponse(
            installed=result.installed,
            status=result.status,
            mode=result.mode,
            encrypted_nodes=result.encrypted_nodes,
            total_nodes=None,
            coverage=result.coverage,
            note=result.note,
        )

    def xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_7(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = self._port.encryption_status()
        return CiliumEncryptionStatusResponse(
            installed=result.installed,
            status=result.status,
            mode=result.mode,
            encrypted_nodes=result.encrypted_nodes,
            total_nodes=result.total_nodes,
            coverage=None,
            note=result.note,
        )

    def xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_8(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = self._port.encryption_status()
        return CiliumEncryptionStatusResponse(
            installed=result.installed,
            status=result.status,
            mode=result.mode,
            encrypted_nodes=result.encrypted_nodes,
            total_nodes=result.total_nodes,
            coverage=result.coverage,
            note=None,
        )

    def xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_9(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = self._port.encryption_status()
        return CiliumEncryptionStatusResponse(
            status=result.status,
            mode=result.mode,
            encrypted_nodes=result.encrypted_nodes,
            total_nodes=result.total_nodes,
            coverage=result.coverage,
            note=result.note,
        )

    def xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_10(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = self._port.encryption_status()
        return CiliumEncryptionStatusResponse(
            installed=result.installed,
            mode=result.mode,
            encrypted_nodes=result.encrypted_nodes,
            total_nodes=result.total_nodes,
            coverage=result.coverage,
            note=result.note,
        )

    def xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_11(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = self._port.encryption_status()
        return CiliumEncryptionStatusResponse(
            installed=result.installed,
            status=result.status,
            encrypted_nodes=result.encrypted_nodes,
            total_nodes=result.total_nodes,
            coverage=result.coverage,
            note=result.note,
        )

    def xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_12(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = self._port.encryption_status()
        return CiliumEncryptionStatusResponse(
            installed=result.installed,
            status=result.status,
            mode=result.mode,
            total_nodes=result.total_nodes,
            coverage=result.coverage,
            note=result.note,
        )

    def xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_13(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = self._port.encryption_status()
        return CiliumEncryptionStatusResponse(
            installed=result.installed,
            status=result.status,
            mode=result.mode,
            encrypted_nodes=result.encrypted_nodes,
            coverage=result.coverage,
            note=result.note,
        )

    def xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_14(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = self._port.encryption_status()
        return CiliumEncryptionStatusResponse(
            installed=result.installed,
            status=result.status,
            mode=result.mode,
            encrypted_nodes=result.encrypted_nodes,
            total_nodes=result.total_nodes,
            note=result.note,
        )

    def xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_15(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = self._port.encryption_status()
        return CiliumEncryptionStatusResponse(
            installed=result.installed,
            status=result.status,
            mode=result.mode,
            encrypted_nodes=result.encrypted_nodes,
            total_nodes=result.total_nodes,
            coverage=result.coverage,
            )

mutants_xǁCiliumEncryptionStatusUseCaseǁ__init____mutmut['_mutmut_orig'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumEncryptionStatusUseCaseǁ__init____mutmut['xǁCiliumEncryptionStatusUseCaseǁ__init____mutmut_1'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut['_mutmut_orig'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut['xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_1'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut['xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_2'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut['xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_3'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut['xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_4'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut['xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_5'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut['xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_6'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut['xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_7'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut['xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_8'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut['xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_9'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut['xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_10'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut['xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_11'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut['xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_12'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut['xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_13'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut['xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_14'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut['xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_15'] = CiliumEncryptionStatusUseCase.xǁCiliumEncryptionStatusUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
