from hexawyn.application.ports.driven.cross_cluster_incident_port import (
    ClusterFailureSignature,
    CrossClusterIncidentPort,
)


class _FakeSource:
    def fetch_all_cluster_failures(self) -> list[ClusterFailureSignature]:
        return [
            ClusterFailureSignature(
                cluster_name="prod-eu",
                failure_type="ImagePullBackOff",
                pod_count=8,
                onset_utc="2026-06-16T09:00:00Z",
                affected_service="payment-service",
                shared_dependency="ghcr.io",
            )
        ]


class TestPortImplementation:
    def test_is_cross_cluster_incident_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.cross_cluster_incident_adapter import (
            CrossClusterIncidentAdapter,
        )

        assert isinstance(
            CrossClusterIncidentAdapter(source=_FakeSource()), CrossClusterIncidentPort
        )

    def test_delegates_to_source(self) -> None:
        from hexawyn.adapters.secondary.gitops.cross_cluster_incident_adapter import (
            CrossClusterIncidentAdapter,
        )

        adapter = CrossClusterIncidentAdapter(source=_FakeSource())
        result = adapter.list_all_cluster_failures()

        assert result[0]["cluster_name"] == "prod-eu"
        assert result[0]["pod_count"] == 8
