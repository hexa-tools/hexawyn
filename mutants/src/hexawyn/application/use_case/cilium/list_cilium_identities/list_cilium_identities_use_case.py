from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.list_cilium_identities.command import (
    ListCiliumIdentitiesCommand,
)
from hexawyn.application.use_case.cilium.list_cilium_identities.response import (
    CiliumIdentityOutput,
    ListCiliumIdentitiesResponse,
)
from hexawyn.domain.models.cilium import CiliumIdentityInfo


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁListCiliumIdentitiesUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut: MutantDict = {}  # type: ignore


class ListCiliumIdentitiesUseCase:
    @_mutmut_mutated(mutants_xǁListCiliumIdentitiesUseCaseǁ__init____mutmut)
    def __init__(self, port: CiliumPort) -> None:
        self._port = port
    def xǁListCiliumIdentitiesUseCaseǁ__init____mutmut_orig(self, port: CiliumPort) -> None:
        self._port = port
    def xǁListCiliumIdentitiesUseCaseǁ__init____mutmut_1(self, port: CiliumPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut)
    def execute(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = self._port.list_identities()
        identities: list[CiliumIdentityOutput] | None = None
        if result.identities is not None:
            identities = [self._to_output(identity) for identity in result.identities]
        return ListCiliumIdentitiesResponse(
            installed=result.installed,
            status=result.status,
            total_identities=result.total_identities,
            identities=identities,
            note=result.note,
        )

    def xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_orig(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = self._port.list_identities()
        identities: list[CiliumIdentityOutput] | None = None
        if result.identities is not None:
            identities = [self._to_output(identity) for identity in result.identities]
        return ListCiliumIdentitiesResponse(
            installed=result.installed,
            status=result.status,
            total_identities=result.total_identities,
            identities=identities,
            note=result.note,
        )

    def xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_1(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = None
        identities: list[CiliumIdentityOutput] | None = None
        if result.identities is not None:
            identities = [self._to_output(identity) for identity in result.identities]
        return ListCiliumIdentitiesResponse(
            installed=result.installed,
            status=result.status,
            total_identities=result.total_identities,
            identities=identities,
            note=result.note,
        )

    def xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_2(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = self._port.list_identities()
        identities: list[CiliumIdentityOutput] | None = ""
        if result.identities is not None:
            identities = [self._to_output(identity) for identity in result.identities]
        return ListCiliumIdentitiesResponse(
            installed=result.installed,
            status=result.status,
            total_identities=result.total_identities,
            identities=identities,
            note=result.note,
        )

    def xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_3(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = self._port.list_identities()
        identities: list[CiliumIdentityOutput] | None = None
        if result.identities is None:
            identities = [self._to_output(identity) for identity in result.identities]
        return ListCiliumIdentitiesResponse(
            installed=result.installed,
            status=result.status,
            total_identities=result.total_identities,
            identities=identities,
            note=result.note,
        )

    def xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_4(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = self._port.list_identities()
        identities: list[CiliumIdentityOutput] | None = None
        if result.identities is not None:
            identities = None
        return ListCiliumIdentitiesResponse(
            installed=result.installed,
            status=result.status,
            total_identities=result.total_identities,
            identities=identities,
            note=result.note,
        )

    def xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_5(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = self._port.list_identities()
        identities: list[CiliumIdentityOutput] | None = None
        if result.identities is not None:
            identities = [self._to_output(None) for identity in result.identities]
        return ListCiliumIdentitiesResponse(
            installed=result.installed,
            status=result.status,
            total_identities=result.total_identities,
            identities=identities,
            note=result.note,
        )

    def xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_6(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = self._port.list_identities()
        identities: list[CiliumIdentityOutput] | None = None
        if result.identities is not None:
            identities = [self._to_output(identity) for identity in result.identities]
        return ListCiliumIdentitiesResponse(
            installed=None,
            status=result.status,
            total_identities=result.total_identities,
            identities=identities,
            note=result.note,
        )

    def xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_7(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = self._port.list_identities()
        identities: list[CiliumIdentityOutput] | None = None
        if result.identities is not None:
            identities = [self._to_output(identity) for identity in result.identities]
        return ListCiliumIdentitiesResponse(
            installed=result.installed,
            status=None,
            total_identities=result.total_identities,
            identities=identities,
            note=result.note,
        )

    def xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_8(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = self._port.list_identities()
        identities: list[CiliumIdentityOutput] | None = None
        if result.identities is not None:
            identities = [self._to_output(identity) for identity in result.identities]
        return ListCiliumIdentitiesResponse(
            installed=result.installed,
            status=result.status,
            total_identities=None,
            identities=identities,
            note=result.note,
        )

    def xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_9(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = self._port.list_identities()
        identities: list[CiliumIdentityOutput] | None = None
        if result.identities is not None:
            identities = [self._to_output(identity) for identity in result.identities]
        return ListCiliumIdentitiesResponse(
            installed=result.installed,
            status=result.status,
            total_identities=result.total_identities,
            identities=None,
            note=result.note,
        )

    def xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_10(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = self._port.list_identities()
        identities: list[CiliumIdentityOutput] | None = None
        if result.identities is not None:
            identities = [self._to_output(identity) for identity in result.identities]
        return ListCiliumIdentitiesResponse(
            installed=result.installed,
            status=result.status,
            total_identities=result.total_identities,
            identities=identities,
            note=None,
        )

    def xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_11(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = self._port.list_identities()
        identities: list[CiliumIdentityOutput] | None = None
        if result.identities is not None:
            identities = [self._to_output(identity) for identity in result.identities]
        return ListCiliumIdentitiesResponse(
            status=result.status,
            total_identities=result.total_identities,
            identities=identities,
            note=result.note,
        )

    def xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_12(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = self._port.list_identities()
        identities: list[CiliumIdentityOutput] | None = None
        if result.identities is not None:
            identities = [self._to_output(identity) for identity in result.identities]
        return ListCiliumIdentitiesResponse(
            installed=result.installed,
            total_identities=result.total_identities,
            identities=identities,
            note=result.note,
        )

    def xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_13(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = self._port.list_identities()
        identities: list[CiliumIdentityOutput] | None = None
        if result.identities is not None:
            identities = [self._to_output(identity) for identity in result.identities]
        return ListCiliumIdentitiesResponse(
            installed=result.installed,
            status=result.status,
            identities=identities,
            note=result.note,
        )

    def xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_14(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = self._port.list_identities()
        identities: list[CiliumIdentityOutput] | None = None
        if result.identities is not None:
            identities = [self._to_output(identity) for identity in result.identities]
        return ListCiliumIdentitiesResponse(
            installed=result.installed,
            status=result.status,
            total_identities=result.total_identities,
            note=result.note,
        )

    def xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_15(self, command: ListCiliumIdentitiesCommand) -> ListCiliumIdentitiesResponse:
        result = self._port.list_identities()
        identities: list[CiliumIdentityOutput] | None = None
        if result.identities is not None:
            identities = [self._to_output(identity) for identity in result.identities]
        return ListCiliumIdentitiesResponse(
            installed=result.installed,
            status=result.status,
            total_identities=result.total_identities,
            identities=identities,
            )

    @staticmethod
    @_mutmut_mutated(mutants_xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut)
    def _to_output(identity: CiliumIdentityInfo) -> CiliumIdentityOutput:
        return {
            "id": identity.id,
            "labels": list(identity.labels),
            "endpoint_count": identity.endpoint_count,
        }

    @staticmethod
    def xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_orig(identity: CiliumIdentityInfo) -> CiliumIdentityOutput:
        return {
            "id": identity.id,
            "labels": list(identity.labels),
            "endpoint_count": identity.endpoint_count,
        }

    @staticmethod
    def xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_1(identity: CiliumIdentityInfo) -> CiliumIdentityOutput:
        return {
            "XXidXX": identity.id,
            "labels": list(identity.labels),
            "endpoint_count": identity.endpoint_count,
        }

    @staticmethod
    def xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_2(identity: CiliumIdentityInfo) -> CiliumIdentityOutput:
        return {
            "ID": identity.id,
            "labels": list(identity.labels),
            "endpoint_count": identity.endpoint_count,
        }

    @staticmethod
    def xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_3(identity: CiliumIdentityInfo) -> CiliumIdentityOutput:
        return {
            "id": identity.id,
            "XXlabelsXX": list(identity.labels),
            "endpoint_count": identity.endpoint_count,
        }

    @staticmethod
    def xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_4(identity: CiliumIdentityInfo) -> CiliumIdentityOutput:
        return {
            "id": identity.id,
            "LABELS": list(identity.labels),
            "endpoint_count": identity.endpoint_count,
        }

    @staticmethod
    def xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_5(identity: CiliumIdentityInfo) -> CiliumIdentityOutput:
        return {
            "id": identity.id,
            "labels": list(None),
            "endpoint_count": identity.endpoint_count,
        }

    @staticmethod
    def xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_6(identity: CiliumIdentityInfo) -> CiliumIdentityOutput:
        return {
            "id": identity.id,
            "labels": list(identity.labels),
            "XXendpoint_countXX": identity.endpoint_count,
        }

    @staticmethod
    def xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_7(identity: CiliumIdentityInfo) -> CiliumIdentityOutput:
        return {
            "id": identity.id,
            "labels": list(identity.labels),
            "ENDPOINT_COUNT": identity.endpoint_count,
        }

mutants_xǁListCiliumIdentitiesUseCaseǁ__init____mutmut['_mutmut_orig'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁ__init____mutmut['xǁListCiliumIdentitiesUseCaseǁ__init____mutmut_1'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut['_mutmut_orig'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut['xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_1'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut['xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_2'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut['xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_3'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut['xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_4'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut['xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_5'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut['xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_6'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut['xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_7'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut['xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_8'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut['xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_9'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut['xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_10'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut['xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_11'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut['xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_12'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut['xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_13'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut['xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_14'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁexecute__mutmut['xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_15'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated

mutants_xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut['_mutmut_orig'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_orig # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut['xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_1'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_1 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut['xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_2'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_2 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut['xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_3'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_3 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut['xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_4'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_4 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut['xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_5'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_5 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut['xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_6'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_6 # type: ignore # mutmut generated
mutants_xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut['xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_7'] = ListCiliumIdentitiesUseCase.xǁListCiliumIdentitiesUseCaseǁ_to_output__mutmut_7 # type: ignore # mutmut generated
