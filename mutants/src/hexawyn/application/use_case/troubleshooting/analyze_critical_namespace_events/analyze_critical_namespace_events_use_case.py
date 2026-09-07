# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.use_case.troubleshooting.analyze_critical_namespace_events.command import (
    AnalyzeCriticalNamespaceEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.analyze_critical_namespace_events.response import (  # noqa: E501
    AnalyzeCriticalNamespaceEventsResponse,
    CriticalIncidentDict,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest
from hexawyn.domain.services.event_analysis.progressive_namespace_analysis import (
    CriticalEventsAnalysis,
    analyze_critical_events,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut: MutantDict = {}  # type: ignore


class AnalyzeCriticalNamespaceEventsUseCase:
    @_mutmut_mutated(mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ__init____mutmut)
    def __init__(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port
    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁ__init____mutmut_orig(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port
    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁ__init____mutmut_1(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = None
        self._k8s_port = k8s_port
    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁ__init____mutmut_2(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = None

    @_mutmut_mutated(mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut)
    def execute(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)  # type: ignore
        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        analysis = analyze_critical_events(command.namespace, raw_events)  # type: ignore
        return _to_response(analysis)

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_orig(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)  # type: ignore
        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        analysis = analyze_critical_events(command.namespace, raw_events)  # type: ignore
        return _to_response(analysis)

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_1(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        self._validate_namespace_exists(None)  # type: ignore
        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        analysis = analyze_critical_events(command.namespace, raw_events)  # type: ignore
        return _to_response(analysis)

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_2(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)  # type: ignore
        request = None
        raw_events = self._events_port.list_events(request)
        analysis = analyze_critical_events(command.namespace, raw_events)  # type: ignore
        return _to_response(analysis)

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_3(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)  # type: ignore
        request = GetNamespaceEventsRequest(
            namespace=None,
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        analysis = analyze_critical_events(command.namespace, raw_events)  # type: ignore
        return _to_response(analysis)

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_4(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)  # type: ignore
        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=None,
        )
        raw_events = self._events_port.list_events(request)
        analysis = analyze_critical_events(command.namespace, raw_events)  # type: ignore
        return _to_response(analysis)

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_5(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)  # type: ignore
        request = GetNamespaceEventsRequest(
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        analysis = analyze_critical_events(command.namespace, raw_events)  # type: ignore
        return _to_response(analysis)

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_6(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)  # type: ignore
        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            )
        raw_events = self._events_port.list_events(request)
        analysis = analyze_critical_events(command.namespace, raw_events)  # type: ignore
        return _to_response(analysis)

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_7(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)  # type: ignore
        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = None
        analysis = analyze_critical_events(command.namespace, raw_events)  # type: ignore
        return _to_response(analysis)

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_8(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)  # type: ignore
        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(None)
        analysis = analyze_critical_events(command.namespace, raw_events)  # type: ignore
        return _to_response(analysis)

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_9(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)  # type: ignore
        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        analysis = None  # type: ignore
        return _to_response(analysis)

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_10(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)  # type: ignore
        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        analysis = analyze_critical_events(None, raw_events)  # type: ignore
        return _to_response(analysis)

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_11(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)  # type: ignore
        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        analysis = analyze_critical_events(command.namespace, None)  # type: ignore
        return _to_response(analysis)

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_12(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)  # type: ignore
        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        analysis = analyze_critical_events(raw_events)  # type: ignore
        return _to_response(analysis)

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_13(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)  # type: ignore
        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        analysis = analyze_critical_events(command.namespace, )  # type: ignore
        return _to_response(analysis)

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_14(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)  # type: ignore
        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        raw_events = self._events_port.list_events(request)
        analysis = analyze_critical_events(command.namespace, raw_events)  # type: ignore
        return _to_response(None)

    @_mutmut_mutated(mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut)
    def _validate_namespace_exists(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_orig(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_1(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = None
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_2(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_3(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(None):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_4(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["XXnameXX"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_5(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["NAME"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_6(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] != namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_7(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                None, context={"namespace": namespace}
            )

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_8(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context=None
            )

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_9(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                context={"namespace": namespace}
            )

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_10(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", )

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_11(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"XXnamespaceXX": namespace}
            )

    def xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_12(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"NAMESPACE": namespace}
            )

mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ__init____mutmut['_mutmut_orig'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ__init____mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁ__init____mutmut_1'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ__init____mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁ__init____mutmut_2'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut['_mutmut_orig'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_1'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_2'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_3'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_4'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_5'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_6'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_7'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_8'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_9'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_10'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_11'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_12'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_13'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_14'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated

mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['_mutmut_orig'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_1'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_2'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_3'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_4'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_5'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_6'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_7'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_8'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_9'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_10'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_11'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_12'] = AnalyzeCriticalNamespaceEventsUseCase.xǁAnalyzeCriticalNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
def _to_response(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=item.incident.reason,
                involved_objects=item.incident.involved_objects,
                event_count=len(item.incident.events),
                likely_root_cause=item.incident.likely_root_cause,
                runbook_id=item.runbook.runbook_id,
                runbook_title=item.runbook.title,
                runbook_steps=item.runbook.steps,
            )
            for item in analysis.critical_incidents
        ],
    )


def x__to_response__mutmut_orig(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=item.incident.reason,
                involved_objects=item.incident.involved_objects,
                event_count=len(item.incident.events),
                likely_root_cause=item.incident.likely_root_cause,
                runbook_id=item.runbook.runbook_id,
                runbook_title=item.runbook.title,
                runbook_steps=item.runbook.steps,
            )
            for item in analysis.critical_incidents
        ],
    )


def x__to_response__mutmut_1(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=None,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=item.incident.reason,
                involved_objects=item.incident.involved_objects,
                event_count=len(item.incident.events),
                likely_root_cause=item.incident.likely_root_cause,
                runbook_id=item.runbook.runbook_id,
                runbook_title=item.runbook.title,
                runbook_steps=item.runbook.steps,
            )
            for item in analysis.critical_incidents
        ],
    )


def x__to_response__mutmut_2(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=None,
    )


def x__to_response__mutmut_3(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=item.incident.reason,
                involved_objects=item.incident.involved_objects,
                event_count=len(item.incident.events),
                likely_root_cause=item.incident.likely_root_cause,
                runbook_id=item.runbook.runbook_id,
                runbook_title=item.runbook.title,
                runbook_steps=item.runbook.steps,
            )
            for item in analysis.critical_incidents
        ],
    )


def x__to_response__mutmut_4(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        )


def x__to_response__mutmut_5(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=None,
                involved_objects=item.incident.involved_objects,
                event_count=len(item.incident.events),
                likely_root_cause=item.incident.likely_root_cause,
                runbook_id=item.runbook.runbook_id,
                runbook_title=item.runbook.title,
                runbook_steps=item.runbook.steps,
            )
            for item in analysis.critical_incidents
        ],
    )


def x__to_response__mutmut_6(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=item.incident.reason,
                involved_objects=None,
                event_count=len(item.incident.events),
                likely_root_cause=item.incident.likely_root_cause,
                runbook_id=item.runbook.runbook_id,
                runbook_title=item.runbook.title,
                runbook_steps=item.runbook.steps,
            )
            for item in analysis.critical_incidents
        ],
    )


def x__to_response__mutmut_7(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=item.incident.reason,
                involved_objects=item.incident.involved_objects,
                event_count=None,
                likely_root_cause=item.incident.likely_root_cause,
                runbook_id=item.runbook.runbook_id,
                runbook_title=item.runbook.title,
                runbook_steps=item.runbook.steps,
            )
            for item in analysis.critical_incidents
        ],
    )


def x__to_response__mutmut_8(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=item.incident.reason,
                involved_objects=item.incident.involved_objects,
                event_count=len(item.incident.events),
                likely_root_cause=None,
                runbook_id=item.runbook.runbook_id,
                runbook_title=item.runbook.title,
                runbook_steps=item.runbook.steps,
            )
            for item in analysis.critical_incidents
        ],
    )


def x__to_response__mutmut_9(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=item.incident.reason,
                involved_objects=item.incident.involved_objects,
                event_count=len(item.incident.events),
                likely_root_cause=item.incident.likely_root_cause,
                runbook_id=None,
                runbook_title=item.runbook.title,
                runbook_steps=item.runbook.steps,
            )
            for item in analysis.critical_incidents
        ],
    )


def x__to_response__mutmut_10(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=item.incident.reason,
                involved_objects=item.incident.involved_objects,
                event_count=len(item.incident.events),
                likely_root_cause=item.incident.likely_root_cause,
                runbook_id=item.runbook.runbook_id,
                runbook_title=None,
                runbook_steps=item.runbook.steps,
            )
            for item in analysis.critical_incidents
        ],
    )


def x__to_response__mutmut_11(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=item.incident.reason,
                involved_objects=item.incident.involved_objects,
                event_count=len(item.incident.events),
                likely_root_cause=item.incident.likely_root_cause,
                runbook_id=item.runbook.runbook_id,
                runbook_title=item.runbook.title,
                runbook_steps=None,
            )
            for item in analysis.critical_incidents
        ],
    )


def x__to_response__mutmut_12(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                involved_objects=item.incident.involved_objects,
                event_count=len(item.incident.events),
                likely_root_cause=item.incident.likely_root_cause,
                runbook_id=item.runbook.runbook_id,
                runbook_title=item.runbook.title,
                runbook_steps=item.runbook.steps,
            )
            for item in analysis.critical_incidents
        ],
    )


def x__to_response__mutmut_13(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=item.incident.reason,
                event_count=len(item.incident.events),
                likely_root_cause=item.incident.likely_root_cause,
                runbook_id=item.runbook.runbook_id,
                runbook_title=item.runbook.title,
                runbook_steps=item.runbook.steps,
            )
            for item in analysis.critical_incidents
        ],
    )


def x__to_response__mutmut_14(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=item.incident.reason,
                involved_objects=item.incident.involved_objects,
                likely_root_cause=item.incident.likely_root_cause,
                runbook_id=item.runbook.runbook_id,
                runbook_title=item.runbook.title,
                runbook_steps=item.runbook.steps,
            )
            for item in analysis.critical_incidents
        ],
    )


def x__to_response__mutmut_15(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=item.incident.reason,
                involved_objects=item.incident.involved_objects,
                event_count=len(item.incident.events),
                runbook_id=item.runbook.runbook_id,
                runbook_title=item.runbook.title,
                runbook_steps=item.runbook.steps,
            )
            for item in analysis.critical_incidents
        ],
    )


def x__to_response__mutmut_16(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=item.incident.reason,
                involved_objects=item.incident.involved_objects,
                event_count=len(item.incident.events),
                likely_root_cause=item.incident.likely_root_cause,
                runbook_title=item.runbook.title,
                runbook_steps=item.runbook.steps,
            )
            for item in analysis.critical_incidents
        ],
    )


def x__to_response__mutmut_17(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=item.incident.reason,
                involved_objects=item.incident.involved_objects,
                event_count=len(item.incident.events),
                likely_root_cause=item.incident.likely_root_cause,
                runbook_id=item.runbook.runbook_id,
                runbook_steps=item.runbook.steps,
            )
            for item in analysis.critical_incidents
        ],
    )


def x__to_response__mutmut_18(analysis: CriticalEventsAnalysis) -> AnalyzeCriticalNamespaceEventsResponse:
    return AnalyzeCriticalNamespaceEventsResponse(
        namespace=analysis.namespace,
        critical_incidents=[  # type: ignore
            CriticalIncidentDict(  # type: ignore
                reason=item.incident.reason,
                involved_objects=item.incident.involved_objects,
                event_count=len(item.incident.events),
                likely_root_cause=item.incident.likely_root_cause,
                runbook_id=item.runbook.runbook_id,
                runbook_title=item.runbook.title,
                )
            for item in analysis.critical_incidents
        ],
    )

mutants_x__to_response__mutmut['_mutmut_orig'] = x__to_response__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_1'] = x__to_response__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_2'] = x__to_response__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_3'] = x__to_response__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_4'] = x__to_response__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_5'] = x__to_response__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_6'] = x__to_response__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_7'] = x__to_response__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_8'] = x__to_response__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_9'] = x__to_response__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_10'] = x__to_response__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_11'] = x__to_response__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_12'] = x__to_response__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_13'] = x__to_response__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_14'] = x__to_response__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_15'] = x__to_response__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_16'] = x__to_response__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_17'] = x__to_response__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_18'] = x__to_response__mutmut_18 # type: ignore # mutmut generated
