from __future__ import annotations

from hexawyn.application.ports.driven.monthly_incident_port import (
    IncidentSnapshotData,
    MonthlyIncidentPort,
)
from kubernetes import client, config


class MonthlyIncidentAdapter(MonthlyIncidentPort):
    def fetch_incidents(self, month: str) -> list[IncidentSnapshotData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentSnapshotData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    result.append(
                        IncidentSnapshotData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            severity="warning",
                            downtime_minutes=0,
                            timestamp=str(event.first_timestamp) if event.first_timestamp else "",
                            resolved_at=str(event.last_timestamp) if event.last_timestamp else "",
                            is_planned_maintenance=False,
                            reopened=bool(event.count and event.count > 1),
                        )
                    )
            return result
        except Exception:
            return []
