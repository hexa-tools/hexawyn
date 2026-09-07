from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.cilium_bandwidth_audit.command import (
    CiliumBandwidthAuditCommand,
)
from hexawyn.application.use_case.cilium.cilium_bandwidth_audit.response import (
    CiliumBandwidthAuditResponse,
    CiliumBandwidthEntryOutput,
)
from hexawyn.domain.models.cilium import CiliumBandwidthEntry


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCiliumBandwidthAuditUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut: MutantDict = {}  # type: ignore


class CiliumBandwidthAuditUseCase:
    @_mutmut_mutated(mutants_xǁCiliumBandwidthAuditUseCaseǁ__init____mutmut)
    def __init__(self, port: CiliumPort) -> None:
        self._port = port
    def xǁCiliumBandwidthAuditUseCaseǁ__init____mutmut_orig(self, port: CiliumPort) -> None:
        self._port = port
    def xǁCiliumBandwidthAuditUseCaseǁ__init____mutmut_1(self, port: CiliumPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut)
    def execute(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = self._port.bandwidth_audit()
        entries: list[CiliumBandwidthEntryOutput] | None = None
        if result.entries is not None:
            entries = [self._to_entry(entry) for entry in result.entries]
        return CiliumBandwidthAuditResponse(
            installed=result.installed,
            status=result.status,
            total_pods=result.total_pods,
            entries=entries,
            note=result.note,
        )

    def xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_orig(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = self._port.bandwidth_audit()
        entries: list[CiliumBandwidthEntryOutput] | None = None
        if result.entries is not None:
            entries = [self._to_entry(entry) for entry in result.entries]
        return CiliumBandwidthAuditResponse(
            installed=result.installed,
            status=result.status,
            total_pods=result.total_pods,
            entries=entries,
            note=result.note,
        )

    def xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_1(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = None
        entries: list[CiliumBandwidthEntryOutput] | None = None
        if result.entries is not None:
            entries = [self._to_entry(entry) for entry in result.entries]
        return CiliumBandwidthAuditResponse(
            installed=result.installed,
            status=result.status,
            total_pods=result.total_pods,
            entries=entries,
            note=result.note,
        )

    def xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_2(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = self._port.bandwidth_audit()
        entries: list[CiliumBandwidthEntryOutput] | None = ""
        if result.entries is not None:
            entries = [self._to_entry(entry) for entry in result.entries]
        return CiliumBandwidthAuditResponse(
            installed=result.installed,
            status=result.status,
            total_pods=result.total_pods,
            entries=entries,
            note=result.note,
        )

    def xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_3(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = self._port.bandwidth_audit()
        entries: list[CiliumBandwidthEntryOutput] | None = None
        if result.entries is None:
            entries = [self._to_entry(entry) for entry in result.entries]
        return CiliumBandwidthAuditResponse(
            installed=result.installed,
            status=result.status,
            total_pods=result.total_pods,
            entries=entries,
            note=result.note,
        )

    def xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_4(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = self._port.bandwidth_audit()
        entries: list[CiliumBandwidthEntryOutput] | None = None
        if result.entries is not None:
            entries = None
        return CiliumBandwidthAuditResponse(
            installed=result.installed,
            status=result.status,
            total_pods=result.total_pods,
            entries=entries,
            note=result.note,
        )

    def xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_5(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = self._port.bandwidth_audit()
        entries: list[CiliumBandwidthEntryOutput] | None = None
        if result.entries is not None:
            entries = [self._to_entry(None) for entry in result.entries]
        return CiliumBandwidthAuditResponse(
            installed=result.installed,
            status=result.status,
            total_pods=result.total_pods,
            entries=entries,
            note=result.note,
        )

    def xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_6(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = self._port.bandwidth_audit()
        entries: list[CiliumBandwidthEntryOutput] | None = None
        if result.entries is not None:
            entries = [self._to_entry(entry) for entry in result.entries]
        return CiliumBandwidthAuditResponse(
            installed=None,
            status=result.status,
            total_pods=result.total_pods,
            entries=entries,
            note=result.note,
        )

    def xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_7(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = self._port.bandwidth_audit()
        entries: list[CiliumBandwidthEntryOutput] | None = None
        if result.entries is not None:
            entries = [self._to_entry(entry) for entry in result.entries]
        return CiliumBandwidthAuditResponse(
            installed=result.installed,
            status=None,
            total_pods=result.total_pods,
            entries=entries,
            note=result.note,
        )

    def xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_8(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = self._port.bandwidth_audit()
        entries: list[CiliumBandwidthEntryOutput] | None = None
        if result.entries is not None:
            entries = [self._to_entry(entry) for entry in result.entries]
        return CiliumBandwidthAuditResponse(
            installed=result.installed,
            status=result.status,
            total_pods=None,
            entries=entries,
            note=result.note,
        )

    def xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_9(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = self._port.bandwidth_audit()
        entries: list[CiliumBandwidthEntryOutput] | None = None
        if result.entries is not None:
            entries = [self._to_entry(entry) for entry in result.entries]
        return CiliumBandwidthAuditResponse(
            installed=result.installed,
            status=result.status,
            total_pods=result.total_pods,
            entries=None,
            note=result.note,
        )

    def xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_10(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = self._port.bandwidth_audit()
        entries: list[CiliumBandwidthEntryOutput] | None = None
        if result.entries is not None:
            entries = [self._to_entry(entry) for entry in result.entries]
        return CiliumBandwidthAuditResponse(
            installed=result.installed,
            status=result.status,
            total_pods=result.total_pods,
            entries=entries,
            note=None,
        )

    def xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_11(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = self._port.bandwidth_audit()
        entries: list[CiliumBandwidthEntryOutput] | None = None
        if result.entries is not None:
            entries = [self._to_entry(entry) for entry in result.entries]
        return CiliumBandwidthAuditResponse(
            status=result.status,
            total_pods=result.total_pods,
            entries=entries,
            note=result.note,
        )

    def xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_12(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = self._port.bandwidth_audit()
        entries: list[CiliumBandwidthEntryOutput] | None = None
        if result.entries is not None:
            entries = [self._to_entry(entry) for entry in result.entries]
        return CiliumBandwidthAuditResponse(
            installed=result.installed,
            total_pods=result.total_pods,
            entries=entries,
            note=result.note,
        )

    def xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_13(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = self._port.bandwidth_audit()
        entries: list[CiliumBandwidthEntryOutput] | None = None
        if result.entries is not None:
            entries = [self._to_entry(entry) for entry in result.entries]
        return CiliumBandwidthAuditResponse(
            installed=result.installed,
            status=result.status,
            entries=entries,
            note=result.note,
        )

    def xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_14(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = self._port.bandwidth_audit()
        entries: list[CiliumBandwidthEntryOutput] | None = None
        if result.entries is not None:
            entries = [self._to_entry(entry) for entry in result.entries]
        return CiliumBandwidthAuditResponse(
            installed=result.installed,
            status=result.status,
            total_pods=result.total_pods,
            note=result.note,
        )

    def xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_15(self, command: CiliumBandwidthAuditCommand) -> CiliumBandwidthAuditResponse:
        result = self._port.bandwidth_audit()
        entries: list[CiliumBandwidthEntryOutput] | None = None
        if result.entries is not None:
            entries = [self._to_entry(entry) for entry in result.entries]
        return CiliumBandwidthAuditResponse(
            installed=result.installed,
            status=result.status,
            total_pods=result.total_pods,
            entries=entries,
            )

    @staticmethod
    @_mutmut_mutated(mutants_xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut)
    def _to_entry(entry: CiliumBandwidthEntry) -> CiliumBandwidthEntryOutput:
        return {
            "namespace": entry.namespace,
            "pod": entry.pod,
            "ingress_limit": entry.ingress_limit,
            "egress_limit": entry.egress_limit,
            "usage_ratio": entry.usage_ratio,
            "state": entry.state,
            "note": entry.note,
        }

    @staticmethod
    def xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_orig(entry: CiliumBandwidthEntry) -> CiliumBandwidthEntryOutput:
        return {
            "namespace": entry.namespace,
            "pod": entry.pod,
            "ingress_limit": entry.ingress_limit,
            "egress_limit": entry.egress_limit,
            "usage_ratio": entry.usage_ratio,
            "state": entry.state,
            "note": entry.note,
        }

    @staticmethod
    def xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_1(entry: CiliumBandwidthEntry) -> CiliumBandwidthEntryOutput:
        return {
            "XXnamespaceXX": entry.namespace,
            "pod": entry.pod,
            "ingress_limit": entry.ingress_limit,
            "egress_limit": entry.egress_limit,
            "usage_ratio": entry.usage_ratio,
            "state": entry.state,
            "note": entry.note,
        }

    @staticmethod
    def xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_2(entry: CiliumBandwidthEntry) -> CiliumBandwidthEntryOutput:
        return {
            "NAMESPACE": entry.namespace,
            "pod": entry.pod,
            "ingress_limit": entry.ingress_limit,
            "egress_limit": entry.egress_limit,
            "usage_ratio": entry.usage_ratio,
            "state": entry.state,
            "note": entry.note,
        }

    @staticmethod
    def xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_3(entry: CiliumBandwidthEntry) -> CiliumBandwidthEntryOutput:
        return {
            "namespace": entry.namespace,
            "XXpodXX": entry.pod,
            "ingress_limit": entry.ingress_limit,
            "egress_limit": entry.egress_limit,
            "usage_ratio": entry.usage_ratio,
            "state": entry.state,
            "note": entry.note,
        }

    @staticmethod
    def xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_4(entry: CiliumBandwidthEntry) -> CiliumBandwidthEntryOutput:
        return {
            "namespace": entry.namespace,
            "POD": entry.pod,
            "ingress_limit": entry.ingress_limit,
            "egress_limit": entry.egress_limit,
            "usage_ratio": entry.usage_ratio,
            "state": entry.state,
            "note": entry.note,
        }

    @staticmethod
    def xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_5(entry: CiliumBandwidthEntry) -> CiliumBandwidthEntryOutput:
        return {
            "namespace": entry.namespace,
            "pod": entry.pod,
            "XXingress_limitXX": entry.ingress_limit,
            "egress_limit": entry.egress_limit,
            "usage_ratio": entry.usage_ratio,
            "state": entry.state,
            "note": entry.note,
        }

    @staticmethod
    def xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_6(entry: CiliumBandwidthEntry) -> CiliumBandwidthEntryOutput:
        return {
            "namespace": entry.namespace,
            "pod": entry.pod,
            "INGRESS_LIMIT": entry.ingress_limit,
            "egress_limit": entry.egress_limit,
            "usage_ratio": entry.usage_ratio,
            "state": entry.state,
            "note": entry.note,
        }

    @staticmethod
    def xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_7(entry: CiliumBandwidthEntry) -> CiliumBandwidthEntryOutput:
        return {
            "namespace": entry.namespace,
            "pod": entry.pod,
            "ingress_limit": entry.ingress_limit,
            "XXegress_limitXX": entry.egress_limit,
            "usage_ratio": entry.usage_ratio,
            "state": entry.state,
            "note": entry.note,
        }

    @staticmethod
    def xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_8(entry: CiliumBandwidthEntry) -> CiliumBandwidthEntryOutput:
        return {
            "namespace": entry.namespace,
            "pod": entry.pod,
            "ingress_limit": entry.ingress_limit,
            "EGRESS_LIMIT": entry.egress_limit,
            "usage_ratio": entry.usage_ratio,
            "state": entry.state,
            "note": entry.note,
        }

    @staticmethod
    def xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_9(entry: CiliumBandwidthEntry) -> CiliumBandwidthEntryOutput:
        return {
            "namespace": entry.namespace,
            "pod": entry.pod,
            "ingress_limit": entry.ingress_limit,
            "egress_limit": entry.egress_limit,
            "XXusage_ratioXX": entry.usage_ratio,
            "state": entry.state,
            "note": entry.note,
        }

    @staticmethod
    def xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_10(entry: CiliumBandwidthEntry) -> CiliumBandwidthEntryOutput:
        return {
            "namespace": entry.namespace,
            "pod": entry.pod,
            "ingress_limit": entry.ingress_limit,
            "egress_limit": entry.egress_limit,
            "USAGE_RATIO": entry.usage_ratio,
            "state": entry.state,
            "note": entry.note,
        }

    @staticmethod
    def xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_11(entry: CiliumBandwidthEntry) -> CiliumBandwidthEntryOutput:
        return {
            "namespace": entry.namespace,
            "pod": entry.pod,
            "ingress_limit": entry.ingress_limit,
            "egress_limit": entry.egress_limit,
            "usage_ratio": entry.usage_ratio,
            "XXstateXX": entry.state,
            "note": entry.note,
        }

    @staticmethod
    def xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_12(entry: CiliumBandwidthEntry) -> CiliumBandwidthEntryOutput:
        return {
            "namespace": entry.namespace,
            "pod": entry.pod,
            "ingress_limit": entry.ingress_limit,
            "egress_limit": entry.egress_limit,
            "usage_ratio": entry.usage_ratio,
            "STATE": entry.state,
            "note": entry.note,
        }

    @staticmethod
    def xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_13(entry: CiliumBandwidthEntry) -> CiliumBandwidthEntryOutput:
        return {
            "namespace": entry.namespace,
            "pod": entry.pod,
            "ingress_limit": entry.ingress_limit,
            "egress_limit": entry.egress_limit,
            "usage_ratio": entry.usage_ratio,
            "state": entry.state,
            "XXnoteXX": entry.note,
        }

    @staticmethod
    def xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_14(entry: CiliumBandwidthEntry) -> CiliumBandwidthEntryOutput:
        return {
            "namespace": entry.namespace,
            "pod": entry.pod,
            "ingress_limit": entry.ingress_limit,
            "egress_limit": entry.egress_limit,
            "usage_ratio": entry.usage_ratio,
            "state": entry.state,
            "NOTE": entry.note,
        }

mutants_xǁCiliumBandwidthAuditUseCaseǁ__init____mutmut['_mutmut_orig'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁ__init____mutmut['xǁCiliumBandwidthAuditUseCaseǁ__init____mutmut_1'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut['_mutmut_orig'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut['xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_1'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut['xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_2'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut['xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_3'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut['xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_4'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut['xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_5'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut['xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_6'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut['xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_7'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut['xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_8'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut['xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_9'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut['xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_10'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut['xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_11'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut['xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_12'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut['xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_13'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut['xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_14'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut['xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_15'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated

mutants_xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut['_mutmut_orig'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut['xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_1'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut['xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_2'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut['xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_3'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut['xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_4'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut['xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_5'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut['xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_6'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut['xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_7'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut['xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_8'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut['xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_9'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut['xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_10'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut['xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_11'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut['xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_12'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut['xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_13'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut['xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_14'] = CiliumBandwidthAuditUseCase.xǁCiliumBandwidthAuditUseCaseǁ_to_entry__mutmut_14 # type: ignore # mutmut generated
