from __future__ import annotations

from hexawyn.application.ports.driven.unauthorized_access_port import (
    UnauthorizedAccessRaw,
)
from kubernetes import client, config


class EmptyUnauthorizedAccessSource:
    def fetch_unauthorized_access_data(self) -> UnauthorizedAccessRaw:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=100)

            attempt_count = 0
            source_type = "unknown"
            for event in events.items:
                if event.type == "Warning" and event.reason:
                    reason_lower = event.reason.lower()
                    if any(
                        keyword in reason_lower
                        for keyword in ("forbidden", "unauthorized", "access denied")
                    ):
                        attempt_count += event.count or 1
                        if event.involved_object and event.involved_object.kind:
                            source_type = event.involved_object.kind

            return UnauthorizedAccessRaw(
                attempt_count=attempt_count,
                window_minutes=30,
                source_type=source_type,
            )
        except Exception:
            return UnauthorizedAccessRaw(attempt_count=0, window_minutes=30, source_type="unknown")
