from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.use_case.troubleshooting.get_pod_events.command import (
    GetPodEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.get_pod_events.response import (
    GetPodEventsResponse,
)
from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGetPodEventsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class GetPodEventsUseCase:
    @_mutmut_mutated(mutants_xǁGetPodEventsUseCaseǁ__init____mutmut)
    def __init__(
        self,
        events_port: NamespaceEventsPort,
        k8s_port: K8sPort,
    ) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port
    def xǁGetPodEventsUseCaseǁ__init____mutmut_orig(
        self,
        events_port: NamespaceEventsPort,
        k8s_port: K8sPort,
    ) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port
    def xǁGetPodEventsUseCaseǁ__init____mutmut_1(
        self,
        events_port: NamespaceEventsPort,
        k8s_port: K8sPort,
    ) -> None:
        self._events_port = None
        self._k8s_port = k8s_port
    def xǁGetPodEventsUseCaseǁ__init____mutmut_2(
        self,
        events_port: NamespaceEventsPort,
        k8s_port: K8sPort,
    ) -> None:
        self._events_port = events_port
        self._k8s_port = None

    @_mutmut_mutated(mutants_xǁGetPodEventsUseCaseǁexecute__mutmut)
    def execute(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_orig(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_1(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = None
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_2(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=None,
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_3(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=None,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_4(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_5(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_6(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace and "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_7(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "XXXX",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_8(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = None
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_9(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(None)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_10(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = None

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_11(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name and ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_12(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or "XXXX"

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_13(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = None

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_14(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name not in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_15(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object and "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_16(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "XXXX")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_17(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=None,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_18(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=None,
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_19(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=None,
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_20(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=None,
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_21(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_22(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_23(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_24(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_25(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace and "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_26(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "XXXX",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_27(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "XXevent_typeXX": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_28(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "EVENT_TYPE": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_29(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "XXreasonXX": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_30(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "REASON": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_31(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "XXmessageXX": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_32(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "MESSAGE": e.message,
                    "object": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_33(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "XXobjectXX": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_34(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "OBJECT": e.object,
                    "count": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_35(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "XXcountXX": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_36(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "COUNT": e.count,
                    "last_seen": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_37(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "XXlast_seenXX": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

    def xǁGetPodEventsUseCaseǁexecute__mutmut_38(self, command: GetPodEventsCommand) -> GetPodEventsResponse:
        request = GetNamespaceEventsRequest(
            namespace=command.namespace or "",
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        pod_name = command.pod_name or ""

        filtered = [e for e in raw_events if pod_name in (e.object or "")]

        return GetPodEventsResponse(
            pod_name=pod_name,
            namespace=command.namespace or "",
            events=[
                {
                    "event_type": e.event_type,
                    "reason": e.reason,
                    "message": e.message,
                    "object": e.object,
                    "count": e.count,
                    "LAST_SEEN": e.last_seen,
                }
                for e in filtered
            ],
            total_events=len(filtered),
        )

mutants_xǁGetPodEventsUseCaseǁ__init____mutmut['_mutmut_orig'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁ__init____mutmut['xǁGetPodEventsUseCaseǁ__init____mutmut_1'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁ__init____mutmut['xǁGetPodEventsUseCaseǁ__init____mutmut_2'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['_mutmut_orig'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_1'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_2'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_3'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_4'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_5'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_6'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_7'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_8'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_9'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_10'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_11'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_12'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_13'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_14'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_15'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_16'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_17'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_18'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_19'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_20'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_21'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_22'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_23'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_24'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_25'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_26'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_27'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_28'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_29'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_30'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_31'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_32'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_33'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_34'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_35'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_36'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_37'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGetPodEventsUseCaseǁexecute__mutmut['xǁGetPodEventsUseCaseǁexecute__mutmut_38'] = GetPodEventsUseCase.xǁGetPodEventsUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
