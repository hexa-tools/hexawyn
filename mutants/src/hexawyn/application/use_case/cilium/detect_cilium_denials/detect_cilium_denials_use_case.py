from __future__ import annotations

from hexawyn.application.ports.driven.cilium_hubble_port import CiliumHubblePort
from hexawyn.application.use_case.cilium.detect_cilium_denials.command import (
    DetectCiliumDenialsCommand,
)
from hexawyn.application.use_case.cilium.detect_cilium_denials.response import (
    CiliumDenialGroupOutput,
    DetectCiliumDenialsResponse,
)
from hexawyn.domain.models.cilium import CiliumDenialGroup, CiliumDenialsQuery


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDetectCiliumDenialsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut: MutantDict = {}  # type: ignore


class DetectCiliumDenialsUseCase:
    @_mutmut_mutated(mutants_xǁDetectCiliumDenialsUseCaseǁ__init____mutmut)
    def __init__(self, port: CiliumHubblePort) -> None:
        self._port = port
    def xǁDetectCiliumDenialsUseCaseǁ__init____mutmut_orig(self, port: CiliumHubblePort) -> None:
        self._port = port
    def xǁDetectCiliumDenialsUseCaseǁ__init____mutmut_1(self, port: CiliumHubblePort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut)
    def execute(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_orig(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_1(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = None
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_2(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=None,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_3(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=None,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_4(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=None,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_5(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_6(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_7(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_8(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = None
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_9(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(None)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_10(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = ""
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_11(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_12(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = None
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_13(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(None) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_14(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=None,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_15(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=None,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_16(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=None,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_17(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=None,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_18(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=None,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_19(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_20(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            total_denials=result.total_denials,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_21(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            groups=groups,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_22(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            note=result.note,
        )

    def xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_23(self, command: DetectCiliumDenialsCommand) -> DetectCiliumDenialsResponse:
        query = CiliumDenialsQuery(
            namespace=command.namespace,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.detect_denials(query)
        groups: list[CiliumDenialGroupOutput] | None = None
        if result.groups is not None:
            groups = [self._to_group(group) for group in result.groups]
        return DetectCiliumDenialsResponse(
            installed=result.installed,
            status=result.status,
            total_denials=result.total_denials,
            groups=groups,
            )

    @staticmethod
    @_mutmut_mutated(mutants_xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut)
    def _to_group(group: CiliumDenialGroup) -> CiliumDenialGroupOutput:
        return {
            "policy": group.policy,
            "source": group.source,
            "destination": group.destination,
            "source_namespace": group.source_namespace,
            "destination_namespace": group.destination_namespace,
            "reason": group.reason,
            "count": group.count,
        }

    @staticmethod
    def xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_orig(group: CiliumDenialGroup) -> CiliumDenialGroupOutput:
        return {
            "policy": group.policy,
            "source": group.source,
            "destination": group.destination,
            "source_namespace": group.source_namespace,
            "destination_namespace": group.destination_namespace,
            "reason": group.reason,
            "count": group.count,
        }

    @staticmethod
    def xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_1(group: CiliumDenialGroup) -> CiliumDenialGroupOutput:
        return {
            "XXpolicyXX": group.policy,
            "source": group.source,
            "destination": group.destination,
            "source_namespace": group.source_namespace,
            "destination_namespace": group.destination_namespace,
            "reason": group.reason,
            "count": group.count,
        }

    @staticmethod
    def xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_2(group: CiliumDenialGroup) -> CiliumDenialGroupOutput:
        return {
            "POLICY": group.policy,
            "source": group.source,
            "destination": group.destination,
            "source_namespace": group.source_namespace,
            "destination_namespace": group.destination_namespace,
            "reason": group.reason,
            "count": group.count,
        }

    @staticmethod
    def xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_3(group: CiliumDenialGroup) -> CiliumDenialGroupOutput:
        return {
            "policy": group.policy,
            "XXsourceXX": group.source,
            "destination": group.destination,
            "source_namespace": group.source_namespace,
            "destination_namespace": group.destination_namespace,
            "reason": group.reason,
            "count": group.count,
        }

    @staticmethod
    def xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_4(group: CiliumDenialGroup) -> CiliumDenialGroupOutput:
        return {
            "policy": group.policy,
            "SOURCE": group.source,
            "destination": group.destination,
            "source_namespace": group.source_namespace,
            "destination_namespace": group.destination_namespace,
            "reason": group.reason,
            "count": group.count,
        }

    @staticmethod
    def xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_5(group: CiliumDenialGroup) -> CiliumDenialGroupOutput:
        return {
            "policy": group.policy,
            "source": group.source,
            "XXdestinationXX": group.destination,
            "source_namespace": group.source_namespace,
            "destination_namespace": group.destination_namespace,
            "reason": group.reason,
            "count": group.count,
        }

    @staticmethod
    def xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_6(group: CiliumDenialGroup) -> CiliumDenialGroupOutput:
        return {
            "policy": group.policy,
            "source": group.source,
            "DESTINATION": group.destination,
            "source_namespace": group.source_namespace,
            "destination_namespace": group.destination_namespace,
            "reason": group.reason,
            "count": group.count,
        }

    @staticmethod
    def xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_7(group: CiliumDenialGroup) -> CiliumDenialGroupOutput:
        return {
            "policy": group.policy,
            "source": group.source,
            "destination": group.destination,
            "XXsource_namespaceXX": group.source_namespace,
            "destination_namespace": group.destination_namespace,
            "reason": group.reason,
            "count": group.count,
        }

    @staticmethod
    def xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_8(group: CiliumDenialGroup) -> CiliumDenialGroupOutput:
        return {
            "policy": group.policy,
            "source": group.source,
            "destination": group.destination,
            "SOURCE_NAMESPACE": group.source_namespace,
            "destination_namespace": group.destination_namespace,
            "reason": group.reason,
            "count": group.count,
        }

    @staticmethod
    def xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_9(group: CiliumDenialGroup) -> CiliumDenialGroupOutput:
        return {
            "policy": group.policy,
            "source": group.source,
            "destination": group.destination,
            "source_namespace": group.source_namespace,
            "XXdestination_namespaceXX": group.destination_namespace,
            "reason": group.reason,
            "count": group.count,
        }

    @staticmethod
    def xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_10(group: CiliumDenialGroup) -> CiliumDenialGroupOutput:
        return {
            "policy": group.policy,
            "source": group.source,
            "destination": group.destination,
            "source_namespace": group.source_namespace,
            "DESTINATION_NAMESPACE": group.destination_namespace,
            "reason": group.reason,
            "count": group.count,
        }

    @staticmethod
    def xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_11(group: CiliumDenialGroup) -> CiliumDenialGroupOutput:
        return {
            "policy": group.policy,
            "source": group.source,
            "destination": group.destination,
            "source_namespace": group.source_namespace,
            "destination_namespace": group.destination_namespace,
            "XXreasonXX": group.reason,
            "count": group.count,
        }

    @staticmethod
    def xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_12(group: CiliumDenialGroup) -> CiliumDenialGroupOutput:
        return {
            "policy": group.policy,
            "source": group.source,
            "destination": group.destination,
            "source_namespace": group.source_namespace,
            "destination_namespace": group.destination_namespace,
            "REASON": group.reason,
            "count": group.count,
        }

    @staticmethod
    def xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_13(group: CiliumDenialGroup) -> CiliumDenialGroupOutput:
        return {
            "policy": group.policy,
            "source": group.source,
            "destination": group.destination,
            "source_namespace": group.source_namespace,
            "destination_namespace": group.destination_namespace,
            "reason": group.reason,
            "XXcountXX": group.count,
        }

    @staticmethod
    def xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_14(group: CiliumDenialGroup) -> CiliumDenialGroupOutput:
        return {
            "policy": group.policy,
            "source": group.source,
            "destination": group.destination,
            "source_namespace": group.source_namespace,
            "destination_namespace": group.destination_namespace,
            "reason": group.reason,
            "COUNT": group.count,
        }

mutants_xǁDetectCiliumDenialsUseCaseǁ__init____mutmut['_mutmut_orig'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁ__init____mutmut['xǁDetectCiliumDenialsUseCaseǁ__init____mutmut_1'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['_mutmut_orig'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_1'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_2'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_3'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_4'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_5'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_6'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_7'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_8'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_9'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_10'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_11'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_12'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_13'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_14'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_15'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_16'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_17'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_18'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_19'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_20'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_21'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_22'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁexecute__mutmut['xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_23'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated

mutants_xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut['_mutmut_orig'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut['xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_1'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut['xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_2'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut['xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_3'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut['xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_4'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut['xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_5'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut['xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_6'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut['xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_7'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut['xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_8'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut['xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_9'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut['xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_10'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut['xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_11'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut['xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_12'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut['xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_13'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut['xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_14'] = DetectCiliumDenialsUseCase.xǁDetectCiliumDenialsUseCaseǁ_to_group__mutmut_14 # type: ignore # mutmut generated
