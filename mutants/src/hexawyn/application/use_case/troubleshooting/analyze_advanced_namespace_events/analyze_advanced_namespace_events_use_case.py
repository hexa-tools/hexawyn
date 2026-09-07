from __future__ import annotations

from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.use_case.troubleshooting.analyze_advanced_namespace_events.command import (
    AnalyzeAdvancedNamespaceEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.analyze_advanced_namespace_events.response import (  # noqa: E501
    AdvancedNamespaceEventAnalyticsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAnalyzeAdvancedNamespaceEventsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class AnalyzeAdvancedNamespaceEventsUseCase:
    @_mutmut_mutated(mutants_xǁAnalyzeAdvancedNamespaceEventsUseCaseǁ__init____mutmut)
    def __init__(self, port: NamespaceEventsPort) -> None:
        self._port = port
    def xǁAnalyzeAdvancedNamespaceEventsUseCaseǁ__init____mutmut_orig(self, port: NamespaceEventsPort) -> None:
        self._port = port
    def xǁAnalyzeAdvancedNamespaceEventsUseCaseǁ__init____mutmut_1(self, port: NamespaceEventsPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut)
    def execute(
        self, command: AnalyzeAdvancedNamespaceEventsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        events = self._port.list_events(  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        return AdvancedNamespaceEventAnalyticsResponse(
            namespace=command.namespace,
            total_events=len(events),
        )

    def xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_orig(
        self, command: AnalyzeAdvancedNamespaceEventsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        events = self._port.list_events(  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        return AdvancedNamespaceEventAnalyticsResponse(
            namespace=command.namespace,
            total_events=len(events),
        )

    def xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_1(
        self, command: AnalyzeAdvancedNamespaceEventsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        events = None
        return AdvancedNamespaceEventAnalyticsResponse(
            namespace=command.namespace,
            total_events=len(events),
        )

    def xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_2(
        self, command: AnalyzeAdvancedNamespaceEventsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        events = self._port.list_events(  # type: ignore
            namespace=None,
            time_window_minutes=command.time_window_minutes,
        )
        return AdvancedNamespaceEventAnalyticsResponse(
            namespace=command.namespace,
            total_events=len(events),
        )

    def xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_3(
        self, command: AnalyzeAdvancedNamespaceEventsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        events = self._port.list_events(  # type: ignore
            namespace=command.namespace,
            time_window_minutes=None,
        )
        return AdvancedNamespaceEventAnalyticsResponse(
            namespace=command.namespace,
            total_events=len(events),
        )

    def xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_4(
        self, command: AnalyzeAdvancedNamespaceEventsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        events = self._port.list_events(  # type: ignore
            time_window_minutes=command.time_window_minutes,
        )
        return AdvancedNamespaceEventAnalyticsResponse(
            namespace=command.namespace,
            total_events=len(events),
        )

    def xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_5(
        self, command: AnalyzeAdvancedNamespaceEventsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        events = self._port.list_events(  # type: ignore
            namespace=command.namespace,
            )
        return AdvancedNamespaceEventAnalyticsResponse(
            namespace=command.namespace,
            total_events=len(events),
        )

    def xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_6(
        self, command: AnalyzeAdvancedNamespaceEventsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        events = self._port.list_events(  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        return AdvancedNamespaceEventAnalyticsResponse(
            namespace=None,
            total_events=len(events),
        )

    def xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_7(
        self, command: AnalyzeAdvancedNamespaceEventsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        events = self._port.list_events(  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        return AdvancedNamespaceEventAnalyticsResponse(
            namespace=command.namespace,
            total_events=None,
        )

    def xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_8(
        self, command: AnalyzeAdvancedNamespaceEventsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        events = self._port.list_events(  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        return AdvancedNamespaceEventAnalyticsResponse(
            total_events=len(events),
        )

    def xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_9(
        self, command: AnalyzeAdvancedNamespaceEventsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        events = self._port.list_events(  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        return AdvancedNamespaceEventAnalyticsResponse(
            namespace=command.namespace,
            )

mutants_xǁAnalyzeAdvancedNamespaceEventsUseCaseǁ__init____mutmut['_mutmut_orig'] = AnalyzeAdvancedNamespaceEventsUseCase.xǁAnalyzeAdvancedNamespaceEventsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAnalyzeAdvancedNamespaceEventsUseCaseǁ__init____mutmut['xǁAnalyzeAdvancedNamespaceEventsUseCaseǁ__init____mutmut_1'] = AnalyzeAdvancedNamespaceEventsUseCase.xǁAnalyzeAdvancedNamespaceEventsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut['_mutmut_orig'] = AnalyzeAdvancedNamespaceEventsUseCase.xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_1'] = AnalyzeAdvancedNamespaceEventsUseCase.xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_2'] = AnalyzeAdvancedNamespaceEventsUseCase.xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_3'] = AnalyzeAdvancedNamespaceEventsUseCase.xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_4'] = AnalyzeAdvancedNamespaceEventsUseCase.xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_5'] = AnalyzeAdvancedNamespaceEventsUseCase.xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_6'] = AnalyzeAdvancedNamespaceEventsUseCase.xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_7'] = AnalyzeAdvancedNamespaceEventsUseCase.xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_8'] = AnalyzeAdvancedNamespaceEventsUseCase.xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_9'] = AnalyzeAdvancedNamespaceEventsUseCase.xǁAnalyzeAdvancedNamespaceEventsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
