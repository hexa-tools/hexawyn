from __future__ import annotations

from hexawyn.application.ports.driven.cross_cluster_incident_port import ClusterFailureSignature


class EmptyFailureSignatureSource:
    def fetch_all_cluster_failures(self) -> list[ClusterFailureSignature]:
        return []
