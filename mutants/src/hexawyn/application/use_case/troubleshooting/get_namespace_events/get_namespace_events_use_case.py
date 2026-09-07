from __future__ import annotations

from datetime import UTC, datetime

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.use_case.troubleshooting.get_namespace_events.command import (
    GetNamespaceEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.get_namespace_events.mapper import to_response
from hexawyn.application.use_case.troubleshooting.get_namespace_events.response import (
    GetNamespaceEventsResponse,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.namespace_event import (
    GetNamespaceEventsRequest,
)
from hexawyn.domain.services.event_analysis.namespace_event_filter import get_namespace_events


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGetNamespaceEventsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut: MutantDict = {}  # type: ignore


class GetNamespaceEventsUseCase:
    @_mutmut_mutated(mutants_xǁGetNamespaceEventsUseCaseǁ__init____mutmut)
    def __init__(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port
    def xǁGetNamespaceEventsUseCaseǁ__init____mutmut_orig(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port
    def xǁGetNamespaceEventsUseCaseǁ__init____mutmut_1(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = None
        self._k8s_port = k8s_port
    def xǁGetNamespaceEventsUseCaseǁ__init____mutmut_2(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = None

    @_mutmut_mutated(mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut)
    def execute(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, raw_events, observed_at=datetime.now(UTC))
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_orig(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, raw_events, observed_at=datetime.now(UTC))
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_1(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(None)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, raw_events, observed_at=datetime.now(UTC))
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_2(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = None
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, raw_events, observed_at=datetime.now(UTC))
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_3(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=None,
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, raw_events, observed_at=datetime.now(UTC))
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_4(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=None,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, raw_events, observed_at=datetime.now(UTC))
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_5(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            top_n=None,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, raw_events, observed_at=datetime.now(UTC))
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_6(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, raw_events, observed_at=datetime.now(UTC))
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_7(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, raw_events, observed_at=datetime.now(UTC))
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_8(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, raw_events, observed_at=datetime.now(UTC))
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_9(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = None
        result = get_namespace_events(request, raw_events, observed_at=datetime.now(UTC))
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_10(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(None)
        result = get_namespace_events(request, raw_events, observed_at=datetime.now(UTC))
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_11(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = None
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_12(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(None, raw_events, observed_at=datetime.now(UTC))
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_13(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, None, observed_at=datetime.now(UTC))
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_14(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, raw_events, observed_at=None)
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_15(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(raw_events, observed_at=datetime.now(UTC))
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_16(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, observed_at=datetime.now(UTC))
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_17(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, raw_events, )
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_18(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, raw_events, observed_at=datetime.now(None))
        return to_response(result)

    def xǁGetNamespaceEventsUseCaseǁexecute__mutmut_19(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            top_n=command.top_n,
        )
        raw_events = self._events_port.list_events(request)
        result = get_namespace_events(request, raw_events, observed_at=datetime.now(UTC))
        return to_response(None)

    @_mutmut_mutated(mutants_xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut)
    def _validate_namespace_exists(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_orig(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_1(self, namespace: str) -> None:
        namespaces = None
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_2(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_3(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(None):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_4(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["XXnameXX"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_5(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["NAME"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_6(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] != namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_7(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                None, context={"namespace": namespace}
            )

    def xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_8(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context=None
            )

    def xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_9(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                context={"namespace": namespace}
            )

    def xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_10(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", )

    def xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_11(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"XXnamespaceXX": namespace}
            )

    def xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_12(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"NAMESPACE": namespace}
            )

mutants_xǁGetNamespaceEventsUseCaseǁ__init____mutmut['_mutmut_orig'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁ__init____mutmut['xǁGetNamespaceEventsUseCaseǁ__init____mutmut_1'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁ__init____mutmut['xǁGetNamespaceEventsUseCaseǁ__init____mutmut_2'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['_mutmut_orig'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_1'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_2'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_3'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_4'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_5'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_6'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_7'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_8'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_9'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_10'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_11'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_12'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_13'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_14'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_15'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_16'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_17'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_18'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁexecute__mutmut['xǁGetNamespaceEventsUseCaseǁexecute__mutmut_19'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated

mutants_xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['_mutmut_orig'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_1'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_2'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_3'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_4'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_5'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_6'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_7'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_8'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_9'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_10'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_11'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_12'] = GetNamespaceEventsUseCase.xǁGetNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_12 # type: ignore # mutmut generated
