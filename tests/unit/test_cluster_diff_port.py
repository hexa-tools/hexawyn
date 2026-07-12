from abc import ABC


class TestClusterDiffPortContract:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driven.cluster_diff_port import ClusterDiffPort

        assert issubclass(ClusterDiffPort, ABC)

    def test_declares_get_resource_inventory(self) -> None:
        from hexawyn.application.ports.driven.cluster_diff_port import ClusterDiffPort

        assert "get_resource_inventory" in ClusterDiffPort.__abstractmethods__


class TestRawTypedDicts:
    def test_resource_inventory_raw_shape(self) -> None:
        from hexawyn.application.ports.driven.cluster_diff_port import ResourceInventoryRaw

        raw: ResourceInventoryRaw = {
            "kind": "Deployment",
            "name": "payment-service",
            "namespace": "production",
            "image_tag": "v1.3",
            "replicas": 3,
            "is_secret": False,
        }

        assert raw["kind"] == "Deployment"
        assert raw["image_tag"] == "v1.3"

    def test_cluster_inventory_data_shape(self) -> None:
        from hexawyn.application.ports.driven.cluster_diff_port import ClusterInventoryData

        data: ClusterInventoryData = {
            "cluster_name": "staging",
            "resources": [],
        }

        assert data["cluster_name"] == "staging"
