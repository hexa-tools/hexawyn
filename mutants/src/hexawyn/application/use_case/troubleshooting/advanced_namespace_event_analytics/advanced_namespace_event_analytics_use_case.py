# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.use_case.troubleshooting.advanced_namespace_event_analytics.command import (  # noqa: E501
    AdvancedNamespaceEventAnalyticsCommand,
)
from hexawyn.application.use_case.troubleshooting.advanced_namespace_event_analytics.response import (  # noqa: E501  # type: ignore
    AdvancedNamespaceEventAnalyticsResponse,
    EventStormDict,
    IncidentSummaryDict,
    ReasonCountDict,
    SampleEventDict,
    TimelineBucketDict,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.event import ClassifiedEvent
from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest
from hexawyn.domain.services.event_analysis.advanced_event_analytics import (
    AdvancedEventAnalyticsReport,
    IncidentSummary,
    generate_advanced_event_analytics,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut: MutantDict = {}  # type: ignore


class AdvancedNamespaceEventAnalyticsUseCase:
    @_mutmut_mutated(mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ__init____mutmut)
    def __init__(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port
    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁ__init____mutmut_orig(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port
    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁ__init____mutmut_1(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = None
        self._k8s_port = k8s_port
    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁ__init____mutmut_2(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = None

    @_mutmut_mutated(mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut)
    def execute(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw_events = self._events_port.list_events(request)
        report = generate_advanced_event_analytics(command.namespace, raw_events)
        return _to_response(report)

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_orig(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw_events = self._events_port.list_events(request)
        report = generate_advanced_event_analytics(command.namespace, raw_events)
        return _to_response(report)

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_1(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        self._validate_namespace_exists(None)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw_events = self._events_port.list_events(request)
        report = generate_advanced_event_analytics(command.namespace, raw_events)
        return _to_response(report)

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_2(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        self._validate_namespace_exists(command.namespace)

        request = None
        raw_events = self._events_port.list_events(request)
        report = generate_advanced_event_analytics(command.namespace, raw_events)
        return _to_response(report)

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_3(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=None,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw_events = self._events_port.list_events(request)
        report = generate_advanced_event_analytics(command.namespace, raw_events)
        return _to_response(report)

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_4(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=None,  # type: ignore
        )
        raw_events = self._events_port.list_events(request)
        report = generate_advanced_event_analytics(command.namespace, raw_events)
        return _to_response(report)

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_5(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw_events = self._events_port.list_events(request)
        report = generate_advanced_event_analytics(command.namespace, raw_events)
        return _to_response(report)

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_6(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            )
        raw_events = self._events_port.list_events(request)
        report = generate_advanced_event_analytics(command.namespace, raw_events)
        return _to_response(report)

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_7(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw_events = None
        report = generate_advanced_event_analytics(command.namespace, raw_events)
        return _to_response(report)

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_8(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw_events = self._events_port.list_events(None)
        report = generate_advanced_event_analytics(command.namespace, raw_events)
        return _to_response(report)

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_9(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw_events = self._events_port.list_events(request)
        report = None
        return _to_response(report)

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_10(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw_events = self._events_port.list_events(request)
        report = generate_advanced_event_analytics(None, raw_events)
        return _to_response(report)

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_11(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw_events = self._events_port.list_events(request)
        report = generate_advanced_event_analytics(command.namespace, None)
        return _to_response(report)

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_12(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw_events = self._events_port.list_events(request)
        report = generate_advanced_event_analytics(raw_events)
        return _to_response(report)

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_13(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw_events = self._events_port.list_events(request)
        report = generate_advanced_event_analytics(command.namespace, )
        return _to_response(report)

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_14(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw_events = self._events_port.list_events(request)
        report = generate_advanced_event_analytics(command.namespace, raw_events)
        return _to_response(None)

    @_mutmut_mutated(mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut)
    def _validate_namespace_exists(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_orig(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_1(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = None
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_2(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_3(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(None):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_4(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["XXnameXX"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_5(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["NAME"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_6(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] != namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_7(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                None, context={"namespace": namespace}
            )

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_8(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context=None
            )

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_9(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                context={"namespace": namespace}
            )

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_10(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", )

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_11(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"XXnamespaceXX": namespace}
            )

    def xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_12(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"NAMESPACE": namespace}
            )

mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ__init____mutmut['_mutmut_orig'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ__init____mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁ__init____mutmut_1'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ__init____mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁ__init____mutmut_2'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut['_mutmut_orig'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_1'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_2'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_3'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_4'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_5'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_6'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_7'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_8'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_9'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_10'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_11'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_12'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_13'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_14'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated

mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut['_mutmut_orig'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_1'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_2'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_3'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_4'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_5'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_6'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_7'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_8'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_9'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_10'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_11'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut['xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_12'] = AdvancedNamespaceEventAnalyticsUseCase.xǁAdvancedNamespaceEventAnalyticsUseCaseǁ_validate_namespace_exists__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
def _to_response(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_orig(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_1(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=None,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_2(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=None,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_3(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=None,
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_4(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=None,
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_5(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=None,
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_6(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=None,
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_7(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=None,
    )


def x__to_response__mutmut_8(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_9(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_10(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_11(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_12(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_13(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_14(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        )


def x__to_response__mutmut_15(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=None, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_16(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=None, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_17(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=None)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_18(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_19(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_20(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, )
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_21(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=None, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_22(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=None, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_23(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=None
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_24(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_25(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_26(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_27(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=None, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_28(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=None) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_29(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_30(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, ) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(item) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
    )


def x__to_response__mutmut_31(report: AdvancedEventAnalyticsReport) -> AdvancedNamespaceEventAnalyticsResponse:
    return AdvancedNamespaceEventAnalyticsResponse(  # type: ignore
        namespace=report.namespace,
        total_events=report.total_events,
        timeline=[
            TimelineBucketDict(minute=bucket.minute, count=bucket.count, is_spike=bucket.is_spike)
            for bucket in report.timeline
        ],
        storms=[
            EventStormDict(
                start_time=storm.start_time, end_time=storm.end_time, event_count=storm.event_count
            )
            for storm in report.storms
        ],
        top_reasons=[
            ReasonCountDict(reason=item.reason, count=item.count) for item in report.top_reasons
        ],
        correlated_incidents=[_to_incident_dict(None) for item in report.correlated_incidents],
        sampling_applied=report.sampling_applied,
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
mutants_x__to_response__mutmut['x__to_response__mutmut_19'] = x__to_response__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_20'] = x__to_response__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_21'] = x__to_response__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_22'] = x__to_response__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_23'] = x__to_response__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_24'] = x__to_response__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_25'] = x__to_response__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_26'] = x__to_response__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_27'] = x__to_response__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_28'] = x__to_response__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_29'] = x__to_response__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_30'] = x__to_response__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_31'] = x__to_response__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_incident_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_incident_dict__mutmut)
def _to_incident_dict(incident: IncidentSummary) -> IncidentSummaryDict:
    return IncidentSummaryDict(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        event_count=incident.event_count,
        likely_root_cause=incident.likely_root_cause,
        sample_events=[_to_sample_event_dict(event) for event in incident.sample_events],
    )


def x__to_incident_dict__mutmut_orig(incident: IncidentSummary) -> IncidentSummaryDict:
    return IncidentSummaryDict(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        event_count=incident.event_count,
        likely_root_cause=incident.likely_root_cause,
        sample_events=[_to_sample_event_dict(event) for event in incident.sample_events],
    )


def x__to_incident_dict__mutmut_1(incident: IncidentSummary) -> IncidentSummaryDict:
    return IncidentSummaryDict(
        reason=None,
        involved_objects=incident.involved_objects,
        event_count=incident.event_count,
        likely_root_cause=incident.likely_root_cause,
        sample_events=[_to_sample_event_dict(event) for event in incident.sample_events],
    )


def x__to_incident_dict__mutmut_2(incident: IncidentSummary) -> IncidentSummaryDict:
    return IncidentSummaryDict(
        reason=incident.reason,
        involved_objects=None,
        event_count=incident.event_count,
        likely_root_cause=incident.likely_root_cause,
        sample_events=[_to_sample_event_dict(event) for event in incident.sample_events],
    )


def x__to_incident_dict__mutmut_3(incident: IncidentSummary) -> IncidentSummaryDict:
    return IncidentSummaryDict(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        event_count=None,
        likely_root_cause=incident.likely_root_cause,
        sample_events=[_to_sample_event_dict(event) for event in incident.sample_events],
    )


def x__to_incident_dict__mutmut_4(incident: IncidentSummary) -> IncidentSummaryDict:
    return IncidentSummaryDict(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        event_count=incident.event_count,
        likely_root_cause=None,
        sample_events=[_to_sample_event_dict(event) for event in incident.sample_events],
    )


def x__to_incident_dict__mutmut_5(incident: IncidentSummary) -> IncidentSummaryDict:
    return IncidentSummaryDict(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        event_count=incident.event_count,
        likely_root_cause=incident.likely_root_cause,
        sample_events=None,
    )


def x__to_incident_dict__mutmut_6(incident: IncidentSummary) -> IncidentSummaryDict:
    return IncidentSummaryDict(
        involved_objects=incident.involved_objects,
        event_count=incident.event_count,
        likely_root_cause=incident.likely_root_cause,
        sample_events=[_to_sample_event_dict(event) for event in incident.sample_events],
    )


def x__to_incident_dict__mutmut_7(incident: IncidentSummary) -> IncidentSummaryDict:
    return IncidentSummaryDict(
        reason=incident.reason,
        event_count=incident.event_count,
        likely_root_cause=incident.likely_root_cause,
        sample_events=[_to_sample_event_dict(event) for event in incident.sample_events],
    )


def x__to_incident_dict__mutmut_8(incident: IncidentSummary) -> IncidentSummaryDict:
    return IncidentSummaryDict(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        likely_root_cause=incident.likely_root_cause,
        sample_events=[_to_sample_event_dict(event) for event in incident.sample_events],
    )


def x__to_incident_dict__mutmut_9(incident: IncidentSummary) -> IncidentSummaryDict:
    return IncidentSummaryDict(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        event_count=incident.event_count,
        sample_events=[_to_sample_event_dict(event) for event in incident.sample_events],
    )


def x__to_incident_dict__mutmut_10(incident: IncidentSummary) -> IncidentSummaryDict:
    return IncidentSummaryDict(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        event_count=incident.event_count,
        likely_root_cause=incident.likely_root_cause,
        )


def x__to_incident_dict__mutmut_11(incident: IncidentSummary) -> IncidentSummaryDict:
    return IncidentSummaryDict(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        event_count=incident.event_count,
        likely_root_cause=incident.likely_root_cause,
        sample_events=[_to_sample_event_dict(None) for event in incident.sample_events],
    )

mutants_x__to_incident_dict__mutmut['_mutmut_orig'] = x__to_incident_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_incident_dict__mutmut['x__to_incident_dict__mutmut_1'] = x__to_incident_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_incident_dict__mutmut['x__to_incident_dict__mutmut_2'] = x__to_incident_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_incident_dict__mutmut['x__to_incident_dict__mutmut_3'] = x__to_incident_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_incident_dict__mutmut['x__to_incident_dict__mutmut_4'] = x__to_incident_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_incident_dict__mutmut['x__to_incident_dict__mutmut_5'] = x__to_incident_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_incident_dict__mutmut['x__to_incident_dict__mutmut_6'] = x__to_incident_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_incident_dict__mutmut['x__to_incident_dict__mutmut_7'] = x__to_incident_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_incident_dict__mutmut['x__to_incident_dict__mutmut_8'] = x__to_incident_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_incident_dict__mutmut['x__to_incident_dict__mutmut_9'] = x__to_incident_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_incident_dict__mutmut['x__to_incident_dict__mutmut_10'] = x__to_incident_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_incident_dict__mutmut['x__to_incident_dict__mutmut_11'] = x__to_incident_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_sample_event_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_sample_event_dict__mutmut)
def _to_sample_event_dict(event: ClassifiedEvent) -> SampleEventDict:
    return SampleEventDict(
        reason=event.reason,
        message=event.message,
        involved_object=event.involved_object,
        severity=event.severity.value,
        timestamp=event.last_timestamp.isoformat() if event.last_timestamp else "",
    )


def x__to_sample_event_dict__mutmut_orig(event: ClassifiedEvent) -> SampleEventDict:
    return SampleEventDict(
        reason=event.reason,
        message=event.message,
        involved_object=event.involved_object,
        severity=event.severity.value,
        timestamp=event.last_timestamp.isoformat() if event.last_timestamp else "",
    )


def x__to_sample_event_dict__mutmut_1(event: ClassifiedEvent) -> SampleEventDict:
    return SampleEventDict(
        reason=None,
        message=event.message,
        involved_object=event.involved_object,
        severity=event.severity.value,
        timestamp=event.last_timestamp.isoformat() if event.last_timestamp else "",
    )


def x__to_sample_event_dict__mutmut_2(event: ClassifiedEvent) -> SampleEventDict:
    return SampleEventDict(
        reason=event.reason,
        message=None,
        involved_object=event.involved_object,
        severity=event.severity.value,
        timestamp=event.last_timestamp.isoformat() if event.last_timestamp else "",
    )


def x__to_sample_event_dict__mutmut_3(event: ClassifiedEvent) -> SampleEventDict:
    return SampleEventDict(
        reason=event.reason,
        message=event.message,
        involved_object=None,
        severity=event.severity.value,
        timestamp=event.last_timestamp.isoformat() if event.last_timestamp else "",
    )


def x__to_sample_event_dict__mutmut_4(event: ClassifiedEvent) -> SampleEventDict:
    return SampleEventDict(
        reason=event.reason,
        message=event.message,
        involved_object=event.involved_object,
        severity=None,
        timestamp=event.last_timestamp.isoformat() if event.last_timestamp else "",
    )


def x__to_sample_event_dict__mutmut_5(event: ClassifiedEvent) -> SampleEventDict:
    return SampleEventDict(
        reason=event.reason,
        message=event.message,
        involved_object=event.involved_object,
        severity=event.severity.value,
        timestamp=None,
    )


def x__to_sample_event_dict__mutmut_6(event: ClassifiedEvent) -> SampleEventDict:
    return SampleEventDict(
        message=event.message,
        involved_object=event.involved_object,
        severity=event.severity.value,
        timestamp=event.last_timestamp.isoformat() if event.last_timestamp else "",
    )


def x__to_sample_event_dict__mutmut_7(event: ClassifiedEvent) -> SampleEventDict:
    return SampleEventDict(
        reason=event.reason,
        involved_object=event.involved_object,
        severity=event.severity.value,
        timestamp=event.last_timestamp.isoformat() if event.last_timestamp else "",
    )


def x__to_sample_event_dict__mutmut_8(event: ClassifiedEvent) -> SampleEventDict:
    return SampleEventDict(
        reason=event.reason,
        message=event.message,
        severity=event.severity.value,
        timestamp=event.last_timestamp.isoformat() if event.last_timestamp else "",
    )


def x__to_sample_event_dict__mutmut_9(event: ClassifiedEvent) -> SampleEventDict:
    return SampleEventDict(
        reason=event.reason,
        message=event.message,
        involved_object=event.involved_object,
        timestamp=event.last_timestamp.isoformat() if event.last_timestamp else "",
    )


def x__to_sample_event_dict__mutmut_10(event: ClassifiedEvent) -> SampleEventDict:
    return SampleEventDict(
        reason=event.reason,
        message=event.message,
        involved_object=event.involved_object,
        severity=event.severity.value,
        )


def x__to_sample_event_dict__mutmut_11(event: ClassifiedEvent) -> SampleEventDict:
    return SampleEventDict(
        reason=event.reason,
        message=event.message,
        involved_object=event.involved_object,
        severity=event.severity.value,
        timestamp=event.last_timestamp.isoformat() if event.last_timestamp else "XXXX",
    )

mutants_x__to_sample_event_dict__mutmut['_mutmut_orig'] = x__to_sample_event_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_sample_event_dict__mutmut['x__to_sample_event_dict__mutmut_1'] = x__to_sample_event_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_sample_event_dict__mutmut['x__to_sample_event_dict__mutmut_2'] = x__to_sample_event_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_sample_event_dict__mutmut['x__to_sample_event_dict__mutmut_3'] = x__to_sample_event_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_sample_event_dict__mutmut['x__to_sample_event_dict__mutmut_4'] = x__to_sample_event_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_sample_event_dict__mutmut['x__to_sample_event_dict__mutmut_5'] = x__to_sample_event_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_sample_event_dict__mutmut['x__to_sample_event_dict__mutmut_6'] = x__to_sample_event_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_sample_event_dict__mutmut['x__to_sample_event_dict__mutmut_7'] = x__to_sample_event_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_sample_event_dict__mutmut['x__to_sample_event_dict__mutmut_8'] = x__to_sample_event_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_sample_event_dict__mutmut['x__to_sample_event_dict__mutmut_9'] = x__to_sample_event_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_sample_event_dict__mutmut['x__to_sample_event_dict__mutmut_10'] = x__to_sample_event_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_sample_event_dict__mutmut['x__to_sample_event_dict__mutmut_11'] = x__to_sample_event_dict__mutmut_11 # type: ignore # mutmut generated
