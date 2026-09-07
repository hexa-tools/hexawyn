from __future__ import annotations

from hexawyn.application.ports.driven.recurring_incident_port import (
    IncidentFrequencyData,
    RecurringIncidentPort,
)
from kubernetes import client, config


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut: MutantDict = {}  # type: ignore


class RecurringIncidentAdapter(RecurringIncidentPort):
    @_mutmut_mutated(mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut)
    def fetch_incidents(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_orig(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_1(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = None

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_2(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = None

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_3(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=None)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_4(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=101)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_5(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = None
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_6(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" or event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_7(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type != "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_8(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "XXWarningXX" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_9(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_10(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "WARNING" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_11(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = None
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_12(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(None) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_13(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else "XXXX"
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_14(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        None
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_15(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=None,  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_16(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=None,
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_17(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=None,
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_18(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=None,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_19(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=None,
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_20(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_21(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_22(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_23(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_24(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_25(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid and f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_26(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason and "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_27(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "XXunknownXX",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_28(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "UNKNOWN",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_29(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=1,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_30(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(None) if event.last_timestamp else "",
                        )
                    )
            return result
        except Exception:
            return []
    def xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_31(self, window_days: int) -> list[IncidentFrequencyData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentFrequencyData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentFrequencyData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            root_cause=event.reason or "unknown",
                            duration_minutes=0,
                            timestamp=str(event.last_timestamp) if event.last_timestamp else "XXXX",
                        )
                    )
            return result
        except Exception:
            return []

mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['_mutmut_orig'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_1'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_2'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_3'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_4'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_5'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_6'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_7'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_8'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_9'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_10'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_11'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_12'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_13'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_14'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_15'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_16'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_17'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_18'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_19'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_20'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_21'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_22'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_23'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_24'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_25'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_26'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_27'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_28'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_29'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_30'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRecurringIncidentAdapterǁfetch_incidents__mutmut['xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_31'] = RecurringIncidentAdapter.xǁRecurringIncidentAdapterǁfetch_incidents__mutmut_31 # type: ignore # mutmut generated
