from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.cluster_diff_port import (
    ClusterDiffPort,
    ClusterInventoryData,
)


class ClusterInventorySource(Protocol):
    def fetch_resource_inventory(self, cluster_context: str) -> ClusterInventoryData: ...


class ClusterDiffAdapter(ClusterDiffPort):
    def __init__(self, source: ClusterInventorySource) -> None:
        self._source = source

    def get_resource_inventory(self, cluster_context: str) -> ClusterInventoryData:
        return self._source.fetch_resource_inventory(cluster_context)
