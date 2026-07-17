from hexawyn.adapters.secondary.gitops.cross_cluster_incident_source import (
    EmptyFailureSignatureSource,
)


class TestEmptyFailureSignatureSource:
    def test_returns_empty(self) -> None:
        assert EmptyFailureSignatureSource().fetch_all_cluster_failures() == []
