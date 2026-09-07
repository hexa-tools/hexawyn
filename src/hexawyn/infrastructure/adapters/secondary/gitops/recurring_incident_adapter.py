from __future__ import annotations

from hexawyn.application.ports.driven.recurring_incident_port import (
    IncidentFrequencyData,
    RecurringIncidentPort,
)
from kubernetes import client, config


class RecurringIncidentAdapter(RecurringIncidentPort):
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
