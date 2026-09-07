from __future__ import annotations

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda.keda_scaledobject_get.command import (
    KedaScaledobjectGetCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobject_get.response import (
    KedaScaledobjectGetResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKedaScaledobjectGetUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class KedaScaledobjectGetUseCase:
    @_mutmut_mutated(mutants_xǁKedaScaledobjectGetUseCaseǁ__init____mutmut)
    def __init__(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaScaledobjectGetUseCaseǁ__init____mutmut_orig(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaScaledobjectGetUseCaseǁ__init____mutmut_1(self, port: KedaPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut)
    def execute(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_orig(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_1(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = None
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_2(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=None, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_3(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=None)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_4(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_5(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, )
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_6(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=None,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_7(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=None,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_8(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=None,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_9(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=None,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_10(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=None,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_11(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=None,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_12(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=None,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_13(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=None,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_14(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=None,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_15(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=None,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_16(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=None,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_17(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=None,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_18(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=None,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_19(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=None,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_20(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=None,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_21(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=None,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_22(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=None,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_23(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_24(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_25(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_26(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_27(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_28(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_29(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_30(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_31(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_32(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_33(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_34(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_35(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_36(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_37(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            ready=so.ready,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_38(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            message=so.message,  # type: ignore
        )

    def xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_39(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,  # type: ignore
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,  # type: ignore
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            )

mutants_xǁKedaScaledobjectGetUseCaseǁ__init____mutmut['_mutmut_orig'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁ__init____mutmut['xǁKedaScaledobjectGetUseCaseǁ__init____mutmut_1'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['_mutmut_orig'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_1'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_2'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_3'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_4'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_5'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_6'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_7'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_8'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_9'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_10'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_11'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_12'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_13'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_14'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_15'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_16'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_17'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_18'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_19'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_20'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_21'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_22'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_23'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_24'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_25'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_26'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_27'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_28'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_29'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_30'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_31'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_32'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_33'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_34'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_35'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_36'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_37'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_38'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁKedaScaledobjectGetUseCaseǁexecute__mutmut['xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_39'] = KedaScaledobjectGetUseCase.xǁKedaScaledobjectGetUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
