from __future__ import annotations

from hexawyn.application.ports.driven.trace_event_correlation_port import (
    TraceEventCorrelationPort,
)
from hexawyn.domain.models.trace_k8s_events import (  # noqa: E501
    K8sEvent,
    K8sEventType,
    TraceEventCorrelationRequest,
)
from kubernetes import client, config


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut: MutantDict = {}  # type: ignore


class KubernetesEventAdapter(TraceEventCorrelationPort):
    @_mutmut_mutated(mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut)
    def fetch_k8s_events(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_orig(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_1(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = None

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_2(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = None

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_3(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=None)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_4(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=51)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_5(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = None
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_6(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    None
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_7(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=None,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_8(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=None,
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_9(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=None,
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_10(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=None,
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_11(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=None,
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_12(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_13(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_14(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_15(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_16(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_17(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else "XXXX"),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_18(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(None) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_19(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else "XXXX"),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_20(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else "XXXX"
                        ),
                        reason=event.reason or "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_21(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason and "",
                    )
                )
            return result
        except Exception:
            return []
    def xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_22(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[K8sEvent] = []
            for event in events.items:
                result.append(
                    K8sEvent(
                        event_type=K8sEventType.OTHER,
                        pod_name=(event.involved_object.name if event.involved_object else ""),
                        timestamp=(str(event.last_timestamp) if event.last_timestamp else ""),
                        namespace=(
                            event.involved_object.namespace if event.involved_object else ""
                        ),
                        reason=event.reason or "XXXX",
                    )
                )
            return result
        except Exception:
            return []

    @_mutmut_mutated(mutants_xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut)
    def fetch_slowest_span(self, request: TraceEventCorrelationRequest) -> str | None:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=20)

            warning_events = [e for e in events.items if e.type == "Warning" and e.involved_object]
            if warning_events:
                top = warning_events[0]
                return f"{top.involved_object.kind}/{top.involved_object.name}: {top.reason}"
            return None
        except Exception:
            return None

    def xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_orig(self, request: TraceEventCorrelationRequest) -> str | None:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=20)

            warning_events = [e for e in events.items if e.type == "Warning" and e.involved_object]
            if warning_events:
                top = warning_events[0]
                return f"{top.involved_object.kind}/{top.involved_object.name}: {top.reason}"
            return None
        except Exception:
            return None

    def xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_1(self, request: TraceEventCorrelationRequest) -> str | None:
        try:
            config.load_kube_config()
            v1 = None

            events = v1.list_event_for_all_namespaces(limit=20)

            warning_events = [e for e in events.items if e.type == "Warning" and e.involved_object]
            if warning_events:
                top = warning_events[0]
                return f"{top.involved_object.kind}/{top.involved_object.name}: {top.reason}"
            return None
        except Exception:
            return None

    def xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_2(self, request: TraceEventCorrelationRequest) -> str | None:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = None

            warning_events = [e for e in events.items if e.type == "Warning" and e.involved_object]
            if warning_events:
                top = warning_events[0]
                return f"{top.involved_object.kind}/{top.involved_object.name}: {top.reason}"
            return None
        except Exception:
            return None

    def xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_3(self, request: TraceEventCorrelationRequest) -> str | None:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=None)

            warning_events = [e for e in events.items if e.type == "Warning" and e.involved_object]
            if warning_events:
                top = warning_events[0]
                return f"{top.involved_object.kind}/{top.involved_object.name}: {top.reason}"
            return None
        except Exception:
            return None

    def xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_4(self, request: TraceEventCorrelationRequest) -> str | None:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=21)

            warning_events = [e for e in events.items if e.type == "Warning" and e.involved_object]
            if warning_events:
                top = warning_events[0]
                return f"{top.involved_object.kind}/{top.involved_object.name}: {top.reason}"
            return None
        except Exception:
            return None

    def xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_5(self, request: TraceEventCorrelationRequest) -> str | None:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=20)

            warning_events = None
            if warning_events:
                top = warning_events[0]
                return f"{top.involved_object.kind}/{top.involved_object.name}: {top.reason}"
            return None
        except Exception:
            return None

    def xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_6(self, request: TraceEventCorrelationRequest) -> str | None:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=20)

            warning_events = [e for e in events.items if e.type == "Warning" or e.involved_object]
            if warning_events:
                top = warning_events[0]
                return f"{top.involved_object.kind}/{top.involved_object.name}: {top.reason}"
            return None
        except Exception:
            return None

    def xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_7(self, request: TraceEventCorrelationRequest) -> str | None:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=20)

            warning_events = [e for e in events.items if e.type != "Warning" and e.involved_object]
            if warning_events:
                top = warning_events[0]
                return f"{top.involved_object.kind}/{top.involved_object.name}: {top.reason}"
            return None
        except Exception:
            return None

    def xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_8(self, request: TraceEventCorrelationRequest) -> str | None:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=20)

            warning_events = [e for e in events.items if e.type == "XXWarningXX" and e.involved_object]
            if warning_events:
                top = warning_events[0]
                return f"{top.involved_object.kind}/{top.involved_object.name}: {top.reason}"
            return None
        except Exception:
            return None

    def xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_9(self, request: TraceEventCorrelationRequest) -> str | None:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=20)

            warning_events = [e for e in events.items if e.type == "warning" and e.involved_object]
            if warning_events:
                top = warning_events[0]
                return f"{top.involved_object.kind}/{top.involved_object.name}: {top.reason}"
            return None
        except Exception:
            return None

    def xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_10(self, request: TraceEventCorrelationRequest) -> str | None:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=20)

            warning_events = [e for e in events.items if e.type == "WARNING" and e.involved_object]
            if warning_events:
                top = warning_events[0]
                return f"{top.involved_object.kind}/{top.involved_object.name}: {top.reason}"
            return None
        except Exception:
            return None

    def xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_11(self, request: TraceEventCorrelationRequest) -> str | None:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=20)

            warning_events = [e for e in events.items if e.type == "Warning" and e.involved_object]
            if warning_events:
                top = None
                return f"{top.involved_object.kind}/{top.involved_object.name}: {top.reason}"
            return None
        except Exception:
            return None

    def xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_12(self, request: TraceEventCorrelationRequest) -> str | None:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=20)

            warning_events = [e for e in events.items if e.type == "Warning" and e.involved_object]
            if warning_events:
                top = warning_events[1]
                return f"{top.involved_object.kind}/{top.involved_object.name}: {top.reason}"
            return None
        except Exception:
            return None

mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['_mutmut_orig'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_1'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_2'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_3'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_4'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_5'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_6'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_7'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_8'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_9'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_10'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_11'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_12'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_13'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_14'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_15'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_16'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_17'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_18'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_19'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_20'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_21'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut['xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_22'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_k8s_events__mutmut_22 # type: ignore # mutmut generated

mutants_xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut['_mutmut_orig'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut['xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_1'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut['xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_2'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut['xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_3'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut['xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_4'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut['xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_5'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut['xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_6'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut['xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_7'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut['xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_8'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut['xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_9'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut['xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_10'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut['xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_11'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut['xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_12'] = KubernetesEventAdapter.xǁKubernetesEventAdapterǁfetch_slowest_span__mutmut_12 # type: ignore # mutmut generated
