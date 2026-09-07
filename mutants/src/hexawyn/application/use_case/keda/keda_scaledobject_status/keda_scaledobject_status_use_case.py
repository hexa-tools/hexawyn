from __future__ import annotations

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda.keda_scaledobject_status.command import (
    KedaScaledobjectStatusCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobject_status.response import (
    KedaScaledobjectStatusResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKedaScaledobjectStatusUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class KedaScaledobjectStatusUseCase:
    @_mutmut_mutated(mutants_xǁKedaScaledobjectStatusUseCaseǁ__init____mutmut)
    def __init__(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaScaledobjectStatusUseCaseǁ__init____mutmut_orig(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaScaledobjectStatusUseCaseǁ__init____mutmut_1(self, port: KedaPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut)
    def execute(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_orig(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_1(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = None
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_2(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=None, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_3(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=None)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_4(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_5(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, )
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_6(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=None,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_7(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=None,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_8(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=None,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_9(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=None,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_10(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=None,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_11(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=None,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_12(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=None,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_13(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=None,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_14(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_15(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_16(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_17(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_18(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_19(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_20(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_21(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            )

mutants_xǁKedaScaledobjectStatusUseCaseǁ__init____mutmut['_mutmut_orig'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁ__init____mutmut['xǁKedaScaledobjectStatusUseCaseǁ__init____mutmut_1'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['_mutmut_orig'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_1'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_2'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_3'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_4'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_5'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_6'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_7'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_8'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_9'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_10'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_11'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_12'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_13'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_14'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_15'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_16'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_17'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_18'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_19'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_20'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut['xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_21'] = KedaScaledobjectStatusUseCase.xǁKedaScaledobjectStatusUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
