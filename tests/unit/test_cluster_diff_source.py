from hexawyn.adapters.secondary.gitops.cluster_diff_source import EmptyClusterInventorySource


class TestEmptyClusterInventorySource:
    def test_returns_empty(self) -> None:
        result = EmptyClusterInventorySource().fetch_resource_inventory("staging")
        assert result["cluster_name"] == "staging"
        assert result["resources"] == []
