"""CalicoEncryptionStatusUseCase — WireGuard encryption status."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.calico_encryption_status.command import (
    CalicoEncryptionStatusCommand,
)
from hexawyn.application.use_case.calico.calico_encryption_status.response import (
    CalicoEncryptionStatusResponse,
)
from hexawyn.domain.models.calico import DataplaneMode
from hexawyn.domain.services.calico.encryption_status_service import (
    build_calico_encryption_status,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCalicoEncryptionStatusUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CalicoEncryptionStatusUseCase:
    """Orchestrates WireGuard status — depends only on ``CalicoPort``."""

    @_mutmut_mutated(mutants_xǁCalicoEncryptionStatusUseCaseǁ__init____mutmut)
    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def xǁCalicoEncryptionStatusUseCaseǁ__init____mutmut_orig(self, port: CalicoPort) -> None:
        self._port = port

    def xǁCalicoEncryptionStatusUseCaseǁ__init____mutmut_1(self, port: CalicoPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut)
    def execute(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_orig(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_1(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = None
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_2(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_3(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=None,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_4(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=None,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_5(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=None,
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_6(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=None,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_7(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_8(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_9(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_10(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_11(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_12(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_13(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=True,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_14(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = None
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_15(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = None
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_16(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=None, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_17(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=None)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_18(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_19(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, )
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_20(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = None
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_21(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=None,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_22(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=None,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_23(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=None,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_24(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=None,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_25(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=None,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_26(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=None,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_27(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=None,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_28(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_29(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_30(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_31(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_32(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_33(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            error=result.error,
        )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_34(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            )

    def xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_35(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(None),
            summary=result.summary,
            error=result.error,
        )

mutants_xǁCalicoEncryptionStatusUseCaseǁ__init____mutmut['_mutmut_orig'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁ__init____mutmut['xǁCalicoEncryptionStatusUseCaseǁ__init____mutmut_1'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['_mutmut_orig'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_1'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_2'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_3'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_4'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_5'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_6'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_7'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_8'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_9'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_10'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_11'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_12'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_13'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_14'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_15'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_16'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_17'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_18'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_19'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_20'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_21'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_22'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_23'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_24'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_25'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_26'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_27'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_28'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_29'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_30'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_31'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_32'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_33'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_34'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut['xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_35'] = CalicoEncryptionStatusUseCase.xǁCalicoEncryptionStatusUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
