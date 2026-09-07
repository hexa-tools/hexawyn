from __future__ import annotations

from hexawyn.application.ports.driven.cluster_diff_port import (
    ClusterInventoryData,
)


class EmptyClusterInventorySource:
    def fetch_resource_inventory(self, cluster_context: str) -> ClusterInventoryData:
        return ClusterInventoryData(cluster_name=cluster_context, resources=[])
