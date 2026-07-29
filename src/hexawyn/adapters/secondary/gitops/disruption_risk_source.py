from __future__ import annotations

from hexawyn.application.ports.driven.disruption_risk_port import RiskEventRaw
from kubernetes import client, config


class EmptyDisruptionRiskSource:
    def fetch_disruption_risks(self, warning_days: int) -> list[RiskEventRaw]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=200)

            result: list[RiskEventRaw] = []
            for event in events.items:
                if event.type != "Warning" or not event.involved_object:
                    continue
                result.append(
                    RiskEventRaw(  # type: ignore
                        kind=event.involved_object.kind or "",
                        name=event.involved_object.name or "",
                        namespace=event.involved_object.namespace or "",
                        reason=event.reason or "",
                        message=(event.message or "")[:200],
                        count=event.count or 1,
                        last_seen=str(event.last_timestamp) if event.last_timestamp else "",
                    )
                )
            return result
        except Exception:
            return []
