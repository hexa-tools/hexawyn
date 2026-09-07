from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.use_case.troubleshooting.summarize_namespace_events.command import (
    SummarizeNamespaceEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.summarize_namespace_events.response import (
    SummarizeNamespaceEventsResponse,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest
from hexawyn.domain.services.event_analysis.progressive_namespace_analysis import (
    NamespaceEventsSummary,
    summarize_namespace_events,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSummarizeNamespaceEventsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut: MutantDict = {}  # type: ignore


class SummarizeNamespaceEventsUseCase:
    @_mutmut_mutated(mutants_xǁSummarizeNamespaceEventsUseCaseǁ__init____mutmut)
    def __init__(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port
    def xǁSummarizeNamespaceEventsUseCaseǁ__init____mutmut_orig(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port
    def xǁSummarizeNamespaceEventsUseCaseǁ__init____mutmut_1(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = None
        self._k8s_port = k8s_port
    def xǁSummarizeNamespaceEventsUseCaseǁ__init____mutmut_2(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events_port = events_port
        self._k8s_port = None

    @_mutmut_mutated(mutants_xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut)
    def summarize(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace, time_window_minutes=command.time_window_minutes
        )
        raw_events = self._events_port.list_events(request)
        summary = summarize_namespace_events(command.namespace, raw_events)
        return _to_response(summary)

    def xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_orig(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace, time_window_minutes=command.time_window_minutes
        )
        raw_events = self._events_port.list_events(request)
        summary = summarize_namespace_events(command.namespace, raw_events)
        return _to_response(summary)

    def xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_1(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse:
        self._validate_namespace_exists(None)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace, time_window_minutes=command.time_window_minutes
        )
        raw_events = self._events_port.list_events(request)
        summary = summarize_namespace_events(command.namespace, raw_events)
        return _to_response(summary)

    def xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_2(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = None
        raw_events = self._events_port.list_events(request)
        summary = summarize_namespace_events(command.namespace, raw_events)
        return _to_response(summary)

    def xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_3(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=None, time_window_minutes=command.time_window_minutes
        )
        raw_events = self._events_port.list_events(request)
        summary = summarize_namespace_events(command.namespace, raw_events)
        return _to_response(summary)

    def xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_4(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace, time_window_minutes=None
        )
        raw_events = self._events_port.list_events(request)
        summary = summarize_namespace_events(command.namespace, raw_events)
        return _to_response(summary)

    def xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_5(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            time_window_minutes=command.time_window_minutes
        )
        raw_events = self._events_port.list_events(request)
        summary = summarize_namespace_events(command.namespace, raw_events)
        return _to_response(summary)

    def xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_6(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace, )
        raw_events = self._events_port.list_events(request)
        summary = summarize_namespace_events(command.namespace, raw_events)
        return _to_response(summary)

    def xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_7(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace, time_window_minutes=command.time_window_minutes
        )
        raw_events = None
        summary = summarize_namespace_events(command.namespace, raw_events)
        return _to_response(summary)

    def xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_8(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace, time_window_minutes=command.time_window_minutes
        )
        raw_events = self._events_port.list_events(None)
        summary = summarize_namespace_events(command.namespace, raw_events)
        return _to_response(summary)

    def xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_9(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace, time_window_minutes=command.time_window_minutes
        )
        raw_events = self._events_port.list_events(request)
        summary = None
        return _to_response(summary)

    def xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_10(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace, time_window_minutes=command.time_window_minutes
        )
        raw_events = self._events_port.list_events(request)
        summary = summarize_namespace_events(None, raw_events)
        return _to_response(summary)

    def xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_11(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace, time_window_minutes=command.time_window_minutes
        )
        raw_events = self._events_port.list_events(request)
        summary = summarize_namespace_events(command.namespace, None)
        return _to_response(summary)

    def xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_12(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace, time_window_minutes=command.time_window_minutes
        )
        raw_events = self._events_port.list_events(request)
        summary = summarize_namespace_events(raw_events)
        return _to_response(summary)

    def xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_13(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace, time_window_minutes=command.time_window_minutes
        )
        raw_events = self._events_port.list_events(request)
        summary = summarize_namespace_events(command.namespace, )
        return _to_response(summary)

    def xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_14(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse:
        self._validate_namespace_exists(command.namespace)

        request = GetNamespaceEventsRequest(
            namespace=command.namespace, time_window_minutes=command.time_window_minutes
        )
        raw_events = self._events_port.list_events(request)
        summary = summarize_namespace_events(command.namespace, raw_events)
        return _to_response(None)

    @_mutmut_mutated(mutants_xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut)
    def _validate_namespace_exists(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_orig(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_1(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = None
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_2(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_3(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(None):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_4(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["XXnameXX"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_5(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["NAME"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_6(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] != namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_7(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                None, context={"namespace": namespace}
            )

    def xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_8(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context=None
            )

    def xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_9(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                context={"namespace": namespace}
            )

    def xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_10(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", )

    def xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_11(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"XXnamespaceXX": namespace}
            )

    def xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_12(self, namespace: str) -> None:
        """ECA-5 dependency: list_namespaces validates the namespace before fetching events."""
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"NAMESPACE": namespace}
            )

mutants_xǁSummarizeNamespaceEventsUseCaseǁ__init____mutmut['_mutmut_orig'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁ__init____mutmut['xǁSummarizeNamespaceEventsUseCaseǁ__init____mutmut_1'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁ__init____mutmut['xǁSummarizeNamespaceEventsUseCaseǁ__init____mutmut_2'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut['_mutmut_orig'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut['xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_1'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut['xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_2'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut['xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_3'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut['xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_4'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut['xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_5'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut['xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_6'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut['xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_7'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut['xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_8'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut['xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_9'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut['xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_10'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut['xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_11'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut['xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_12'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut['xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_13'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut['xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_14'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁsummarize__mutmut_14 # type: ignore # mutmut generated

mutants_xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['_mutmut_orig'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_1'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_2'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_3'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_4'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_5'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_6'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_7'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_8'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_9'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_10'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_11'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut['xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_12'] = SummarizeNamespaceEventsUseCase.xǁSummarizeNamespaceEventsUseCaseǁ_validate_namespace_exists__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
def _to_response(summary: NamespaceEventsSummary) -> SummarizeNamespaceEventsResponse:
    return SummarizeNamespaceEventsResponse(
        namespace=summary.namespace,
        total_events=summary.total_events,
        severity_breakdown=summary.severity_breakdown,
        top_affected_pods=summary.top_affected_pods,  # type: ignore
    )


def x__to_response__mutmut_orig(summary: NamespaceEventsSummary) -> SummarizeNamespaceEventsResponse:
    return SummarizeNamespaceEventsResponse(
        namespace=summary.namespace,
        total_events=summary.total_events,
        severity_breakdown=summary.severity_breakdown,
        top_affected_pods=summary.top_affected_pods,  # type: ignore
    )


def x__to_response__mutmut_1(summary: NamespaceEventsSummary) -> SummarizeNamespaceEventsResponse:
    return SummarizeNamespaceEventsResponse(
        namespace=None,
        total_events=summary.total_events,
        severity_breakdown=summary.severity_breakdown,
        top_affected_pods=summary.top_affected_pods,  # type: ignore
    )


def x__to_response__mutmut_2(summary: NamespaceEventsSummary) -> SummarizeNamespaceEventsResponse:
    return SummarizeNamespaceEventsResponse(
        namespace=summary.namespace,
        total_events=None,
        severity_breakdown=summary.severity_breakdown,
        top_affected_pods=summary.top_affected_pods,  # type: ignore
    )


def x__to_response__mutmut_3(summary: NamespaceEventsSummary) -> SummarizeNamespaceEventsResponse:
    return SummarizeNamespaceEventsResponse(
        namespace=summary.namespace,
        total_events=summary.total_events,
        severity_breakdown=None,
        top_affected_pods=summary.top_affected_pods,  # type: ignore
    )


def x__to_response__mutmut_4(summary: NamespaceEventsSummary) -> SummarizeNamespaceEventsResponse:
    return SummarizeNamespaceEventsResponse(
        namespace=summary.namespace,
        total_events=summary.total_events,
        severity_breakdown=summary.severity_breakdown,
        top_affected_pods=None,  # type: ignore
    )


def x__to_response__mutmut_5(summary: NamespaceEventsSummary) -> SummarizeNamespaceEventsResponse:
    return SummarizeNamespaceEventsResponse(
        total_events=summary.total_events,
        severity_breakdown=summary.severity_breakdown,
        top_affected_pods=summary.top_affected_pods,  # type: ignore
    )


def x__to_response__mutmut_6(summary: NamespaceEventsSummary) -> SummarizeNamespaceEventsResponse:
    return SummarizeNamespaceEventsResponse(
        namespace=summary.namespace,
        severity_breakdown=summary.severity_breakdown,
        top_affected_pods=summary.top_affected_pods,  # type: ignore
    )


def x__to_response__mutmut_7(summary: NamespaceEventsSummary) -> SummarizeNamespaceEventsResponse:
    return SummarizeNamespaceEventsResponse(
        namespace=summary.namespace,
        total_events=summary.total_events,
        top_affected_pods=summary.top_affected_pods,  # type: ignore
    )


def x__to_response__mutmut_8(summary: NamespaceEventsSummary) -> SummarizeNamespaceEventsResponse:
    return SummarizeNamespaceEventsResponse(
        namespace=summary.namespace,
        total_events=summary.total_events,
        severity_breakdown=summary.severity_breakdown,
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
