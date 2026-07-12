from hexawyn.application.ports.driven.cluster_diff_port import (
    ClusterDiffPort,
    ClusterInventoryData,
    ResourceInventoryRaw,
)


class _FakeSource:
    def fetch_resource_inventory(self, cluster_context: str) -> ClusterInventoryData:
        return ClusterInventoryData(cluster_name=cluster_context, resources=[])


class TestPortImplementation:
    def test_is_cluster_diff_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.cluster_diff_adapter import ClusterDiffAdapter

        assert isinstance(ClusterDiffAdapter(source=_FakeSource()), ClusterDiffPort)

    def test_delegates_to_source(self) -> None:
        from hexawyn.adapters.secondary.gitops.cluster_diff_adapter import ClusterDiffAdapter

        class StagingSource:
            def fetch_resource_inventory(self, cluster_context: str) -> ClusterInventoryData:
                return ClusterInventoryData(
                    cluster_name=cluster_context,
                    resources=[
                        ResourceInventoryRaw(
                            kind="Deployment",
                            name="notification-service",
                            namespace="production",
                            image_tag="v1.3",
                            replicas=2,
                            is_secret=False,
                        )
                    ],
                )

        adapter = ClusterDiffAdapter(source=StagingSource())

        result = adapter.get_resource_inventory("staging")

        assert result["cluster_name"] == "staging"
        assert result["resources"][0]["name"] == "notification-service"
