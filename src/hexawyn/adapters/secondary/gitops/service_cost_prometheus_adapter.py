from __future__ import annotations

from hexawyn.application.ports.driven.service_cost_port import (
    PodResourceSnapshotData,
    ServiceCostPort,
)


class ServiceCostPrometheusAdapter(ServiceCostPort):
    def fetch_pod_resources(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        return []
