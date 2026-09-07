from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.trace_event_correlation_port import TraceEventCorrelationPort
from hexawyn.application.use_case.troubleshooting.trace_k8s_events.command import (
    TraceK8sEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.trace_k8s_events.response import (
    TraceK8sEventsResponse,
)
from hexawyn.domain.models.trace_k8s_events import TraceEventCorrelationRequest, TraceEventResult


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁTraceK8sEventsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class TraceK8sEventsUseCase:
    @_mutmut_mutated(mutants_xǁTraceK8sEventsUseCaseǁ__init____mutmut)
    def __init__(self, port: TraceEventCorrelationPort) -> None:
        self._port = port
    def xǁTraceK8sEventsUseCaseǁ__init____mutmut_orig(self, port: TraceEventCorrelationPort) -> None:
        self._port = port
    def xǁTraceK8sEventsUseCaseǁ__init____mutmut_1(self, port: TraceEventCorrelationPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut)
    def execute(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_orig(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_1(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = None
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_2(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=None)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_3(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = None
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_4(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(None)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_5(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = None
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_6(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(None)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_7(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = None
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_8(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=None, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_9(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=None, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_10(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=None)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_11(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_12(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_13(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, )
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_14(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=None,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_15(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=None,
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_16(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=None,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_17(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=None,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_18(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_19(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_20(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            conclusion=r.conclusion,
        )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_21(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            )

    def xǁTraceK8sEventsUseCaseǁexecute__mutmut_22(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(None) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )

mutants_xǁTraceK8sEventsUseCaseǁ__init____mutmut['_mutmut_orig'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁ__init____mutmut['xǁTraceK8sEventsUseCaseǁ__init____mutmut_1'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['_mutmut_orig'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_1'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_2'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_3'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_4'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_5'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_6'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_7'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_8'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_9'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_10'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_11'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_12'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_13'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_14'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_15'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_16'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_17'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_18'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_19'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_20'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_21'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTraceK8sEventsUseCaseǁexecute__mutmut['xǁTraceK8sEventsUseCaseǁexecute__mutmut_22'] = TraceK8sEventsUseCase.xǁTraceK8sEventsUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
