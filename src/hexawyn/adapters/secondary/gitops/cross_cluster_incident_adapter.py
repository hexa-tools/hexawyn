from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.cross_cluster_incident_port import (
    ClusterFailureSignature,
    CrossClusterIncidentPort,
)


class FailureSignatureSource(Protocol):
    def fetch_all_cluster_failures(self) -> list[ClusterFailureSignature]: ...


class CrossClusterIncidentAdapter(CrossClusterIncidentPort):
    def __init__(self, source: FailureSignatureSource) -> None:
        self._source = source

    def list_all_cluster_failures(self) -> list[ClusterFailureSignature]:
        return self._source.fetch_all_cluster_failures()
