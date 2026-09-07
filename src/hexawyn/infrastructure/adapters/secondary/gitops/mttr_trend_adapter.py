from __future__ import annotations

from hexawyn.application.ports.driven.mttr_trend_port import (
    IncidentResolutionData,
    MTTRTrendPort,
)
from kubernetes import client, config


class MTTRTrendAdapter(MTTRTrendPort):
    def fetch_incidents_by_month(self, month: str) -> list[IncidentResolutionData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            events = v1.list_event_for_all_namespaces(limit=100)

            result: list[IncidentResolutionData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    uid = str(event.metadata.uid) if event.metadata else ""
                    resolution_minutes = 0
                    if event.first_timestamp and event.last_timestamp:
                        delta = event.last_timestamp - event.first_timestamp
                        resolution_minutes = int(delta.total_seconds() / 60.0)

                    result.append(
                        IncidentResolutionData(
                            incident_id=uid
                            or f"k8s-{event.involved_object.kind}-{event.involved_object.name}",  # noqa: E501
                            service_name=f"{event.involved_object.kind}/{event.involved_object.name}",
                            severity="warning",
                            resolution_minutes=resolution_minutes,
                            resolved=bool(event.last_timestamp),
                            root_cause=event.reason or "unknown",
                        )
                    )
            return result
        except Exception:
            return []
